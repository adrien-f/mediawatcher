from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mediawatcher',
    version='0.0.3',
    description='Watch directories and move media files accordingly.',
    long_description=long_description,
    url='https://github.com/adrien-f/mediawatcher',
    author='Adrien Fillon',
    author_email='adrien.fillon+pypi@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Multimedia',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='media watcher rename',
    packages=['mediawatcher'],
    install_requires=['guessit', 'logbook', 'watchdog', 'pyyaml'],
    include_package_data=True,
    extras_require={
        'dev': [],
        'test': ['nose', 'coverage'],
    },
    entry_points={
        'console_scripts': [
            'mediawatcher=mediawatcher.__main__:main',
        ],
    },
)
