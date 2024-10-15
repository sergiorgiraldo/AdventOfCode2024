_default:
  just --list

_require-venv:
    #!/usr/bin/env python
    import sys
    sys.exit(sys.prefix == sys.base_prefix)

# install dev deps
@install: _require-venv
  # extra flags make this ~ as fast as I want
  pip install -r requirements.txt --quiet --disable-pip-version-check

# run linting and typecheking over the solutions
@lint: _require-venv install
  ruff check --select I --fix
  ruff format --quiet