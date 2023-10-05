import networkx as nx
import sympy
from copy import deepcopy
from functools import reduce

x = sympy.symbols('x')

def independence_poly(tree, coeffs=False):
    res = recursively_generate_poly(tree)
    if coeffs and res != 1:
        return res.coeffs()
    return res

def recursively_generate_poly(tree):
    # base cases
    if len(tree) < 1:
        return 1
    if len(tree) == 1:
        return sympy.Poly(1 + x)
    if len(tree) == 2:
        return sympy.Poly(1 + 2*x)

    reconstruct_dict = {}
    max_node = max(tree.nodes)
    nbrs_of_max_nodes = list(tree.neighbors(max_node)) # iterable
    reconstruct_dict[max_node] = nbrs_of_max_nodes
    for nbr in nbrs_of_max_nodes:
        reconstruct_dict[nbr] = list(tree.neighbors(nbr))
    tree.remove_node(max_node)
    poly_node_removed = sympy.Poly(recursively_generate_poly(tree))
    for node in list(nbrs_of_max_nodes):
        tree.remove_node(node)
    components_neigbors_removed = [tree.subgraph(c).copy() for c in nx.connected_components(tree)]
    poly_nbrs_removed = sympy.Poly(reduce(lambda a, b: a*b, 
                                        [recursively_generate_poly(subgraph) for subgraph in components_neigbors_removed]))
    tree = reconstruct_graph(tree, reconstruct_dict)
    final_poly = poly_node_removed + (x * poly_nbrs_removed)
    return final_poly

def reconstruct_graph(graph, reconstruct_dict):
    for node, nbr_list in reconstruct_dict.items():
        for nbr in nbr_list:
            graph.add_edge(node, nbr)
    return graph


if __name__ == '__main__':
    res = independence_poly(nx.path_graph(5))
    print(res)

    
    
    