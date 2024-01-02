class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        for i in range(0, arr_len):
            for j in range(0, arr_len):  # Iterate through the entire array
                if i != j and (arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]):
                    return True
        return False


