class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> lists = new HashMap<>();
        String sorted;
        String key;
        for(int i=0; i<strs.length; i++){
            char[] str = strs[i].toCharArray();
            Arrays.sort(str);
            sorted = new String(str);
            key = sorted;
            
             lists.computeIfAbsent(key, k -> new ArrayList<>()).add(strs[i]);
        }
        return new ArrayList<>(lists.values());
    }
}
