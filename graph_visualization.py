import pygame
from config import screen, WHITE, BLACK, GREEN, RED

# Draws the graph on the screen
def draw_graph(graph, positions, visited=None, current=None):
    screen.fill(WHITE)

    # Draw edges
    for node, neighbors in graph.graph.items():
        for neighbor in neighbors:
            pygame.draw.line(screen, BLACK, positions[node], positions[neighbor], 2)

    # Draw nodes
    for node, pos in positions.items():
        if visited and node in visited:
            color = GREEN  # Visited node
        elif current and node == current:
            color = RED  # Current node being processed
        else:
            color = BLACK  # Unvisited node

        pygame.draw.circle(screen, color, pos, 20)
        label = pygame.font.SysFont("Arial", 20).render(str(node), True, WHITE)
        screen.blit(label, (pos[0] - 10, pos[1] - 10))

    pygame.display.flip()

# Visualization of BFS and DFS steps
def visualize_graph_algorithm(graph, positions, steps):
    visited = set()

    for node in steps:
        draw_graph(graph, positions, visited=visited, current=node)
        visited.add(node)

        # Control the speed of the visualization
        pygame.time.delay(500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

    return True