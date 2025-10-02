from typing import Annotated
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


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def client(
    ctx: typer.Context,
    database: Annotated[
        str, typer.Option(help="The path to the BeaverDB database file.")
    ] = "beaver.db",
):
    """
    Provides a command-line client to interact with the database.

    All arguments after 'client' are passed directly to the database object.
    Example: beaver client --database my.db dict my_dict get my_key
    """
    try:
        import fire
        from .core import BeaverDB
    except ImportError:
        print(
            "Error: To use the client command, please install the CLI dependencies:\n"
            'pip install "beaver-db[cli]"'
        )
        raise typer.Exit(code=1)

    db = BeaverDB(database)
    # The arguments for fire are passed via ctx.args, which captures everything
    # after the 'client' command.
    fire.Fire(db, command=ctx.args)


if __name__ == "__main__":
    app()
