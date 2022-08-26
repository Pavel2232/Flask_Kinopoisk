import sys
import os
import pkg_resources
from pprint import pprint

def get_pythonpath():
    try:
        return os.environ['PYTHONPATH'].split(os.pathsep)
    except KeyError:
        return None

pprint({
    'PATH': os.environ['PATH'].split(os.pathsep),
    'PYTHONPATH': get_pythonpath(),
    'sys.path': sys.path,
    'sys.executable': sys.executable,
    'sys.prefix': sys.prefix,
    'sys.version_info': sys.version_info,
    'pkg_resources.working_set': list(pkg_resources.working_set),
})