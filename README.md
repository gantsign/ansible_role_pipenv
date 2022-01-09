Ansible Role: Pipenv
====================

[![Tests](https://github.com/gantsign/ansible_role_pipenv/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible_role_pipenv/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.pipenv-blue.svg)](https://galaxy.ansible.com/gantsign/pipenv)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_pipenv/master/LICENSE)

Role to download and install [Pipenv](https://pipenv.pypa.io/) the package
manager for [Python](https://www.python.org) that combines
[pip](https://pypi.org/project/pip/) with
[Virtualenv](https://virtualenv.pypa.io/en/stable/).

Requirements
------------

* Ansible >= 2.8

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Users to install Pipenv for
pipenv_users: []
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.pipenv
      pipenv_users:
        - example
```

Tab Completion for Zsh
----------------------

### Using Ansible

We recommend using the
[gantsign.antigen](https://galaxy.ansible.com/gantsign/antigen) role to enable
tab completion for Pipenv (this must be configured for each user).

```yaml
- hosts: servers
  roles:
    - role: gantsign.pipenv
      pipenv_users:
        - example

    - role: gantsign.antigen
      users:
        - username: example
          antigen_bundles:
            - name: pipenv
              url: gantsign/zsh-plugins
              location: pipenv
```

### Using Antigen

If you prefer to use [Antigen](https://github.com/zsh-users/antigen) directly
add the following to your Antigen configuration:

```bash
antigen bundle gantsign/zsh-plugins pipenv
```

### Manual configuration

To manually configure Zsh add the following to your `.zshrc`:

```bash
eval "$(pipenv --completion)"
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
