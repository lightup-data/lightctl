import click

from lightctl.client.incident_client import IncidentClient

incident_client = IncidentClient()


@click.group()
def incident():
    """
    configure and query lightup monitors
    """


@incident.command()
@click.option("--incident_uuid", type=click.UUID)
@click.option("--preview_uuid", type=click.UUID)
@click.pass_obj
def get_incident_samples(context_obj, incident_uuid, preview_uuid):
    """
    list specified monitor in a workspace
    """
    res = incident_client.get_incident_samples(
        context_obj.workspace_id, str(incident_uuid), str(preview_uuid)
    )
    context_obj.printer.print(res)
