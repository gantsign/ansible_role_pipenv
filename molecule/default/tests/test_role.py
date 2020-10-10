import re


def test_version(host):
    version = host.check_output('sudo --set-home --user test_usr1 ' +
                                'bash --login -c "export LC_ALL=C.UTF-8; ' +
                                'export LANG=C.UTF-8; pipenv --version"')
    pattern = r'version [0-9\.]+'
    assert re.search(pattern, version)
