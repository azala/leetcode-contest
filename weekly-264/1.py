class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(' ')
        punc = set(['!', '.', ','])
        dig = set([str(i) for i in range(10)])        
        ret = 0
        for w in words:
            # empty string is not a word
            if not len(w):
                continue
            is_word = True
            for i, c in enumerate(w):
                # if punctuation, it can only be at the end
                if c in punc:
                    if i != len(w)-1:
                        is_word = False
                        break
                # digits not allowed
                elif c in dig:
                    is_word = False
                    break
            l = w.split('-')
            # only <= 1 hyphen allowed
            if len(l) > 2:
                is_word = False
            elif len(l) == 2:
                a, b = l
                # hyphen cannot be at the end or beginning
                if len(a) == 0 or len(b) == 0:
                    is_word = False
                # character to the left and right must be a letter
                elif (a[-1] in punc) or (b[0] in punc):
                    is_word = False
            ret += int(is_word)
        return ret