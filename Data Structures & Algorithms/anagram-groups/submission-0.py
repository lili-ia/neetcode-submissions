class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for str in strs:
            srtd = ''.join(sorted(str))
            res.setdefault(srtd, []).append(str)

        return list(res.values())