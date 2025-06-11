
import logging
from utils.llm_utils import expand_prompt
from utils.openfabric_stub import call_openfabric_app
from utils.memory import save_to_memory, retrieve_from_memory
from utils.schemas import AppModel, InputClass, OutputClass, ConfigClass, configurations, Stub

def execute(model: AppModel) -> None:
    request: InputClass = model.request
    user_config: ConfigClass = configurations.get('super-user', None)
    logging.info(f"{configurations}")

    app_ids = user_config.app_ids if user_config else []
    stub = Stub(app_ids)

    prompt = request.prompt
    expanded_prompt = expand_prompt(prompt)
    save_to_memory(prompt, expanded_prompt)

    # Call Text-to-Image app
    image_result = call_openfabric_app(stub, 'f0997a01-d6d3-a5fe-53d8-561300318557', {'prompt': expanded_prompt})
    with open('assets/generated.png', 'wb') as f:
        f.write(image_result)

    # Call Image-to-3D app
    model_result = call_openfabric_app(stub, '69543f29-4d41-4afc-7f29-3d51591f11eb', {'image': image_result})
    with open('assets/model.glb', 'wb') as f:
        f.write(model_result)

    response: OutputClass = model.response
    response.message = f"Generated 3D model from prompt: {prompt}"
