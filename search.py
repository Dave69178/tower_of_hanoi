from node import Node
import copy
from collections import deque

def make_move_from_a_to_b(node : Node, a : int, b : int):
    state = copy.deepcopy(node.get_state())
    # Move top disk from tower a to tower b
    state[b].append(state[a].pop())
    return state

def get_new_node_from_move(node: Node, a : int, b : int):
    return Node(make_move_from_a_to_b(node, a, b), node)

def expand_node(node : Node):
    children = []
    for start_ind, tower in enumerate(node.get_state()):
        if tower:
            # The tower contains at least one disk
            for dest_ind, destination in enumerate(node.get_state()):
                if not destination or destination[-1] > tower[-1]:
                    # The top disk in destination tower is a greater size than disk we are moving (or destination is empty)
                    # Hence, this is a valid move - add new node
                    children.append(get_new_node_from_move(node, start_ind, dest_ind))
    return children

def is_node_state_in_path(node : Node):
    parent = node.parent
    while parent is not None:
        if parent == node:
            return True
        else:
            parent = parent.parent
    return False
        
def get_path_to_node(node : Node):
    step_count = 0
    path = [node.get_state()]
    parent = node.parent
    while parent is not None:
        step_count += 1
        path.append(parent.get_state())
        parent = parent.parent
    return "\n".join(map(str, path[::-1])), step_count

def search(initial_state, goal_state, search_type="bfs"):
    fringe = deque()
    fringe.append(Node(initial_state, None))

    if search_type == "bfs":
        while True:
            candidate_children = expand_node(fringe.pop())
            if candidate_children:
                # There are greater than zero candiate children
                for child in candidate_children:
                    if not is_node_state_in_path(child):
                        # The state has not been reached before in this path, thus add to fringe
                        fringe.appendleft(child)
                        if child == Node(goal_state,None):
                             yield get_path_to_node(child)
    elif search_type == "dfs":
        while True:
            candidate_children = expand_node(fringe.popleft())
            if candidate_children:
                # There are greater than zero candiate children
                for child in candidate_children:
                    if not is_node_state_in_path(child):
                        # The state has not been reached before in this path, thus add to fringe
                        fringe.appendleft(child)
                        if child == Node(goal_state,None):
                            yield get_path_to_node(child)
