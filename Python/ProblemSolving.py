"""----You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.----"""

"""class Solution:
    def mergeAlternately(self, word1, word2):
        word = ""
        i, j, count = 0, 0, 0
        while i < len(word1) and j < len(word2):
            if count % 2 == 0:
                word = word + word1[i]
                i+=1
            if count % 2 != 0:
                word = word + word2[j]
                j+=1
            count+=1
        while i < len(word1):
            word = word + word1[i]
            i+=1
        while j < len(word2):
            word = word + word2[j]
            j+=1
        return word"""

"""class Solution:
    def mergeAlternately(self, word1, word2):
        word = ""
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                word = word + word1[i]
                i += 1
            if j < len(word2):
                word = word + word2[j]
                j += 1
        return word"""

"""class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return "".join(result)"""

"""word1 = "vivek"
word2 = "tendulkar"
my_task = Solution()
print(my_task.mergeAlternately(word1, word2))"""

"""----Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.----"""
"""class Solution:
    def gcdOfStrings(self, str1, str2):
        if len(str1) < len(str2):
            base = str1
        base = str2
        while len(base):
            if len(str1) % len(base) == 0 and len(str2) % len(base) == 0:
                k1 = len(str1) // len(base)
                k2 = len(str2) // len(base)
                str_1 = base * k1
                str_2 = base * k2
                if str1 != str_1 or str2 != str_2:
                    base = base[:len(base)-1]
                    break
                return base
            base = base[:len(base)-1]
        return -1 """

"""import math
class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 == str2 + str1:
            k = math.gcd(len(str1), len(str2))
            return str1[:k]
        return -1"""

"""str1 = "abcdabcdabcd"
str2 = "abcdabcd"
my_task = Solution()
print(my_task.gcdOfStrings(str1, str2))"""

"""----Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, 
they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.----"""

"""class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = [True] * len(candies)
        for i in range(len(candies)):
            x = candies[i] + extraCandies
            for j in range(len(candies)):
                if candies[j] > x:
                    result[i] = False
                    break
        return result"""

"""class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies < maxCandies:
                result.append(False)
            else:
                result.append(True)
        return result"""

"""class Solution:
    def kidsWithCandies(self, candies, extraCandies):
	    maxCandies = max(candies)
	    return [candy + extraCandies >= maxCandies for candy in candies]"""

"""candies = [2,3,5,1,3]
extraCandies = 3
my_task = Solution()
print(my_task.kidsWithCandies(candies, extraCandies))"""

"""----Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
->If the group's length is 1, append the character to s.
->Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.----"""

"""class Solution:
    def compress(self, chars) -> int:
        c = 1
        x = ""
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                c+=1
            else:
                if c>1:
                    x = x+chars[i-1]+str(c)
                    c=1
                else:
                    x = x+chars[i-1]
                    c=1
        if c>1:
            x = x+chars[-1]+str(c)
        else:
            x = x+chars[-1]
        print(x) 
        chars = list(x)
        print(chars)
        return len(chars)"""

#Not the proper solution.
"""class Solution:
    def compress(self, chars) -> int:
        i = 0
        j = 0
        k = 0
        while i < len(chars):
            if chars[i] == chars[j]:
                k+=1
                i+=1
            else:
                if k > 1 and k <= 9:
                    del chars[j+1:i]
                    chars.insert(j+1, str(k))
                    j = i
                    k = 0
                elif k > 9 and k <= 99:
                    del chars[j+1:i]
                    chars.insert(j+1, str(k)[0])
                    chars.insert(j+2, str(k)[1])
                    j = i
                    k = 0
                else:
                    del chars[j+1:i]
                    j = i
                    k = 0
        if k > 1 and k <= 9:                    
            del chars[j+1:i]
            chars.insert(j+1, str(k))
        elif k > 9 and k <= 99:
            del chars[j+1:i]
            chars.insert(j+1, str(k)[0])
            chars.insert(j+2, str(k)[1])
        else:
            del chars[j+1:i]
        print(chars)
        return len(chars)"""

"""my_task = Solution()
chars = ["a","a","b","b","c","c","c"]
print(my_task.compress(chars))
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(my_task.compress(chars))"""

"""----Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single 
space separating the words. Do not include any extra spaces.----"""

"""class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        a = s.strip().split()
        while a:
            c = a.pop()
            result.append(c)
        return " ".join(result)"""

"""class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])"""

"""import re #Regular Expression
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(re.sub(r'\s{1,}', ' ', s.strip()).split(' ')[::-1])"""

"""s = "the sky is blue"
my_task = Solution()
print(my_task.reverseWords(s))"""

"""----Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.----"""
"""class Solution:
    def moveZeroes(self, nums):        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                while i+1 < len(nums):
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    i+=1
        return nums"""
    
"""class Solution:
    def moveZeroes(self, nums):        
        j = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                while i+1 < len(nums)-j:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    i+=1
                j+=1
        return nums"""

"""class Solution:
    def moveZeroes(self, nums):
        arr = [] 
        j = 0
        k = len(nums)-1
        for i in range(len(nums)):
            if nums[i] != 0:
                arr.insert(j, nums[i])
                j+=1
            else:
                arr.insert(k, 0)
                k-=1
        for i in range(len(nums)):
            nums[i] = arr[i]
        return nums"""

"""class Solution:
    def moveZeroes(self, nums):
        i = 0
        for k in range(len(nums)):
            if nums[k] != 0:
                nums[i] = nums[k]
                i+=1
        for k in range(i, len(nums)):
            nums[k] = 0
        return nums"""

"""class Solution:
    def moveZeroes(self, nums):
        lastNonZeroFoundAt = 0
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[current], nums[lastNonZeroFoundAt] = nums[lastNonZeroFoundAt], nums[current]
                lastNonZeroFoundAt += 1
        return nums"""

"""nums = [0,1,0,3,12,0,13,0,0,67]    
my_task = Solution()
print(my_task.moveZeroes(nums))"""

""""----You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.----"""

"""from collections import Counter
class Solution:
    def maxOperations(self, nums, k):
        res, d = 0, Counter(nums)
        for val1, cnt in d.items():
            val2 = k - val1
            # it's trick to get rid of duplicates pairs, consider only pairs where val1 <= val2
            if val2 < val1 or val2 not in d: 
                continue
            if val1 != val2: 
                res += min(cnt, d[val2])
            else:
                res += cnt//2
        return res"""
    
"""class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        res, l, r = 0, 0 ,len(nums) - 1

        while l < r:
            S = nums[l] + nums[r]
            if S > k:
                r -= 1
            elif S < k:
                l += 1
            else:
                res += 1
                l += 1
                r -= 1
        return res"""

"""nums = [1,2,3,4]
my_task = Solution()
print(my_task.maxOperations(nums, 5))"""

"""----You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line 
are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.----"""

"""def maxArea(height):
    l = 0
    r = len(height)-1
    maxArea = 0
    while l < r:
        a = (r - l) * min(height[l], height[r])
        maxArea = max(maxArea, a)
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    return maxArea
height = [1,8,6,2,5,4,8,3,7]
maxArea(height)"""

"""----Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.----"""
"""class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i-k] in vowels)
            answer = max(answer, count)
            if answer == k:
                break
        return answer"""
"""s = "abciiidef"
k = 3
my_task = Solution()
print(my_task.maxVowels(s, k))"""

"""----Given a binary array nums, you should delete one element from it. Return the size of the longest non-empty subarray containing 
only 1's in the resulting array. Return 0 if there is no such subarray.----"""
"""class Solution:
    def longestSubarray(self, nums):
        zeroCount = 0
        longestWindow = 0
        start = 0
        for i in range(len(nums)):
            zeroCount += (nums[i] == 0)
            while zeroCount > 1:
                zeroCount -= (nums[start] == 0)
                start += 1
            longestWindow = max(longestWindow, (i - start))
        return longestWindow"""
  
"""class Solution:
    def longestSubarray(self, nums):
        l = 0
        r = 0
        p = []
        zeroCount = 0
        longestWindow = 0
        while r < len(nums):
            if nums[r] == 0:
                zeroCount += 1
                r += 1
                p.append(r)
                if zeroCount > 1:
                    l = p.pop(0)
            else:
                r += 1
            longestWindow = max (longestWindow, (r - l - 1))
        return longestWindow"""

"""nums = [0,1,1,1,0,1,1,0,1]
my_task = Solution()
print(my_task.longestSubarray(nums))"""

"""----There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
Return the highest altitude of a point.----"""    
"""class Solution:
    def largestAltitude(self, gain):
        current_height = 0
        maximum_height = 0
        for i in range(len(gain)):
            current_height = current_height + gain[i] 
            maximum_height = max(maximum_height, current_height)
        return maximum_height"""
"""class Solution:
    def largestAltitude(self, gain):
        height = [0 for i in range(len(gain)+1)]
        for i in range(1, len(gain)+1):
            height[i] = height[i-1] + gain[i-1] 
        print(height)
        return max(height)"""
"""gain = [-5,1,5,0,-7]
my_task = Solution()
print(my_task.largestAltitude(gain))"""

"""----Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers 
strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.----"""
"""class Solution:
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1"""

"""class Solution:
    def pivotIndex(self, nums, k = 0):
        sum_l, sum_r = 0, 0
        for i in range(len(nums)):
            if i < k:
                sum_l = sum_l + nums[i]
            if i > k:
                sum_r = sum_r + nums[i]
        if sum_l == sum_r:
            return k
        if sum_l != sum_r:
            k += 1
            if k < len(nums):
                return self.pivotIndex(nums, k)
            else:
                return -1"""
"""nums = [1,7,3,6,5,6]
my_task = Solution()
print(my_task.pivotIndex(nums))"""
    
"""----A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and 
both diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).----"""
"""class Solution:
    def numMagicSquaresInside(self, grid):
        R, C = len(grid), len(grid[0])

        def magic(a,b,c,d,e,f,g,h,i):
            return ((sorted([a,b,c,d,e,f,g,h,i]) == range(1, 10)) and
                (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15))

        ans = 0
        for r in range(R-2):
            for c in range(C-2):
                if grid[r+1][c+1] != 5: 
                    continue  
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans
grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
my_task = Solution()
print(my_task.numMagicSquaresInside(grid))"""
#There is some problem in the solution.

#Graph
"""----There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, 
denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
return true if you can visit all the rooms, or false otherwise."""
"""class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        visited = [0] * len(rooms)
        stack = rooms[0]
        result = True
        while stack:
            x = stack.pop()
            if x not in visited:
                visited[x] = x
                stack = stack + rooms[x]
        for i in range(len(visited)):
            if i == visited [i]:
                continue
            else:
                result = False
                break
        return result"""
"""class Solution():
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack: 
            node = stack.pop() 
            for key in rooms[node]: 
                if not seen[key]: 
                    seen[key] = True 
                    stack.append(key)
        return all(seen)"""
"""rooms = [[1,3],[3,0,1],[2],[0]]
my_task = Solution()
print(my_task.canVisitAllRooms(rooms))"""

"""class Solution:
    def minReorder(self, n, connections):
        graph = [[] for i in range(0,n)]

        for item in connections:
            graph[item[0]].append([item[1],1])
            graph[item[1]].append([item[0],0])
        print(graph)

        dq = []
        dq.append(0)
        visited = [0 for i in range(0,n)]
        visited[0] = 1
        res = 0
        while(len(dq)>0):
            v = dq.pop(0)
            for x,y in graph[v]:
                if visited[x] == 0:
                    visited[x] = 1
                    dq.append(x);
                    if y == 1: 
                        res += 1
        return res"""
"""class Solution:
    def minReorder(self, n, connections):
        count = 0
        adj = {}
        for item in connections:
            adj[item[0]]=({item[1], 1})
            adj[item[1]]=({item[0], 0})  
        self.DFS(0, -1, adj)  
        return count

    def DFS(self, node, parent, adj):
        for [child,sign] in adj[node]:
            if child != parent:
                count += sign"""
"""n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
my_task = Solution()
print(my_task.minReorder(n, connections))"""

"""----You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and 
values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is 
no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.----"""

"""from typing import List

class Solution:
    def dfs(self, node: str, dest: str, gr: dict, vis: set, ans: List[float], temp: float) -> None:
        if node in vis:
            return
        vis.add(node)
        
        if node == dest:
            ans[0] = temp
            return

        for ne, val in gr[node].items():
            self.dfs(ne, dest, gr, vis, ans, temp * val)

    def buildGraph(self, equations: List[List[str]], values: List[float]) -> dict:
        gr = {}

        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]

            if dividend not in gr:
                gr[dividend] = {}
            if divisor not in gr:
                gr[divisor] = {}

            gr[dividend][divisor] = value
            gr[divisor][dividend] = 1.0 / value

        return gr

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gr = self.buildGraph(equations, values)
        finalAns = []

        for query in queries:
            dividend, divisor = query

            if dividend not in gr or divisor not in gr:
                finalAns.append(-1.0)
            else:
                vis = set()
                ans = [-1.0]
                temp = 1.0
                self.dfs(dividend, divisor, gr, vis, ans, temp)
                finalAns.append(ans[0])
                #print(vis, ans)

        return finalAns""" 

"""from typing import List, Mapping, defaultdict, Hashable

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        T = Hashable
        W = int | float
        WeightedGraph = Mapping[T, Mapping[T, W]]
        def solve_div(graph: WeightedGraph, src: T, dest: T, seen: set[T]) -> W:
            seen.add(src)
            q = next((
                graph[src][v] * x
                for v in graph[src]
                if v not in seen and
                (x := solve_div(graph, v, dest, seen)) != -1
            ), -1) if src != dest else 1
            seen.remove(src)
            return q
        
        g = defaultdict(lambda: defaultdict(int))
        for (n, d), v in zip(equations, values): g[n][d] = v; g[d][n] = 1 / v

        return [solve_div(g, s, d, set()) if s in g and d in g else -1 for s, d in queries]"""         
            
"""equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
my_task = Solution()
#print(my_task.buildGraph(equations, values))
print(my_task.calcEquation(equations, values, queries))"""

"""from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
            """



