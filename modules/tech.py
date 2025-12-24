import requests
from typing import Dict

def detect_tech(domain: str) -> Dict[str, str]:
    """
    Detect technology stack by analyzing HTTP headers.
    """
    tech_info = {}
    protocols = ["https", "http"]
    
    for protocol in protocols:
        try:
            url = f"{protocol}://{domain}"
            response = requests.get(url, timeout=5, allow_redirects=True, verify=False)
            
            headers = response.headers
            if 'Server' in headers:
                tech_info['Server'] = headers['Server']
            if 'X-Powered-By' in headers:
                tech_info['X-Powered-By'] = headers['X-Powered-By']
                
            # Basic cookie analysis
            if 'Set-Cookie' in headers:
                cookies = headers['Set-Cookie']
                if 'JSESSIONID' in cookies:
                    tech_info['Framework'] = 'Java/Spring/JSP'
                elif 'PHPSESSID' in cookies:
                    tech_info['Language'] = 'PHP'
                elif 'csrftoken' in cookies and 'django' in cookies: # Loose check
                    tech_info['Framework'] = 'Django'
            
            # Stop if we got a response
            break
        except requests.RequestException:
            continue
            
    return tech_info
