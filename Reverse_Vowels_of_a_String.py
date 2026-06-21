class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set(['a','e','i','o','u'])
        ss=list(s)
        vowelsPositions={}
        for i in range(len(ss)):
            if ss[i].lower() in vowels:
                vowelsPositions[i]=ss[i]
        #print(vowelsPositions)

        vowelsPositionsRev=dict(reversed(vowelsPositions.items()))
        #print(vowelsPositionsRev)

        #print(ss)
        k=list(vowelsPositionsRev.values())
        #print(k)
        l=0
        for i in range(len(ss)):
            if ss[i].lower() in vowels:
                ss[i]=k[l]
                l=l+1
        return "".join(ss)
    

        
