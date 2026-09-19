class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        left=0
        left1=0
        count=0
        while left<=len(players)-1 and left1<=len(trainers )-1:
            if players[left]<=trainers[left1]:
                count+=1
                left+=1
                left1+=1
            else:
                left1+=1
              
        return count 
                

        