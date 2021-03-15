# Storykube Sentence Tokenizer
Split the article text in sentences, following basic syntactic and grammar rules from English Language.

## Usage
Install
```bash
pip3 install git+https://github.com/storykube/sentence-tokenizer.git
```

Import the package, instance, set and finally get.
```python
#!/usr/bin/python3

from sentence_tokenizer import SentenceTokenizer

s = SentenceTokenizer()
s.set('...') # long text
sentences = s.get()
```
