class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cmp=0
        if n==0:
            return True
        if(len(flowerbed)==1 and flowerbed[0]==0):
            flowerbed[0]==1
            return True
        if(len(flowerbed)==1 and flowerbed[0]==1):
            return False
        if len(flowerbed)>1:
            if flowerbed[0]==0 and flowerbed[1]==0:
                flowerbed[0]=1
                cmp=cmp+1
        
            if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0 :
                flowerbed[len(flowerbed)-1]=1
                cmp=cmp+1
            for i in range(1,len(flowerbed)-1):
                print(f"iteration {i}")
                if flowerbed[i]==0 :
                    print(f"iteration {i} verifie if1 ")
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0 :
                        print(f"iteration {i} verifie if2 ")
                        flowerbed[i]=1
                        cmp=cmp+1
                        print(cmp)
            if cmp==n or cmp>n:
                return True
            else:
                return False    
