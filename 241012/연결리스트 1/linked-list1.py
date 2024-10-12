import sys

input = sys.stdin.readline

s_init = input().rstrip()
n = int(input().rstrip())

class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

    def insert_prev(self, node):
        node.prev = self.prev
        node.next = self
        if self.prev:
            self.prev.next = node
        self.prev = node

    def insert_next(self, node):
        node.prev = self
        node.next = self.next
        if self.next:
            self.next.prev = node
        self.next = node

def print_node(node):
    print(node.prev.value if node.prev else '(Null)', end=' ')
    print(node.value if node else '(Null)', end=' ')
    print(node.next.value if node.next else '(Null)')

cur = Node(s_init)

for i in range(n):
    order = input().rstrip().split()

    if order[0] == '1':
        s_value = order[1]
        cur.insert_prev(Node(s_value))
        print_node(cur)

    elif order[0] == '2':
        s_value = order[1]
        cur.insert_next(Node(s_value))
        print_node(cur)

    elif order[0] == '3':
        if cur.prev:
            cur = cur.prev
        print_node(cur)

    elif order[0] == '4':
        if cur.next:
            cur = cur.next
        print_node(cur)