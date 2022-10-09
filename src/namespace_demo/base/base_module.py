import requests
import random


def random_name():
    names = requests.get(
        'https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt'
    ).text.split('\r\n')
    return random.choice(names)
