# collect_subdomains.py

import requests

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        resp = requests.get(url, timeout=30)  # increased timeout from 10 to 30
        resp.raise_for_status()
        if resp.text.strip() == "":
            print("⚠️ crt.sh returned an empty response.")
            return []
        data = resp.json()
    except Exception as e:
        print(f"❌ Error fetching from crt.sh: {e}")
        return []

    subdomains = set()
    for entry in data:
        names = entry.get("name_value", "").split('\n')
        for sub in names:
            if domain in sub:
                subdomains.add(sub.strip().lower())
    return list(subdomains)
