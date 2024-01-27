from setuptools import setup, find_packages


NAME = "DaltoLLM"
VERSION = '0.0.1' 
AUTHOR = "Shinaayomi Akorede"
AUTHIR_EMAIL = "nictre7@gmail.com"
DESCRIPTION = "Hadrionite Tech's Heuristic Large Langage Model that forms, learn and create natural, engaging text using RLFS"
LONG_DESCRIPTION = 'DaltoLLM is a language model that build up on improving and reinforcing natural and engaging converstions and text'

setup(
        name=NAME, 
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHIR_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)
