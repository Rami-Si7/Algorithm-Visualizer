import pygame
import random
from config import screen, WHITE
from menu import main_menu, sorting_menu, replay_menu, graph_menu, custom_or_predefined_menu
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort
from input_handling import data_input_menu
from visualization import visualize_algorithm
from input_handling import custom_graph_input_menu
from graph_visualization import draw_graph, visualize_graph_algorithm
from graph import Graph
from graph_algorithms import bfs, dfs
from graph import splatter_nodes

def main():
    running = True
    while running:
        section = main_menu()
        if not section:
            running = False
            break
        if section == 'sorting':
            while running:
                section = sorting_menu()
                if not section:
                    running = False
                    break

                if section in ['bubble', 'insertion', 'selection']:
                    data_choice, valid = data_input_menu()
                    if not valid:
                        running = False
                        break

                    if isinstance(data_choice, list):  # User entered data manually
                        arr = data_choice
                    elif data_choice == 'random':
                        arr = [random.randint(1, 100) for _ in range(10)]

                    while True:
                        # Sorting visualization
                        if section == 'bubble':
                            steps = bubble_sort(arr.copy())
                            visualize_algorithm(steps, 'Bubble Sort')
                        elif section == 'insertion':
                            steps = insertion_sort(arr.copy())
                            visualize_algorithm(steps, 'Insertion Sort')
                        elif section == 'selection':
                            steps = selection_sort(arr.copy())
                            visualize_algorithm(steps, 'Selection Sort')

                        # After sorting is done, ask the user what to do next
                        replay_action = replay_menu()
                        if replay_action == 'replay':
                            continue
                        elif replay_action == 'menu':
                            break

                elif section == 'main_menu':
                    break
                elif section == 'quit':
                    running = False
                    break
        elif section == 'graph':
            while running:
                section = graph_menu()
                if not section:
                    running = False
                    break

                if section in ['bfs', 'dfs']:
                    # Ask the user if they want a custom graph or a predefined one
                    graph_choice = custom_or_predefined_menu()
                    if graph_choice == 'custom_graph':
                        graph_data = custom_graph_input_menu()  # Custom graph input
                        if graph_data:
                            # Build the graph from user input
                            custom_graph = Graph()
                            for node in graph_data['nodes']:
                                custom_graph.add_node(node)
                            for edge in graph_data['edges']:
                                custom_graph.add_edge(edge[0], edge[1])

                            # Auto-layout for simple graphs (you may want to customize positions for complex graphs)
                            positions = splatter_nodes(graph_data['nodes'])
                            draw_graph(custom_graph, positions)
                            # Allow user to choose BFS or DFS to visualize on their custom graph
                            if section == 'bfs':
                                steps = bfs(custom_graph, graph_data['nodes'][0])
                            else:
                                steps = dfs(custom_graph, graph_data['nodes'][0])

                            visualize_graph_algorithm(custom_graph, positions, steps)

                    elif graph_choice == 'predefined_graph':
                        # Example predefined graph
                        graph = Graph()
                        graph.add_node(1)
                        graph.add_node(2)
                        graph.add_node(3)
                        graph.add_node(4)
                        graph.add_node(5)
                        graph.add_edge(1, 2)
                        graph.add_edge(1, 3)
                        graph.add_edge(2, 4)
                        graph.add_edge(3, 5)

                        positions = {
                            1: (200, 300),
                            2: (300, 200),
                            3: (300, 400),
                            4: (400, 150),
                            5: (400, 450),
                        }

                        draw_graph(graph, positions)

                        if section == 'bfs':
                            steps = bfs(graph, 1)
                        else:
                            steps = dfs(graph, 1)

                        visualize_graph_algorithm(graph, positions, steps)

                elif section == 'main_menu':
                    break
                elif section == 'quit':
                    running = False

    pygame.quit()


if __name__ == "__main__":
    main()
