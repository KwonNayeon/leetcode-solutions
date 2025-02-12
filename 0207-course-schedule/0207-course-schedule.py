class Solution:
   def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       graph = [[] for _ in range(numCourses)]
       for course, prereq in prerequisites:
           graph[course].append(prereq)
       
       visited = [False] * numCourses
       path = [False] * numCourses
       
       def dfs(course):
           if path[course]:
               return False
           if visited[course]:
               return True
               
           path[course] = True
           
           for prereq in graph[course]:
               if not dfs(prereq):
                   return False
                   
           path[course] = False
           visited[course] = True
           
           return True
       
       for course in range(numCourses):
           if not dfs(course):
               return False
       
       return True