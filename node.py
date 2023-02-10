from collections import deque

class Node:
    def __init__(self, towers, parent) -> None:
        self.towers = towers
        self.parent = parent
    
    def __eq__(self, __o: object) -> bool:
        if self.towers == __o.towers:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        output = f"State: "
        for t in self.towers:
            output += f"{t}, "
        return output[:-2]
        
    def get_state(self):
        return self.towers