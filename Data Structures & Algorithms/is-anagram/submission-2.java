class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> cs = new HashMap<>();
        HashMap<Character, Integer> ct = new HashMap<>();

        for(int i=0; i<s.length(); i++){
            cs.put(s.charAt(i), cs.getOrDefault(s.charAt(i), 0) + 1);
        }

        for(int i=0; i<t.length(); i++){
            ct.put(t.charAt(i), ct.getOrDefault(t.charAt(i), 0) + 1);
        }

        return cs.equals(ct);
    }
}
