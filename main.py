from search import search

initial_state = [[4,3,2,1],[],[]]
goal_state = [[],[],[4,3,2,1]]

#initial_state = [[5,4,3,2,1],[],[],[],[]]
#goal_state = [[],[],[],[],[5,4,3,2,1]]
#initial_state = [[8,7,6,5,4,3,2,1],[],[]]
#goal_state = [[],[],[8,7,6,5,4,3,2,1]]


def find_solution(initial_state, goal_state, search_type="bfs"):
    return search(initial_state, goal_state, search_type=search_type).__next__()

def get_solution_count(initial_state, goal_state, search_type="bfs"):
    solution_count = 0
    for i in search(initial_state, goal_state, search_type=search_type):
        solution_count += 1
    return solution_count

path, path_length = find_solution(initial_state, goal_state, search_type="bfs")
print(f"Step Count: {path_length}, \nPath: \n{path}")