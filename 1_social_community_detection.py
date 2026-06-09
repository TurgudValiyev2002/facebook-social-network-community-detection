from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

RESULTS = Path("results")

def main():
    RESULTS.mkdir(exist_ok=True)
    graph = nx.planted_partition_graph(l=4, k=18, p_in=0.28, p_out=0.025, seed=42)
    communities = list(nx.community.greedy_modularity_communities(graph))
    rows = []
    for cid, members in enumerate(communities):
        for node in sorted(members):
            rows.append({"node": node, "detected_community": cid})
    pd.DataFrame(rows).to_csv(RESULTS / "detected_communities.csv", index=False)
    summary = pd.DataFrame([{"nodes": graph.number_of_nodes(), "edges": graph.number_of_edges(), "density": round(nx.density(graph), 4), "communities": len(communities), "modularity": round(nx.community.modularity(graph, communities), 4)}])
    summary.to_csv(RESULTS / "network_summary.csv", index=False)
    degree = pd.DataFrame({"node": list(dict(graph.degree()).keys()), "degree": list(dict(graph.degree()).values())}).sort_values("degree", ascending=False)
    degree.to_csv(RESULTS / "degree_table.csv", index=False)
    node_to_comm = {r["node"]: r["detected_community"] for r in rows}
    colors = ["#3d6fb6", "#b26a3b", "#4a8f5a", "#8a5fbf", "#555555"]
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_edges(graph, pos, alpha=0.2)
    nx.draw_networkx_nodes(graph, pos, node_size=90, node_color=[colors[node_to_comm[n] % len(colors)] for n in graph.nodes])
    plt.title("Facebook-Style Community Detection")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(RESULTS / "community_graph.png", dpi=180)
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()
