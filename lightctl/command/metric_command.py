import click

from lightctl.client.metric_client import MetricClient

metric_client = MetricClient()


@click.group()
def metric():
    """
    used by commands below
    """


@metric.command()
@click.pass_obj
def list(context_obj):
    res = metric_client.list_metrics()
    context_obj.printer.print(res)


@metric.command()
@click.argument("id", type=click.UUID)
@click.pass_obj
def get(context_obj, id):
    res = metric_client.get_metric(id)
    context_obj.printer.print(res)


@metric.command()
@click.argument("id")
@click.pass_obj
def delete(context_obj, id):
    res = metric_client.delete_metric(id)
    context_obj.printer.print(res)


@metric.command()
@click.argument("id")
@click.pass_obj
def clone(context_obj, id):
    res = metric_client.get_metric(id)
    if not res:
        context_obj.printer.print({"error": "not found"})

    res["metadata"].pop("uuid")
    res["metadata"]["name"] += "_Clone"
    res = metric_client.create_metric(res)
    context_obj.printer.print(res)


@metric.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def create(context_obj, file):
    data = context_obj.file_loader.load(file)
    res = metric_client.create_metric(data)
    context_obj.printer.print(res)


@metric.command()
@click.argument("id")
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def update(context_obj, id, file):
    data = context_obj.file_loader.load(file)
    res = metric_client.update_metric(id, data)
    context_obj.printer.print(res)


@metric.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def inspect_schema(context_obj, file):
    data = context_obj.file_loader.load(file)
    res = metric_client.inspect_schema(data)
    context_obj.printer.print(res)


@metric.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def inspect_data(context_obj, file):
    data = context_obj.file_loader.load(file)
    res = metric_client.inspect_schema(data)
    context_obj.printer.print(res)


@metric.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_obj
def inspect_distinct_values(context_obj, file):
    data = context_obj.file_loader.load(file)
    res = metric_client.inspect_distinct_values(data)
    context_obj.printer.print(res)


@metric.command()
@click.argument("id", type=click.UUID)
@click.pass_obj
def get_schema(context_obj, id):
    res = metric_client.get_schema(id)
    context_obj.printer.print(res)
