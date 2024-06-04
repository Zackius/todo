from flask import request


def validating_required_inputs_for_each_services(required_data:list, input_data: object):
    for r in required_data:
        value = input_data.get(r)
        if not value and value != None and value != 0 and value != bool:
            print(f'ERROR. Input validation failed: REQUIRED: {required_data}, INPUT: {input_data}')
            return False

    return True