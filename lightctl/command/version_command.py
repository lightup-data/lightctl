import click

from lightctl.client.healthz_client import HealthzClient
from lightctl.config import __version__
from lightctl.util import cli_print

healthz_client = HealthzClient()


@click.command()
def version():
    server_info = healthz_client.get_healthz_info()
    backend_image = server_info["image_and_tags"]["backend"]
    backend_version = backend_image.split("@")[0].split(":")[1]
    res = {"server_version": backend_version, "client_version": __version__}
    cli_print(res)
