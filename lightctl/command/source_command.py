import click

from lightctl.client.source_client import SourceClient

source_client = SourceClient()


@click.group()
def source():
    """
    configure and query lightup datasources
    """


@source.command()
@click.pass_obj
def list(context_obj):
    """
    list all datasources configurations in a workspace
    """
    res = source_client.list_sources(context_obj.workspace_id)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def get(context_obj, id):
    """
    list datasource configuration for specified uuid in a workspace
    """
    res = source_client.get_source(context_obj.workspace_id, id)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def delete(context_obj, id):
    """
    delete datasource based on specified uuid
    """
    res = source_client.delete_source(context_obj.workspace_id, id)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def trigger(context_obj, id):
    """
    trigger a datasource scan, if datasource is configured as triggered
    """
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
    """
    create a datasource in the workspace from json or yaml file
    """
    data = context_obj.file_loader.load(file)
    res = source_client.create_source(context_obj.workspace_id, data)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def update(context_obj, id, file):
    """
    update datasource in the workspace from json or yaml file
    """
    data = context_obj.file_loader.load(file)
    res = source_client.update_source(context_obj.workspace_id, id, data)
    context_obj.printer.print(res)


@source.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def inspect(context_obj, file):
    """
    test datasource configuration validity without saving it
    """
    data = context_obj.file_loader.load(file)
    res = source_client.inspect(context_obj.workspace_id, data)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.pass_obj
def list_tables(context_obj, id):
    """
    list all tables in a datasource
    """
    res = source_client.list_tables(context_obj.workspace_id, id)
    context_obj.printer.print(res)


@source.command()
@click.argument("id")
@click.argument("table_name")
@click.pass_obj
def get_table_schema(context_obj, id, table_name):
    """
    get schema for a table in a datasource
    """
    res = source_client.get_schema(context_obj.workspace_id, id, table_name)
    context_obj.printer.print(res)
