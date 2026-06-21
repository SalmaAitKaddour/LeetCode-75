class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max=candies[0]
        for i in range(len(candies)):
           if max<candies[i]:
               max=candies[i]
        print(f"max(candies) : {max}")
        candiesWithExtra=[]
        resultat=[]
        print(len(candies))
        #0->4,
        for i in range(len(candies)):
            tmp=candies[i]+extraCandies
            candiesWithExtra.append(tmp)
            if(tmp > max or tmp == max ):
                resultat.append(True)
            else:
                resultat.append(False)
        return resultat
