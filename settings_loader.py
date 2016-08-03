import yaml
import os
import logging
import sys

primary_config = 'config.yaml',

try:
    primary_config = os.environ['TEMPERATURE_CONFIG']
except Exception as e:
    pass

__yamlfiles__ = [
    "%s" % primary_config,
    '/etc/temperature/config.yaml',
    '/opt/temperature/config.yaml'
]

# USAGE
__doc__ = """
The settingsloader searches for a config.yaml file in:

    - config.yaml
    - /etc/temperature/config.yaml
    - /opt/temperature/config.yaml

The environment variable: :envvar:`TEMPERATURE_CONFIG` can also be used to specify another file. e.g

    TEMPERATURE_CONFIG="/tmp/my.yaml" ./temperature/Update_temperature.py ....

Examples:

    >>> import temperature.settings_loader as settings
    >>> settings.CMDB_URL
    'http://mydomain.com/path'

"""

logging.basicConfig(format='[%(module)s] %(filename)s:%(lineno)s %(asctime)s %(levelname)s %(message)s',
                    stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

logging = logging.getLogger(__name__)
yaml_loaded = False

# defaults which are set / could not be present
defaults = {
    "UPDATE_MOCK_TESTS": False,
    "CMDB_URL": "http://someurl/site.xml",
    "CMDB_FILE": "provision-example.yaml",
    "CMDB_USER": "",
    "CMDB_PASS": "",
    "WEBSERVER_KEY": "data/webserver_key/key.txt",
    "DATA_FOLDER": "data"
}

for yaml_file in __yamlfiles__:
    if not os.path.exists(yaml_file):
        continue

    logging.info("Using yaml file %s" % yaml_file)
    stream = open(yaml_file, 'r')
    yaml_settings = yaml.load(stream)

    # set the defaults
    for default in defaults:
        logging.info("Setting default %s:%s" % (default, defaults[default]))
        globals()[default] = defaults[default]

    # TODO FIXME
    # get each plugins "default" variables and add to globals

    # get the real values if any
    for variable in yaml_settings.keys():
        logging.info("Setting config %s:%s" % (variable, yaml_settings[variable]))
        globals()[variable] = yaml_settings[variable]

    yaml_loaded = True
    logging.debug("Yaml loaded successful")
    break

if yaml_loaded is False:
    msg = "Failed to find config.yaml in any of these locations: %s" % ",".join(__yamlfiles__)
    logging.error(msg)
    raise Exception(msg)
else:

    # DATA_FOLDER = os.path.join("..", globals()['DATA_FOLDER'])
    DATA_FOLDER = globals()['DATA_FOLDER']
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    split = globals()['WEBSERVER_KEY'].split("/")
    WEBSERVER_KEY = os.path.join(globals()['DATA_FOLDER'], *split)
