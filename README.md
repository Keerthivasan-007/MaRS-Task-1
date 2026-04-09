# Mars Rover Programming Challenges - Complete Documentation

##  Table of Contents
1. Learning Experience
2. Problem Summaries & Solutions
3. Equations & Theorems
4. Challenges Faced
5. Approaches Explained

---

##  Learning Experience

### Overview
This project involved solving 5 diverse Mars rover-related programming challenges, ranging from robotics coordinate transformations to pathfinding algorithms. Each challenge required different programming paradigms and mathematical concepts.

### Key Learnings

#### 1. **Coordinate Frame Transformations (Problem 1)**
- Learned rigid body transformations in 3D space
- Understood homogeneous coordinates and 4×4 transformation matrices
- Grasped Euler angles and rotation matrix composition
- Applied matrix multiplication for chaining transformations


#### 2. **Signal Processing & Morse Code (Problems 2 & 3)**
- Gained experience in pattern recognition and decoding
- Learned about substitution ciphers and frequency-based decoding
- Understood string manipulation and dictionary-based lookups
- Practiced with position-dependent transformations



#### 3. **Noise Filtering & Signal Analysis (Problem 4)**
- Learned statistical filtering techniques (mean vs. median)
- Understood sliding window algorithms
- Grasped robustness concepts (outlier resistance)
- Applied dynamic programming concepts



#### 4. **Optimization & Dynamic Programming (Problem 5)**
- Developed understanding of constrained optimization
- Learned dynamic programming for finding optimal paths
- Practiced cost minimization with multiple constraints
- Understood state-space exploration


#### 5. **Pathfinding & Graph Algorithms (Problem 6)**
- Mastered BFS (Breadth-First Search) algorithm
- Learned grid-based pathfinding
- Understood obstacle avoidance in 2D space
- Practiced queue-based state exploration


---

##  Equations, Theorems & Mathematical Foundations

### 1. Rotation Matrices (Problem 1)

#### Rotation around X-axis (Roll):
```
Rx(θ) = [1      0         0    ]
        [0   cos(θ)  -sin(θ) ]
        [0   sin(θ)   cos(θ) ]
```

#### Rotation around Y-axis (Pitch):
```
Ry(φ) = [cos(φ)   0   sin(φ)]
        [  0      1      0   ]
        [-sin(φ)  0   cos(φ)]
```

#### Rotation around Z-axis (Yaw):
```
Rz(ψ) = [cos(ψ)  -sin(ψ)   0]
        [sin(ψ)   cos(ψ)   0]
        [  0        0       1]
```

#### Combined Rotation (XYZ Convention):
```
R_total = Rz(ψ) × Ry(φ) × Rx(θ)
```

#### Homogeneous Transformation Matrix:
```
T = [R | t]  =  [R_3×3 | t_3×1]
    [0 | 1]     [0_1×3 |   1   ]
```

**Point Transformation:**
```
p_new = T × p_old
where p_old = [x, y, z, 1]ᵀ (homogeneous coordinates)
```

---

### 2. Morse Code Mapping (Problem 2)

**Dictionary-based encoding:** Each letter/number maps to unique dot-dash sequence

```
Example: A=·−, B=−···, C=−·−·, ..., 0=−−−−−, 1=·−−−−
```

**Parsing Rules:**
```
Single space = Letter separator
Double space / '/' = Word separator
```

---

### 3. Cipher Decryption - Position-based Shift (Problem 3)

#### Encryption Formula:
```
encrypted_char[i] = original_char[i] + shift_value[i]
where shift_value[i] = i (1-indexed position)
```

#### Decryption Formula:
```
original_char[i] = encrypted_char[i] - shift_value[i]
with wrapping: if result < 'A', add 26
```

**Example:**
```
Position 1: C - 1 = B
Position 2: D - 2 = B
Position 3: F - 3 = C
...
```

---

### 4. Signal Processing - Filtering (Problem 4)

#### Muchiko Filter (Average/Mean):
```
filtered_value = (window[0] + window[1] + ... + window[n-1]) / n
```

**Properties:**
- Sensitive to outliers
- Smooth uniform noise
- Mean of all values in window

#### Sanchiko Filter (Median):
```
sorted_window = sort(window)
filtered_value = sorted_window[n/2]  (middle element)
```

**Properties:**
- Robust to outliers
- Preserves edges better
- 50th percentile value

#### Comparison:
```
If Mean ≈ Median  →  No outliers (clean data)
If Mean ≠ Median  →  Outliers present (noisy data)
```

---

### 5. Dynamic Programming - Manipulator Optimization (Problem 5)

#### Constraint Satisfaction:
```
1. Sum Constraint: Inner + Middle + Outer = Target
2. Limit Constraints: 0 ≤ Inner ≤ L1, 0 ≤ Middle ≤ L2, 0 ≤ Outer ≤ L3
3. Stability: |Inner - Outer| ≤ D
```

#### Cost Function (Wear):
```
Cost(prev, curr) = |Δinner| × W1 + |Δmiddle| × W2 + |Δouter| × W3
```

#### DP Recurrence:
```
dp[target][config] = min(
    dp[prev_target][prev_config] + Cost(prev_config, config)
    for all valid prev_config
)
```

**Complexity:**
```
Time: O(n × C²) where n = targets, C = valid configs per target
Space: O(C) for state storage
```

---

### 6. Graph Algorithms - BFS Pathfinding (Problem 6)

#### Breadth-First Search:
```
Queue-based exploration of states
FIFO: First-In-First-Out
```

**Algorithm:**
```
1. Enqueue start node
2. While queue not empty:
   a. Dequeue current node
   b. If current == goal, return path
   c. For each unvisited neighbor:
      - Mark as visited
      - Enqueue neighbor
3. If queue empty and goal not found, no path exists
```

#### Optimality:
```
BFS finds shortest path in unweighted graphs
Distance = number of edges = number of moves
```

**Complexity:**
```
Time: O(V + E) where V = vertices, E = edges
Space: O(V) for queue and visited set
In grid: O(n × m) for n×m grid
```

---

##  Sketches & Visual Representations

### 1. Coordinate Frame Transformation Chain
```
Camera Frame (x_cam, y_cam, z_cam)
        ↓
    [Rotation R_cam, Translation t_cam]
        ↓
Rover Frame (x_rover, y_rover, z_rover)
        ↓
    [Rotation R_rover, Translation pos_rover]
        ↓
World Frame (x_world, y_world, z_world)
```

### 2. Euler Angle Visualization
```
        Z (Yaw ψ)
        ↑
        |
    Y ← + → X (Roll θ)
        (Pitch φ out of page)
```

### 3. Signal Processing Comparison
```
Original Data:     [2, 5, 3, 100, 4]  (100 is outlier)

Muchiko (Mean):
[2,5,3] → 3.33, [5,3,100] → 36, [3,100,4] → 35.67
Result: [3, 36, 36]  (affected by outlier)

Sanchiko (Median):
[2,5,3] → 3, [5,3,100] → 5, [3,100,4] → 4
Result: [3, 5, 4]  (outlier ignored!)
```

### 4. BFS Pathfinding Visualization
```
Start: S
Destination: D
Obstacle: #

Layer 0: S
Layer 1: Neighbors of S
Layer 2: Neighbors of Layer 1
...
Until D is found

Example Grid:
S 1 1 #    → Layer 1: neighbors of S
1 1 # 1    → Layer 2: neighbors of layer 1
1 # 1 1    → Continue expanding
# 1 1 D    → D found at layer 4
```

### 5. Manipulator Configuration Space
```
Valid configurations for Target T:
- Must satisfy: Inner + Middle + Outer = T
- Must satisfy: 0 ≤ segments ≤ limits
- Must satisfy: |Inner - Outer| ≤ D

3D configuration space with constraints:
  Outer
   ↑
   |    /← Valid region
   |  /
   |/_____ Inner
  /
 Middle
```

---

##  Challenges Faced

### Challenge 1: Understanding 3D Transformations (Problem 1)
**Issue:** Conceptualizing rotation matrices and their composition

**Solution:**
- Studied individual rotation matrices first
- Visualized each axis independently
- Practiced matrix multiplication
- Verified with known test cases

**Learning:** Matrix operations are composable - order matters!


### Challenge 2: Wrapping in Position-based Cipher (Problem 3)
**Issue:** Characters wrapping around alphabet boundaries

**Solution:**
- Implemented modulo arithmetic
- Added while loops for wrap handling
- Tested edge cases (A-1, Z+1)
- Verified with multiple test cases

**Learning:** Circular boundary conditions need explicit handling

---

### Challenge 3: Choosing Between Filters (Problem 4)
**Issue:** When to use mean vs. median

**Solution:**
- Implemented both filters
- Added comparison logic
- Created decision rules based on differences
- Generated detailed analysis output

**Learning:** Algorithm selection depends on data characteristics

---

### Challenge 4: Dynamic Programming State Space (Problem 5)
**Issue:** Exponential complexity without proper optimization

**Solution:**
- Used memoization to store computed states
- Pruned invalid configurations early
- Implemented efficient validation
- Optimized for memory usage

**Learning:** DP requires careful state representation

---

### Challenge 5: BFS vs. Other Pathfinding (Problem 6)
**Issue:** Ensuring shortest path without extra complexity

**Solution:**
- Chose BFS (simpler than A*, guarantees shortest in unweighted)
- Implemented visited set to avoid cycles
- Used queue for proper FIFO ordering
- Verified with multiple test cases

**Learning:** Algorithm choice impacts both correctness and complexity

---

##  Approach Explanations

### Problem 1: Rover Coordinate Transformation
**Approach:** Homogeneous Coordinate Transformation

1. **Decompose problem:**
   - Camera to Rover transformation
   - Rover to World transformation
   - Chain them together

2. **Mathematical basis:**
   - Rotation matrices from Euler angles
   - Translation vectors
   - Matrix multiplication for composition

3. **Implementation:**
   ```python
   # Step 1: Camera → Rover
   R_cam = get_rotation_matrix(cam_rot)
   obj_rover = R_cam @ obj_cam + cam_pos
   
   # Step 2: Rover → World
   R_rover = get_rotation_matrix(rover_rot)
   obj_world = R_rover @ obj_rover + rover_pos
   ```

4. **Validation:**
   - Verify with provided examples
   - Check constraints (limits, stability)
   - Test edge cases

---

### Problem 2: Morse Code Decoder
**Approach:** Dictionary-based Pattern Matching

1. **Build complete mapping:**
   - All letters (A-Z)
   - All digits (0-9)
   - Common punctuation

2. **Parse input:**
   - Split by single space (letters)
   - Split by double space (words)
   - Handle word separator '/'

3. **Decode:**
   - Lookup each Morse sequence
   - Build character string
   - Handle unknown codes gracefully

4. **Validation:**
   - Test with all example messages
   - Verify format handling
   - Check case sensitivity

---

### Problem 3: Position-based Cipher Decoder
**Approach:** Mathematical Position-dependent Transformation

1. **Understand cipher:**
   - Each position has different shift
   - Position = 1-indexed (1, 2, 3, ...)
   - Wraps around alphabet

2. **Implement decryption:**
   ```python
   for position, char in enumerate(encrypted, start=1):
       original_code = ord(char) - position
       if original_code < ord('A'):
           original_code += 26
       decoded += chr(original_code)
   ```

3. **Handle wrapping:**
   - Check boundaries
   - Use modulo arithmetic
   - Add/subtract 26 as needed

4. **Test thoroughly:**
   - Known plaintext-ciphertext pairs
   - Boundary cases
   - Multiple messages

---

### Problem 4: Noise Filtering
**Approach:** Comparative Analysis of Statistical Filters

1. **Implement both filters:**
   - Muchiko: Average (sum/count)
   - Sanchiko: Median (middle value)

2. **Apply to sliding windows:**
   ```python
   for i in range(len(data) - window_size + 1):
       window = data[i:i + window_size]
       # Muchiko: mean of window
       # Sanchiko: median of window
   ```

3. **Compare results:**
   - If same: data is clean
   - If different: outliers present
   - Measure difference magnitude

4. **Select best filter:**
   - Sanchiko preferred for outliers
   - Muchiko for smooth noise
   - Validate with statistics

---

### Problem 5: Manipulator Optimization
**Approach:** Dynamic Programming with Constraint Validation

1. **State representation:**
   - State = (target, configuration)
   - Value = minimum cost to reach

2. **Generate valid configurations:**
   ```python
   for target in targets:
       valid_configs = find_valid_configs(target, limits, D)
       # Valid if: sum=target, in limits, |inner-outer|≤D
   ```

3. **DP transition:**
   ```python
   for next_config in valid_configs:
       for prev_config in previous_state:
           cost = calculate_movement_cost(prev, next)
           dp[next_config] = min(dp[next_config], 
                                 prev_cost + cost)
   ```

4. **Extract solution:**
   - Find minimum cost among final configurations
   - Optionally track path

---

### Problem 6: Rover Pathfinding
**Approach:** Breadth-First Search Graph Exploration

1. **Model as graph:**
   - Nodes = grid positions
   - Edges = allowed moves (4 directions)
   - Obstacles = blocked nodes

2. **BFS implementation:**
   ```python
   queue = deque([(start, [start])])
   visited = {start}
   
   while queue:
       current, path = queue.popleft()
       if current == destination:
           return path
       
       for neighbor in get_neighbors(current):
           if neighbor not in visited and is_safe(neighbor):
               visited.add(neighbor)
               queue.append((neighbor, path + [neighbor]))
   ```

3. **Key properties:**
   - Explores level-by-level
   - Guarantees shortest path
   - FIFO queue ensures optimality

4. **Optimization:**
   - Early termination when found
   - Visited set prevents cycles
   - Efficient neighbor checking

---

##  Resources Used

### Learning Materials

#### 1. Mathematics & Linear Algebra
- **Rotation Matrices:**
  - 3Blue1Brown - Essence of Linear Algebra (YouTube)
  - Wikipedia: Rotation Matrix
  - Robotics Textbooks: Craig - Introduction to Robotics

- **Homogeneous Coordinates:**
  - Computer Graphics fundamentals
  - Wikipedia: Homogeneous coordinates
  - Computer Vision resources

#### 2. Signal Processing
- **Filtering Concepts:**
  - Signal Processing: Oppenheim & Schafer
  - Wikipedia: Mean, Median, Moving Average
  - StatQuest with Josh Starmer (YouTube)

#### 3. Algorithms
- **Dynamic Programming:**
  - "Cracking the Coding Interview" - McDowell
  - LeetCode DP problems
  - GeeksforGeeks DP articles

- **Graph Algorithms:**
  - CLRS: Introduction to Algorithms
  - Wikipedia: Breadth-first search
  - Neetcode.io - Algorithms course

#### 4. Robotics & Transformations
- **Mars Rover Context:**
  - JPL Robotics Resources
  - ROS (Robot Operating System) Documentation
  - TF2 (Transform Framework) - ROS wiki

#### 5. Python Development
- **NumPy Documentation:**
  - Official NumPy documentation
  - Real Python tutorials
  - Stack Overflow solutions

---

### Development Tools & Libraries

#### Languages & Frameworks
- **Python 3.x** - Primary implementation language
- **NumPy** - Numerical computations, matrix operations
- **Collections.deque** - Efficient queue implementation
- **Standard Library** - File I/O, data structures

#### IDE & Environment
- **VS Code** - Code editor
- **Python Interpreter** - Execution
- **Git/GitHub** - Version control

#### Testing & Validation
- Manual test cases
- Visual verification (maps, paths)
- Step-by-step debugging
- Multiple example scenarios


##  Conclusion

Through solving these challenges, I've gained deeper understanding of:
- How coordinate transformations work in robotics
- Signal processing and noise handling
- Optimization under constraints
- Pathfinding in complex environments
- The importance of algorithm selection

  Miscs:
  1) Screen shot of pushing into github
  
  <img width="974" height="258" alt="image" src="https://github.com/user-attachments/assets/fa85e443-0210-4acc-954c-33a4888055ee" />

  2) 
