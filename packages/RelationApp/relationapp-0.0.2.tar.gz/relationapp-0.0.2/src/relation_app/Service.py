from .Schema import Schema


class Service:
    access_automation: bool = True

    settings: Schema

    async def init(self):
        pass

    async def run(self, inputs: Schema|None = None):
        pass

    async def run_connections(self, outputs: Schema|None = None):
        pass