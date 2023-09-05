from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        current_example = []
        all_nodes = []

        current_node = head
        all_nodes.append(current_node)
        current_example.append([current_node.val, current_node.random])
        while current_node.next is not None:
            current_example.append([current_node.next.val, current_node.next.random])
            all_nodes.append(current_node.next)
            current_node = current_node.next

        new_current_example = current_example
        for pos, i in enumerate(current_example):
            if i[1] is None:
                continue
            else:
                new_current_example[pos][1] = all_nodes.index(i[1])

        def create_node(example):
            next_node = None
            for n in range(len(example)):
                current_node = Node(example[-1 - n][0], next_node, None)
                next_node = current_node
            head = current_node

            for n in range(len(example)):
                current_node = head
                k = n
                while k > 0:
                    current_node = current_node.next
                    k -= 1

                random = example[n][1]
                if random is None:
                    random_node = None
                else:
                    random_node = head
                    while random > 0:
                        random_node = random_node.next
                        random -= 1
                current_node.random = random_node

            return head

        return create_node(new_current_example)


def create_node(example):
    next_node = None
    for n in range(len(example)):
        current_node = Node(example[-1 - n][0], next_node, None)
        next_node = current_node
    head = current_node

    for n in range(len(example)):
        current_node = head
        k = n
        while k > 0:
            current_node = current_node.next
            k -= 1

        random = example[n][1]
        if random is None:
            random_node = None
        else:
            random_node = head
            while random > 0:
                random_node = random_node.next
                random -= 1
        current_node.random = random_node

    return head

example1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
head_ex1 = create_node(example1)
s = Solution()
print(s.copyRandomList(head_ex1).val)
print(s.copyRandomList(head_ex1).next.val)
print(s.copyRandomList(head_ex1).next.next.val)
print(s.copyRandomList(head_ex1).next.next.next.val)
print(s.copyRandomList(head_ex1).next.next.next.next.val)
