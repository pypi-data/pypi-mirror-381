#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "../src/graph.h"

namespace py = pybind11;

PYBIND11_MODULE(fastgraphFPMS, m) {
    m.doc() = R"pbdoc(

        FastGraphFPMS - Une librairie de graphes ultra-rapide implémentée en C++
        
        Cette librairie fournit des algorithmes de graphes optimisés pour la performance.
        
        Exemples d'utilisation:
            >>> import fastgraphFPMS as fg
            >>> # Format matrice
            >>> graph = fg.Graph([[0, 1], [1, 0]])
            >>> # Format listes d'adjacence
            >>> head = [0, 1, 3]
            >>> succ = [1, 0, 2]
            >>> weights = [1, 1, 1]
            >>> graph2 = fg.Graph(head, succ, weights)

    )pbdoc";
    
    py::class_<fastgraphfpms::Graph>(m, "Graph", R"pbdoc(

        Représente un graphe avec différentes structures de données.
        
        Cette classe permet de créer et manipuler des graphes, et d'exécuter
        divers algorithmes graphiques optimisés.
        
    )pbdoc")
    
    .def(py::init<>(), R"pbdoc(

        Crée un graphe vide.
        
        Example:
            >>> graph = Graph()

    )pbdoc")
    
    .def(py::init<const vector<vector<int>>&>(), 
         py::arg("matrix"),
         R"pbdoc(

        Crée un graphe à partir d'une matrice d'adjacence.
        
        Args:
            matrix: Matrice d'adjacence représentant le graphe
            
        Example:
            >>> matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
            >>> graph = Graph(matrix)

    )pbdoc")
        
    .def(py::init<const vector<int>&, const vector<int>&, const vector<int>&>(), 
         py::arg("head"), py::arg("succ"), py::arg("weights"),
         R"pbdoc(

        Crée un graphe à partir de listes d'adjacence (format CSR).
        
        Args:
            head: Vecteur Head (indices de début pour chaque nœud)
            succ: Vecteur Succ (successeurs de chaque nœud)
            weights: Vecteur Weights (poids des arêtes)
            
        Example:
            >>> head = [0, 2, 3, 5]    # 3 nœuds
            >>> succ = [1, 2, 0, 1, 2] # successeurs
            >>> weights = [1, 2, 1, 3, 1] # poids
            >>> graph = Graph(head, succ, weights)

    )pbdoc")

    .def(py::init<const string&>(), 
         py::arg("filename"),
         R"pbdoc(

        Crée un graphe à partir d'un fichier.
        
        Le format est détecté automatiquement:
        - Matrice: première ligne = nombre de nœuds, puis matrice
        - Listes: chaque ligne = liste de paires (voisin poids) pour un nœud
        
        Args:
            filename: Chemin vers le fichier contenant le graphe
            
        Example:
            >>> graph = Graph("mon_graphe.txt")

    )pbdoc")
    
    // === MÉTHODES DE BASE ===
    .def("get_num_nodes", &fastgraphfpms::Graph::get_num_nodes, R"pbdoc(

        Retourne le nombre de nœuds du graphe.
        
        Returns:
            int: Nombre de nœuds dans le graphe
            
        Example:
            >>> nb_nodes = graph.get_num_nodes()
            >>> print(f"Le graphe a {nb_nodes} nœuds")

    )pbdoc")

    // === FICHIERS ===
    .def("load_from_file", &fastgraphfpms::Graph::load_from_file, 
         py::arg("filename"), R"pbdoc(

        Charge un graphe depuis un fichier.
        
        Args:
            filename: Chemin vers le fichier contenant la matrice
            
        Format du fichier:
            Première ligne: nombre de nœuds
            Lignes suivantes: matrice d'adjacence
            
        Example:
            >>> graph.load_from_file("graphe.txt")

    )pbdoc")
    
    .def("save_to_file", &fastgraphfpms::Graph::save_to_file, 
         py::arg("filename"), R"pbdoc(

        Sauvegarde le graphe dans un fichier.
        
        Args:
            filename: Chemin où sauvegarder le fichier

    )pbdoc")

    .def("save_to_file_adjacency_list", &fastgraphfpms::Graph::save_to_file_adjacency_list, 
         py::arg("filename"), R"pbdoc(

        Sauvegarde le graphe dans un fichier au format listes d'adjacence.
        
        Args:
            filename: Chemin où sauvegarder le fichier
            
        Example:
            >>> graph.save_to_file_adjacency_list("graphe_listes.txt")

    )pbdoc")

    .def("print", &fastgraphfpms::Graph::print, R"pbdoc(

        Affiche les structures de données Head, Successeurs et Weights.
        
    )pbdoc")
    
    .def("bfs", &fastgraphfpms::Graph::bfs,
        py::arg("start"), R"pbdoc(

        Effectue une exploration en largeur sur le graphique en partant du noeud start.

        Args:
            start: noeud de démarrage pour l'exploration

        )pbdoc")
        
    .def("dfs", &fastgraphfpms::Graph::dfs,
        py::arg("start"), R"pbdoc(

        Effectue une exploration en profondeur sur le graphique en partant du noeud start.

        Args:
            start: noeud de démarrage pour l'exploration

        )pbdoc")
        
        
    .def("find_cc", &fastgraphfpms::Graph::find_cc, R"pbdoc(

        Renvoie le nombre de composante connexe et une liste comprenant chaque composante connexe.
        
        )pbdoc")

    .def("find_scc", &fastgraphfpms::Graph::find_scc, R"pbdoc(

        Renvoie le nombre de composante fortement connexe et une liste comprenant chaque composante fortement connexe.
        
        )pbdoc")
        
    .def("is_bigraph", &fastgraphfpms::Graph::is_bigraph, R"pbdoc(

        Renvoie, si le graph est bipartie, deux listes contenant les noeuds séparés en deux groupes.

        )pbdoc")
        
    .def("prim", &fastgraphfpms::Graph::prim, R"pbdoc(
        
        Renvoie le coût de l'arbre optimale et renvoie également l'arbre sous forme de liste contenant des tuples.
        
        )pbdoc")
        
    .def("kruskal", &fastgraphfpms::Graph::kruskal, R"pbdoc(

        Renvoie le coût de l'arbre optimale et renvoie également l'arbre sous forme de liste contenant des tuples.

        )pbdoc")
        
    .def("dijkstra", &fastgraphfpms::Graph::dijkstra, py::arg("s"), py::arg("t"), R"pbdoc(

        Renvoie deux vecteurs, un vecteur distance et un vecteur parent à l'aide de l'algorithme de Dijkstra.

        )pbdoc")
        
    .def("sedgewick_vitter", &fastgraphfpms::Graph::sedgewick_vitter, py::arg("s"), py::arg("t"), R"pbdoc(
    
        Renvoie deux vecteurs, un vecteur distance et un vecteur parent à l'aide de l'algorithme de Sedgewick et Vitter.

        )pbdoc")
        
    .def("dijkstra_bucket", &fastgraphfpms::Graph::dijkstra_bucket, py::arg("s"), py::arg("t"), R"pbdoc(
    
        Renvoie deux vecteurs, un vecteur distance et un vecteur parent à l'aide de l'algorithme de dijkstra à buckets.
    
        )pbdoc")
        
    .def("bellman_ford", &fastgraphfpms::Graph::bellman_ford, py::arg("s"), py::arg("t"), R"pbdoc(
    
        Renvoie deux vecteurs, un vecteur distance et un vecteur parent à l'aide de l'algorithme de Bellman.
    
        )pbdoc")

    .def("has_negative_cycle", &fastgraphfpms::Graph::has_negative_cycle, R"pbdoc(
        
        Renvoie une variable booléenne si le graphe possède un cycle négatif.
        
        )pbdoc")
        
    .def("floyd_warshall", &fastgraphfpms::Graph::floyd_warshall, R"pbdoc(

        Calcule les plus courts chemins entre toutes les paires de nœuds.
        
        Returns:
            tuple: (distances, next) où:
                - distances: matrice des distances (list of lists)
                - next: matrice pour reconstruire les chemins (list of lists)
                
        Example:
            >>> dist, next = graph.floyd_warshall()
            >>> print(f"Distance de 0 à 5: {dist[0][5]}")

    )pbdoc")

    .def("get_shortest_paths_matrix", &fastgraphfpms::Graph::get_shortest_paths_matrix, R"pbdoc(

        Retourne la matrice des plus courtes distances entre toutes les paires.
        
        Returns:
            list: Matrice des distances (list of lists)
            
        Example:
            >>> dist_matrix = graph.get_shortest_paths_matrix()
            >>> print(f"Distance de 0 à 5: {dist_matrix[0][5]}")

    )pbdoc")

    .def("has_negative_cycle_floyd", &fastgraphfpms::Graph::has_negative_cycle_floyd, R"pbdoc(

        Vérifie si le graphe contient un cycle de poids négatif avec l'algorithme de Floyd-Warshall.
        
        Returns:
            bool: True si un cycle négatif est détecté, False sinon
            
        Example:
            >>> if graph.has_negative_cycle_floyd():
            ...     print("Attention: cycle négatif détecté!")

    )pbdoc")

    .def("find_eulerian_path", &fastgraphfpms::Graph::find_eulerian_path, R"pbdoc(

        Trouve un chemin eulérien dans le graphe (passe par chaque arête exactement une fois).
        
        Returns:
            list: Chemin eulérien, ou liste vide si aucun n'existe
            
        Example:
            >>> path = graph.find_eulerian_path()
            >>> if path:
            ...     print(f"Chemin eulérien: {path}")

    )pbdoc")

    .def("find_eulerian_circuit", &fastgraphfpms::Graph::find_eulerian_circuit, R"pbdoc(

        Trouve un circuit eulérien dans le graphe (cycle qui passe par chaque arête exactement une fois).
        
        Returns:
            list: Circuit eulérien, ou liste vide si aucun n'existe
            
        Example:
            >>> circuit = graph.find_eulerian_circuit()
            >>> if circuit:
            ...     print(f"Circuit eulérien: {circuit}")

    )pbdoc")

    .def("has_eulerian_path", &fastgraphfpms::Graph::has_eulerian_path, R"pbdoc(

        Vérifie si le graphe contient un chemin eulérien.
        
        Returns:
            bool: True si un chemin eulérien existe
            
        Example:
            >>> if graph.has_eulerian_path():
            ...     print("Le graphe a un chemin eulérien")

    )pbdoc")

    .def("has_eulerian_circuit", &fastgraphfpms::Graph::has_eulerian_circuit, R"pbdoc(

        Vérifie si le graphe contient un circuit eulérien.
        
        Returns:
            bool: True si un circuit eulérien existe
            
        Example:
            >>> if graph.has_eulerian_circuit():
            ...     print("Le graphe a un circuit eulérien")

    )pbdoc")

    .def("find_hamiltonian_path", &fastgraphfpms::Graph::find_hamiltonian_path, R"pbdoc(

        Trouve un chemin hamiltonien dans le graphe (passe par chaque sommet exactement une fois).
        
        Note: Algorithme exponentiel, à utiliser uniquement sur de petits graphes.
        
        Returns:
            list: Chemin hamiltonien, ou liste vide si aucun n'existe
            
        Example:
            >>> path = graph.find_hamiltonian_path()
            >>> if path:
            ...     print(f"Chemin hamiltonien: {path}")

    )pbdoc")

    .def("find_hamiltonian_circuit", &fastgraphfpms::Graph::find_hamiltonian_circuit, R"pbdoc(

        Trouve un cycle hamiltonien dans le graphe (cycle qui passe par chaque sommet exactement une fois).
        
        Note: Algorithme exponentiel, à utiliser uniquement sur de petits graphes.
        
        Returns:
            list: Cycle hamiltonien, ou liste vide si aucun n'existe
            
        Example:
            >>> circuit = graph.find_hamiltonian_circuit()
            >>> if circuit:
            ...     print(f"Cycle hamiltonien: {circuit}")

    )pbdoc")

    .def("has_hamiltonian_path", &fastgraphfpms::Graph::has_hamiltonian_path, R"pbdoc(

        Vérifie si le graphe pourrait contenir un chemin hamiltonien (condition nécessaire).
        
        Note: Condition nécessaire mais non suffisante.
        
        Returns:
            bool: True si les conditions nécessaires sont satisfaites
            
        Example:
            >>> if graph.has_hamiltonian_path():
            ...     print("Le graphe pourrait avoir un chemin hamiltonien")

    )pbdoc")

    .def("has_hamiltonian_circuit", &fastgraphfpms::Graph::has_hamiltonian_circuit, R"pbdoc(

        Vérifie si le graphe pourrait contenir un cycle hamiltonien (condition nécessaire).
        
        Note: Condition nécessaire mais non suffisante.
        
        Returns:
            bool: True si les conditions nécessaires sont satisfaites
            
        Example:
            >>> if graph.has_hamiltonian_circuit():
            ...     print("Le graphe pourrait avoir un cycle hamiltonien")

    )pbdoc")
    
    .def("greedy_coloring", &fastgraphfpms::Graph::greedy_coloring, R"pbdoc(

        Colorie le graphe en utilisant l'algorithme glouton.
        
        Returns:
            list: Vecteur où l'élément i est la couleur du nœud i
            
        Example:
            >>> coloring = graph.greedy_coloring()
            >>> print(f"Coloration: {coloring}")

    )pbdoc")

    .def("welsh_powell_coloring", &fastgraphfpms::Graph::welsh_powell_coloring, R"pbdoc(

        Colorie le graphe en utilisant l'algorithme de Welsh-Powell.
        
        Returns:
            list: Vecteur où l'élément i est la couleur du nœud i
            
        Example:
            >>> coloring = graph.welsh_powell_coloring()
            >>> print(f"Coloration: {coloring}")

    )pbdoc")

    .def("dsatur_coloring", &fastgraphfpms::Graph::dsatur_coloring, R"pbdoc(

        Colorie le graphe en utilisant l'algorithme DSATUR (Degree of SATuration).
        
        Returns:
            list: Vecteur où l'élément i est la couleur du nœud i
            
        Example:
            >>> coloring = graph.dsatur_coloring()
            >>> print(f"Coloration: {coloring}")

    )pbdoc")

    .def("chromatic_number", &fastgraphfpms::Graph::chromatic_number, R"pbdoc(

        Retourne le nombre chromatique du graphe (nombre minimum de couleurs nécessaires).
        
        Returns:
            int: Nombre chromatique
            
        Example:
            >>> chi = graph.chromatic_number()
            >>> print(f"Nombre chromatique: {chi}")

    )pbdoc")

    .def("is_bipartite_coloring", &fastgraphfpms::Graph::is_bipartite_coloring, R"pbdoc(

        Vérifie si le graphe est biparti (2-colorable).
        
        Returns:
            bool: True si le graphe est biparti
            
        Example:
            >>> if graph.is_bipartite_coloring():
            ...     print("Le graphe est biparti")

    )pbdoc")

    .def("is_k_colorable", &fastgraphfpms::Graph::is_k_colorable, 
        py::arg("k"), R"pbdoc(

        Vérifie si le graphe est k-colorable.
        
        Args:
            k: Nombre de couleurs
            
        Returns:
            bool: True si le graphe est k-colorable
            
        Example:
            >>> if graph.is_k_colorable(3):
            ...     print("Le graphe est 3-colorable")

    )pbdoc")

    .def("get_color_classes", &fastgraphfpms::Graph::get_color_classes, R"pbdoc(

        Retourne les classes de couleur après coloration.
        
        Returns:
            list: Liste de listes, où chaque sous-liste contient les nœuds d'une couleur
            
        Example:
            >>> classes = graph.get_color_classes()
            >>> for i, class_nodes in enumerate(classes):
            ...     print(f"Couleur {i}: {class_nodes}")

    )pbdoc")
    
    .def("max_flow_ford_fulkerson", &fastgraphfpms::Graph::max_flow_ford_fulkerson, 
        py::arg("source"), py::arg("sink"), R"pbdoc(

        Calcule le flot maximum entre la source et le puits avec Ford-Fulkerson (DFS).
        
        Args:
            source: Nœud source
            sink: Nœud puits
            
        Returns:
            int: Valeur du flot maximum
            
        Example:
            >>> flow = graph.max_flow_ford_fulkerson(0, 5)
            >>> print(f"Flot maximum: {flow}")

    )pbdoc")

    .def("max_flow_edmonds_karp", &fastgraphfpms::Graph::max_flow_edmonds_karp, 
        py::arg("source"), py::arg("sink"), R"pbdoc(

        Calcule le flot maximum entre la source et le puits avec Edmonds-Karp (BFS).
        
        Args:
            source: Nœud source
            sink: Nœud puits
            
        Returns:
            int: Valeur du flot maximum
            
        Example:
            >>> flow = graph.max_flow_edmonds_karp(0, 5)
            >>> print(f"Flot maximum: {flow}")

    )pbdoc");

    // Version
    #ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
    #else
    m.attr("__version__") = "0.1.0";
    #endif
}