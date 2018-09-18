# MDACP integrated into OACIS

A sample code to integrate MDACP into OACIS.

## Prerequisite

- Install [OACIS](https://github.com/crest-cassia/oacis)
- Install numpy and matplotlib

## Usage

1. MDACP is included as a git submodule. Clone the submodule and build MDACP.

```
git submodule update --init --recursive
cd mdacp
[Follow the instruction to build mdacp]
```

2. Register the information of the simulator to OACIS. Run the following command, and a new simulator "MDACP_Langevin" is created.

```
/[path to OACIS]/bin/oacis_ruby register_oacis.rb
```

3. Now you can make jobs using your OACIS.

