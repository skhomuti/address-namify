# address-namify

> let things be weird

This simple tool allows you to create a name for an Ethereum address.
Based on [corpora](https://github.com/dariusk/corpora) collections.

## Usage
First of all, make sure that submodules are initialized:
```bash
git submodule update --init --recursive
```

Generate {num} random names to play with variants:
```bash
python3 ./namify.py --generate {num}
```

Generate name using Ethereum address:
```bash
python3 ./namify.py --address {address}
```

Rough calculation of the collision chance:
```bash
python3 ./namify.py --collisions
```

Set a custom string template:
```bash
# default template
python3 ./namify.py --generate 10 --template="{adj1}-{adj2}-{noun}"

# 2-words template
python3 ./namify.py --generate 10 --template="{adj1}-{noun}"
```
## Misc

This tool provides constant names per address as long as dictionaries stay the same.

The names are *not unique* and there might be collisions. E.g. `{adj1} {adj2} {noun}` has ~0.0005% chance of collision per 100_000 iterations. 

It's possible to use it on-chain by additionally checking the given name for uniqueness 
and optionally adding a numeric prefix like `{name}-{i}` where `i` is the name count already used in the contract.   

Words count and sentence probably might be revised.
