import setuptools
from setuptools.command.develop import develop
from setuptools.command.install import install

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sentence_tokenizer",
    version="0.1.0",
    author="Ottavio Fogliata",
    author_email="ottavio.fogliata@storykube.com",
    description='Storykube Sentence Tokenizer: split the article text in sentences with pySBD.',
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
        'sumy',
        'langdetect',
        'pysbd==0.3.4'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

