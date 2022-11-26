# -----------------------------------------------------------
# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
#   Input: strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#   Input: strs = [""]
#   Output: [[""]]
# Example 3:
#   Input: strs = ["a"]
#   Output: [["a"]]
# -----------------------------------------------------------


import collections

# Solution 1: Dict to count characters, then compare with other words and add to arrays
#   Thoughts: Not ideal since used space from extra arrays.
class Solution(object):
    def groupAnagrams(self, strs):
        ds = []
        w = []
        skip = False
        for s in strs:
            nd = {}
            for x in s:
                if x not in nd:
                    nd[x] = 1
                else:
                    nd[x] += 1
            if nd in ds:
                w[ds.index(nd)].append(s)
            else:
                ds.append(nd)
                w.append([s])
        return w


# Solution 2: Sort words then organize by sorted words.
# Time Complexity: O(k * nlogn) where k is length of strs and n is length of n
#   - Can be O(kn) if using counting sort.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            k = "".join(sorted(s))
            if k not in d:
                d[k] = [s]
            else:
                d[k].append(s)
        r = []
        for v in d.values():
            r.append(v)
        return r


# Solution 3: Dictionary where key is 26 long list representing a count of each letter
# Essentially implementing counting sort. defaultdict for default value list if key doesnt exist
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        c = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for x in s:
                count[ord(x) - ord('a')] += 1
            t = tuple(count)
            c[t].append(s)
        return c.values()

# Quick solution
def ga(strs):
    d = collections.defaultdict(list)
    for x in strs:
        d[tuple(sorted(x))].append(x)
    return d.values()

print(ga(["eat","tea","tan","ate","nat","bat"]))