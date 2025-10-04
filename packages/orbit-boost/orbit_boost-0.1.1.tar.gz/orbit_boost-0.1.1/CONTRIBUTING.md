# Contributing to Orbit Boost

Thanks for considering a contribution! 🎉

## Quick start
```
git clone https://github.com/abdulvahapmutlu/orbit-boost.git
cd orbit-boost
pip install -e .[dev]
pre-commit install
pytest
```

## Guidelines
- Keep PRs focused and include tests.
- Run `ruff` and `mypy` locally before pushing.
- Write clear commit messages and PR descriptions.

## Testing
- Unit tests live in `tests/`.
- Keep tests fast; avoid large datasets or network calls.

## Reporting issues
- Provide Python version, OS, minimal repro code, and full traceback.
