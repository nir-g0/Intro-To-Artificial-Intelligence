from A4_Base import *
#______DO NOT EDIT ABOVE THIS LINE____________#
#use deque functions to add and remove frontier entries
#______EDITING BELOW THIS LINE IS ALLOWED, ONLY EDIT THE INTERNAL IMPLEMENTATION OF THE FUNCTIONS ____________#
from utils import *

class AStarGraph(GraphProblem):
    #use this child class, Inherit from the GraphProblem class, in this class implement hueristic (h) function
    """h function is straight-line distance from a node's state to goal."""
    # in this case use the romania_map.locations attribute to compute h.
    def h(self, node):
        goal_point = romania_map.locations[self.goal]
        current_point = romania_map.locations[node.state]
        # print(node.state)
        # print(current_point)
        dx = current_point[0] - goal_point[0]
        dy = current_point[1] - goal_point[1]
        dx_squared = pow(dx, 2)
        dy_squared = pow(dy, 2)
        dist = dx_squared+dy_squared
        euclidean_distance = pow(dist, 1/2)
        return euclidean_distance

def f(input):
   func_cost = input['path_cost'] + input['heuristic_cost']
   return func_cost

def astar_search(problem, h=None):
    if not h:
        h = problem.h
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    fringe = PriorityQueue('min', f=f)
    fringe.append({'path_cost':0, 'heuristic_cost':0, 'node':node})
    while fringe:
       current = fringe.pop()
       if problem.goal_test(current['node'].state):
        return current['node']
       print(f"{current['node'].state} : {f(current)}")
       for child_node in current['node'].expand(problem):    
        fringe.append({'path_cost':child_node.path_cost, 'heuristic_cost':h(child_node), 'node':child_node})
    return None
    """A* search is best-first (you may use priority queue) graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, (ALREADY ADDED in TEST CASE),
    The tests check through a call to solution() function which returns a list of expanded cities along the path"""
    
    # YOUR CODE GOES HERE

