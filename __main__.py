from openapi_schema_generator.OpenApiSchemaGenerator import OpenApiSchemaGenerator
import argparse
import os
import json
import yaml


def write_json(path, data):
    if ".yml" in path or ".yaml" in path:
        with open(path, "w", encoding='utf8') as f:
            return yaml.dump(data, f)
    if ".json" in path:
        with open(path, "w", encoding='utf8') as f:
            return json.dump(data, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default=None)
    parser.add_argument('--output', type=str, default='result.json')

    args = parser.parse_args()

    if not (args.path and os.path.isfile(args.path)):
        print("Please insert path correctly")
    else:
        generator = OpenApiSchemaGenerator(args.path)
        write_json(args.output, generator.deploy_schema())
