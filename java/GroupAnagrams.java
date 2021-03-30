/**
 * Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 */
class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) {
            return new ArrayList<>();
        }

        // SortedString -> List of words
        final Map<String, List<String>> sortMap = new HashMap<>();
        // Proactively store each new List instead of using map.values() below
        final List<List<String>> sortLists = new ArrayList<>();

        for (String s : strs) {
            // The List within the map
            final List<String> anagramList;

            // Sort the String
            final char[] arr = s.toCharArray();
            Arrays.sort(arr);
            final String sorted = String.valueOf(arr);

            if (sortMap.containsKey(sorted)) {
                // This key already exists, get out of Map
                anagramList = sortMap.get(sorted);
            } else {
                // Create a new List, adding it to both containers
                anagramList = new ArrayList<>();
                sortMap.put(sorted, anagramList);
                sortLists.add(anagramList);
            }

            anagramList.add(s);
        }

        return sortLists;
    }
}
