import fileinput


# A contains B --> ("A", "B")
import pprint
from collections import defaultdict
import re

class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections):
        # internal representation 
        self._graph = defaultdict(dict)
        self._directed = True
        
        # init graph
        for node1, children in connections:
            self.add(node1, children)


    def add(self, node1,children):
        """ Add connection between node1 and node2 """
        self._graph[node1] = children

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        # path always starts at itself
        path = path + [node1]
        
        # path to itself
        if node1 == node2:
            return path

        #invalid start pooint
        if node1 not in self._graph:
            return None

        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))



def initGraphFromInput():
    # CONTAINED bags
    containedBagPattern = r'(\d+) (\w* \w+) bags*'

    # CONTAINER bags
    containerBagPattern = r'^(\w* \w+) bags'


    inputArr = [line.strip() for line in fileinput.input()]

    connections = []
    for line in inputArr:
        matches = re.match(containerBagPattern, line)
        cont_colour = matches.groups()[0]

        matches = re.findall(containedBagPattern, line)
        contained = {colour: int(weight) for weight, colour in matches}
        connections.append((cont_colour, contained))


    # pretty_print.pprint(connections)
    g = Graph(connections)
    return g

def partOne():
    g = initGraphFromInput()
    pretty_print = pprint.PrettyPrinter()
    pretty_print.pprint(g._graph)

    counter = 0
    for start_node in g._graph:
        if (start_node == 'shiny gold'): continue
        if g.find_path(start_node, 'shiny gold'):
            counter += 1
            print(f'exists path from {start_node} to shiny')


    print(counter)

totalSum = 0

def partTwo():
    g = initGraphFromInput()
    pretty_print = pprint.PrettyPrinter()
    pretty_print.pprint(g._graph)

    toLeaf(g._graph, g._graph, 'shiny gold', 1)
    print(totalSum)


def toLeaf(g, parent, root, multiplier):
    global totalSum

    print(f'\n-------- parent: {"g" if parent == g else parent}, root: {root}, sum:{totalSum} --------')
    if g[root] == {}:
        print(f'returning {parent[root]}')
        return parent[root] 
    
    print(f'at root: {root}')
    for value in g[root]:
        additionToSum =  multiplier * toLeaf(g, g[root], value, multiplier * g[root][value])
        totalSum += additionToSum
        print(f'adding: {additionToSum}')
    
    
    print(f'returning node val of {parent[root]}')
    return parent[root]
        
    
    
    
        



partTwo()