# -*- coding:utf8 -*-

import pandas as pd
import string
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

"""
Author:     JGY
Creation:   10/02
We create here all the functions needed to clean a text.
"""

#
nltk.data.path.append('./nltk_data')

# Defining the object for stemming
porter_stemmer = PorterStemmer()

# Defining the object for Lemmatization
wordnet_lemmatizer = WordNetLemmatizer()


def remove_punctuation(text):
    """
    Remove punctuation from a string of character

    :param text: string
    :return: string
    """

    clean_text = "".join([i for i in text if i not in string.punctuation])

    return clean_text


def tokenization(text):
    """
    Obtain the list of the words used in the text

    :param text: string
    :return: list of string
    """
    tokens = re.split(' +',text)

    return tokens


def stemming(l_text):
    """
    Transform all words from the list to normalize them. From plural to singular or past tense to infinitive form.

    :param l_text: list of string
    :return: list of string
    """

    stem_text = [porter_stemmer.stem(word) for word in l_text]

    return stem_text


def lemmatizer(l_text):
    """
    Allow us to group words given if they're synonyms or not

    :param l_text: list of string
    :return: list of string
    """
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in l_text]

    return lemm_text


def text_cleaning(text):
    """
    Clean a string of character by using all 5 functions described above

    :param text: string
    :return: string
    """

    punctuationfree = remove_punctuation(text)
    lowered = punctuationfree.lower()
    tokens = tokenization(lowered)
    #  nonstop = remove_stopwords(tokens)
    stem_text = stemming(tokens)
    lemm_text = lemmatizer(stem_text)

    return lemm_text


if __name__ == '__main__':
    # Given a test sentence we test all the cleaning function we have
    test_sentence = \
        "Given the fact that I'm a world champion in retailing sofas," \
        " selling one or two divans shouldn't be too much of a problem." \
        " There is no difficulty in that factually"

    print("First phase: Removing punctuation")
    ts_1 = remove_punctuation(test_sentence)
    print(ts_1)

    print("Second phase: Removing uppercases and tokenize")
    ts_2 = tokenization(ts_1.lower())
    print(ts_2)

    print("Third phase: Apply stemming and lemming")
    ts_3 = lemmatizer(stemming(ts_2))
    print(ts_3)