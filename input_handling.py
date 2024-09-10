import pygame
from button import Button
from config import *

def draw_data_input_menu():
    screen.fill(WHITE)
    title = font.render('Would you like to enter data or generate randomly?', True, BLACK)
    screen.blit(title, (150, 100))

    enter_data_button = Button('Enter Data Manually', (320, 200), 200, 40, font, bg=BUTTON_COLOR)
    random_data_button = Button('Generate Random Data', (320, 300), 200, 40, font, bg=BUTTON_COLOR)

    buttons = [enter_data_button, random_data_button]
    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.draw(screen, mouse_pos)

    pygame.display.flip()
    return buttons

def data_input_menu():
    buttons = draw_data_input_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None, False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event):
                        if button.text == 'Enter Data Manually':
                            arr = text_input_menu()
                            if arr is None:
                                return None, False
                            return arr, True
                        elif button.text == 'Generate Random Data':
                            return 'random', True

def text_input_menu():
    input_box = pygame.Rect(150, 250, 500, 50)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    user_text = ''
    error_message = ''

    font_input = pygame.font.SysFont('Arial', 32)
    font_error = pygame.font.SysFont('Arial', 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            arr = list(map(int, user_text.split(',')))
                            if len(arr) < 2:
                                error_message = 'Please enter more than one number.'
                            else:
                                return arr
                        except ValueError:
                            error_message = 'Invalid input. Please enter numbers separated by commas.'
                            user_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        screen.fill(WHITE)
        title = font.render('Enter a comma-separated list of numbers:', True, BLACK)
        screen.blit(title, (150, 150))

        txt_surface = font_input.render(user_text, True, color)
        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10))

        if error_message:
            error_surface = font_error.render(error_message, True, pygame.Color('red'))
            screen.blit(error_surface, (150, 350))

        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()


import pygame
from config import screen, WHITE, BLACK, font, BUTTON_COLOR
from button import Button


def custom_graph_input_menu():
    input_box = pygame.Rect(150, 250, 500, 50)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    user_text = ''
    error_message = ''  # Variable to store error messages
    graph_data = {
        'nodes': [],
        'edges': []
    }
    input_type = 'node'  # Start by asking for nodes

    # Buttons
    finish_node_button = Button("Finish Node Entry", (350, 350), 200, 40, font,
                                bg=BUTTON_COLOR)  # Finish node input button
    finish_edge_button = Button("Finish Edge Entry", (350, 400), 200, 40, font,
                                bg=BUTTON_COLOR)  # Finish edge input button

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None  # Exit if window is closed

            # Handle mouse clicks for input box or buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

                # If finish button is clicked for nodes, move to edge input
                if finish_node_button.is_clicked(event) and input_type == 'node' and len(graph_data['nodes']) >= 2:
                    input_type = 'edge'
                    error_message = ''  # Clear any previous error messages

                # If finish button is clicked for edges, finish edge input
                if finish_edge_button.is_clicked(event) and input_type == 'edge':
                    if len(graph_data['edges']) > 0:
                        return graph_data  # Return the graph data if at least one edge is added

            # Handle key input for text box
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if input_type == 'node':
                            node = user_text.strip()
                            if node not in graph_data['nodes']:  # Only add unique nodes
                                graph_data['nodes'].append(node)
                                user_text = ''
                                error_message = ''
                            else:
                                error_message = f"Node '{node}' already exists."
                        elif input_type == 'edge':
                            try:
                                # Assume the user inputs the edge in the format node1,node2
                                node1, node2 = user_text.split(',')
                                node1, node2 = node1.strip(), node2.strip()

                                # Check if both nodes exist
                                if node1 not in graph_data['nodes'] or node2 not in graph_data['nodes']:
                                    error_message = 'Both nodes must be added first.'
                                    user_text = ''
                                else:
                                    edge = (node1, node2)

                                    # Check if the edge already exists (bidirectional check)
                                    if edge in graph_data['edges'] or (node2, node1) in graph_data['edges']:
                                        error_message = 'This edge already exists.'
                                    else:
                                        graph_data['edges'].append(edge)
                                        user_text = ''
                                        error_message = ''

                                        # Check if the maximum number of edges is reached
                                        max_edges = len(graph_data['nodes']) * (len(graph_data['nodes']) - 1) // 2
                                        if len(graph_data['edges']) >= max_edges:
                                            return graph_data  # Return graph data if maximum edges are added
                            except ValueError:
                                error_message = 'Invalid input format. Enter edges as "node1,node2".'
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        screen.fill(WHITE)

        # Display different prompts for node and edge input
        title = font.render('Enter Nodes (Press Enter after each node)', True, BLACK) if input_type == 'node' else \
            font.render('Enter Edges as "node1,node2" (Press Enter after each edge)', True, BLACK)
        screen.blit(title, (100, 150))

        # Display error message if any
        if error_message:
            error_surface = font.render(error_message, True, pygame.Color('red'))
            screen.blit(error_surface, (150, 400))

        # Draw the input text box
        txt_surface = font.render(user_text, True, BLACK)
        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10))

        # Draw the input box and the buttons
        pygame.draw.rect(screen, color, input_box, 2)
        if input_type == 'node':
            finish_node_button.draw(screen, pygame.mouse.get_pos())  # Only show the finish button during node input
        elif input_type == 'edge':
            finish_edge_button.draw(screen, pygame.mouse.get_pos())  # Show the finish button during edge input

        pygame.display.flip()


