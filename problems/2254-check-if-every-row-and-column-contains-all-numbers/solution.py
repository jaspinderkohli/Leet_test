class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        match = [x for x in range(1,len(matrix[0])+1)]
        # print(match)
        for i in range(len(matrix)):
            match = [x for x in range(1,len(matrix[0])+1)]
            # print(matrix[i])
            for j in range(len(matrix[i])):
                # print("in")
                try:
                    match.remove(matrix[i][j])
                except:
                    pass
                # print("-",match)
                # print(j, len(matrix[i])-1)
                # print("--",match)
                if j == len(matrix[i])-1 and len(match) != 0:
                    return False
        for i in range(len(matrix)):
            match = [x for x in range(1,len(matrix[0])+1)]
            # print(matrix[i])
            for j in range(len(matrix[i])):
                # print("in")
                try:
                    match.remove(matrix[j][i])
                except:
                    pass
                # print("-",match)
                # print(j, len(matrix[i])-1)
                # print("--",match)
                if j == len(matrix[i])-1 and len(match) != 0:
                    return False
        return True
