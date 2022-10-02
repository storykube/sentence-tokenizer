#!/usr/bin/python3
import re
import string

from sumy.nlp.tokenizers import Tokenizer
import pysbd
from langdetect import detect


class SingletonSentenceTokenizerContainer:
    nlp_model = None

    def __init__(self):
        pass


class SentenceTokenizer:
    """
    The Storykube Sentence Tokenizer / A wrapper of PySBD
    https://github.com/nipunsadvilkar/pySBD
    """

    def __init__(self):
        pass

    def set(self, text):
        self.text = text
        return self

    def get(self) -> list:
        seg = pysbd.Segmenter(language=detect(self.text[:256]), clean=False)
        return seg.segment(self.text)

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
