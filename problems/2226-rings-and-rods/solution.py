class Solution:
    def countPoints(self, rings: str) -> int:
        places_dict = [{
            x: set() for x in range(10)
        }]
        color_idx = 0
        for color_pos in range(1,len(rings),2):
            places_dict[0][int(rings[color_pos])].add(rings[color_pos-1])
        cnt = 0
        for k, v in places_dict[0].items():
            if len(v) == 3:
                cnt+=1
        return cnt
