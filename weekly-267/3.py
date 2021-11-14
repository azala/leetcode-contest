class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        c = (n + (rows-1)) // rows # number of columns = length of string / rows, rounded up
        ret = ''
        for i in range(c): # iterate over diagonals starting at (0, 0), (0, 1), ... (0, c-1)
            for j in range(rows):
                idx = i + j + c*j # convert (j, i+j) to index in encodedText
                if idx < n: # watch out for out of bounds indices
                    ret += encodedText[idx]
        return ret.rstrip() # strip trailing spaces