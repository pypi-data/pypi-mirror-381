# NLP Lab Package (nlp-lab-pkg-i061)

A utility package for basic Natural Language Processing tasks including tokenization, stopword removal, stemming, and POS tagging, developed for I061 Lab 2.

## Installation

```bash
pip install nlp-lab-pkg-i061

Usage :
import nlp_lab_pkg

text = "The quick brown foxes are running."
tokens = nlp_lab_pkg.tokenize_text(text)
print(tokens)

# Example: Remove stopwords
clean_tokens = nlp_lab_pkg.remove_stopwords(tokens)
print(clean_tokens)

***

## 2. Re-run the Build Command ✅

Once the `README.md` file exists and has content, run the build command again:

```bash
python setup.py sdist bdist_wheel
