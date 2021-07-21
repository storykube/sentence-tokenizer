import setuptools
from setuptools.command.develop import develop
from setuptools.command.install import install

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def installNLTKDependencies():
    import nltk
    nltk.download("gutenberg")
    nltk.download("webtext")
    nltk.download("punkt")
    nltk.download("stopwords")


setuptools.setup(
    name="sentence_tokenizer",
    version="0.0.5",
    author="Ottavio Fogliata",
    author_email="ottavio.fogliata@storykube.com",
    description='Storykube Sentence Tokenizer. It splits the article text in sentences, following basic syntactic and '
                'grammar rules from English Language.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/storykube/sentence_tokenizer",
    project_urls={
        "Bug Tracker": "https://github.com/storykube/sentence_tokenizer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'nltk',
        'spacy',
        'langdetect'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

installNLTKDependencies()
