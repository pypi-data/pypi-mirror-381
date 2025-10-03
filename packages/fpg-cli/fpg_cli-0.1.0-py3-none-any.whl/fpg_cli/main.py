"""Fantasy Premier Game CLI main module.

Provides command-line interface commands for interacting with the Fantasy Premier Game API.
"""

# fpg_cli/main.py

import requests
import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer(help="Fantasy Premier Game CLI")

API_BASE = "https://fpg-app.com"  # change to your FastAPI URL


@app.command()
def current_round(player_id: int | None):
    """Fetch the current round from the API."""
    params = {"player_id": player_id} if player_id else {}
    data = requests.get(url=f"{API_BASE}/current_round", params=params, timeout=10).json()

    console.print(f"[bold green]✔ Current Round:[/bold green] {data['Round ID']}")
    console.print(f"[bold blue]📅 Season:[/bold blue] {data['season']}")


@app.command()
def available_choices(player_id: int | None, season: int | None = None):
    """Fetch available choices from the API."""
    params = {"player_id": player_id, "season": season}
    data = requests.get(url=f"{API_BASE}/get_available_choices", params=params, timeout=10).json()

    table = Table(title=f"⚽ Available Choices for Player {player_id} (Season {season})")

    table.add_column("#", style="cyan", justify="right")
    table.add_column("Team", style="magenta", justify="left")

    for i, team in enumerate(data, start=1):
        table.add_row(str(i), team["TEAM_NAME"])

    console.print(table)


if __name__ == "__main__":
    app()
