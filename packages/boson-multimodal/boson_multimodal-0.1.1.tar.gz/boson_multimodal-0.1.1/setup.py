from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="boson_multimodal",
    version="0.1.1",
    author="Boson AI",
    author_email="contact@boson-ai.com",
    description="Boson Multimodal - A multimodal AI framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/boson_multimodal",
    packages=find_packages(include=['boson_multimodal', 'boson_multimodal.*']),
    package_data={
        'boson_multimodal': ['*.py', '**/*.py', '**/**/*.py'],
    },
    python_requires='>=3.8',
    install_requires=[
        'descript-audio-codec',
        'torch',
        'transformers>=4.45.1,<4.47.0',
        'librosa',
        'dacite',
        'boto3==1.35.36',
        's3fs',
        'torchvision',
        'torchaudio',
        'json_repair',
        'pandas',
        'pydantic',
        'vector_quantize_pytorch',
        'loguru',
        'pydub',
        'ruff==0.12.2',
        'omegaconf',
        'click',
        'langid',
        'jieba',
        'accelerate>=0.26.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
