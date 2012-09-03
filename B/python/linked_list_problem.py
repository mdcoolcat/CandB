# linked list problem from CareerCup

from linked_list import *

# remove nodes with duplicated key from the list, without extra space
# O(n)
def remove_dup(l):
    if l.size() < 2:
        return l
    cur = l.get_first()
    while cur.next is not None:
        print l
        print cur
        prev = cur
        while prev.next is not None:
            print prev.next
            if prev.next == cur:
                prev.next = prev.next.next
                print 'after remove...prev ' + str(prev.next)
            if prev.next is None:
                break
            prev = prev.next
        if cur.next is None:
            break
        cur = cur.next
    return l


def main():
    l = Linked_list()
    l.append(Node(1))
    l.append(Node(1))
    l.append(Node(1))
    l.append(Node(1))
    l.append(Node(1))
    print remove_dup(l)

if __name__ == '__main__':
    main()
