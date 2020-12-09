import click

from lightctl.client.source_client import SourceClient
from lightctl.util import cli_print

source_client = SourceClient()


@click.group()
@click.option(
    "--json", "use_json", default=False, is_flag=True, help="Use json instead of yaml"
)
@click.pass_context
def source(use_json):
    ctx.obj.use_json = use_json


@source.command()
def list(ctx):
    res = source_client.list_sources()
    cli_print(res, ctx.obj.use_json)


@source.command()
@click.argument("id")
def get(ctx, id):
    res = source_client.get_source(id)
    cli_print(res, ctx.obj.use_json)


@source.command()
@click.argument("input", type=str)
def create(ctx, input):
    res = source_client.create_source_with_file(input, ctx.obj.use_json)
    cli_print(res, ctx.obj.use_json)


@source.command()
@click.argument("id")
@click.argument("input", type=str)
def update(ctx, id, input):
    res = source_client.update_source(id, input, ctx.obj.use_json)
    cli_print(res, ctx.obj.use_json)


@source.command()
@click.argument("id")
def delete(ctx, id):
    res = source_client.delete_source(id)
    cli_print(res, ctx.obj.use_json)
