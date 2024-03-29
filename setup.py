from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '0.1.1'
DESCRIPTION = 'Fork of the original bnltk by ashwoolford'
LONG_DESCRIPTION = 'Fork of the original bnltk by ashwoolford'

# Setting up
setup(
    name="bnltk-revamped",
    version=VERSION,
    project_urls={
        "Github": "https://github.com/parthokr/bnltk-revamped"
    },
    author="Partho KR",
    author_email="<partho.kr@protonmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'scikit-learn', 'keras'],
    keywords=['python', 'nlp', 'bengali', 'bnltk'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)
