class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0
        for thours in hours:
            if thours >= target:
                cnt+=1
        return cnt
