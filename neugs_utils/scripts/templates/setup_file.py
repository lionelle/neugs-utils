from typing import Dict, Any


__setup_template = """#!/usr/bin/env bash
## Autogenerated template by neugs_utils
{c_setup}
apt-get install -y python3 python3-pip python3-dev
pip3 install -r /autograder/source/requirements.txt
"""

__c_setup = """
apt-get install -y clang
apt-get install -y gcc
"""


def build_setup(config: Dict[str, Any]) -> str:
    """Builds the setup based on config options. Currently
    just simple subs


    Args:
        config (Dict[str, Any]): the config options

    Returns:
        str: the file to write
    """
    cstring = __c_setup if config["cpp"] else ""
    return __setup_template.format(c_setup=cstring)