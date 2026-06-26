class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = defaultdict(list)

        for strr in strs:
            key = ''.join(sorted(strr))
            lists[key].append(strr)
        
        return list(lists.values())

             


        