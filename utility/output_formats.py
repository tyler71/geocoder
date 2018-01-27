import json
import csv
import pprint

import io


def output_json(input_object):
    """Convert object to json"""
    return json.dumps(input_object).strip()


def output_python(input_object):
    """Convert object to python"""
    output = io.StringIO()
    pprint.pprint(input_object, stream=output)
    return output.getvalue().strip()


def output_csv(input_object):
    """Convert object to csv"""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(input_object.values())
    return output.getvalue().strip()
