import pytest
import os
from ipaddress import IPv4Address
import process_pcap

@pytest.fixture
def extracted_pcap_test_file():
    return process_pcap.get_dst_addresses(file=os.path.join('test_files', 'test_capture.pcap'))

@pytest.fixture
def bad_extracted_pcap_test_file_name():
    return process_pcap.get_dst_addresses(file=os.path.join('test_files', 'bad_file_name.pcap'))

@pytest.fixture
def bad_extracted_pcap_test_file_name():
    return process_pcap.get_dst_addresses(file=os.path.join('test_files', 'bad_format.pcap'))

def test_extract_file_not_exists(bad_extracted_pcap_test_file_name):
    assert bad_extracted_pcap_test_file_name == None

def test_extract_file_bad_format(bad_extracted_pcap_test_file_name):
    assert bad_extracted_pcap_test_file_name == None

def test_extract_dict_len(extracted_pcap_test_file):
    assert len(extracted_pcap_test_file) == 94

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