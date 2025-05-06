# Hash Table Implementation - INF01124 Data Sorting and Searching (Exercise 4)

## Overview

This project, developed for the INF01124 Data Sorting and Searching course under Professor João Comba, implements a Hash Table to manage and query a dataset of 18,944 FIFA player records from the `players-fifa.csv` file. The project focuses on efficient data storage and retrieval, using a custom hash function and chaining for collision resolution. It evaluates performance across multiple table sizes (997, 1999, 3989, 7993) and generates detailed statistics on table construction and query execution.

The significance of this project lies in its demonstration of core data structure concepts, particularly hash tables, which are fundamental to database systems, caching, and search applications. By handling a real-world dataset and analyzing performance metrics like occupancy rate, list sizes, and query efficiency, it provides practical experience in optimizing data structures for scalability and speed. The project also includes an optional bonus challenge (BEE 1256 - Hash Tables) to deepen understanding of hash table applications.

## Project Structure

The project processes the `players-fifa.csv` dataset, which contains:
- **sofifa_id**: Unique player identifier (key).
- **name**: Player's full name.
- **player_positions**: String of positions (e.g., "RW, ST, CF").

The Hash Table is tested with:
- **Table Sizes**: Prime numbers 997, 1999, 3989, and 7993 (close to 1000, 2000, 4000, 8000).
- **Queries**: Player lookups by `sofifa_id` from `consultas.csv`.

### Hash Table Implementation
The Hash Table is implemented with the following components:
1. **Hash Function**:
   - Uses Python’s built-in `hash()` function modulo the table size (`hash(chave) % tamanho`).
   - Maps keys (`sofifa_id`) to indices between 0 and M-1, where M is the table size.
   - Ensures uniform distribution for efficient lookups.

2. **Collision Resolution**:
   - Employs **closed addressing with chaining**, where each table slot contains a linked list of `Nodo` objects.
   - Each `Nodo` stores a key (`sofifa_id`), value (tuple of name and positions), and a pointer to the next node.
   - Handles collisions by appending new entries to the list at the hashed index.

3. **Insertion Operation**:
   - Computes the index using the hash function.
   - If the slot is empty, creates a new list with the `Nodo`.
   - If the slot is occupied, appends the `Nodo` to the existing list.
   - Time complexity: O(1) average case, assuming low collision rates.

4. **Search Operation**:
   - Computes the index for the given `sofifa_id`.
   - Traverses the linked list at that index to find the matching key.
   - Returns the player’s name and positions if found, or `None` if not.
   - Tracks the number of nodes checked (`testes_realizados`) for performance analysis.
   - Time complexity: O(1) average case, O(n) worst case for high collisions.

### Performance Evaluation
The project conducts experiments for each table size, measuring:
- **Table Construction**:
  - **Time**: Duration to load all 18,944 players (in milliseconds).
  - **Occupancy Rate**: Ratio of used slots to table size (`occupied_slots / table_size`).
  - **Maximum List Size**: Length of the longest linked list.
  - **Average List Size**: Mean length of non-empty lists.

- **Query Performance**:
  - **Total Query Time**: Time to process all queries from `consultas.csv` (in milliseconds).
  - **Query Results**: For each `sofifa_id`, outputs the player’s name or "NAO ENCONTRADO", plus the number of nodes checked.
  - **Maximum Tests**: Highest number of nodes checked in any query.
  - **Average Tests**: Mean number of nodes checked across all queries.

Results are saved in files named `experimentoM.txt` (M = 997, 1999, 3989, 7993) with the specified format.

### Sorting Algorithms
While the project focuses on hash table operations, sorting is implicitly involved in organizing results for analysis:
- **No Explicit Sorting**: Query results are written in the order of `consultas.csv`, but performance metrics (e.g., max/average tests) require aggregation.
- **Python’s Timsort**: Used internally for computing maximum and average list sizes, leveraging O(n log n) efficiency for small datasets.

The absence of explicit sorting in the core functionality underscores the hash table’s strength: direct key-based access eliminates the need for ordered data, achieving near-constant-time operations when collisions are minimized.

## Implementation

The code is implemented in **Python** with a modular design:
- **Nodo Class**: Represents a key-value pair with a link to the next node for chaining.
- **TabelaHash Class**:
  - Initializes the table with a given size.
  - Implements `funcao_hash`, `inserir`, and `buscar` methods.
- **Utility Functions**:
  - `carregar_dados`: Reads `players-fifa.csv` and populates the table.
  - `carregar_consultas`: Loads query IDs from `consultas.csv`.
  - `executar_experimento`: Runs the experiment for a given table size, computing and saving statistics.
- **Output Formatting**: Writes results to `experimentoM.txt` files in the required format, ensuring precise metrics (e.g., time in milliseconds, averages to two decimal places).

### Key Features
- **Efficiency**: Optimized for fast insertion and lookup with minimal collisions due to prime table sizes.
- **Robustness**: Handles all 18,944 players and arbitrary queries reliably.
- **Performance Tracking**: Detailed statistics provide insights into hash table behavior (e.g., collision frequency, query cost).
- **Modularity**: Separates data loading, table operations, and result generation for maintainability.

## Importance of the Project

This project is a critical component of the Data Sorting and Searching course, as it introduces students to hash tables—one of the most widely used data structures in computer science. Hash tables are foundational to applications like databases (e.g., indexing), caching (e.g., memoization), and search systems (e.g., dictionaries). By implementing and analyzing a hash table with real-world data, the project:
- **Demonstrates Efficiency**: Shows how hash tables achieve O(1) average-case performance for insertions and lookups.
- **Highlights Trade-offs**: Explores the impact of table size on collision rates and query performance, teaching optimization strategies.
- **Prepares for Scalability**: Handling 18,944 records prepares students for larger datasets in real-world applications.
- **Encourages Analytical Thinking**: Performance metrics (e.g., occupancy rate, list sizes) foster a deeper understanding of data structure design.

The optional bonus challenge (BEE 1256) reinforces these concepts by applying hash tables to a competitive programming problem, enhancing problem-solving skills and earning up to 25% extra points.

## How to Run

1. **Prerequisites**: Python 3.x installed.
2. **Input Files**: Place `players-fifa.csv` and `consultas.csv` in the same directory as the script.
3. **Execution**:
   ```bash
   python hash_table.py
