# src/dns_hijack_detector.py

import json
import sys
import os
from collect_subdomains import get_subdomains
from resolve_cname import resolve_cname

def main(domain):
    print(f"🔍 Collecting subdomains for: {domain}")
    subdomains = get_subdomains(domain)
    print(f"✅ Found {len(subdomains)} subdomains")

    resolved = []
    for sd in subdomains[:20]:  # limit for test
        cname = resolve_cname(sd)
        resolved.append({"subdomain": sd, "points_to": cname})

    output_path = os.path.join("..", "data", "resolved_records.json")
    with open(output_path, "w") as f:
        json.dump(resolved, f, indent=2)
    print(f"✅ Saved resolved records to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dns_hijack_detector.py <domain>")
    else:
        main(sys.argv[1])
