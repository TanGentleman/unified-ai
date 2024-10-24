# test_migration.py

"""
Guide for Using Functions and Performing Tests

This module contains tests for functions that convert YAML to models, models to TypeScript,
and save TypeScript and YAML strings to files. The tests are written using the pytest framework.

Functions:
- test_yaml_to_models: Tests the conversion of a YAML string to a list of model dictionaries.
- test_models_to_typescript: Tests the conversion of a list of model dictionaries to a TypeScript string.
- test_save_to_typescript_file: Tests saving a TypeScript string to a file.
- save_files_to_subfolder: Saves TypeScript and YAML strings to files in a specified subfolder.
- test_save_files_to_subfolder: Tests saving TypeScript and YAML strings to files in a subfolder.

How to Run Tests:
1. Ensure pytest is installed in your environment. You can install it using pip:   ```
   pip install pytest   ```

2. Run the tests using the following command in the terminal:   ```
   pytest py-src/test_migration.py   ```

3. The test results will be displayed in the terminal, indicating which tests passed or failed.

Note:
- The `tmp_path` fixture provided by pytest is used to create temporary directories for file operations during testing.
- Ensure that the `migration` module is correctly implemented and available in the `py-src` directory.
"""

import pytest
from migration import yaml_to_models, models_to_typescript, save_to_typescript_file
import os

def test_yaml_to_models():
    """
    Test the conversion of a YAML string to a list of model dictionaries.
    """
    yaml_string = """
    model_list:
      - model_name: test-model
        litellm_params:
          model: test-model-id
          api_base: http://example.com/api
    """
    models = yaml_to_models(yaml_string)
    assert len(models) == 1, "Expected one model in the list"
    assert models[0]['name'] == 'test-model', "Model name mismatch"
    assert models[0]['id'] == 'test-model-id', "Model ID mismatch"
    assert models[0]['base_url'] == 'http://example.com/api', "Base URL mismatch"

def test_models_to_typescript():
    """
    Test the conversion of a list of model dictionaries to a TypeScript string.
    """
    models = [{
        'id': 'test-model-id',
        'updated_at': '2023-10-01T00:00:00',
        'created_at': '2023-10-01T00:00:00',
        'name': 'test-model',
        'prompt': '',
        'option': 'test-model-id',
        'temperature': '1',
        'pinned': False,
        'vision': False,
        'base_url': 'http://example.com/api',
    }]
    ts_string = models_to_typescript(models)
    assert 'export const TEST_MODEL' in ts_string, "TypeScript export statement missing"
    assert 'id: "test-model-id"' in ts_string, "Model ID not found in TypeScript string"

def test_save_to_typescript_file(tmp_path):
    """
    Test saving a TypeScript string to a file.
    """
    ts_string = 'export const TEST_MODEL = {};'
    file_path = tmp_path / 'models.ts'
    save_to_typescript_file(ts_string, file_path)
    assert file_path.read_text() == ts_string, "File content mismatch"

def save_files_to_subfolder(ts_string, yml_string, subfolder_name='generated_files'):
    """
    Save TypeScript and YAML strings to files in a specified subfolder.

    Args:
        ts_string (str): The TypeScript string to save.
        yml_string (str): The YAML string to save.
        subfolder_name (str): The name of the subfolder to save files in.
    """
    # Create the subfolder path
    subfolder_path = os.path.join('tests', subfolder_name)
    
    # Create the subfolder if it doesn't exist
    os.makedirs(subfolder_path, exist_ok=True)
    
    # Define file paths
    ts_file_path = os.path.join(subfolder_path, 'models.ts')
    yml_file_path = os.path.join(subfolder_path, 'models.yml')
    
    # Save the TypeScript string to a file
    with open(ts_file_path, 'w') as ts_file:
        ts_file.write(ts_string)
    
    # Save the YAML string to a file
    with open(yml_file_path, 'w') as yml_file:
        yml_file.write(yml_string)

def test_save_files_to_subfolder(tmp_path):
    """
    Test saving TypeScript and YAML strings to files in a subfolder.
    """
    ts_string = 'export const TEST_MODEL = {};'
    yml_string = """
    model_list:
      - model_name: test-model
        litellm_params:
          model: test-model-id
          api_base: http://example.com/api
    """
    save_files_to_subfolder(ts_string, yml_string)
    subfolder_path = os.path.join('tests', 'generated_files')
    assert os.path.exists(os.path.join(subfolder_path, 'models.ts')), "TypeScript file not found"
    assert os.path.exists(os.path.join(subfolder_path, 'models.yml')), "YAML file not found"
