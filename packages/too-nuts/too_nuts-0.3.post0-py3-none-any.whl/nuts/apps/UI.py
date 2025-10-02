"""
Module to run the GCN and TNS listeners via the command line interface.
:Author: Tobias Heibges (theibges@mines.edu)
:Last edit by: Tobias Heibges (theibges@mines.edu)
:Date: 2024-03-11
"""

import os
import subprocess
import sys
import webbrowser
from pathlib import Path

import click


@click.command()
@click.option("--port", default=8501, help="Port to run the Streamlit server on.")
@click.option(
    "--open/--no-open", default=True, help="Open the browser when the server is ready."
)
@click.option(
    "--background/--no-background",
    default=False,
    help="Run Streamlit in the background.",
)
def GUI(port: int, open: bool, background: bool) -> None:
    """Launch the Streamlit GUI as a child process.

    This avoids importing Streamlit in the CLI process. It starts a child Python
    process using the same interpreter (sys.executable -m streamlit run ...),
    sets STREAMLIT_SUPPRESS_CONFIG_WARNINGS in the child's environment, and
    optionally opens a browser when the server is ready.
    """
    this_path = Path(__file__)
    gui_path = this_path.parent.parent.resolve() / "UI/tabs_GUI.py"

    env = os.environ.copy()
    env.setdefault("STREAMLIT_SUPPRESS_CONFIG_WARNINGS", "true")

    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(gui_path),
        "--server.port",
        str(port),
        "--server.headless",
        "true",
    ]

    if background:
        proc = subprocess.Popen(
            cmd,
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        click.echo(
            f"Started Streamlit GUI in background (pid={proc.pid}) on port {port}"
        )
        return

    # Foreground: stream output and open browser when ready
    proc = subprocess.Popen(
        cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )
    opened = False
    try:
        for line in proc.stdout:
            # Filter out noisy Streamlit warning about ScriptRunContext
            if "missing ScriptRunContext" in line or "ScriptRunContext" in line:
                continue

            click.echo(line.rstrip())
            if (not opened) and (
                "You can now view your Streamlit app" in line
                or "Local URL" in line
                or "Network URL" in line
            ):
                if open:
                    webbrowser.open(f"http://localhost:{port}")
                opened = True
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
        raise
