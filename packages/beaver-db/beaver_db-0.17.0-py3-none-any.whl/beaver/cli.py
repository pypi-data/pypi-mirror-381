import typer
import rich

app = typer.Typer()


@app.command()
def serve(
    database: str = typer.Option(
        "beaver.db", "--database", "-d", help="Path to the database file."
    ),
    host: str = typer.Option(
        "127.0.0.1", "--host", "-h", help="The host to bind the server to."
    ),
    port: int = typer.Option(
        8000, "--port", "-p", help="The port to run the server on."
    ),
):
    """
    Starts a RESTful API server for a BeaverDB instance.
    """
    try:
        from .server import serve as run_server
    except ImportError as e:
        rich.print(f"[red]Error: {e}[/]")
        rich.print('[yellow]Please install the server dependencies with `pip install "beaver-db[server]"`[/]')
        raise typer.Exit(code=1)

    rich.print(f"[blue]Starting server for database at '{database}' on http://{host}:{port}[/]")
    run_server(db_path=database, host=host, port=port)


if __name__ == "__main__":
    app()
