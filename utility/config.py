import configparser


# noinspection PyPep8
def write_config(file):
    config = configparser.ConfigParser()

    config['api_keys'] = dict()
    # noinspection PyPep8
    config['api_keys']['GoogleV3'] = "'yourapikey' # https://developers.google.com/maps/documentation/javascript/get-api-key"
    config['api_keys']['OpenCage'] = "'yourapikey' # https://geocoder.opencagedata.com/api"

    with open(file, 'w') as file:
        config.write(file)

