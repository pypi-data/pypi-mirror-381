# your_package_name/__init__.py (based on your original code)

import nltk
from nltk.corpus import stopwords as nltk_stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize as nltk_word_tokenize
import string

# Download necessary NLTK data (Crucial for PyPI use: do this once or handle errors)
# IMPORTANT: When running this in a package, only download *if* needed and ensure it's not during import time.
# For simplicity in this package, we'll assume the user runs a setup or it's downloaded on first use.
# For now, keep the initial download for setup, but consider removing "all" for just what you need.

# A more robust download check (recommended for production):
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/wordnet')
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    print("Downloading required NLTK data...")
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')


def tokenize_text(text: str) -> list:
    """Tokenizes a single string of text into a list of words."""
    # Corrected function: uses the NLTK function directly
    return nltk_word_tokenize(text)


def remove_stopwords(word_list: list) -> list:
    """Removes standard English stopwords from a list of words."""
    # Use NLTK's comprehensive list
    stopwords = set(nltk_stopwords.words('english'))
    filtered_list = [word for word in word_list if word.lower() not in stopwords]
    return filtered_list


def remove_punctuation(word_list: list) -> list:
    """Removes punctuation from a list of words."""
    punctuation = string.punctuation
    filtered_list = [word for word in word_list if word not in punctuation]
    return filtered_list


def apply_stemming(words: list):
    """Prints the stem for each word in the list."""
    stemmer = PorterStemmer()
    for word in words:
        rootWord = stemmer.stem(word)
        print(f"{word} : {rootWord}")


def apply_lemmatizing(words: list):
    """Prints the lemma for each word in the list."""
    lemmatizer = WordNetLemmatizer()
    for word in words:
        print(f"{word}: {lemmatizer.lemmatize(word)}")


def apply_pos_tagging(words: list) -> list:
    """Performs Part-of-Speech (POS) tagging on a list of words."""
    tagged_words = nltk.pos_tag(words)
    return tagged_words
