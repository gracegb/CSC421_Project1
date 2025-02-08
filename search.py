# search.py
# Group: Grace Bergquist and Phinehas Maina
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start State: " + str(problem.getStartState()))
    print("Is the start state ( " + str(problem.getStartState()) + " ) a goal?: " + str(problem.isGoalState(problem.getStartState())))
    
    # Demonstrate how successor function works
    print("Successor function of initial start state ( " + str(problem.getStartState()) + " ) yields a tuple with 3 pieces:")
    print("\t(nextState, actionFromCurrStateToNextState, costToGetFromCurrStateToNextState)")
    for statePortion in problem.getSuccessors(problem.getStartState()):
        print("\t" + str(statePortion))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack  # Using Stack for DFS

    stack = Stack()
    visited = set()

    # Push the start state with an empty action list
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        state, actions = stack.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    stack.push((successor, actions + [action]))

    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue  # Using Priority Queue for UCS

    pq = PriorityQueue()
    visited = set()
    start_state = problem.getStartState()

    # Push the start state with cost 0
    pq.push((start_state, [], 0), 0)  

    while not pq.isEmpty():
        state, actions, cost = pq.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in visited:
                    new_cost = cost + step_cost
                    pq.push((successor, actions + [action], new_cost), new_cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue  # Using Priority Queue for A*
    
    pq = PriorityQueue()
    visited = {}
    start_state = problem.getStartState()

    # Push the start state with cost 0 + heuristic
    pq.push((start_state, [], 0), heuristic(start_state, problem))
    
    while not pq.isEmpty():
        state, actions, cost = pq.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited or cost < visited[state]:
            visited[state] = cost

            for successor, action, step_cost in problem.getSuccessors(state):
                new_cost = cost + step_cost
                priority = new_cost + heuristic(successor, problem)
                pq.push((successor, actions + [action], new_cost), priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
