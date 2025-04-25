# Python Toolbox

A comprehensive collection of algorithms and data structures implemented in Python.

## Features

- Data structures
  - Singly Linked List with tail pointer
    - O(1) append and prepend operations
    - O(1) access to last element
    - Efficient memory management
- Well-documented and type-hinted code
- Comprehensive test suite

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-toolbox.git
cd python-toolbox

# Install in development mode
pip install -e .
```

## Usage

```python
from python_toolbox.data_structures.linked_list import SinglyLinkedList

# Create a new linked list
ll = SinglyLinkedList()

# Append elements
ll.append(1)
ll.append(2)
ll.append(3)

# Prepend an element
ll.prepend(0)

# Check if an element exists
print(ll.contains(2))  # True
print(ll.contains(5))  # False

# Get the last element
print(ll.get_last())  # 3

# Iterate over the list
for element in ll:
    print(element)  # 0, 1, 2, 3
```

## Project Structure

```
python-toolbox/
├── src/
│   ├── data_structures/
│   │   └── linked_list/
│   │       ├── __init__.py
│   │       └── singly_linked_list.py
│   └── __init__.py
├── tests/
│   └── data_structures/
│       └── test_linked_list.py
├── examples/
│   └── linked_list_example.py
└── docs/
```

## Development

1. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

2. Run tests:
   ```bash
   pytest tests/
   ```

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

MIT License 