```markdown
# Team Pikachu Connect 4 Agent

> *CS156 Spring 2025 Group Project*

---

## 🚀 Project Overview

**Team Pikachu** built a Python agent that plays Connect 4 using:

- **Search**: Monte Carlo Tree Search (MCTS)  
- **Representation**: Frame‑based (wraps a simple `Board` class)  
- **Reasoning**:  
  - Immediate win/block checks (deduction)  
  - Abduction & inference via forward‑chaining  
  - Resolution of tactical threats  

---

## 📂 What’s Inside

```

├── board.py                 # Core 6×7 board logic (drop, legal moves, win/draw)
├── threat\_detection.py      # Immediate win/block pattern checks
├── frame\_based\_representation.py
│     └─ Frame class for simulations
├── mcts\_logic.py            # Flat MCTS + threat‑filter hybrid agent
├── play\_vs\_agent.py         # Human vs. AI demo loop
└── README.md                # (You’re reading this!)

````

---

## 🛠️ Getting Started

1. **Clone** this repo  
   ```bash
   git clone https://github.com/Opbabe/pikachu.git
   cd pikachu
````

2. **Install** (no external dependencies!)

   ```bash
   python3 --version   # ensure Python 3.9+
   ```

3. **Play** against the AI

   ```bash
   python play_vs_agent.py
   ```

   * You’re **Player 1** (enter 0–6 to drop your disc).
   * Agent will think (≤ 1 s) and reply.

---

## 🎯 How It Works

1. **Threat Filter**

   * Check “Can I win now?” → play winning move
   * Else “Can opponent win next?” → block

2. **MCTS Search**

   * Run random playouts for a fixed time budget
   * Track visits & wins per first move
   * Choose the column with the highest win rate

---

## 📈 Results

* **Win/Tie rate** ≥ 95% vs. naïve agents
* **Decision time** ≈ 0.4 s per move on a 6×7 board

---

