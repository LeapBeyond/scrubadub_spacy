import glob
import os
from setuptools import setup, find_packages

# read in the description from README
with open("README.rst") as stream:
    long_description = stream.read()

github_url = 'https://github.com/LeapBeyond/scrubadub_spacy'


def read_packages_from_file(filename):
    with open(filename, 'r') as stream:
        for line in stream:
            package = line.strip().split('#')[0]
            if package:
                yield package


def get_package_list(location):
    location = os.path.join('requirements', location)
    return list(read_packages_from_file(location))


# get the version
version = None
with open(os.path.join('scrubadub_spacy', '__init__.py')) as stream:
    for line in stream:
        if 'version' in line.lower():
            version = line.split()[-1].replace('"', '').replace("'", '')

setup(
    name='scrubadub_spacy',
    version=version,
    description=(
        "Use Spacy NER models to clean personally identifiable information from dirty dirty text."
    ),
    long_description=long_description,
    url=github_url,
    download_url="%s/archives/master" % github_url,
    author='Thomas Bird',
    author_email='thomas.bird@leapbeyond.ai',
    license='MIT',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    install_requires=get_package_list('python'),
)
