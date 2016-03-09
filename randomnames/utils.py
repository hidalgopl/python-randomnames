
from .nouns import NOUNS
from .adjectives import ADJECTIVES
import random

def random_noun():
    return random.choice(NOUNS).title()

def random_adjective():
    return random.choice(ADJECTIVES).title()

def random_namepair():
    return u"{} {}".format(random_adjective(), random_noun())

