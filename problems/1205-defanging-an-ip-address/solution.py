class Solution:
    def defangIPaddr(self, address: str) -> str:
    
        deranged_ip = address.replace('.','[.]')
        return deranged_ip
