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
def current_round(player_id: int | None = None):
    """Fetch the current round from the API."""
    params = {"player_id": player_id} if player_id else {}
    data = requests.get(url=f"{API_BASE}/current_round", params=params, timeout=10).json()

    console.print(f"[bold green]✔ Current Round:[/bold green] {data['Round ID']}")
    console.print(f"[bold blue]📅 Season:[/bold blue] {data['season']}")


@app.command()
def available_choices(player_id: int | None = None, season: int | None = None):
    """Fetch available choices from the API."""
    params = {"player_id": player_id, "season": season}
    data = requests.get(url=f"{API_BASE}/get_available_choices", params=params, timeout=10).json()

    table = Table(title=f"⚽ Available Choices for Player {player_id} (Season {season})")

    table.add_column("#", style="#E6FF2B", justify="left")
    table.add_column("Team", style="#0B4650", justify="left")

    for i, team in enumerate(data, start=1):
        table.add_row(str(i), team["TEAM_NAME"])

    console.print(table)


@app.command()
def standings(season: int | None = None):
    """Fetch league standings from the API."""
    params = {"season": season} if season else {}
    data = requests.get(url=f"{API_BASE}/get_standings", params=params, timeout=10).json()

    table = Table(title=f"🏆 League Standings (Season {season})")

    table.add_column("#", style="#E6FF2B", justify="right")
    table.add_column("Player", style="#0B4650", justify="left")
    table.add_column("Goal Difference", style="#FF5733", justify="right")
    table.add_column("Points", style="#00FF00", justify="right")

    for entry in data:
        table.add_row(str(entry["Position"]), entry["User"], str(entry["Goal Diff"]), str(entry["Score"]))

    console.print(table)


@app.command()
def choices(season: int | None = None, round: int | None = None, method: int | None = 0):
    """Fetch all choices from the API."""
    params = {"season": season, "round_id": round, "inc_method": bool(method)}
    data = requests.get(url=f"{API_BASE}/get_choices", params=params, timeout=10).json()

    if not bool(method):
        table = Table(title=f"📋 All Choices (Season {season}, Round {round})")

        table.add_column("Player ID", style="#E6FF2B", justify="left")
        table.add_column("Choice", style="#FF5733", justify="left")

        for i, (team_id, team_name) in enumerate(data.items(), start=1):
            table.add_row(team_id, team_name)
    else:
        table = Table(title=f"📋 All Choices with Method (Season {season}, Round {round})")

        table.add_column("Player ID", style="#E6FF2B", justify="left")
        table.add_column("Choice", style="#FF5733", justify="left")
        table.add_column("Method", style="#00FF00", justify="left")

        for i, (team_id, details) in enumerate(data.items(), start=1):
            table.add_row(team_id, details["Choice"], details["Method"])

    console.print(table)


if __name__ == "__main__":
    app()
