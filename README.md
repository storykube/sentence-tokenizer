_**public**_

# Sentence Tokenizer
Sentence tokenization is the process of splitting text into individual sentences. 

This Sentence Tokenizer can be used when preparing or augmenting data to train, or to process a long article by handling it as a simple group of sentences.

## Usage
First of all, install it from github.

```bash
pip3 install git+https://github.com/storykube/sentence-tokenizer.git
```

Then, in your python script, import the package, instance it, set and finally get.
```python
#!/usr/bin/python3

from sentence_tokenizer import SentenceTokenizer

s = SentenceTokenizer()
s.set('...') # long text
sentences = s.get()
```

**Some notes**

The first run of the Storykube **SentenceTokenizer**, just after the import - I mean, the first occurence -
can be very slow, because it must initialize and train the PunktSentenceTokenizer. \
The next calls, on the other hand, will be made in an acceptable amount of time (ms).

