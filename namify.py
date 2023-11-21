#!python

import json
import random
import argparse
import string
from hashlib import sha256


DEFAULT_TEMPLATE = "{adj1}-{adj2}-{noun}"

with open("corpora/data/words/adjs.json") as json_file:
    adjectives = json.load(json_file).get("adjs")

with open("corpora/data/words/states_of_drunkenness.json") as json_file:
    adjectives.extend(json.load(json_file).get("states_of_drunkenness"))

# with open("corpora/data/words/adverbs.json") as json_file:
#     adverbs = json.load(json_file).get("adverbs")

with open("corpora/data/words/personal_nouns.json") as json_file:
    personal_nouns = json.load(json_file).get("personalNouns")

# with open("corpora/data/words/prepositions.json") as json_file:
#     prepositions = json.load(json_file).get("prepositions")

# with open("corpora/data/words/nouns.json") as json_file:
#     nouns = json.load(json_file).get("nouns")


class SoftFormatter(string.Formatter):
    def get_value(self, key, args, kwargs):
        try:
            return super(SoftFormatter, self).get_value(key, args, kwargs)
        except KeyError:
            return '{' + key + '}'


f = SoftFormatter()


def get_name(adj1, adj2, noun):
    return f.format(getattr(args, "template", DEFAULT_TEMPLATE),
                    adj1=adjectives[adj1].replace(" ", "-"),
                    adj2=adjectives[adj2].replace(" ", "-"),
                    noun=personal_nouns[noun].replace(" ", "-"))


def generate(num):
    for i in range(num):
        adj1 = random.randint(0, len(adjectives))
        adj2 = random.randint(0, len(adjectives))
        noun = random.randint(0, len(personal_nouns))
        yield get_name(adj1, adj2, noun)


def from_address(address: str):
    address_int = int(address, 16) + sum([int(digit) for digit in str(int(address, 16))])
    address = hex(address_int)
    address_sha = sha256(address.encode("utf-8")).hexdigest()
    left_sha = sha256(address[:len(address) // 2].encode("utf-8")).hexdigest()
    right_sha = sha256(address[len(address) // 2:].encode("utf-8")).hexdigest()

    adj_index1 = int(address_sha, 16) % len(adjectives)
    adj_index2 = int(left_sha, 16) % len(adjectives)
    noun_index = int(right_sha, 16) % len(personal_nouns)
    return get_name(adj_index1, adj_index2, noun_index)


def generate_ethereum_address():
    return "0x" + sha256(str(random.randint(0, 2**256)).encode('utf-8')).hexdigest()[:40]


def collisions():
    chances = []
    for j in range(10):
        names = {}
        collision_count = 0
        iterations = 100000
        for i in range(iterations):
            address = generate_ethereum_address()
            name = from_address(address)
            if names.get(name):
                collision_count += 1

            names[name] = True
        print(f"{collision_count} collisions of {iterations} iterations. Chance is", collision_count / iterations * 100, "%")
        chances.append(collision_count / iterations)

    print("Collision chance", f"{sum(chances) / len(chances) * 100:f}%")


args = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate', type=int, help='generate random phrases')
    parser.add_argument('--address', type=str, help='generate phrase from address')
    parser.add_argument('--collisions', action=argparse.BooleanOptionalAction, help='calculate collisions')
    parser.add_argument('--template',
                        type=str,
                        help='name template. Possible words are: adj1, adj2, noun',
                        default=DEFAULT_TEMPLATE
                        )
    args = parser.parse_args()
    if args.generate:
        print(f"{args.generate} random phrases:")
        for phrase in generate(args.generate):
            print(" - " + phrase)
    if args.address:
        print(from_address(args.address))
    if args.collisions:
        collisions()
