import os
import yaml
import sys

def validate_yaml(file_path, count, total_files, failed_flag):
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        print(f"Validation passed for {file_path} ({count}/{total_files})")
    except Exception as e:
        print(f"Validation failed for {file_path}: {str(e)} ({count}/{total_files})")
        failed_flag[0] = True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_yaml.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Get the list of YAML files to be processed
    yaml_files = [f for f in os.listdir(os.path.dirname(file_path)) if f.endswith(".yaml")]

    total_files = len(yaml_files)
    failed_flag = [False]

    for count, yaml_file in enumerate(yaml_files, start=1):
        file_path = os.path.join(os.path.dirname(file_path), yaml_file)
        validate_yaml(file_path, count, total_files, failed_flag)

    if failed_flag[0]:
        sys.exit(1)
