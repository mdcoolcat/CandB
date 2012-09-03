# Implementation of single linked_list 
# Danielle Mei

import sys
import os
import commands
import re

class Node(object):
    def __init__(self, key):
        self.key = key
        self.next = None

    def __repr__(self):
        return '%r' % (self.key)

    def __str__(self):
        return str(self.key)

    def  __cmp__(self, other):
        return self.key - other.key

class Linked_list(object):
    def __init__(self):
        self.__head = None 
        self.__tail = None
        self.__len = 0

    def size(self):
        return self.__len
# **** get ****
    def get_first(self):
        return self.__head

    def get_last(self):
        return self.__tail

    # return index of the element, -1 if not found
    def index_of(self, element):
        if self.__len == 0:
            return -1 
        index = 0
        n = self.__head
        while n is not None and n is not element:
            n = n.next
            index += 1
        if n is None:
            return -1
        return index

# **** add ****
    # append a node to list end. O(1)
    def append(self, element):
        if self.__len == 0:
            self.__head = element
            self.__tail = element
        else:
            self.__tail.next = element
            self.__tail = element
        self.__len += 1

    # prepend a node O(1)
    def prepend(self, element):
        if self.__len == 0:
            self.__head = element
            self.__tail = element
        else:
            element.next = self.__head
            self.__head = element
        self.__len += 1

    # insert a node as sorted (natual order of key), O(n)
    def insert(self, element):
        if (self.__len == 0) or \
                (self.__len > 0 and self.__head >= element):
            self.prepend(element)
        else:
            n = self.__head
            while n.next is not None and n.next < element:
                n = n.next
            element.next = n.next
            n.next = element
            if element.next is None:
                self.__tail = element
        self.__len += 1

# ***** remove ****
    def remove_first(self):
        if self.__len == 0:
            return None
        ele = self.__head
        self.__head = self.__head.next
        if self.__len ==  1: # it's the only element
            self.__tail = None
        self.__len -= 0
        return ele

    def remove_last(self):
        if self.__len == 0:
            return None
        elif self.__len == 1:
            ele = self.__head
            self.__head = None
            self.__tail = None
            self.__len = 0
            return ele
        else:
            # find the new last... should impl as double list to lower time
            ele = self.__tail
            prev = self.__head
            while prev.next is not self.__tail:
                prev = prev.next
            prev.next = None
            self.__tail = prev
            self.__len -= 1
            return ele

    # delete node
    # return the deleted node, or None if not found
    def remove(self, element):
        if self.__len == 0:
            return None
        n = self.__head
        while n.next is not None and n.next is not element:
            n = n.next
        if n.next is None:
            return None
        ele = n.next    # the one will be deleted
        n.next = ele.next
        if ele.next is None:
            self.__tail = n
        self.__len -= 1
        return ele


    # print the list
    def __str__(self):
        s = str()
        n = self.__head
        while n is not None:
            s = s + str(n.key) + ' -> '
            n = n.next

        return s
  
# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
      if got == expected:
          prefix = ' OK '
      else:
          prefix = '  X '

      print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    l = Linked_list()
    n = Node(6)
    n2 = Node(-1)
    n3 = Node(0)
    l.insert(Node(2))
    l.insert(n)
    l.insert(Node(5))
    l.insert(n2)
    l.prepend(Node(6))
    print l, l.get_first(), l.get_last()
    print l.index_of(n), l.index_of(n3)
    print l.remove(n)
    print l, l.get_first(), l.get_last()
    print l.remove_last()
    print l, l.get_first(), l.get_last()

if __name__ == '__main__':
    main()
