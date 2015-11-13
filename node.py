#!/usr/bin/env python

#    Copyright (C) 2015, Jim Walters <tryggth2009@gmail.com>
#    All rights reserved.

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

__author__ = """\n""".join(['Jim Walters (tryggth2009@gmail.com)',
                            'Jim Walters (jimw@bugopolis.com)'])

VERSION = '0.1'


class Node(object):
    """
    Base class for undirected graphs.
    A Graph stores nodes and edges with optional data, or attributes.
    Graphs hold undirected edges.  Self loops are allowed but multiple
    (parallel) edges are not.
    Nodes can be arbitrary (hashable) Python objects with optional
    key/value attributes.
    Edges are represented as links between nodes with optional
    key/value attributes.
    Parameters
    ----------
    data : input graph
        Data to initialize graph.  If data=None (default) an empty
        graph is created.  The data can be an edge list, or any
        NetworkX graph object.  If the corresponding optional Python
        packages are installed the data can also be a NumPy matrix
        or 2d ndarray, a SciPy sparse matrix, or a PyGraphviz graph.
    attr : keyword arguments, optional (default= no attributes)
        Attributes to add to graph as key=value pairs.
    See Also
    --------
    DiGraph
    MultiGraph
    MultiDiGraph
    Examples
    --------
    Create an empty graph structure (a "null graph") with no nodes and
    no edges.
    >>> G = Graph()
    G can be grown in several ways.
    **Nodes:**
    Add one node at a time:
    >>> G.add_node(1)
    Add the nodes from any container (a list, dict, set or
    even the lines from a file or the nodes from another graph).
    >>> G.add_nodes_from([2,3])
    >>> G.add_nodes_from(range(100,110))
    >>> H=nx.Graph()
    >>> H.add_path([0,1,2,3,4,5,6,7,8,9])
    >>> G.add_nodes_from(H)
    """

    def __init__(self, nodes=None, edges=None, **attr):
        """Initialize a graph with nodes, edges, graph attributes.
        Parameters
        ----------
        data : input graph
            Data to initialize graph.  If data=None (default) an empty
            graph is created.  The data can be an edge list, or any
            NetworkX graph object.  If the corresponding optional Python
            packages are installed the data can also be a NumPy matrix
            or 2d ndarray, a SciPy sparse matrix, or a PyGraphviz graph.
        name : string, optional (default='')
            An optional name for the graph.
        attr : keyword arguments, optional (default= no attributes)
            Attributes to add to graph as key=value pairs.
        See Also
        --------
        convert
        Examples
        --------
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G = nx.Graph(name='my graph')
        >>> e = [(1,2),(2,3),(3,4)] # list of edges
        >>> G = nx.Graph(e)
        Arbitrary graph attribute pairs (key=value) may be assigned
        >>> G=nx.Graph(e, day="Friday")
        >>> G.graph
        {'day': 'Friday'}
        """
        self.nodes = nodes
        self.edges = edges

    @property
    def name(self):
        return self.graph.get('name', '')

    @name.setter
    def name(self, s):
        self.graph['name'] = s

    def __str__(self):
        """Return the graph name.
        Returns
        -------
        name : string
            The name of the graph.
        Examples
        --------
        >>> G = nx.Graph(name='foo')
        >>> str(G)
        'foo'
        """
        return self.name

    def __iter__(self):
        """Iterate over the nodes. Use the expression 'for n in G'.
        Returns
        -------
        niter : iterator
            An iterator over all nodes in the graph.
        Examples
        --------
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_path([0,1,2,3])
        """
        return iter(self.node)

    def __contains__(self, n):
        """Return True if n is a node, False otherwise. Use the expression
        'n in G'.
        Examples
        --------
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_path([0,1,2,3])
        >>> 1 in G
        True
        """
        try:
            return n in self.node
        except TypeError:
            return False

    def __len__(self):
        """Return the number of nodes. Use the expression 'len(G)'.
        Returns
        -------
        nnodes : int
            The number of nodes in the graph.
        Examples
        --------
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_path([0,1,2,3])
        >>> len(G)
        4
        """
        return len(self.node)

    def __getitem__(self, n):
        """Return a dict of neighbors of node n.  Use the expression 'G[n]'.
        Parameters
        ----------
        n : node
           A node in the graph.
        Returns
        -------
        adj_dict : dictionary
           The adjacency dictionary for nodes connected to n.
        Notes
        -----
        G[n] is similar to G.neighbors(n) but the internal data dictionary
        is returned instead of a list.
        Assigning G[n] will corrupt the internal graph data structure.
        Use G[n] for reading data only.
        Examples
        --------
        >>> G = nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_path([0,1,2,3])
        >>> G[0]
        {1: {}}
        """
        return self.adj[n]
