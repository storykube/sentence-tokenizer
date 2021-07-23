#!/usr/bin/python3
from sentence_tokenizer import SentenceTokenizer

s = SentenceTokenizer()

s = s.set("If you're a plant lover: this guide is just for you. ##In fact, we're going to find out together how to take care of your plants at home even in the winter, with the thermostats on. Drought and temperature fluctuations can put your plants at risk for survival, but Attention to the thermometers.")


print(s.get())

