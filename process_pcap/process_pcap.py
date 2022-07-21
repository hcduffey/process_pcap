from ipaddress import IPv4Address
import pcapkit
import requests

def get_dst_addresses(file: str) -> dict:
    """
    This function processes a pcap file, returning a dict that contains the dst addresses and their frequency contained in that file.

    Parameters
    ----------
    file : str
        Filename for the pcap file to be processed
    
    Returns
    -------
    dict
        A dict containing all dst ip addresses (key) and their frequencies in the file (value) 
    None
        if there is an unrecoverable error
    """
    try:
        extraction = pcapkit.extract(fin=file, fout=None, nofile=True, format='json', extension=False)
    except FileNotFoundError:
        return None
    except pcapkit.utilities.exceptions.FileError:
        return None
    
    frames = extraction.frame
    dst_addresses = {}

    for frame in frames:
        try:
            dst_addr = frame["ethernet"]["ipv4"]["dst"]

            if(dst_addr.is_private):
                continue

            if dst_addr in dst_addresses:
                dst_addresses[dst_addr.exploded] += 1
            else:
                dst_addresses[dst_addr.exploded] = 1

        except KeyError:
            continue

    return dst_addresses

def get_geoloc(ip_address: IPv4Address): 
    """
    This function retreives geoloc information for a given IP address from a REST end-point provided by ip-api.com.
    Parameters
    ----------
    ip_address : IPv4Address
        The IP address to be used for retrieving geoloc info
    
    Returns
    -------
    json
        a json object containing the geoloc info 
    None
        if there is an unrecoverable error
    """
    connection_attempts = 0

    while(connection_attempts < 3):
        try:
            url = f"http://ip-api.com/json/{ip_address}"
            r = requests.get(url=url)  
            r.raise_for_status()

            if r.status_code == 200:
                return r.json()

        except requests.exceptions.HTTPError:
            return None
        except requests.exceptions.ConnectionError:
            return None
        except requests.exceptions.Timeout:
            connection_attempts += 1
            continue

    return None


