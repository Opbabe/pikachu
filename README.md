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

pikachu-connect4/
├── README.md
├── requirements.txt
├── src
│   ├── board.py
│   ├── threat_detection.py
│   ├── frame_based_representation.py
│   ├── mcts_logic.py
│   └── play_vs_agent.py
├── tests
│   ├── test_board.py
│   ├── test_threat_detection.py
│   ├── test_frame.py
│   └── test_mcts.py
└── .gitignore

````

---

## 🛠️ Getting Started

1. **Clone** this repo  
   ```bash
   git clone https://github.com/Opbabe/pikachu.git
   cd pikachu
````

2. **Verify** Python version (3.9+):

   ```bash
   python3 --version
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




```
```
