# Tsukasa credit card gag scam

NOTE: This is a joke program, it has zero malicious intent and is simply
designed to have fun with an old Internet joke.

This is a fork of Bleeplo's version with a more standardised project
structure, and built-in releases.

## Example

![A GIF animation of the program running][example-gif]

## Getting Started

### Dependencies

The main project has very few library dependencies. They're all listed in
[`pyproject.toml`][pyproject-toml].

The project assumes Python version 3.11.0 or newer.

The project is tested on the latest versions of Windows,
Mac OS, and Ubuntu, and it has also been tested on both CPython
and PyPy. Using other implementations or operating systems
may work, but is not guaranteed.

### Installation

To install the project with development dependencies,

1. Install `uv`: [`uv` documentation][uv-docs]
2. Within the project directory, run `uv sync`

### Running the program

```sh
uv run tccgs
```

### Running linters

```sh
uv run ruff check .
```

If you wish to auto-fix certain issues,

```sh
uv run ruff check . --fix
```

### Running formatters

```sh
uv run ruff format
```

## Version history

The project's changelog can be found [here][changelog].

## Special thanks

* [@Bleeplo][], for creating the original program. You can find their original
  executable release [here][original-exe].

[changelog]: ./CHANGELOG.md
[example-gif]: ./docs/assets/example.gif
[pyproject-toml]: ./pyproject.toml
[uv-docs]: https://docs.astral.sh/uv/
[@Bleeplo]: https://github.com/Bleeplo
[original-exe]: https://drive.google.com/file/d/1gVKI089Y7Ub7MrqNmRwsvOGZYS3msnIu/view?usp=sharing
