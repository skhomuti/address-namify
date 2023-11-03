#!python

import json
import random
import argparse
from hashlib import sha256

max_range = int("0xffffffffffffffffffffffffffffffffffffffff", 16)


with open("corpora/data/words/adjs.json") as json_file:
    adjectives = json.load(json_file).get("adjs")

with open("corpora/data/words/states_of_drunkenness.json") as json_file:
    adjectives.extend(json.load(json_file).get("states_of_drunkenness"))

with open("corpora/data/words/adverbs.json") as json_file:
    adverbs = json.load(json_file).get("adverbs")

with open("corpora/data/words/personal_nouns.json") as json_file:
    personal_nouns = json.load(json_file).get("personalNouns")

with open("corpora/data/words/prepositions.json") as json_file:
    prepositions = json.load(json_file).get("prepositions")

with open("corpora/data/words/nouns.json") as json_file:
    nouns = json.load(json_file).get("nouns")


combinations_count = len(adjectives) * len(adverbs) * len(personal_nouns)


def generate(num):
    for i in range(num):
        adj = random.randint(0, len(adjectives))
        noun = random.randint(0, len(personal_nouns))
        yield f"{adjectives[adj]} {personal_nouns[noun]}".replace(" ", "-")


def from_address(address: str):
    address_sha = sha256(address.encode("utf-8")).hexdigest()

    sum_digits = sum([int(digit) for digit in str(int(args.address, 16))])
    sum_sha_digits = sum([int(digit) for digit in str(int(address_sha, 16))])

    adj_index = sum_digits % len(adjectives)
    noun_index = sum_sha_digits % len(personal_nouns)
    return f"{adjectives[adj_index]} {personal_nouns[noun_index]}".replace(" ", "-")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate', type=int, help='generate random phrases')
    parser.add_argument('--address', type=str, help='generate phrase from address')
    args = parser.parse_args()
    if args.generate:
        print(f"{args.generate} random phrases:")
        for phrase in generate(args.generate):
            print(" - " + phrase)
    if args.address:
        print(from_address(args.address))
