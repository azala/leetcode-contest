class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ret = 0
        for i in range(n):
            if word[i] in 'aeiou':
                # for any vowel at index i, count the number of substrings that contain it:
                # You can pick the left bound of the substring to be anywhere from index 0...i
                # You can pick the right bound to be anywhere from i...n-1
                # Multiply the two to get the # of combinations of left/right bounds that contain this vowel
                ret += (i+1) * (n-i)
        return ret