NOUNS: str = ''

GRAMMATICAL_NAME: dict = {
    'Noun phrase': '',
    'Noun clause': '',
    'Adjectival phrase': '',
}

import networkx as nx 

"""The networkx module will serve as a base for DaltoLLM. DaltoLLM uses graph to understand and build it's language model"""

text = open('AI\DaLToAGI\DaltoLLM\TextArchive\text123.txt')
text_buffer = text.read()

print(text_buffer)