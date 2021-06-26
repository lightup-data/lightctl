import click

from lightctl.client.rule_client import RuleClient

rule_client = RuleClient()


@click.group()
def rule():
    pass


@rule.command()
@click.pass_obj
def list(context_obj):
    res = rule_client.list_rules()
    context_obj.printer.print(res)


@rule.command()
@click.argument("id")
@click.pass_obj
def get(context_obj, id):
    res = rule_client.get_rule(id)
    context_obj.printer.print(res)


@rule.command()
@click.argument("id")
@click.pass_obj
def delete(context_obj, id):
    res = rule_client.delete_rule(id)
    context_obj.printer.print(res)


@rule.command()
@click.argument("id")
@click.pass_obj
def clone(context_obj, id):
    res = rule_client.get_rule(id)
    if not res:
        context_obj.printer.print({"error": "not found"})

    res["metadata"].pop("uuid")
    res["metadata"]["name"] += "_Clone"
    res = rule_client.create_rule(res)
    context_obj.printer.print(res)


@rule.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def create(context_obj, file):
    data = context_obj.file_loader.load(file)
    res = rule_client.create_rule(data)
    context_obj.printer.print(res)


@rule.command()
@click.argument("id")
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def update(context_obj, id, file):
    data = context_obj.file_loader.load(file)
    res = rule_client.update_rule(id, data)
    context_obj.printer.print(res)
