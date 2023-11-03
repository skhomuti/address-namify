# address-namify

> let things be weird

This simple tool allows you to create a name for an Ethereum address.
Based on [corpora](https://github.com/dariusk/corpora) collections.

## Usage

Generate {num} random names to play with variants:
```commandline
./namify.py --generate {num}
```

Generate name using Ethereum address:
```commandline
./namify --address {address}
```

Rough calculation of the collision chance:
```commandline
./namify --collisions
```

## Misc

This tool provides constant names per address as long as dictionaries stay the same.

The names are *not unique* and there might be collisions. E.g. `{adj1} {adj2} {noun}` has ~0.0005% chance of collision. 

It's possible to use it on-chain by additionally checking the given name for uniqueness 
and optionally adding a numeric prefix like `{name}-{i}` where `i` is the name count already used in the contract.   

Words count and sentence probably might be revised.
