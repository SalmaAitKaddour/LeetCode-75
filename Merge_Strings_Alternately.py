class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        k= max(n,m)
        chaine=""
        for i in range(k):
            if(i < n):
                chaine=chaine+word1[i]
            if(i < m):
                chaine=chaine+word2[i]
        return chaine


        
