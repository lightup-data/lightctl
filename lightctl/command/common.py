from lightctl.util import CliPrinter, FileLoader


class ContextObject:
    """ an object that pass to child command """

    def __init__(self, printer: CliPrinter, file_loader: FileLoader):
        self.printer = printer
        self.file_loader = file_loader
