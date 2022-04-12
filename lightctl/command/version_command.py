import click

from lightctl.client.healthz_client import HealthzClient
from lightctl.command.common import ContextObject
from lightctl.config import API_VERSION
from lightctl.version import __version__

healthz_client = HealthzClient()


@click.command()
@click.pass_obj
def version(context_obj: ContextObject):
    server_info = healthz_client.get_healthz_info()
    backend_image = server_info["image_and_tags"]["backend"]
    backend_version = backend_image.split("@")[0].split(":")[1]
    res = {
        "api_version": API_VERSION,
        "cluster": f"{healthz_client.url_base} ({backend_version})",
        "version": __version__,
    }
    context_obj.printer.print(res)
