import click

from lightctl.client.source_client import SourceClient

source_client = SourceClient()


@click.group()
def source():
    """
    used by commands below
    """


@source.command()
@click.pass_obj
def list(context_obj):
    res = source_client.list_sources(context_obj.workspace_id)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def get(context_obj, id):
    res = source_client.get_source(context_obj.workspace_id, id)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def delete(context_obj, id):
    res = source_client.delete_source(context_obj.workspace_id, id)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def clone(context_obj, id):
    res = source_client.get_source(context_obj.workspace_id, id)
    if not res:
        context_obj.printer.print({"error": "not found"})
        return

    res["metadata"].pop("uuid")
    res["metadata"]["name"] += "_Clone"
    res = source_client.create_source(context_obj.workspace_id, res)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def trigger(context_obj, id):
    res = source_client.get_source(context_obj.workspace_id, id)
    if not res:
        context_obj.printer.print({"error": "not found"})
        return
    res = source_client.trigger_source(id)
    context_obj.printer.print(res)


@source.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def create(context_obj, file):
    data = context_obj.file_loader.load(file)
    res = source_client.create_source(context_obj.workspace_id, data)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def update(context_obj, id, file):
    data = context_obj.file_loader.load(file)
    res = source_client.update_source(context_obj.workspace_id, id, data)
    context_obj.printer.print(res)


@source.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def inspect(context_obj, file):
    data = context_obj.file_loader.load(file)
    res = source_client.inspect(context_obj.workspace_id, data)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def list_tables(context_obj, id):
    res = source_client.list_tables(context_obj.workspace_id, id)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.argument("table_name")
@click.pass_obj
def get_schema(context_obj, id, table_name):
    res = source_client.get_schema(context_obj.workspace_id, id, table_name)
    context_obj.printer.print(res)
