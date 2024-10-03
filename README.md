# hello-click

A reference project for a simple command line application using [Click](https://click.palletsprojects.com/en/7.x/).

## Installation

You need to have [rye](https://rye.astral.sh/) installed.

Then, clone this repository and run:

```bash
% cd hello-click
% rye sync
```

To install the package locally, run:

```bash
% rye build
% rye install --path dist/hello_click-0.1.0-py3-none-any.whl hello-click
```

## Usage

```bash
% hello-click --help
```

## Development

Run formatter, linter, static analysis and tests:

```bash
% rye fmt
% rye lint
% rye check
% rye test
# or all together
% rye run all
```

## Run development version

```bash
% rye run hello-click
```
