import json


def save_object_to_file(object_to_save, output_filename):
    with open(output_filename, 'w') as outfile:
        json.dump(object_to_save, outfile)