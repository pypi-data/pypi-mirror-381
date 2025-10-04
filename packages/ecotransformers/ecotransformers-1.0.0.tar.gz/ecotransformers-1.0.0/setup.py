from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='ecotransformers',   
    version='1.0.0',
    description="Towards Net-Zero AI: Reducing Latency and Energy Consumption with Eco-Transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=["Shriaarthy E","Sangeetha S"],
    url='https://github.com/aarthyviven/ecotransformers',
    license='MIT',
    packages=find_packages(),  
    install_requires=[      
        'torch>=1.13.0',
        'transformers>=4.30.0',
        'codecarbon>=2.2.2',
        'evaluate>=0.4.0',
        'numpy>=1.24.0', 
        'rouge_score>=0.1.2',
        'nltk>=3.8.0',
        'absl-py>=1.4.0'
    ],
    entry_points={
        'console_scripts': [
            'eco_transformer=ecotransformers.main:transformer',
        ],
    },
    python_requires='>=3.8',
)
