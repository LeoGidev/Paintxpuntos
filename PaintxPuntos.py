import cv2
import numpy as np

# Variables globales
dragging = False
selected_vertex = None
vertices = []

# Función para manejar el evento del mouse
def mouse_handler(event, x, y, flags, param):
    global dragging, selected_vertex, vertices

    if event == cv2.EVENT_LBUTTONDOWN:
        # Agregar un nuevo vértice
        vertices.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        # Detener el arrastre del vértice
        dragging = False
        selected_vertex = None

    elif event == cv2.EVENT_MOUSEMOVE:
        # Arrastrar el último vértice agregado
        if len(vertices) > 0:
            vertices[-1] = (x, y)

