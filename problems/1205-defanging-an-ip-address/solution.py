class Solution:
    def defangIPaddr(self, address: str) -> str:
    
        # deranged_ip = address.replace('.','[.]')
        # return deranged_ip
        deranged_ip = ''
        for i in range(len(address)):
            if address[i] != '.':
                deranged_ip += address[i]
            else:
                deranged_ip += '[.]'
        return deranged_ip
