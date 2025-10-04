EcoTransformers

Sustainable LLM Inference

EcoTransformers is a Python library designed for efficient and sustainable Large Language Model (LLM) inference.
It helps developers to reduce inference time, energy consumption, and CO₂ emissions — through lightweight, built-in optimizations.

Key Features:

   ◦ Optimized inference for Hugging Face transformer models

   ◦ Primat Technique — a unified optimization method that intelligently reduces redundant computations, skips negligible activations, and applies smart caching

   ◦ Accelerates inference and lowers the environmental cost of LLM experiments without compromising performance.

Installation:

Install directly from PyPI:

    pip install ecotransformers

Usage Examples:

1. Command-line Interface
python -m ecotransformers.main \
    --model "<your model name>" \
    --prompt "What are the benefits of sustainable AI?" \
    --reference "Sustainable AI reduces energy usage and CO₂ emissions."

2. Python API

from ecotransformers.main import transformer
results = transformer(
    model_name="<your model name>"
)
print(results)


PRIMAT(Pruning-Integrated Masked Activation for Transformers) Technique:

◦ The Primat Technique is the optimization engine behind EcoTransformers.
◦ PRIMAT uses adaptive pruning and activation masking for effective execution while maintaining model accuracy. 
◦ The Primat Technique is applied automatically — no manual configuration required.

License:
This project is licensed under the MIT License — see the LICENSE file for details.

Citation:

If you use EcoTransformers in your research, please cite:

@software{ecotransformers2025,
  author = {"Shriaarthy E","Sangeetha S"},
  title = {Towards Net-Zero AI: Reducing Latency and Energy Consumption with Eco-Transformers},
  year = {2025},
  url = {https://pypi.org/project/ecotransformers/},
  license = {MIT}
}
