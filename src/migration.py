import yaml
from datetime import datetime
import os

LITELLM_BASE_URL = "http://localhost:4000/v1"
DEFAULT_TEMPERATURE = "0"

def yaml_to_models(yaml_string):
    """
    Converts a YAML string to a list of model dictionaries.
    
    :param yaml_string: The YAML string to convert.
    :return: A list of model dictionaries.
    """
    try:
        doc = yaml.safe_load(yaml_string)
        if 'model_list' in doc:
            models = []
            for item in doc['model_list']:
                model = {
                    'id': item['litellm_params']['model'],
                    'updated_at': datetime.now().isoformat(),
                    'created_at': datetime.now().isoformat(),
                    'name': item['model_name'],
                    'prompt': '',  # Default or extracted from YAML if available
                    'option': item['litellm_params']['model'],
                    'temperature': DEFAULT_TEMPERATURE,  # Default or extracted from YAML if available
                    'pinned': False,  # Default or extracted from YAML if available
                    'vision': False,  # Default or extracted from YAML if available
                    'base_url': LITELLM_BASE_URL,
                    # 'original_base_url': item['litellm_params'].get('api_base', 'https://api.openai.com/v1'),
                }
                models.append(model)
            return models
        else:
            raise ValueError("YAML string does not contain 'model_list' key.")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML: {e}")

def models_to_typescript(models):
    """
    Converts a list of model dictionaries to TypeScript model definitions.
    
    :param models: The list of model dictionaries to convert.
    :return: A string containing TypeScript model definitions.
    """
    ts_models = []
    for model in models:
        # Replace characters that may cause issues in TypeScript constant names
        constant_name = model['name'].replace('-', '_').replace('.', '_').upper()
        ts_model = f"""
export const {constant_name}: Model = {{
    id: "{model['id']}",
    updated_at: "{model['updated_at']}",
    created_at: "{model['created_at']}",
    name: "{model['name']}",
    prompt: "{model['prompt']}",
    option: "{model['option']}",
    temperature: "{model['temperature']}",
    pinned: {str(model['pinned']).lower()},
    vision: {str(model['vision']).lower()},
    base_url: "{model['base_url']}",
}};
"""
        ts_models.append(ts_model)
    return "\n".join(ts_models)

def save_to_typescript_file(ts_string, file_path):
    """
    Saves the TypeScript model definitions to a file.
    
    :param ts_string: The TypeScript string to save.
    :param file_path: The path to the file where the TypeScript string will be saved.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(ts_string)
    except Exception as e:
        raise ValueError(f"Error saving TypeScript string to file: {e}")

def convert_yaml_file_to_typescript(yaml_file_path, ts_file_path):
    """
    Converts a YAML file to TypeScript model definitions and saves them to a file.
    
    :param yaml_file_path: The path to the YAML file to convert.
    :param ts_file_path: The path to the file where the TypeScript string will be saved.
    """
    try:
        with open(yaml_file_path, 'r') as file:
            yaml_string = file.read()
        models = yaml_to_models(yaml_string)
        ts_string = models_to_typescript(models)
        save_to_typescript_file(ts_string, ts_file_path)
    except Exception as e:
        raise ValueError(f"Error converting YAML file to TypeScript: {e}")


# Example usage
def main():
    INPUT_FILE = "models.yml"
    OUTPUT_FILE = "models.ts"
    INPUTS_DIR = os.path.join("data/inputs")
    OUTPUTS_DIR = os.path.join("data/outputs")
    yaml_file_path = os.path.join(INPUTS_DIR, INPUT_FILE)
    ts_file_path = os.path.join(OUTPUTS_DIR, OUTPUT_FILE)
    convert_yaml_file_to_typescript(yaml_file_path, ts_file_path)

if __name__ == "__main__":
    main()
