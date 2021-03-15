# Sentence Tokenizer
Sentence tokenization is the process of splitting text into individual sentences. 

## Usage
Install
```bash
pip3 install git+https://github.com/storykube/sentence-tokenizer.git
```

Import the package, instance it, set and finally get.
```python
#!/usr/bin/python3

from sentence_tokenizer import SentenceTokenizer

s = SentenceTokenizer()
s.set('...') # long text
sentences = s.get()
```

The first run of the Storykube SentenceTokenizer, just after the import - I mean, the first occurence -
can be very slow, because it must initialize and train the PunktSentenceTokenizer.