from types import List 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
    
# Time Complexity: O(m + n), where m is the size of prerequisites, and n is the number of courses

# Space Complexity: O(m + n), where m is the size of prerequisites, and n is the number of courses.

# Create the adjacency list using the given prequisites. After, perform DFS on all the nodes in the Graph and check if there is a cycle, if there is a cycle, we know that 
# it is not possible to take all the courses required, return False. If there are no cycles, return True.
