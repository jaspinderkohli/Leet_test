class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic = []
        cnt=0
        for i in items:
            item = {
                'type':i[0],
                'color':i[1],
                'name': i[2]
            }
            dic.append(item)
        for i in dic:
            if ruleValue == i[ruleKey]:
                cnt+=1
        return cnt
