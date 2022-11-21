import click

from lightctl.client.incident_client import IncidentClient

incident_client = IncidentClient()


@click.group()
def incident():
    """
    configure and query lightup monitors
    """


@incident.command()
@click.argument("id", type=click.UUID)
@click.pass_obj
def get_incident_samples(context_obj, id):
    """
    list specified monitor in a workspace
    """
    res = incident_client.get_incident_samples(context_obj.workspace_id, id)
    context_obj.printer.print(res)
