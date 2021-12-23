# pbt_basic_python
Property Based Testing examples: Simple examples to help get started with PBT.

The testing code is implemented using the excellent Hypothesis Python library.

# How to use this repo
This repo contains several small tests, each self-contained.

The only common thing is the Pipfile that manages package dependencies.

## Install python and pipenv
*(section missing, will be added later)*

## Install python packages
Start by running this from the repo root:
(this also creates the virtualenv if needed)
```sh
./devtools/reinstall_pipenv_packages.sh
```

## Run tests:
Go into one of the tests directories.
For example:
```sh
cd examples/test_sort_with_definition
```
Then run the tests:
```sh
./devtools/run_tests.sh
```
Inside each example, there is a separate README file with explanations about the test and what you should expect to see when you run the test.
