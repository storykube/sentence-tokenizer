_**public**_

# Sentence Tokenizer
Sentence tokenization is the process of splitting text into individual sentences. 

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
