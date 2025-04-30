#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        visited = set()  # Set to track visited nodes
        
        while head:
            if head in visited:  # If the node has already been visited, a loop is detected
                # Find the start of the loop
                loop_start = head
                count = 1
                node = head.next
                while node != loop_start:  # Traverse the loop to count the length
                    count += 1
                    node = node.next
                return count  # Return the length of the loop
            visited.add(head)  # Add the current node to the visited set
            head = head.next  # Move to the next node
        
        return 0  # No loop detected, return 0


#{ 
 # Driver Code Starts
import sys


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


def loop_here(head, pos):
    if pos == 0:
        return

    walk = head
    for _ in range(1, pos):
        walk = walk.next

    tail = head
    while tail.next:
        tail = tail.next

    tail.next = walk


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        k = int(data[index + 1])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        loop_here(head, k)
        ob = Solution()
        res = ob.countNodesInLoop(head)
        print(res)
        print("~")
        index += 2

# } Driver Code Ends