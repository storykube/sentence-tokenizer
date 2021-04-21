#!/usr/bin/python3

import re
import string
from functools import lru_cache

import nltk
from nltk.corpus import gutenberg, stopwords, webtext
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer
from sumy.nlp.tokenizers import Tokenizer

from .abbrevs import Abbrevs


class SingletonSentenceTokenizerContainer:
    tokenizer = False
    cache = {}


class StaticSentenceTokenizerInstance:

    flag = False

    @staticmethod
    def initialize_static():

        abbrevsClass = Abbrevs()
        abbrevs = abbrevsClass.get()

        input_text = ""
        for file_id in gutenberg.fileids():
            input_text += gutenberg.raw(file_id)

        for file_id in webtext.fileids():
            input_text += webtext.raw(file_id)

        trainer = PunktTrainer(verbose=False)
        trainer.INCLUDE_ALL_COLLOCS = True
        trainer.INCLUDE_ABBREV_COLLOCS = True
        trainer.train(input_text, verbose=False)
        SingletonSentenceTokenizerContainer.tokenizer = PunktSentenceTokenizer(
            trainer.get_params(), verbose=False)

        for abbrev in abbrevs:
            SingletonSentenceTokenizerContainer.tokenizer.\
                _params.abbrev_types.add(abbrev)

        alphabet = list(string.ascii_lowercase)
        SingletonSentenceTokenizerContainer.tokenizer._params.abbrev_types.update(
            alphabet)

        StaticSentenceTokenizerInstance.flag = True


class SentenceTokenizer:
    """
    The Storykube Sentente Tokenizer. 
    It Wrap the segtok segmenter, and improve the logic behind it
    keeping in mind some of English basic syntactic and grammar rules.
    """

    DOT_REPLACE = "[[[1]]]"
    ASK_REPLACE = "[[[2]]]"
    EXC_REPLACE = "[[[3]]]"
    DOT_DOT_REPLACE = "[[[4]]]"

    def __init__(self):

        self.text = ""
        self.stop_words = set(stopwords.words('english'))

        if not StaticSentenceTokenizerInstance.flag:
            StaticSentenceTokenizerInstance.initialize_static()

    def set(self, text):

        self.text = text

        return self

    def get(self, protect=True) -> list:

        def protect_chars_between_quotes(text):
            text = text.replace('“', '"')
            text = text.replace('”', '"')
            text = re.sub(
                r'\.\.\.(?!(?:[^"]*"[^"]*")*[^"]*$)', SentenceTokenizer.DOT_DOT_REPLACE, text)
            text = re.sub(r'\.(?!(?:[^"]*"[^"]*")*[^"]*$)',
                          SentenceTokenizer.DOT_REPLACE, text)
            text = re.sub(r'\?(?!(?:[^"]*"[^"]*")*[^"]*$)',
                          SentenceTokenizer.ASK_REPLACE, text)
            text = re.sub(r'\!(?!(?:[^"]*"[^"]*")*[^"]*$)',
                          SentenceTokenizer.EXC_REPLACE, text)
            return text

        def restore_protected_chars(text):
            text = text.replace(SentenceTokenizer.DOT_DOT_REPLACE, "...")
            text = text.replace(SentenceTokenizer.DOT_REPLACE, ".")
            text = text.replace(SentenceTokenizer.ASK_REPLACE, "?")
            text = text.replace(SentenceTokenizer.EXC_REPLACE, "!")

            # restore doubled quotes
            text = re.sub(r'(^|\s)\"', " “", text)
            text = re.sub(r'\"\s', "” ", text)
            text = re.sub(r'\"\.', "”.", text)
            text = re.sub(r'\"\,', "”,", text)
            text = re.sub(r'\"\-', "”-", text)
            text = re.sub(r'\"\s\-', "” -", text)
            text = re.sub(r'\"$', "”", text)
            text = text.replace('"', '“')  # latest tentative, classic replace.

            return text

        # Get result from the cache:
        if self.text in SingletonSentenceTokenizerContainer.cache.keys():
            return SingletonSentenceTokenizerContainer.cache[self.text]

        # That is important to avoid all the problems regarding the sentence
        # tokenizer on quotes. For example:
        # "Exhale and out." Mindfulness practices
        # -> could become a wrong tokenized sentences: '"Exhale and out.', '"Mindfulness practices"
        # (with quotes on the next sentence).
        quotes_sentences = re.finditer(r"\“(.+?)\”", self.text)
        for q in quotes_sentences:
            q = str(q.group(0))

            if q.endswith('.”'):
                q = str(q).replace('.”', '')
                self.text = self.text.replace(f'{q}.”', f'{q}”. ')

        # Now, tokenize it.
        if protect:
            protected_text = protect_chars_between_quotes(self.text)
        else:
            protected_text = text

        # logger.info(protected_text)
        sentences = SingletonSentenceTokenizerContainer.tokenizer.tokenize(protected_text)

        # Trying to fix misunderstanding about abbreviations
        # For example: if we have u.s.a. followed by a stopwords, probably is a new sentence,
        # so, trying to split and push them separately.
        result = []
        sentence_sep_fix = '~)N(~'
        for sent in sentences:
            # logger.info(sent)
            if '. ' in sent:
                how_many_dot = sent.count('. ')
                for i in range(1, how_many_dot):
                    words_after_dot = sent.split('. ')[i].strip()
                    word_after_dot = words_after_dot.split(' ')[0].strip()
                    # logger.info("[Sentence-Tokenizer-Fix] The word immediately after dot: " + word_after_dot)
                    # logger.info("[Sentence-Tokenizer-Fix] The first letter after dot: " + word_after_dot[0])
                    if word_after_dot.lower() in self.stop_words \
                            and word_after_dot.lower() not in ['and', 'or'] \
                            and word_after_dot[0].isupper():
                        # logger.info(f'[Sentence-Tokenizer-Fix] Found: {word_after_dot}')
                        # keep the space after the sent replace, to avoid confusion (an != and)
                        sent = sent.replace(
                            f'. {word_after_dot} ', f'. {sentence_sep_fix}{word_after_dot} ')

                if sentence_sep_fix in sent:
                    split_sentences = sent.split(sentence_sep_fix)
                    for single_part in split_sentences:
                        result.append(single_part.strip())
                else:
                    result.append(restore_protected_chars(sent))
            else:
                result.append(restore_protected_chars(sent))

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
