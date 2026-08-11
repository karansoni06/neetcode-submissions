class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_output = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_output[sorted_word].append(word)
        return list(anagram_output.values())