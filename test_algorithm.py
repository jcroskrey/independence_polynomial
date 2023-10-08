import networkx as nx
from ind_poly_algorithm import independence_poly

def test_base_case1():
    tree = nx.path_graph(0)
    assert independence_poly(tree, coeffs=True) == 1

def test_base_case2():
    tree = nx.path_graph(1)
    assert independence_poly(tree, coeffs=True) == [1, 1]

def test_base_case3():
    tree = nx.path_graph(2)
    assert independence_poly(tree, coeffs=True) == [2, 1]

def test_4_node_path():
    path = nx.path_graph(4)
    assert independence_poly(path, coeffs=True) == [3, 4, 1]

def test_5_node_path():
    path = nx.path_graph(5)
    assert independence_poly(path, coeffs=True) == [1, 6, 5, 1]

def test_3_leaf_star():
    star = nx.star_graph(3)
    assert independence_poly(star, coeffs=True) == [1, 3, 4, 1]

def test_4_leaf_star():
    star = nx.star_graph(4)
    assert independence_poly(star, coeffs=True) == [1, 4, 6, 5, 1]

def test_custom_labels_star():
    """
    Tests that tree with max node as center is still properly calculated.
    """
    # star with the max node as the center
    star = nx.Graph()
    star.add_edges_from([(5, 1), (5, 2), (5, 3)])
    assert independence_poly(star, coeffs=True) == [1, 3, 4, 1]

def test_reconstructed_tree_isomorphic_to_original():
    """
    Tests that the graph is reconstructed correctly and is isomorphic to it's starting state.
    """
    original_star = nx.star_graph(5)
    star = original_star.copy()
    _ = independence_poly(star)
    assert nx.isomorphism.tree_isomorphism(original_star, star)

def test_claw_graph():
    """
    Tests graph T1 found on page 3 of: 
    "On unimodality of independence polynomials of some well-covered trees" by Vadim Levit and Eugen Madrescu

    https://www.academia.edu/818273/On_unimodality_of_independence_polynomials_of_some_well_covered_trees
    """
    graph = nx.Graph()
    graph.add_edges_from([
        (1, 2),
        (2, 3),
        (3, 4),
        (3, 9),
        (9, 10),
        (3, 5), 
        (5, 7), 
        (5, 6),
        (6, 8)
    ])
    assert independence_poly(graph, coeffs=True) == [14, 47, 60, 36, 10, 1]

def test_claw_graph2():
    """
    Tests graph T2 found on page 3 of: 
    "On unimodality of independence polynomials of some well-covered trees" by Vadim Levit and Eugen Madrescu

    https://www.academia.edu/818273/On_unimodality_of_independence_polynomials_of_some_well_covered_trees
    """
    graph = nx.Graph()
    graph.add_edges_from([
        (1, 2),
        (2, 3),
        (3, 4),
        (3, 9),
        (9, 10),
        (3, 5), 
        (5, 7), 
        (5, 6),
        (6, 8),
        (6, 11),
        (11, 12),
    ])
    assert independence_poly(graph, coeffs=True) == [23, 93, 151, 125, 55, 12, 1]
    
    