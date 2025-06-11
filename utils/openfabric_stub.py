
def call_openfabric_app(stub, app_id, input_dict):
    result = stub.call(app_id, input_dict, 'super-user')
    return result.get('result')
