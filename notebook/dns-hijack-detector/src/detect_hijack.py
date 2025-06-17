# src/detect_hijack.py

import json
import os

# Step 1: Load resolved DNS records
def load_records(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# Step 2: Detect suspicious subdomains
def detect_suspicious(records, safe_services):
    suspicious = []
    for record in records:
        if record["points_to"] and record["points_to"] not in safe_services:
            suspicious.append(record)
    return suspicious

# Step 3: Main
def main():
    input_path = os.path.join("..", "data", "resolved_records.json")
    records = load_records(input_path)

    safe_services = [
        "ghs.googlehosted.com",
        "pages.github.io",
        "s3.amazonaws.com",
        "c.storage.googleapis.com",
        "sites.google.com"
    ]

    suspicious = detect_suspicious(records, safe_services)

    print(f"🚨 Found {len(suspicious)} suspicious subdomains:")
    for item in suspicious:
        print(f" - {item['subdomain']} → {item['points_to']}")

if __name__ == "__main__":
    main()
