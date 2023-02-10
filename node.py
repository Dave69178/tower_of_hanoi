from collections import deque

class Node:
    def __init__(self, tower1 : deque, tower2 : deque, tower3 : deque, parent) -> None:
        self.tower1 = tower1
        self.tower2 = tower2
        self.tower3 = tower3
        self.parent = parent
    
    def __eq__(self, __o: object) -> bool:
        if self.tower1 == __o.tower1 and self.tower2 == __o.tower2 and self.tower3 == __o.tower3:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return f"State: [{self.tower1}, {self.tower2}, {self.tower3}], Parent: {self.parent}"
        
    def get_state(self):
        return [self.tower1, self.tower2, self.tower3]
