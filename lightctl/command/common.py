from lightctl.util import CliPrinter


class ContextObject:
    def __init__(self, printer: CliPrinter):
        self.printer = printer
