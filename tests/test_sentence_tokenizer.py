#!/usr/bin/python3
from sentence_tokenizer import SentenceTokenizer

s = SentenceTokenizer()

s = s.set("OVER 500,000. THAT was the number of people who have died from Covid-19 as of early March. " \
    "The pandemic continues stealing mothers, brothers, sisters, friends. So much loss is hard to grasp. Death is not a subject "\
    "we want to talk about, but the tragedy becomes worse when a loved one dies without a will or plans for burial, and familial "\
    "infighting begins as assets are divided and argued over. My father died suddenly at 39 years old, and it tore my family apart."
    )


print(s.get())

