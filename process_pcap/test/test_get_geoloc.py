from ipaddress import IPv4Address
import pytest
import process_pcap

@pytest.fixture(scope="session")
def good_geoloc_ip():
    return process_pcap.get_geoloc(IPv4Address('1.1.1.1'))

@pytest.fixture(scope="session")
def bad_geoloc_ip():
    return process_pcap.get_geoloc(IPv4Address('0.0.0.0'))

@pytest.fixture(scope="session")
def bad_data_type_geoloc_ip():
    return process_pcap.get_geoloc("not an ip")

def test_good_geoloc_ip(good_geoloc_ip):
    assert good_geoloc_ip['status'] == "success"

def test_bad_geoloc_ip(bad_geoloc_ip):
    assert bad_geoloc_ip['status'] == "fail"

def test_bad_data_type_geoloc_ip(bad_data_type_geoloc_ip):
    assert bad_data_type_geoloc_ip['status'] == "fail"