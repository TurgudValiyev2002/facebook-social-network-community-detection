# Facebook-Style Social Network Community Detection

## 1. Motivation

This graph AI lab uses a synthetic Facebook-style social network because downloading the SNAP Facebook dataset may require internet. The motivation is to detect communities and understand modular structure.

## 2. Project Goal

Build a small, reproducible AI research lab with clear outputs and honest limitations.

## 3. Dataset, Paper, Or Problem Description

Dataset/problem: planted partition graph with social-network-like dense groups and sparse cross-group links.

## 4. Tools

Tools: Python, NetworkX, pandas, matplotlib.

## 5. Models Or Methods

Method: greedy modularity community detection and degree analysis.

## 6. Hyperparameters When Relevant

Hyperparameters: 4 groups, 18 nodes each, p_in=0.28, p_out=0.025, seed=42.

## 7. Results

Results include network summary, detected communities, degree table, and graph figure.

## 8. Interpretation Of Results

Interpretation: high modularity means nodes connect more inside communities than across them.

## 9. Conclusion

Conclusion: community detection helps summarize large networks, but real Facebook data would need privacy and bias care.

## 10. How To Run

```bash
pip install -r requirements.txt
python 1_*.py
```
