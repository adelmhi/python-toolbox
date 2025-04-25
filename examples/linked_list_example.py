"""
Example usage of the python-toolbox linked list implementation.
"""
from python_toolbox.data_structures.linked_list.singly_linked_list import SinglyLinkedList

def main():
    # Create a new linked list
    ll = SinglyLinkedList()
    
    # Append some elements
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    # Prepend an element
    ll.prepend(0)
    
    # Print the list
    print(f"Linked list: {ll}")
    print(f"Length: {len(ll)}")
    
    # Check if an element exists
    print(f"Contains 2: {ll.contains(2)}")
    print(f"Contains 5: {ll.contains(5)}")
    
    # Get the last element
    print(f"Last element: {ll.get_last()}")
    
    # Iterate over the list
    print("Elements:")
    for element in ll:
        print(f"- {element}")

if __name__ == "__main__":
    main() 