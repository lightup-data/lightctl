import click

from lightctl.client.source_client import SourceClient

source_client = SourceClient()


@click.group()
def source():
    pass


@source.command()
@click.pass_obj
def list(context_obj):
    res = source_client.list_sources()
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def get(context_obj, id):
    res = source_client.get_source(id)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def delete(context_obj, id):
    res = source_client.delete_source(id)
    context_obj.printer.print(res)
