"""
Implementation of a singly linked list with a tail pointer.

This module provides a SinglyLinkedList class that implements a singly linked list
data structure with O(1) append and prepend operations. The list maintains a tail
pointer for efficient access to the last element.

Example:
    >>> lst = SinglyLinkedList()
    >>> lst.append(1)
    >>> lst.append(2)
    >>> lst.prepend(0)
    >>> list(lst)  # Convert to list for display
    [0, 1, 2]
"""

from typing import Any, Optional, Iterator


class Node:
    """
    A node in the singly linked list.
    
    Attributes:
        data (Any): The data stored in the node
        next (Optional[Node]): Reference to the next node in the list
    """
    def __init__(self, data: Any, next: "Node" = None):
        self.data = data
        self.next: Optional[Node] = next


class SinglyLinkedList:
    """
    A singly linked list implementation with a tail pointer.
    
    This implementation provides O(1) append and prepend operations by maintaining
    a tail pointer. It supports iteration, length checking, and various insertion
    and deletion operations.
    
    Attributes:
        __head (Optional[Node]): The first node in the list
        __tail (Optional[Node]): The last node in the list
        __size (int): The number of nodes in the list
    
    Example:
        >>> lst = SinglyLinkedList()
        >>> lst.append(1)
        >>> lst.append(2)
        >>> len(lst)
        2
        >>> lst.prepend(0)
        >>> list(lst)
        [0, 1, 2]
    """
    
    def __init__(self):
        self.__head: Optional[Node] = None
        self.__tail: Optional[Node] = None
        self.__size: int = 0

    def __len__(self) -> int:
        """
        Return the number of nodes in the list.
        
        Returns:
            int: The number of nodes in the list
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> len(lst)
            1
        """
        return self.__size

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over the data in the list.
        
        Yields:
            Any: The data stored in each node
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> [x for x in lst]
            [1, 2]
        """
        current = self.__head
        while current is not None:
            yield current.data
            current = current.next

    def is_empty(self) -> bool:
        """
        Check if the list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.is_empty()
            True
            >>> lst.append(1)
            >>> lst.is_empty()
            False
        """
        return self.__size == 0

    def __is_singleton(self) -> bool:
        """
        Check if the list has only one node.
        
        Returns:
            bool: True if the list has exactly one node, False otherwise
        """
        return self.__head == self.__tail

    def __get_previous_node(self, target_node: Node) -> Optional[Node]:
        """
        Get the previous node of the target node.
        
        Args:
            target_node (Node): The node whose previous node we want to find
            
        Returns:
            Optional[Node]: The previous node if found, None otherwise
        """
        current = self.__head
        while current is not None and current.next != target_node:
            current = current.next
        return current

    def append(self, data: Any) -> None:
        """
        Append a new node with the given data to the end of the list.
        
        This operation is O(1) due to the tail pointer.
        
        Args:
            data: The data to append
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> list(lst)
            [1, 2]
        """
        new_node = Node(data)
        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def prepend(self, data: Any) -> None:
        """
        Prepend a new node with the given data to the beginning of the list.
        
        This operation is O(1).
        
        Args:
            data: The data to prepend
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.prepend(2)
            >>> lst.prepend(1)
            >>> list(lst)
            [1, 2]
        """
        new_node = Node(data, self.__head)
        if self.is_empty():
            self.__head = self.__tail = new_node
        self.__head = new_node
        self.__size += 1

    def insert_after(self, target_data: Any, data: Any) -> None:
        """
        Insert a new node with the given data after the node containing target_data.
        
        This operation is O(n) in the worst case as it requires traversing the list
        to find the target node.
        
        Args:
            target_data: The data of the node after which to insert
            data: The data to insert
            
        Raises:
            ValueError: If target_data is not found in the list
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(3)
            >>> lst.insert_after(1, 2)
            >>> list(lst)
            [1, 2, 3]
        """
        current = self.__head
        while current is not None and current.data != target_data:
            current = current.next
            
        if current is None:
            raise ValueError(f"Target data {target_data} not found in the list")
            
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        
        if current == self.__tail:
            self.__tail = new_node
            
        self.__size += 1

    def get_index(self, data: Any) -> int:
        """
        Get the index of the first occurrence of the given data.

        This operation is O(n) in the worst case as it requires traversing the list
        to find the target node.
        
        Args:
            data: The data to search for
            
        Returns:
            int: The index of the first occurrence, or -1 if not found
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> lst.get_index(2)
            1
        """
        if self.is_empty():
            return -1
        current = self.__head
        index = 0
        while current is not None and current.data != data:
            current = current.next
            index += 1
        return index if current is not None else -1

    def delete_first(self) -> bool:
        """
        Delete the first node in the list.
        
        Returns:
            bool: True if the deletion was successful, False otherwise
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> lst.delete_first()
            True
            >>> list(lst)
            [2]
        """
        if self.is_empty():
            print("Warning: Cannot delete from empty list")
            return False
        if self.__is_singleton():
            self.__head = self.__tail = None
        else:
            new_head = self.__head.next
            self.__head = None # help garbage collection
            self.__head = new_head
        self.__size -= 1
        return True

    def delete_last(self) -> bool:
        """
        Delete the last node in the list.
        
        Returns:
            bool: True if the deletion was successful, False otherwise
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> lst.delete_last()
            True
            >>> list(lst)
            [1]
        """
        if self.is_empty():
            print("Warning: Cannot delete from empty list")
            return False
        if self.__is_singleton():
            self.__head = self.__tail = None
        else:
            new_tail = self.__get_previous_node(self.__tail)
            new_tail.next = None # help garbage collection
            self.__tail = new_tail
        self.__size -= 1
        return True

    def delete_index(self, index: int) -> bool:
        """
        Delete the node at the given index.
        
        Args:
            index: The index of the node to delete
            
        Returns:
            bool: True if the deletion was successful, False otherwise
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> lst.append(3)
            >>> lst.delete_index(1)
            True
            >>> list(lst)
            [1, 3]
        """
        if index < 0 or index >= self.__size:
            print("Warning: Index out of bounds")
            return False
        elif index == 0:
            return self.delete_first()
        elif index == self.__size -1:
            return self.delete_last()
        else:
            previous = self.__head
            for _ in range(index - 1):
                previous = previous.next
            current = previous.next
            previous.next = current.next
            current.next = None # help garbage collection
            self.__size -= 1
            return True

    def remove(self, data: Any) -> bool:
        """
        Remove the first node containing the given data.
        
        Args:
            data: The data to remove
            
        Returns:
            bool: True if the removal was successful, False otherwise
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> lst.append(3)
            >>> lst.remove(2)
            True
            >>> list(lst)
            [1, 3]
        """
        if self.is_empty():
            print("Warning: Cannot remove from empty list")
            return False
            
        index = self.get_index(data)
        if index == -1:
            print(f"Warning: Data {data} not found in the list")
            return False
        return self.delete_index(index)

    def get_last(self) -> Any:
        """
        Get the data of the last node in the list.
        
        This operation is O(1) due to the tail pointer.
        
        Returns:
            Any: The data of the last node
            
        Raises:
            IndexError: If the list is empty
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> lst.get_last()
            2
        """
        if self.is_empty():
            raise IndexError("Cannot get last element from empty list")
        return self.__tail.data

    def contains(self, data: Any) -> bool:
        """
        Indicates if the list contains the given data.
        
        Args:
            data: The data to search for
            
        Returns:
            bool: True if the data is found, False otherwise
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> lst.contains(2)
            True
            >>> lst.contains(3)
            False
        """
        return self.get_index(data) != -1

    def __str__(self) -> str:
        """
        Return a string representation of the list.
        
        Returns:
            str: A string representation of the list
            
        Example:
            >>> lst = SinglyLinkedList()
            >>> lst.append(1)
            >>> lst.append(2)
            >>> str(lst)
            '1 -> 2'
        """
        elements = []
        current = self.__head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return ' -> '.join(elements) 
    
    def __repr__(self) -> str:
        """
        Return a string representation of the list.
        
        Returns:
            str: A string representation of the list
        """
        return self.__str__()

if __name__ == "__main__":
    lst = SinglyLinkedList()
    lst.append(2)
    print(lst)
    lst.prepend(1)
    print(lst)

