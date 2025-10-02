import shutil
from pathlib import Path

import click


@click.argument("path", type=str, default="./", required=False)
@click.command()
def init(path: str):
    """Initialize the NUTS directory structure."""
    build_init(path)


def build_init(path: str):
    path = Path(path).resolve()

    # Create the directory structure for NUTS
    print(f"Creating NUTS directory structure at {path}...")
    catalogs = path
    if catalogs.exists():
        print(f"Path {catalogs} already exists. No changes made.")
        return
    # Create the main directories
    catalogs.mkdir(parents=True, exist_ok=True)
    database = catalogs / "Database"
    database.mkdir(parents=True, exist_ok=True)
    general = catalogs / "General"
    general.mkdir(parents=True, exist_ok=True)
    listeners = catalogs / "Listeners"
    listeners.mkdir(parents=True, exist_ok=True)
    pointing = catalogs / "Pointing"
    pointing.mkdir(parents=True, exist_ok=True)
    trajectories = catalogs / "Trajectories"
    trajectories.mkdir(parents=True, exist_ok=True)
    gcn = listeners / "GCN"
    gcn.mkdir(parents=True, exist_ok=True)
    gcn_unknown = gcn / "unknown"
    gcn_unknown.mkdir(parents=True, exist_ok=True)
    tns = listeners / "TNS"
    tns.mkdir(parents=True, exist_ok=True)

    # Copy the required data into the appropriate directories
    print("Copying initial data files...")
    steady_database = (
        Path(__file__).parent.parent / "Catalogs" / "Database" / "SteadySources.csv"
    )
    if steady_database.exists():
        shutil.copy(steady_database, database)
    else:
        print(f"Error: {steady_database} does not exist. Skipping copy.")

    gcn_alerts = (
        Path(__file__).parent.parent / "Catalogs" / "General" / "GCN_alerts.csv"
    )
    if gcn_alerts.exists():
        shutil.copy(gcn_alerts, general)
    else:
        print(
            f"Error: {steady_database} does not exist. Skipping copy. This is a required file for NUTS to function properly."
        )

    priorities = (
        Path(__file__).parent.parent / "Catalogs" / "General" / "Priorities.csv"
    )
    if priorities.exists():
        shutil.copy(priorities, general)
    else:
        print(
            f"Error: {steady_database} does not exist. Skipping copy. This is a required file for NUTS to function properly."
        )
