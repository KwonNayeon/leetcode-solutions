"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
   def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       if not node:
           return None

       dict = {}

       def dfs(node):
           if node.val in dict:  # 이미 복사한 노드라면
               return dict[node.val]  # 해당 복사본 반환

           # 새로운 노드 생성
           copy = Node(node.val)
           dict[node.val] = copy  # dictionary에 기록

           # 각 neighbor에 대해서도 같은 과정 수행
           for neighbor in node.neighbors:
               copy.neighbors.append(dfs(neighbor))

           return copy

       return dfs(node)
        