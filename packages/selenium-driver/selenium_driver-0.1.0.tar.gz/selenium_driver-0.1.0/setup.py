from setuptools import setup, find_packages

setup(
    name="selenium_driver",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0"
    ],
    python_requires=">=3.9",
    description="Pacote para automação Selenium customizado",
    author="Seu Nome",
    url="https://github.com/seu_usuario/selenium_driver",  # opcional
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
)
