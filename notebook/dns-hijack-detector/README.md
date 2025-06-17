# 🛡️ DNS Hijack Detector using Python

This project helps detect **subdomain hijacking** by building a DNS graph and identifying potentially misconfigured or risky CNAME entries. We use `crt.sh` to enumerate subdomains, `dnspython` to resolve CNAMEs, and `networkx` to visualize the DNS structure.

---

## 📁 Folder Structure
dns-hijack-detector/
├── data/
│ └── resolved_records.json # CNAME mappings (generated)
├── src/
│ ├── collect_subdomains.py # Fetch subdomains from crt.sh
│ ├── resolve_cname.py # Resolve CNAME of subdomains
│ ├── dns_hijack_detector.py # Main script to generate data
│ ├── detect_hijack.py # Flags suspicious subdomains
│ ├── build_graph.py # Builds and saves DNS graph
│ └── dns_graph_s3_amazonaws_com.png # Output graph image (generated)
├── requirements.txt # Required Python libraries
└── README.md # You're here!



---

## 📚 What This Project Does

This project helps you identify potential **subdomain hijacking risks** using Python.
Subdomain hijacking happens when a domain (like `sub.example.com`) points to an external hosting service (e.g., GitHub Pages, S3, Netlify), but the linked resource is deleted or unclaimed — allowing attackers to "take over" that subdomain.
This tool automates:

1. 🔍 **Subdomain Enumeration**  
   Fetches a list of publicly visible subdomains for a given domain using [crt.sh](https://crt.sh/).

2. 🧠 **CNAME Resolution**  
   Resolves each subdomain to its CNAME target (e.g., `ghs.googlehosted.com` or `*.s3.amazonaws.com`).

3. 🚨 **Hijack Risk Detection**  
   Compares the CNAME targets against a list of trusted platforms and flags unknown or risky destinations.

4. 🗺️ **DNS Graph Visualization**  
   Builds a graph showing the DNS relationships using `networkx` and saves the visualization as an image.

5. 📂 **Data Outputs**  
   - A `.json` file with resolved records
   - A `.png` file showing the DNS graph
   - Optional terminal output showing suspicious subdomains


---

## 💻 Prerequisites

Ensure you have **Python 3.8+** installed. This project was tested on Windows with Anaconda and standard Python.

---

# 🧪 Step 1: Set Up the Environment

### 1.1 🆕 Create a folder
Create a project folder and clone this repository or add the files manually.


## 1.2 Create a Virtual Environment (Windows)
### a): Create the virtual environment
```bash
python -m venv venv
```

### 1.2.1 Activate the virtual environment
```bash
venv\Scripts\activate
```
# 1.3 Install all required Python libraries
```bash
pip install -r requirements.txt
```

If you don’t have a **requirements.txt**, create one with the following content:
requests==2.31.0
dnspython==2.4.2
networkx==3.2.1
matplotlib==3.8.4

## 🛠 Step 2: Add the Code Files
Inside a folder named src/, place the following files:
 - collect_subdomains.py
 - resolve_cname.py
 - dns_hijack_detector.py
 - detect_hijack.py
 - build_graph.py

Create another folder named data/ at the same level as src/.

## 🚀 Step 3: Run the Code (Test with s3.amazonaws.com)
### 📥 Step 3.1: Get subdomains and resolve CNAMEs
```bash
cd src
python dns_hijack_detector.py s3.amazonaws.com
```

This will:
- Query crt.sh for subdomains of s3.amazonaws.com
- Resolve each subdomain’s CNAME
- Save the output to ../data/resolved_records.json

### 🧯 Step 3.2: Detect potentially hijacked subdomains
```bash
python detect_hijack.py
```

### 🗺️ Step 3.3: Visualize the DNS graph
```bash
python build_graph.py
```

When prompted:
``` java
Enter domain (used for title and filename):
```

Type:
```bash
s3.amazonaws.com
```

You will see:

``` css
🖼️ Graph saved to dns_graph_s3_amazonaws_com.png
```

✅ The image will be saved in the src/ folder.


## 🔍 What You Can Analyze
 - Which subdomains resolve to legitimate AWS infrastructure
 - Which subdomains resolve to unknown or expired platforms
 - Visual structure of your DNS/CNAME setup

##📌 Example Output
 - data/resolved_records.json → Contains raw subdomain-to-CNAME mappings
 - src/dns_graph_s3_amazonaws_com.png → Visual graph image of DNS paths
 - Console → Flags suspicious subdomains (if any)

##📢 Coming Soon (You Can Add These)
 - Export suspicious results to CSV
 - Email alert for risky CNAMEs
 - Graph clustering by region or service
 - Integration with WHOIS / RDAP data

##🧠 Credits & Inspiration
Built as a lightweight, Python-only solution to visualize and audit DNS CNAME mappings for security use cases like:
 -Subdomain hijacking
 -Misconfigured DNS entries
 -Security posture monitoring for cloud-based services

##🧼 Deactivating Environment
```bash
deactivate
```

## ⭐ Credits
 -Maintained by [@s-aparnaa](https://github.com/s-aparnaa)



