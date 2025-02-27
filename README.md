# **♞ Knight's Tour Solver - CSP Approach**  
### **Master 1 - Visual Computing, USTHB (2024/2025)**  

**Course:** Problem Solving - TP by *Dr. Meriem Sebai*  
<br>  

📄 **[Assignment Support (PDF)](./📄_knights_tour_csp.pdf)**  
<br>  

![Knight's Tour Example](https://i.pinimg.com/originals/32/b8/15/32b815125e9761081319d0a57aec1798.gif)  
<br>  

---

## **📌 About**  
The **Knight's Tour** is a classic chess puzzle where the knight must visit every square on the chessboard exactly once. This project solves the problem using a **Constraint Satisfaction Problem (CSP)** approach, implementing a **backtracking algorithm** to find valid sequences of moves.  

---

## **✨ Features**  
- ✅ **Backtracking Algorithm**: Efficiently explores possible moves and backtracks when constraints are violated.  
- ✅ **Knight Class**: Manages the knight's position, path, and move validation.  
- ✅ **Move Validation**: Ensures the knight stays within the chessboard and avoids revisiting squares.  
- ✅ **Visualization**: Displays the optimal solution on a chessboard using **Pygame**.  

---

## **⚙️ How It Works**  
### **1. Knight Class**  
The `Knight` class is the core of the solver. It tracks the knight's position, assignment (sequence of moves), and path (visited squares). Here's how it works:  

#### **Attributes**  
- **`position`**: The current coordinates `(x, y)` of the knight on the chessboard.  
- **`assignment`**: A list of moves (directions) taken by the knight.  
- **`path`**: A list of positions `(x, y)` visited by the knight.  

#### **Methods**  
- **`move_forward(direction)`**: Moves the knight in the specified direction.  
- **`move_backward()`**: Reverses the last move, backtracking to the previous position.  
- **`addMove(direction)`**: Adds a move to the assignment and updates the path.  
- **`removeMove()`**: Removes the last move and backtracks.  
- **`consistent(m)`**: Checks if a move is valid (within bounds and not revisiting a square).  

#### **Example Code**  
```python
class Knight:
    def __init__(self):
        self.position = (0, 0)  # Start at (0, 0)
        self.assignment = []     # No moves initially
        self.path = [self.position]  # Path starts with initial position

    def move_forward(self, direction):
        move = moves[direction]  # Get move from dictionary
        position = self.position
        self.position = (position[0] + move[0], position[1] + move[1])  # Update position

    def move_backward(self):
        if len(self.path) > 1:  # Ensure there's a move to backtrack
            self.path.pop()  # Remove last position
            self.position = self.path[-1]  # Set position to previous square

    def addMove(self, direction):
        self.assignment.append(direction)  # Add move to assignment
        self.move_forward(direction)      # Move knight forward
        self.path.append(self.position)   # Add new position to path

    def removeMove(self):
        self.assignment.pop()  # Remove last move
        self.move_backward()   # Move knight backward

    def consistent(self, m):
        move = moves[m]  # Get move from dictionary
        pos = (self.position[0] + move[0], self.position[1] + move[1])  # New position

        # Check if position is out of bounds
        if pos[0] < 0 or pos[1] < 0 or pos[0] > 7 or pos[1] > 7:
            return False

        # Check if position has already been visited
        elif self.path.count(pos) > 0:
            return False

        # Move is valid
        else:
            return True
```

---

### **2. Backtracking Algorithm**  
The backtracking algorithm uses the `Knight` class to explore all possible moves:  
1. Starts from the initial position `(0, 0)`.  
2. Recursively explores all valid moves.  
3. Backtracks and tries alternative paths when a dead end is reached.  

---

## **📦 Installation**  
1️⃣ Clone the repository:  
```bash  
git clone https://github.com/selma-Bentaiba/Backtracking-KnightTour.git  
```  

2️⃣ Install **Pygame**:  
```bash  
pip install pygame  
```  

3️⃣ Run the solver:  
```bash  
python __main__.py  
```  

---

## **📜 Code Overview**  
### **🔹 `knight.py`**  
- Defines the `Knight` class and its methods for move management and validation.  

### **🔹 `display.py`**  
- Handles the visualization of the knight's path using **Pygame**.  

### **🔹 `__main__.py`**  
- Runs the backtracking algorithm and displays the solution.  

---

## **🤖 Future Improvements**  
- 🔹 **Optimization**: Implement heuristics (e.g., Warnsdorff's rule) to reduce backtracking.  
- 🔹 **Interactive GUI**: Add user controls to step through the solution.  
- 🔹 **Performance Metrics**: Measure and improve the algorithm's efficiency for larger boards.  

---
