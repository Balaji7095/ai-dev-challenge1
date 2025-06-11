
class InputClass:
    def __init__(self, prompt):
        self.prompt = prompt

class OutputClass:
    def __init__(self):
        self.message = ""

class AppModel:
    def __init__(self, request):
        self.request = request
        self.response = OutputClass()

class ConfigClass:
    def __init__(self, app_ids):
        self.app_ids = app_ids

configurations = {'super-user': ConfigClass(['f0997a01-d6d3-a5fe-53d8-561300318557', '69543f29-4d41-4afc-7f29-3d51591f11eb'])}

class Stub:
    def __init__(self, app_ids):
        self.app_ids = app_ids
    def call(self, app_id, payload, user):
        return {'result': b'dummy-data'}
