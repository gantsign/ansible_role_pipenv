import os

import testinfra.utils.ansible_runner

import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_version(host):
    version = host.check_output('sudo --set-home --user test_usr1 ' +
                                'bash --login -c "pipenv --version"')
    pattern = r'version [0-9\.]+'
    assert re.search(pattern, version)
