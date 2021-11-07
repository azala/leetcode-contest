class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ret = 0
        # iterate over all possible substring left bounds
        for i in range(len(word)):
            s = set() # set of vowels we've seen so far, starting with index i
            # iterate over all possible substring right bounds
            for j in range(i, len(word)):
                if word[j] not in 'aeiou':
                    break # invalid substring
                else:
                    s.add(word[j]) # add vowel to the collection of seen so far
                ret += int(len(s) == 5) # if we've seen all vowels, add 1 to the count
        return ret