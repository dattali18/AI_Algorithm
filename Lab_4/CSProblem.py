#Graph Colouring
import math
#The graph is represented by a list with an item for every node.
#Item i represents node i+1 (the nodes are positive integers.)
#Each node is represented by a list of 3 items: 
#   The color of the node (1...N). 0 for no color (yet)
#   A list of the node's neighbors (positive integers)
#   The domain -  a list of integers (1...N)

N = 0 # The colours are numbered 1...N

def create(fpath="graph.txt"):
# fpath first line contains the num. of colours to be used.
# The second line contains the list of neighbours of node 1.
# The third line contains the list of neighbours of node 2.
#...
    global N
    p = []
    f=open(fpath, "r")
    N =  int(f.readline())
    s=f.readline()
    while s!="":
        p += [[ 0, [int(i) for i in s.split()], list(range(1, N + 1))]]
        s=f.readline()
    f.close()
    present(p)
    return p

def domain(problem, v):
#Returns the domain of v
    return problem[v - 1][2][:]

def domain_size(problem, v):
#Returns the domain size of v
    return len(problem[v - 1][2])

def assign_val(problem, v, x):
#Assigns x in var. v
    problem[v - 1][0] = x

def get_val(problem, v):
#Returns the val. of v
    return problem[v - 1][0]
    
def erase_from_domain(problem, v, x):
#Erases x from the domain of v
    problem[v - 1][2].remove(x)

def get_list_of_free_vars(problem):
#Returns a list of vars. that were not assigned a val.
    l=[]

    ### your code here ###

    return l

def is_solved(problem):
#Returns True iff the problem is solved
    for i in problem:
        if i[0] == 0:
            return False
    return True
    
def is_consistent(problem, v1, v2, x1, x2):

    ### your code here ###


def list_of_influenced_vars(problem, v):

    ### your code here ###

def present(problem):
    for p in problem:
        print(p) 
    print("************")
            
                                    