from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.service.pluggin_runner import run_plugin


class x(ActionRunner):

    @staticmethod
    async def build(**kwargs):
        print('build', kwargs)
        return x(**kwargs)

    def __init__(self, **kwargs):
        print('init', kwargs)

    async def run(self, payload):
        print('run', payload)

    async def close(self):
        print('close')


run_plugin(x, {"init": 1}, {"payload": 2})
