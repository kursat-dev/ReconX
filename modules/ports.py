import socket
from typing import List

def scan_ports(domain: str, ports: List[int] = None) -> List[int]:
    """
    Scan a list of common ports on the target domain.
    """
    if ports is None:
        ports = [21, 22, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 3306, 3389, 5432, 8080, 8443]

    open_ports = []
    
    # Resolve domain to IP first to avoid repeated DNS lookups
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        return []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Short timeout for speed
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass
            
    return open_ports
