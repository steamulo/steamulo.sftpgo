![Build Status](https://github.com/STEAMULO//steamulo.sftpgo/actions/workflows/test.yml/badge.svg?branch=master)

SFTPGO
=========

Installation and configuration of [SFTPGO](https://github.com/drakkan/sftpgo)

Role Variables
------------

Here are the main variables that should be set :

```yaml
# SFTPGO version you want to install
sftpgo_version: 2.3.5

# URL template for retrieving SFTPGO
sftpgo_archive_url_template: "https://github.com/drakkan/sftpgo/releases/download/v{{ sftpgo_version }}/sftpgo_v{{ sftpgo_version }}_{{ ansible_system | lower }}_x86_64.tar.xz"

# SFTPGO configuration (in yaml)
# see all the configuration options here: https://github.com/drakkan/sftpgo/blob/main/docs/full-configuration.md
sftpgo_configuration:

# SFTPGO user
sftpgo_user: sftpgo

# SFTPGO default admin account
# you need to set data_provider.create_default_admin to true for user initialization
sftpgo_default_admin_username: ""
sftpgo_default_admin_password: ""
```

Development
------------

This role use the [molecule framework](https://molecule.readthedocs.io/en/stable/) in order to simplify the development process.

Requirements:
* [Python 3](https://www.python.org/download)
* [Docker](https://docs.docker.com/get-docker/)

Setup your local environnement with python virtualenv prior to using molecule : `. venv.sh`

This command will create a virtual env, activate it and download python dependencies.

Use ```molecule converge``` to create a local environnement and ```molecule login``` to log into the test machine.

Before any commit ensure that every test are passing with ```molecule test```

License
------------

BSD

Author Information
------------

Steamulo - www.steamulo.com
