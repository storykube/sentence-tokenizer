#!/usr/bin/python3
import spacy
import re
import string
from functools import lru_cache

import nltk
from nltk.corpus import gutenberg, stopwords, webtext
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer
from sumy.nlp.tokenizers import Tokenizer

from .abbrevs import Abbrevs
from langdetect import detect


class SpacyStatic:
    MAP = {
        'it': 'it_core_news_sm',
        'en': 'en_core_web_sm',
        'es': 'es_core_news_sm',
        'fr': 'fr_core_news_sm',
        'de': 'de_core_news_sm',
        'ru': 'ru_core_news_sm',
    }

    NLP_MEM = {}

    def __init__(self):
        pass


class SingletonSentenceTokenizerContainer:
    nlp_model = None
    cache = {}

    def __init__(self):
        pass


class SentenceTokenizer:
    """
    The Storykube Sentence Tokenizer.
    """

    DOT_REPLACE = "~~1~~"
    ASK_REPLACE = "~~2~~"
    EXC_REPLACE = "~~3~~"
    DOT_DOT_REPLACE = "~~4~~"
    COLON_REPLACE = "~~5~~"

    def __init__(self):

        pass

    def set(self, text):

        self.text = text

        return self

    def get(self) -> list:

        def protect_chars_between_quotes(text_str):
            text_str = text_str.replace('“', '"')
            text_str = text_str.replace('”', '"')
            text_str = re.sub(
                r'\.\.\.(?!(?:[^"]*"[^"]*")*[^"]*$)', SentenceTokenizer.DOT_DOT_REPLACE, text_str)

            text_str = re.sub(r'\.(?!(?:[^"]*"[^"]*")*[^"]*$)',
                              SentenceTokenizer.DOT_REPLACE, text_str)

            text_str = re.sub(r'\?(?!(?:[^"]*"[^"]*")*[^"]*$)',
                              SentenceTokenizer.ASK_REPLACE, text_str)

            text_str = re.sub(r'\!(?!(?:[^"]*"[^"]*")*[^"]*$)',
                              SentenceTokenizer.EXC_REPLACE, text_str)

            text_str = re.sub(r'\:(?!(?:[^"]*"[^"]*")*[^"]*$)',
                              SentenceTokenizer.COLON_REPLACE, text_str)

            return text_str

        def restore_protected_chars(text_str):
            text_str = text_str.replace(SentenceTokenizer.DOT_DOT_REPLACE, "...")
            text_str = text_str.replace(SentenceTokenizer.DOT_REPLACE, ".")
            text_str = text_str.replace(SentenceTokenizer.ASK_REPLACE, "?")
            text_str = text_str.replace(SentenceTokenizer.EXC_REPLACE, "!")
            text_str = text_str.replace(SentenceTokenizer.COLON_REPLACE, ":")

            # restore doubled quotes
            text_str = re.sub(r'(^|\s)\"', " “", text_str)
            text_str = re.sub(r'\"\s', "” ", text_str)
            text_str = re.sub(r'\"\.', "”.", text_str)
            text_str = re.sub(r'\"\,', "”,", text_str)
            text_str = re.sub(r'\"\-', "”-", text_str)
            text_str = re.sub(r'\"\s\-', "” -", text_str)
            text_str = re.sub(r'\"$', "”", text_str)
            text_str = text_str.replace('"', '“')  # latest tentative, classic replace.

            return text_str

        lang_code = detect(self.text)

        if lang_code not in SpacyStatic.NLP_MEM.keys():
            if lang_code not in SpacyStatic.MAP:
                lang_code = 'en'

            SpacyStatic.NLP_MEM[lang_code] = \
                spacy.load(SpacyStatic.MAP[lang_code])

        # Get result from the cache:
        if self.text in SingletonSentenceTokenizerContainer.cache.keys():
            return SingletonSentenceTokenizerContainer.cache[self.text]

        text = protect_chars_between_quotes(self.text)

        tokens = SpacyStatic.NLP_MEM[lang_code](text)

        result = []

        for sent in tokens.sents:
            result.append(restore_protected_chars(str(sent).strip()))

        # Saving in the cache
        SingletonSentenceTokenizerContainer.cache[self.text] = result

        return result

    # these two methods will be used from the sumy package (mixer)

    @staticmethod
    def to_sentences(text):
        st = SentenceTokenizer()
        st.set(text)
        return st.get()

    @staticmethod
    def to_words(text):
        t = Tokenizer("english")
        return t.to_words(sentence=text)
