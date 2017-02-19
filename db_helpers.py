import json


def save_object_to_file(object_to_save, output_filename):
    with open(output_filename, 'w') as outfile:
        json.dump(object_to_save, outfile)


def get_object_from_file(input_filename):
    with open(input_filename, 'r') as infile:
        return json.load(infile)