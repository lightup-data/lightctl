from lightctl.util import CliPrinter


class ContextObject:
    """ an object that pass to child command """

    def __init__(self, printer: CliPrinter):
        self.printer = printer
