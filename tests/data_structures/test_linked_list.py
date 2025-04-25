from python_toolbox.data_structures.linked_list.singly_linked_list import SinglyLinkedList

def test_empty_list():
    ll = SinglyLinkedList()
    assert len(ll) == 0
    assert str(ll) == ""

def test_append():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert len(ll) == 3
    assert str(ll) == "1 -> 2 -> 3"

def test_prepend():
    ll = SinglyLinkedList()
    ll.prepend(1)
    ll.prepend(2)
    ll.prepend(3)
    assert len(ll) == 3
    assert str(ll) == "3 -> 2 -> 1"

def test_delete_index():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    assert ll.delete_index(2) is True
    assert len(ll) == 2
    assert str(ll) == "1 -> 2"
    
    assert ll.delete_index(4) is False
    assert len(ll) == 2

def test_remove():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    assert ll.remove(2) is True
    assert len(ll) == 2
    assert str(ll) == "1 -> 3"
    
    assert ll.remove(4) is False
    assert len(ll) == 2

def test_contains():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    assert ll.contains(2) is True
    assert ll.contains(4) is False 