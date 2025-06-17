# src/build_graph.py

import json
import os
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Load resolved records
def load_records(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# Step 2: Build graph from DNS data
def build_dns_graph(records):
    G = nx.DiGraph()
    for record in records:
        sub = record["subdomain"]
        target = record["points_to"]
        if target:
            G.add_edge(sub, target)
    return G

# Step 3: Visualize the graph
def visualize_graph(G, domain):
    plt.figure(figsize=(12, 8))
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=9, arrows=True)
    plt.title(f"DNS Graph for {domain}")
    plt.tight_layout()
    output_path = f"dns_graph_{domain.replace('.', '_')}.png"
    plt.savefig(output_path)
    print(f"🖼️ Graph saved to {output_path}")
    plt.show()

# Step 4: Main
def main():
    domain = input("Enter domain (used for title and filename): ").strip()
    input_path = os.path.join("..", "data", "resolved_records.json")
    records = load_records(input_path)
    G = build_dns_graph(records)
    visualize_graph(G, domain)

if __name__ == "__main__":
    main()
