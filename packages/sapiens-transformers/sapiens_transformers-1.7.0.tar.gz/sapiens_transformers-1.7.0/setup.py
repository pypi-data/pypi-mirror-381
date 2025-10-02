"""
    #################################################################################################################################################################################################
    # This code library is an adaptation of the original Transformers and was designed, developed and programmed by Sapiens Technology®.                                                            #
    # Any alteration and/or disclosure of this code without prior authorization is strictly prohibited and is subject to legal action that will be forwarded by the Sapiens Technology® legal team. #
    # This set of algorithms aims to download, train, fine-tune and/or infer large language models from various sources and slopes.                                                                 #
    #################################################################################################################################################################################################
"""
from setuptools import setup, find_packages
package_name = 'sapiens_transformers'
version = '1.7.0'
setup(
    name=package_name,
    version=version,
    author='SAPIENS TECHNOLOGY',
    packages=find_packages(),
    install_requires=[
        'transformers==4.45.2',
        'huggingface-hub==0.28.1',
        'requests',
        'certifi',
        'tqdm',
        'numpy==1.25.2',
        'torch==2.4.1',
        'torchvision==0.19.1',
        'torchaudio==2.4.1',
        'accelerate',
        'sapiens-machine',
        'sapiens-accelerator',
        'sapiens-generalization',
        'tokenizers==0.20.1',
        'regex',
        'datasets',
        'sentencepiece',
        'protobuf',
        'optimum',
        'einops',
        'nemo-toolkit==2.1.0',
        'hydra-core',
        'lightning',
        'braceexpand',
        'webdataset',
        'h5py',
        'ijson',
        'matplotlib',
        'diffusers==0.32.2',
        'moviepy==1.0.3',
        'llama-cpp-python==0.3.6',
        'llamacpp==0.1.14',
        'beautifulsoup4',
        'av',
        'ftfy',
        'tiktoken',
        'opencv-python',
        'scipy',
        'TTS',
        'pydub',
        'megatron-core==0.10.0'
    ],
    extras_require={
        'toolkit': ['nemo-toolkit[all]==2.1.0'],
        'multimedia': [
            'av; python_version>="3.12"',
            'pyav; python_version<"3.12"',
            'TTS; python_version<"3.12"'
        ]
    },
    url='https://github.com/sapiens-technology/sapiens_transformers',
    license='Proprietary Software'
)
"""
    #################################################################################################################################################################################################
    # This code library is an adaptation of the original Transformers and was designed, developed and programmed by Sapiens Technology®.                                                            #
    # Any alteration and/or disclosure of this code without prior authorization is strictly prohibited and is subject to legal action that will be forwarded by the Sapiens Technology® legal team. #
    # This set of algorithms aims to download, train, fine-tune and/or infer large language models from various sources and slopes.                                                                 #
    #################################################################################################################################################################################################
"""
