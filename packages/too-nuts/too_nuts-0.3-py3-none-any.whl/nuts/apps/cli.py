import click

from . import init, kml_download, listen, make_config, run, single


@click.group()
def cli():
    pass


cli.add_command(make_config.make_config)
cli.add_command(listen.listen)
cli.add_command(run.run)
cli.add_command(single.single)
cli.add_command(init.init)
# cli.add_command(kml_download.get_kml)


@click.command(name="gui")
@click.option("--port", default=8501, help="Port to run the Streamlit server on.")
@click.option(
    "--open/--no-open", default=True, help="Open the browser when the server is ready."
)
@click.option(
    "--background/--no-background",
    default=False,
    help="Run Streamlit in the background.",
)
def ui(port: int, open: bool, background: bool) -> None:
    """Run the NuTS GUI"""
    try:
        from . import UI as ui_mod
    except Exception as e:
        raise click.ClickException(f"Failed to import UI module: {e}")

    # UI.GUI is a click Command object; its underlying Python function is available
    # as .callback. Call that to execute the command logic without re-importing click.
    try:
        return ui_mod.GUI.callback(port=port, open=open, background=background)
    except AttributeError:
        # Fallback: call directly if UI.GUI is a plain function
        return ui_mod.GUI(port=port, open=open, background=background)


cli.add_command(ui)
