import pygame
from button import Button
from config import screen, font, WHITE, BLACK, BUTTON_COLOR  # Import globals


def draw_sorting_menu():
    screen.fill(WHITE)
    title = font.render('Sorting Algorithms', True, BLACK)
    screen.blit(title, (300, 100))
    buttons = [
        Button('Bubble Sort', (320, 150), 200, 40, font, bg=BUTTON_COLOR),
        Button('Insertion Sort', (320, 200), 200, 40, font, bg=BUTTON_COLOR),
        Button('Selection Sort', (320, 250), 200, 40, font, bg=BUTTON_COLOR),
        Button('Back to Main Menu', (320, 400), 200, 40, font, bg=BUTTON_COLOR),
    ]
    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.draw(screen, mouse_pos)
    pygame.display.flip()
    return buttons

def sorting_menu():
    buttons = draw_sorting_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event):
                        if button.text == 'Bubble Sort':
                            return 'bubble'
                        elif button.text == 'Insertion Sort':
                            return 'insertion'
                        elif button.text == 'Selection Sort':
                            return 'selection'
                        elif button.text == 'Back to Main Menu':
                            return 'main_menu'

def draw_replay_menu():
    screen.fill(WHITE)
    title = font.render('Sorting Complete! What would you like to do?', True, BLACK)
    screen.blit(title, (200, 100))

    replay_button = Button('Replay', (320, 200), 200, 40, font, bg=BUTTON_COLOR)
    return_button = Button('Return to Sorting Menu', (320, 300), 200, 40, font, bg=BUTTON_COLOR)

    buttons = [replay_button, return_button]
    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.draw(screen, mouse_pos)

    pygame.display.flip()
    return buttons

def replay_menu():
    buttons = draw_replay_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event):
                        if button.text == 'Replay':
                            return 'replay'
                        elif button.text == 'Return to Sorting Menu':
                            return 'menu'


def draw_graph_menu():
    """Draws the graph algorithms menu on the screen."""
    screen.fill(WHITE)
    title = font.render('Graph Algorithms', True, BLACK)
    screen.blit(title, (300, 100))

    buttons = [
        Button('Breadth-First Search (BFS)', (300, 200), 250, 40, font, bg=BUTTON_COLOR),
        Button('Depth-First Search (DFS)', (300, 250), 250, 40, font, bg=BUTTON_COLOR),
        Button('Back to Main Menu', (300, 400), 250, 40, font, bg=BUTTON_COLOR),
    ]

    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.draw(screen, mouse_pos)

    pygame.display.flip()
    return buttons

def graph_menu():
    """Handles the user interaction with the graph algorithms menu."""
    buttons = draw_graph_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event):
                        if button.text == 'Breadth-First Search (BFS)':
                            return 'bfs'
                        elif button.text == 'Depth-First Search (DFS)':
                            return 'dfs'
                        elif button.text == 'Back to Main Menu':
                            return 'main_menu'
        pygame.display.flip()


def draw_custom_or_predefined_menu():
    """Draws the menu asking if the user wants to use a custom or predefined graph."""
    screen.fill(WHITE)
    title = font.render('Custom or Predefined Graph?', True, BLACK)
    screen.blit(title, (300, 100))

    buttons = [
        Button('Custom Graph', (300, 200), 250, 40, font, bg=BUTTON_COLOR),
        Button('Predefined Graph', (300, 250), 250, 40, font, bg=BUTTON_COLOR),
        Button('Back to Algorithm Menu', (300, 400), 250, 40, font, bg=BUTTON_COLOR),
    ]

    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.draw(screen, mouse_pos)

    pygame.display.flip()
    return buttons

def custom_or_predefined_menu():
    """Handles the user interaction for choosing a custom or predefined graph."""
    buttons = draw_custom_or_predefined_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event):
                        if button.text == 'Custom Graph':
                            return 'custom_graph'
                        elif button.text == 'Predefined Graph':
                            return 'predefined_graph'
                        elif button.text == 'Back to Algorithm Menu':
                            return 'graph_menu'
        pygame.display.flip()


def draw_main_menu():
    screen.fill(WHITE)
    title_font = pygame.font.SysFont("Arial", 60)
    title_surf = title_font.render("Algorithm Visualizer", True, BLACK)
    title_rect = title_surf.get_rect(center=(screen.get_width() / 2, 100))
    screen.blit(title_surf, title_rect)

    sorting_button = Button('Sorting Algorithms', (320, 200), 200, 40, font, bg=BUTTON_COLOR)
    graph_button = Button('Graph Algorithms', (320, 250), 200, 40, font, bg=BUTTON_COLOR)  # Added graph algorithms
    exit_button = Button('Exit', (320, 300), 200, 40, font, bg=BUTTON_COLOR)

    buttons = [sorting_button, graph_button, exit_button]
    mouse_pos = pygame.mouse.get_pos()

    for button in buttons:
        button.draw(screen, mouse_pos)

    pygame.display.flip()
    return buttons


def main_menu():
    buttons = draw_main_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event):
                        if button.text == 'Sorting Algorithms':
                            return 'sorting'
                        elif button.text == 'Graph Algorithms':
                            return 'graph'  # Handle graph algorithms
                        elif button.text == 'Exit':
                            pygame.quit()
                            return False
        pygame.display.flip()
