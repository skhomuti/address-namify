#!python

import json
import random
import argparse

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


combinations_count = len(adjectives) * len(adverbs) * len(personal_nouns) * len(prepositions) * len(nouns)


def generate(num):
    for i in range(num):
        adj = random.randint(0, len(adjectives))
        adv = random.randint(0, len(adverbs))
        noun = random.randint(0, len(personal_nouns))
        prep = random.randint(0, len(prepositions))
        noun2 = random.randint(0, len(nouns))
        yield f"{adjectives[adj]} {adverbs[adv]} {personal_nouns[noun]} {prepositions[prep]} {nouns[noun2]}".replace(" ", "-")


def from_address(address):
    adj = int(address / max_range * len(adjectives))
    adv = int(address / max_range * len(adverbs))
    noun = int(address / max_range * len(personal_nouns))
    prep = int(address / max_range * len(prepositions))
    noun2 = int(address / max_range * len(nouns))
    return f"{adjectives[adj]} {adverbs[adv]} {personal_nouns[noun]} {prepositions[prep]} {nouns[noun2]}".replace(" ", "-")


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
        print(from_address(int(args.address, 16)))
