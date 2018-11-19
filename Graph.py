import random
import argparse


class Graph(object):
    def __init__(self, nodes, edges=None):
        self.nodes = nodes
        if edges:
            self.edges = edges
        else:
            self.edges = []
            self.edge_set = set()

    def add_edge(self, edge):
        if edge not in self.edge_set:
            self.edges.append(edge)
            self.edge_set.add(edge)
            return True
        return False

    def make_random_edge(self):
        """Generate edge between two random node in the graph"""
        random_edge = tuple(random.sample(self.nodes, 2))
        return  random_edge

    def add_random_edge(self, total_edges):
        """Add Random edges until the total number og edge is reached"""
        while len(self.edges) < total_edges:
            self.add_edge(self.make_random_edge())


def check_edge_number(nodes, edges):
    num_nodes = len(nodes)

    # Check lower bound
    min_edges = num_nodes - 1
    if edges < min_edges:
        raise ValueError("Number of edges Lower than the minimum required edges")
    # Check Upper bound
    if edges > num_nodes*(num_nodes -1):
        raise ValueError('Number of edges greater than the maximum possible link between the nodes')


def random_walk(nodes, num_edge):
    # Idea is to create a Uniform spanning Tree using a random walk
    # Add Random Edge until the number of desired edge is reached
    check_edge_number(nodes, num_edge)

    # Create Two partition, S and T. Initially store all nodes in S
    S, T = set(nodes), set()

    # Pick a Random node and mark it as visited and current node
    current_node = random.sample(nodes, 1).pop()
    S.remove(current_node)
    T.add(current_node)

    graph = Graph(nodes)

    # Creation of the random connected Graph
    while S:
        # Randomly pick the next node from the neighbors of the current node.
        # As we are generated a connected graph, we assume a complete graph
        neighbor_node = random.sample(nodes, 1).pop()

        # If the new node hasn't been visited, add the edge from current to next
        if neighbor_node not in T:
            edge = (current_node, neighbor_node)
            graph.add_edge(edge)
            S.remove(neighbor_node)
            T.add(neighbor_node)

        # Set the neighbor as the new current node
        current_node = neighbor_node

    # Add random Edge until the number of edge is reached
    graph.add_random_edge(num_edge)

    return graph

if __name__ == '__main__':

    # Nodes
    nb_nodes =  5
    nodes = [x for x in range(int(nb_nodes))]
    print(nodes)

    # Edges
    nb_edges = 10
    print(nb_edges)

    graph = random_walk(nodes, nb_edges)
    print(graph.edges)
