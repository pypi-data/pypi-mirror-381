from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="test_juliano_image_processing",
    version="0.0.1",
    author="Antonio Juliano",
    author_email="julianoxt@gmail.com",
    description="Pacote de processamento de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/julianoxt/image-processing-package",
    package=find_packages(),
    install_requires = requirements,
    python_requires = '>=3.8',
)   