import click

from lightctl.client.monitor_client import MonitorClient

monitor_client = MonitorClient()


@click.group()
def monitor():
    """
    used by commands below
    """


@monitor.command()
@click.pass_obj
def list(context_obj):
    res = monitor_client.list_monitors()
    context_obj.printer.print(res)


@monitor.command()
@click.argument("id")
@click.pass_obj
def get(context_obj, id):
    res = monitor_client.get_monitor(id)
    context_obj.printer.print(res)


@monitor.command()
@click.argument("id")
@click.pass_obj
def delete(context_obj, id):
    res = monitor_client.delete_monitor(id)
    context_obj.printer.print(res)


@monitor.command()
@click.argument("id")
@click.pass_obj
def clone(context_obj, id):
    res = monitor_client.get_monitor(id)
    if not res:
        context_obj.printer.print({"error": "not found"})

    res["metadata"].pop("uuid")
    res["metadata"]["name"] += "_Clone"
    res = monitor_client.create_monitor(res)
    context_obj.printer.print(res)


@monitor.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def create(context_obj, file):
    data = context_obj.file_loader.load(file)
    res = monitor_client.create_monitor(data)
    context_obj.printer.print(res)


@monitor.command()
@click.argument("id")
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def update(context_obj, id, file):
    data = context_obj.file_loader.load(file)
    res = monitor_client.update_monitor(id, data)
    context_obj.printer.print(res)
