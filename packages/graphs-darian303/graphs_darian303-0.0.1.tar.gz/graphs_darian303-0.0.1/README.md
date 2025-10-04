# graphs_darian303

Python package implementing Dijstra's shortest path algorithm.

This package follows the naming convention `graphs_<username>` and is structured for easy installation and usage. 

---

# Installation

pip install -e . 

Note: If you encounter import issues, you can termporarily set your PYTHONPATH:

Powershell: $env:PYTHONPATH="$PWD\src\graphs_darian303"

---

# Usage

Run the test script with a graph file:

py test.py example1.txt

---

# Project Structure

src
|__graphs_darian303
   |__ __init__.py
   |__ heapq.py
   |__ sp.py
|__test.py
|__README.md
|__pyproject.toml

---

# Repository: 

GitHub repository: https://github.com/darian303/graphs_darian303

---

# Notes:

Python 3.8+ is recommended.
No changes to provided code or project structure are required.
The package can be installed and imported as:

from graphs_darian303 import sp

Bonus: The package also includes bfs(graph, start) for breadth-first traversal.
