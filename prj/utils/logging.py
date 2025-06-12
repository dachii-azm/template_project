import logging

class PrjLogger(logging.Logger):
    def __init__(self, name, level=logging.INFO, filename=None, format_str=None, dateformat=None, stream=None, file=None, style="%"):
        super().__init__(name, level)
        if file is not None:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler(stream)
        self._formatter = logging.Formatter(format_str, dateformat, style)
        handler.setFormatter(self._formatter)
        super().addHandler(handler)

    def debug(self, msg, *args, **kwargs):
        super().debug(msg, *args, **kwargs)

logger = PrjLogger(
    name="prj", level=logging.INFO, format_str="%(message)s"
)
        