# SCA-Unit TestPyPI Publishing

Goal: publish SCA-Unit first to TestPyPI before publishing to real PyPI.

## Important rule

Do not store PyPI tokens in the repository.
Do not commit passwords or API keys.

## Publishing order

1. Run tests.
2. Build dist files.
3. Run twine check.
4. Upload to TestPyPI using a token.
5. Install from TestPyPI in a clean environment.
6. Only then consider real PyPI.
