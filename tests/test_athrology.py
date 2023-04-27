import json
import jsonschema
import pytest

def test_athrology_data():
    # Load the JSON schema
    with open('../schemas/athrology.schema.json', 'r') as f:
        schema = json.load(f)

    # Load the JSON data
    with open('./inputs/athrology/athrology-data.json', 'r') as f:
        data = json.load(f)

    # Validate the data against the schema
    jsonschema.validate(data, schema)

def test_athrology_no_joints():
    # Load the JSON schema
    with open('../schemas/athrology.schema.json', 'r') as f:
        schema = json.load(f)

    # Load the JSON data
    with open('./inputs/athrology/athrology-no-joints.json', 'r') as f:
        data = json.load(f)

    with pytest.raises(jsonschema.ValidationError) as exc_info:
        jsonschema.validate(instance=data, schema=schema)
    assert "None is not of type 'array'" in str(exc_info.value)

def test_athrology_null_joint():
    # Load the JSON schema
    with open('../schemas/athrology.schema.json', 'r') as f:
        schema = json.load(f)

    # Load the JSON data
    with open('./inputs/athrology/athrology-null-joint.json', 'r') as f:
        data = json.load(f)

    with pytest.raises(jsonschema.ValidationError) as exc_info:
        jsonschema.validate(instance=data, schema=schema)
    assert "None is not of type 'string'" in str(exc_info.value)
