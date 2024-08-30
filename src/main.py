from fastapi import FastAPI

from helpers.ioc_core import IOCCore


class Application(FastAPI):
    def __init__(self, ioc_core=IOCCore()):
        super().__init__()
        self._ioc_core = ioc_core


app = Application()
