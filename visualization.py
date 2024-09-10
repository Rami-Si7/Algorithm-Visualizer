import pygame
from config import *  # Import screen and font

def visualize_algorithm(steps, algorithm):
    clock = pygame.time.Clock()

    for step in steps:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        screen.fill((255, 255, 255))

        if algorithm == 'Bubble Sort':
            draw_bubble_sort(step[0], step[1], step[2:])
        elif algorithm == 'Insertion Sort':
            draw_insertion_sort(step[0], step[1], step[2])
        elif algorithm == 'Selection Sort':
            draw_selection_sort(step[0], step[1], step[2])

        pygame.display.flip()
        clock.tick(10)

    return True

def draw_bubble_sort(arr, sorted_index, active_indices):
    width = 800 // len(arr)
    max_height = max(arr)
    for i, val in enumerate(arr):
        bar_height = val / max_height * 500
        x = i * width
        y = 600 - bar_height
        if i in active_indices:
            color = (0, 255, 0)
        elif sorted_index == -1 or i > sorted_index:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)
        pygame.draw.rect(screen, color, (x, y, width, bar_height))
        label = font.render(str(val), True, (0, 0, 0))
        screen.blit(label, (x, y - 20))

def draw_insertion_sort(arr, sorted_indices, active_index):
    width = 800 // len(arr)
    max_height = max(arr)
    for i, val in enumerate(arr):
        bar_height = val / max_height * 500
        x = i * width
        y = 600 - bar_height
        if i in sorted_indices:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)
        pygame.draw.rect(screen, color, (x, y, width, bar_height))
        label = font.render(str(val), True, (0, 0, 0))
        screen.blit(label, (x, y - 20))

def draw_selection_sort(arr, sorted_index, min_index):
    width = 800 // len(arr)
    max_height = max(arr)
    for i, val in enumerate(arr):
        bar_height = val / max_height * 500
        x = i * width
        y = 600 - bar_height
        if i == min_index:
            color = (0, 255, 0)
        elif sorted_index == -1 or i > sorted_index:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)
        pygame.draw.rect(screen, color, (x, y, width, bar_height))
        label = font.render(str(val), True, (0, 0, 0))
        screen.blit(label, (x, y - 20))


def draw_graph(graph, positions):
    screen.fill(WHITE)

    # Draw edges
    for node, neighbors in graph.graph.items():
        for neighbor in neighbors:
            pygame.draw.line(screen, BLACK, positions[node], positions[neighbor], 2)

    # Draw nodes
    for node, pos in positions.items():
        pygame.draw.circle(screen, GREEN, pos, 20)
        label = font.render(str(node), True, BLACK)
        screen.blit(label, (pos[0] - 10, pos[1] - 10))

    pygame.display.flip()

