import networkx as nx
import sympy
from functools import reduce

x = sympy.symbols('x')
nx.Graph().add_edge
def independence_poly(tree, coeffs=False, yield_tree=False):
    res = recursively_generate_poly(tree)
    if coeffs and res != 1:
        res = res.coeffs()
    if yield_tree:
        return res, tree 
    return res

def recursively_generate_poly(tree, memo={}):
    # base cases
    if len(tree) < 1:
        return 1
    if len(tree) == 1:
        return sympy.Poly(1 + x)
    if len(tree) == 2:
        return sympy.Poly(1 + 2*x)
    
    # check memo
    key = frozenset(tree.edges)
    if key in memo:
        return memo[key]

    reconstruct_dict = {}
    max_node = max(tree.nodes)
    nbrs_of_max_nodes = list(tree.neighbors(max_node)) # iterable
    reconstruct_dict[max_node] = nbrs_of_max_nodes
    for nbr in nbrs_of_max_nodes:
        reconstruct_dict[nbr] = list(tree.neighbors(nbr))
    tree.remove_node(max_node)
    components_max_removed = [tree.subgraph(c).copy() for c in nx.connected_components(tree)]
    poly_max_removed = sympy.Poly(reduce(lambda a, b: a*b, 
                                        [recursively_generate_poly(subgraph, memo=memo) for subgraph in components_max_removed]))
    for node in list(nbrs_of_max_nodes):
        tree.remove_node(node)
    components_neigbors_removed = [tree.subgraph(c).copy() for c in nx.connected_components(tree)]
    if len(components_neigbors_removed) == 0:
        poly_nbrs_removed = 1
    else:
        poly_nbrs_removed = sympy.Poly(reduce(lambda a, b: a*b, 
                                            [recursively_generate_poly(subgraph, memo=memo) for subgraph in components_neigbors_removed]))
    
    tree = reconstruct_graph(tree, reconstruct_dict)
    final_poly = poly_max_removed + (x * poly_nbrs_removed)
    memo[key] = final_poly
    return final_poly

def reconstruct_graph(graph, reconstruct_dict):
    for node, nbr_list in reconstruct_dict.items():
        for nbr in nbr_list:
            graph.add_edge(max(node, nbr), min(node, nbr))
    return graph


if __name__ == '__main__':
    tree = nx.path_graph(30)
    res = independence_poly(tree, coeffs=True)
    print(res)

    
    
    