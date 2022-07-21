import pytest
import os
import process_pcap

@pytest.fixture
def extracted_pcap_test_file():
    return process_pcap.get_dst_addresses(file=os.path.join('test', 'test_capture.pcap'))

@pytest.fixture
def bad_extracted_pcap_test_file_name():
    return process_pcap.get_dst_addresses(file=os.path.join('test', 'bad_file_name.pcap'))

@pytest.fixture
def bad_extracted_pcap_test_file_name():
    return process_pcap.get_dst_addresses(file=os.path.join('test', 'bad_format.pcap'))

def test_extract_file_not_exists(bad_extracted_pcap_test_file_name):
    assert bad_extracted_pcap_test_file_name == None

def test_extract_file_bad_format(bad_extracted_pcap_test_file_name):
    assert bad_extracted_pcap_test_file_name == None

def test_extract_dict_len(extracted_pcap_test_file):
    assert len(extracted_pcap_test_file) == 94
