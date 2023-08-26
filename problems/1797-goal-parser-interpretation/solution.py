class Solution:
    def interpret(self, command: str) -> str:
        goal_map = {
            "G": "G",
            "()": "o",
            "(al)": "al"
        }
        i = 0
        n = len(command)
        interpreted = ""
        while i < n:
            if command[i]  == 'G':
                interpreted += goal_map["G"]
                i+=1
            elif command[i:i+2] == "()":
                interpreted += goal_map["()"]
                i+=2
            elif command[i:i+4] == "(al)":
                interpreted += goal_map["(al)"]
                i+=4
        return interpreted

