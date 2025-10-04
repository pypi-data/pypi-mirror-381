# demo-greeter-pkg

A tiny example Python package with one function and a CLI command `greet`.

## Install (from source)

```bash
pip install -e .
```

## Usage

```bash
greet Alice
# -> Hello, Alice!
```

## Development

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip build twine pytest
pytest
python -m build
```

This creates `dist/*.whl` and `dist/*.tar.gz`.