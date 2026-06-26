class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # //gives each key a default list. we can assign whatever ds we want here as default :)
        lists = defaultdict(list) 

        for strr in strs:
            key = ''.join(sorted(strr))
            lists[key].append(strr)
        
        return list(lists.values())

             


        