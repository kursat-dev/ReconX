import requests
from typing import List, Set

def enumerate_subdomains(domain: str) -> List[str]:
    """
    Enumerate subdomains using crt.sh certificate transparency logs.
    """
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    subdomains: Set[str] = set()
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                name_value = entry.get('name_value')
                if name_value:
                    # Handle multi-line names (sometimes multiple domains in one cert)
                    lines = name_value.split('\n')
                    for line in lines:
                        if domain in line and '*' not in line:
                             subdomains.add(line.strip())
    except Exception as e:
        # In a real tool we might log this, but for now we'll just return what we found or empty
        print(f"Error enumerating subdomains: {e}")
        pass

    return sorted(list(subdomains))
