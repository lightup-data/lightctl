import click

from lightctl.client.healthz_client import HealthzClient
from lightctl.command.common import ContextObject
from lightctl.config import API_VERSION, __version__

healthz_client = HealthzClient()


@click.command()
@click.pass_obj
def version(context_obj: ContextObject):
    server_info = healthz_client.get_healthz_info()
    backend_image = server_info["image_and_tags"]["backend"]
    backend_version = backend_image.split("@")[0].split(":")[1]
    res = {
        "server_version": backend_version,
        "client_version": __version__,
        "api_version": API_VERSION,
    }
    context_obj.printer.print(res)
