<div align="center">
    <h1 align="center">SURAK</h1>

</div>

<div align="center">
  <h4>Universal CI/CD Policy Engine</h4>
</div>
<br/>
<p align="center">
<a href="https://pypi.org/project/rbom/"><img alt="SURAK" src="https://img.shields.io/badge/policy-SURAK-ffc900?"></a>
<a href="https://opensource.org/licenses/Apache-2.0"><img alt="PyPI" src="https://img.shields.io/badge/License-Apache_2.0-blue.svg"></a>
<a href="https://pypi.org/project/rbom/"><img alt="PyPI" src="https://img.shields.io/pypi/v/rbom"></a>

</p>

### Overview 

Pluggable engine.


### Dev

```bash
# Setup environment
pyenv install 3.12.0
pyenv local 3.12.0
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Format code
black surak tests
ruff check surak tests
```







03/10/2025
