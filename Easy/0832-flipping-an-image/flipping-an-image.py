class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i].reverse()
        
            first=0
            while first <len(image[i]):
                if image[i][first]==0:
                    image[i][first]=1
        
                else:
                    image[i][first]=0
                first+=1
        return image 
                
        