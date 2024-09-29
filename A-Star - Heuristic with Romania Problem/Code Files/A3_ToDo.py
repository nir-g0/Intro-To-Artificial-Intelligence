from A3_Base import *

#______DO NOT EDIT ABOVE THIS LINE____________#

#use deque functions to add and remove frontier entries


#______EDITING BELOW THIS LINE IS ALLOWED, ONLY EDIT THE INTERNAL IMPLEMENTATION OF THE FUNCTIONS ____________#
def breadth_first_graph_search(problem):
    """
    Implement the breadth first search for the graph here.
    some skeleton code is provided, feel free to edit it.
    Search through the successors/actions of a problem to find a goal.
    The initial frontier should be an empty queue.
    Does not get trapped by loops.
    If two paths reach a state, only use the first one.
    """
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
       current = frontier.popleft()
       if problem.goal_test(current.state):
        return current
       explored.add(current)
       for child_node in current.expand(problem):
            if child_node not in explored:
                frontier.append(child_node)
    return None

def depth_first_graph_search(problem):
    """
    Search the deepest nodes in the search tree first.
    Search through the successors/actions of a problem to find a goal.
    The initial frontier should be an empty queue.
    Does not get trapped by loops.
    If two paths reach a state, only use the first one.
    """
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = [(Node(problem.initial))]  # Stack
    explored = set()
    while frontier:
       current = frontier.pop()
       if problem.goal_test(current.state):
        return current
       explored.add(current)
       for child_node in current.expand(problem):
            if child_node not in explored:
                frontier.append(child_node)
    return None


