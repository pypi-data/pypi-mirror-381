

from setuptools import setup, find_packages

setup(
    name="aek-seq-trainer",
    version="0.1.1",
    author="Alp Emre Karaahmet",
    author_email="alpemrekaraahmet@gmail.com",
    description="AI sequence trainer",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/aek-seq-trainer",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0",
        "scikit-learn>=1.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries"
    ],
    include_package_data=True,
)
