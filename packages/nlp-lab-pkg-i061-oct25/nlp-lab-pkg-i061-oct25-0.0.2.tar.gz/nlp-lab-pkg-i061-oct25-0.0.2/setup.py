# setup.py
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nlp-lab-pkg-i061-oct25", # Make this unique on PyPI
    version="0.0.2",
    author="Jind Saini",
    author_email="jindsaini20@gmail.com",
    description="NLP Lab utilities for tokenization, stemming, and tagging.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jindsaini2013/nlp-lab-pkg-i061.git", # Replace with your repo link
    packages=setuptools.find_packages(), # Finds the 'nlp_lab_pkg' directory
    install_requires=[
        'nltk>=3.5', # Dependency on NLTK
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
