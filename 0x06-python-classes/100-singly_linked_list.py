#!/usr/bin/python3
"""A class node that defines a singliy linked list"""
class Node:
    """Private instance atrribute data"""
    
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self._data = value
        
    @property
    def next_node(self):
        return self._next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        else:
            self._next_node = value   

"""a class SinglyLinkedList that defines a singly linked list"""

class SinglyLinkedList:
    """Private instance atrribute head"""
    
    def __init__(self):
        self.head = None
        
    def sorted_insert(self, value):
        new_node = Node(value)
        
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()