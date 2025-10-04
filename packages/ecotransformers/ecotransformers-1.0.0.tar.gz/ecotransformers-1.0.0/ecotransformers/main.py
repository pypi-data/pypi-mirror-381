import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import numpy as np
import evaluate
import gc
import argparse


torch.manual_seed(42)
np.random.seed(42)


model = None
tokenizer = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

perplexity_metric = evaluate.load("perplexity", module_type="metric")
bleu_metric = evaluate.load("bleu")
rouge_metric = evaluate.load("rouge")

frozen_layers = {}
frozen_layer_names = []

prompt_cache = {}


def load_model(model_name):
    """Loads the model and tokenizer."""
    global model, tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device).eval()
    return model, tokenizer


def freeze_hook(module, input, output, layer_name):
    """Freezes near-zero activations to save computation."""
    frozen_output = torch.where(torch.abs(output) < 1e-4,
                                torch.zeros_like(output), output)
    frozen_layers[layer_name] = frozen_output.detach()
    return frozen_output

def apply_freeze_hooks(model):
    """Applies the freeze hook to all MLP layers in the model."""
    for name, module in model.named_modules():
        if "mlp" in name and hasattr(module, "forward"):
            module.register_forward_hook(
                lambda mod, inp, out, n=name: freeze_hook(mod, inp, out, n)
            )
            frozen_layer_names.append(name)


def self_prune(model, threshold=1e-12):
    """Prunes model weights that are below a certain threshold."""
    with torch.no_grad():
        for name, param in model.named_parameters():
            if "weight" in name and len(param.shape) > 1:
                mask = param.abs() > threshold
                param.mul_(mask.float())


def free_gpu_memory():
    """Frees up GPU memory."""
    torch.cuda.empty_cache()
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.ipc_collect()
        torch.cuda.empty_cache()


def cached_infer(prompt, model_name):
    """Performs inference with caching to avoid re-computing for the same prompt."""
    if model is None or tokenizer is None:
        raise ValueError("Model not loaded. Please call load_model(model_name) first.")

    if prompt in prompt_cache:
        return prompt_cache[prompt]

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.inference_mode(): 
        outputs = model.generate(**inputs, max_length=50, do_sample=False)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    prompt_cache[prompt] = result
    free_gpu_memory()  
    return result


def evaluate_model(prompt, reference, model_name):
    """Evaluates the model on the generated text using PPL, BLEU, and ROUGE."""
    if model is None or tokenizer is None:
        raise ValueError("Model not loaded. Please call load_model(model_name) first.")

    generated = cached_infer(prompt, model_name)
    ppl = perplexity_metric.compute(predictions=[generated],
                                      model_id=model_name)["perplexities"][0]
    bleu = bleu_metric.compute(predictions=[generated],
                                 references=[reference])["bleu"]
    rouge = rouge_metric.compute(predictions=[generated],
                                   references=[reference])["rougeL"]

def transformer(model_name, prompt, reference):
    """
    The main pipeline function for the ecotransformers package.
    It automatically loads a model, applies eco-friendly optimizations
    (pruning, activation freezing), and runs an evaluation.
    This process is designed to reduce computation time and CO2 emissions.
    """
    free_gpu_memory()
    load_model(model_name)

    
    self_prune(model, threshold=1e-12)
    apply_freeze_hooks(model)

    
    start_opt = time.time()
    evaluate_model(prompt, reference, model_name)
    end_opt = time.time()
    optimized_time = end_opt - start_opt

    free_gpu_memory()  

def main():
    """
    This is an example of how to use the ecotransformers package.
    It shows how to call the main 'transformer' function.
    """
    parser = argparse.ArgumentParser(
        description="Run the Eco-Transformer pipeline with automatic optimizations."
    )
    parser.add_argument("--model", type=str, required=True,
                        help="Hugging Face causal LM model (e.g., 'gpt2')")
    parser.add_argument("--prompt", type=str, required=True,
                        help="Prompt for text generation")
    parser.add_argument("--reference", type=str, required=True,
                        help="Reference text for evaluation")
    args = parser.parse_args()

    
    transformer(args.model, args.prompt, args.reference)


if __name__ == "__main__":
    main()