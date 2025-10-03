# FPG CLI

[![PyPI version](https://img.shields.io/pypi/v/fpg-cli.svg?color=blue)](https://pypi.org/project/fpg-cli/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)

A command-line interface for the **Fantasy Premier Game (FPG)**.
Quickly check rounds, make choices, and view standings — all from your terminal.

## Features

- Get the current round and season
- View available team choices
- Submit or update your weekly choices
- Fetch standings, points, and player info
- Prettified output with **Rich** tables & colors
- Installable via `pip` or `uv`

## Installation

From PyPI:

```bash
pip install fpg-cli
```

Or with **uv**:

```bash
uv tool install fpg-cli
```

## Usage

Show commands:

```bash
fpg --help
```

Examples:

```bash
# Get current round
fpg current-round --player-id 6

# See available choices
fpg available-choices --player-id 6 --season 2025

```

Sample output:

```
Available Choices for Player 6 (Season 2025)
────────────────────────────────────────────
#   Team
1   Manchester United
2   Newcastle
3   Bournemouth
…
20  Sunderland
```

## Development

```bash
git clone https://github.com/yourusername/fpg-cli.git
cd fpg-cli
uv pip install -e .
```

## Roadmap

- [ ] Interactive team selection (arrow-key menu)
- [ ] Store default player ID and season in a config file
- [ ] Authentication (Firebase JWT)
- [ ] Publish to PyPI with versioning
- [ ] CI/CD release pipeline (GitHub Actions)

## License

This project is licensed under the [MIT License](LICENSE).
