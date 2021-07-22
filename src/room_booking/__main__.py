import click


@click.group()
def cli() -> None:
    pass


@cli.command()
def serve() -> None:
    from room_booking.webapp import run_app
    run_app()

if __name__ == '__main__':
    cli()
