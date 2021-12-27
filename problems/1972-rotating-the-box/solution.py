class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        new_row = []
        for row in box:
            rowo = []
            
            index = 0
            for i,ele in enumerate(row):
                
                if ele == '.':
                    rowo.insert(index,ele)
                elif ele == '#': 
                    rowo.append(ele)
        
                if ele == '*':
                    index = i+1
                    rowo.append(ele)
            
            new_row.insert(0,rowo)
        # print(new_row)
        return list(map(list, zip(*new_row)))
