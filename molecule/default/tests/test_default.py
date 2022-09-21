import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sftpgo_running_and_enabled(host):
    service = host.service("sftpgo")
    assert service.is_running
    assert service.is_enabled


def test_sftpgo_listening_sftp(host):
    assert host.socket("tcp://0.0.0.0:2022").is_listening


def test_sftpgo_listening_http(host):
    assert host.socket("tcp://127.0.0.1:8080").is_listening


def test_sftpgo_health(host):
    resp = host.run("curl http://localhost:8080/healthz").stdout
    assert 'ok' in resp
