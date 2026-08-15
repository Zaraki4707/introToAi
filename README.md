<div align="center">

# Introduction to AI - Laboratory

**Hands-on labs for the ENSIA *Introduction to AI* course (Semester 2)**

Build classic AI systems from scratch: agents, search, games, and logic, following the
[_Artificial Intelligence: A Modern Approach_](https://aima.cs.berkeley.edu/) (Russell & Norvig) curriculum.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![AI](https://img.shields.io/badge/AI-Agents%20%7C%20Search%20%7C%20Games%20%7C%20Logic-4B32C3)
![AIMA](https://img.shields.io/badge/Reference-AIMA%20(Russell%20%26%20Norvig)-00599C)
![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)

</div>

---

## About

This repository gathers the **12 laboratory sheets** of the *Introduction to AI* course. It is designed to take
you from **zero Python** to implementing **real AI algorithms**, the same ones that power planning systems, game
AIs, optimizers, and automated reasoners.

Each lab is a **Jupyter Notebook** that mixes:

- **Theory** - clear explanations tied to the AIMA textbook chapters
- **Starter code** - working skeletons you complete yourself
- **Exercises and mini-projects** - puzzles, games, and real optimization problems

Many notebooks are the **"EMPTY" versions**: the scaffolding is provided, and *you* fill in the intelligence.
That is the point. The best way to learn AI is to build it.

---

## Table of Contents

- [The Curriculum](#the-curriculum)
- [Suggested Learning Path](#suggested-learning-path)
- [What You'll Master](#what-youll-master)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Tips for Learning](#tips-for-learning)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

---

## The Curriculum

| Lab | Notebook | AIMA Ch. | What you'll implement |
|-----|----------|:--------:|-----------------------|
| **02** | [`Lab2_Intro_Python.ipynb`](Lab2_Intro_Python.ipynb) | - | **Python fundamentals**: control flow, lists, matrices, sets and dicts, strings, functions, OOP, file handling, decorators, generators, `map` / `filter` / `reduce` |
| **03** | [`Lab3__Agent_Environement.ipynb`](Lab3__Agent_Environement.ipynb) | Ch. 2 | **Agents and environments (I)**: the 8-puzzle, Tic-Tac-Toe, and maze navigation modeled with OOP |
| **04** | [`LAB4____Agents.ipynb`](LAB4____Agents.ipynb) | Ch. 2 | **Agents and environments (II)**: a vacuum-cleaner world with reflex, goal-based, utility-based, and model-based agents (energy-aware 8x8 grid) |
| **05** | [`Lab5____Search__Part_I.ipynb`](Lab5____Search__Part_I.ipynb) | Ch. 3 | **Uninformed search**: problem formulation (5-aspect standard) plus BFS and DFS via a general graph-search algorithm |
| **06** | [`Lab6__informed_Search_EMPTY.ipynb`](Lab6__informed_Search_EMPTY.ipynb) | Ch. 3 | **Informed search**: depth-limited search, iterative deepening, uniform-cost, greedy best-first, and **A\*** on a travel-planning problem |
| **07** | [`Lab7_Local_Search.ipynb`](Lab7_Local_Search.ipynb) | Ch. 4 | **Local search**: steepest-ascent hill climbing for combinatorial problems |
| **08** | [`LAB8_V1_Empty.ipynb`](LAB8_V1_Empty.ipynb) | Ch. 4 | **Advanced local search**: random-restart hill climbing and simulated annealing (TSP, 8-Queens) |
| **09** | [`LAB9_V1_Empty.ipynb`](LAB9_V1_Empty.ipynb) | Ch. 4 | **Genetic algorithms**: selection, crossover, and mutation to evolve solutions (TSP, 8-Queens) |
| **10** | [`Lab10_V1_Empty.ipynb`](Lab10_V1_Empty.ipynb) | Ch. 5 | **Adversarial search**: the MiniMax algorithm for an unbeatable Tic-Tac-Toe player |
| **11** | [`LAB11_CSP_Empty.ipynb`](LAB11_CSP_Empty.ipynb) | Ch. 6 | **Constraint satisfaction**: Sudoku solved with backtracking, arc consistency (AC-3), and the MRV heuristic |
| **12** | [`LAB12_Empty_V1.ipynb`](LAB12_Empty_V1.ipynb) | Ch. 7 | **Logical agents**: truth-table entailment (model checking) and forward chaining |
| **13** | [`LAB13_Resolution_empty.ipynb`](LAB13_Resolution_empty.ipynb) | Ch. 7 | **Automated reasoning**: CNF transformation (AST pipeline) and the resolution rule in propositional logic |

---

## Suggested Learning Path

```
Lab 02   Python warm-up (required for everything else)
   |
   v
Labs 03-04   Agents and environments: how AI interacts with the world
   |
   v
Labs 05-06   Classical search: from blind search (BFS/DFS) to smart search (A*)
   |
   v
Labs 07-09   Optimization: local search and evolutionary algorithms
   |
   v
Lab 10       Game playing: Minimax for adversarial games
   |
   v
Lab 11       Constraint satisfaction: solving Sudoku efficiently
   |
   v
Labs 12-13   Knowledge and logic: agents that reason
```

> The labs build on each other. Later notebooks assume you know the OOP patterns and data structures
> introduced in earlier ones. Follow them in order for the full experience.

---

## What You'll Master

By the end of this course you will be able to:

- Model real-world problems with **object-oriented Python**
- Design AI **agents** and their **environments**
- Implement **uninformed** (BFS, DFS) and **informed** (A\*, greedy) search
- Apply **local search** and **genetic algorithms** to combinatorial optimization
- Build a game-playing AI with **Minimax**
- Solve **constraint satisfaction problems** like Sudoku
- Implement **logical inference**: entailment, forward chaining, resolution

---

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Jupyter Notebook / JupyterLab** (or VS Code with the Jupyter extension)
- Only the Python **standard library** is required, no extra packages needed

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/Zaraki4707/introToAi.git
cd introToAi

# 2. (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 3. Launch Jupyter
jupyter notebook
```

Or open the repository directly in **VS Code** and run the notebooks from there.

### Running a Lab

1. Open any notebook from the list above.
2. Read the theory cells carefully. They explain the *why*.
3. Complete the `# TODO` or empty method cells.
4. Run the provided test cells to check your implementation.

---

## Repository Structure

```
introToAi/
|-- Lab2_Intro_Python.ipynb          # Python basics
|-- Lab3__Agent_Environement.ipynb   # Agents and environments (I)
|-- LAB4____Agents.ipynb             # Agents and environments (II)
|-- Lab5____Search__Part_I.ipynb     # Uninformed search
|-- Lab6__informed_Search_EMPTY.ipynb# Informed search (A*, ...)
|-- Lab7_Local_Search.ipynb          # Local search
|-- LAB8_V1_Empty.ipynb              # Advanced local search
|-- LAB9_V1_Empty.ipynb              # Genetic algorithms
|-- Lab10_V1_Empty.ipynb             # Game theory and Minimax
|-- LAB11_CSP_Empty.ipynb            # Constraint satisfaction (Sudoku)
|-- LAB12_Empty_V1.ipynb             # Logical agents (inference)
|-- LAB13_Resolution_empty.ipynb     # Resolution and CNF
`-- exemple.txt                      # Sample file used in Lab 2 (file handling)
```

---

## Tips for Learning

- **Type, do not copy-paste.** Retyping the code is how it sticks.
- **Break things on purpose.** Change parameters, break the solver, then fix it.
- **Run the test cells.** They are your grading rubric for correctness.
- **Compare algorithms.** Time BFS vs. A\* on the same problem and observe the difference.
- **Ask questions.** Open an [issue](https://github.com/Zaraki4707/introToAi/issues) if you are stuck.

---

## Contributing

Found a bug? Solved a lab and want to share your solution? Have an idea for a new exercise?

Contributions are **welcome and appreciated**! Here is how:

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-improvement`
3. Make your changes (keep the existing style and structure)
4. Test that your notebook runs end-to-end
5. Open a **Pull Request** with a clear description

**Ideas for contributions:**

- Completed versions of the "EMPTY" labs, in a separate `solutions/` branch
- Extra exercises or challenges for each lab
- French translations of the lab text
- Visualizations (for example, an animated search on the maze)
- Fixed typos, better comments, or clearer explanations

---

## Acknowledgments

- [**ENSIA**](https://ensia.edu.dz/) (Ecole nationale superieure d'intelligence artificielle), the institution
  this course belongs to
- **Stuart Russell and Peter Norvig**, authors of *Artificial Intelligence: A Modern Approach* (4th ed.), the
  reference behind the AIMA chapter mapping used in every lab
- All the students who will learn, break, and rebuild these labs

---

*Built for the next generation of AI engineers. Happy hacking.*