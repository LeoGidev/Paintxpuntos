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

# Crear una imagen en blanco
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Crear una ventana y asociar la función de manejo del mouse
cv2.namedWindow("Arrastrar Vértices")
cv2.setMouseCallback("Arrastrar Vértices", mouse_handler)

# Bucle principal
while True:
    # Copiar la imagen para evitar sobrescribir los vértices
    canvas = image.copy()

    # Dibujar los vértices del polígono
    for vertex in vertices:
        cv2.circle(canvas, vertex, 5, (0, 0, 255), -1)

    # Dibujar el polígono con líneas entre los vértices
    if len(vertices) > 1:
        cv2.polylines(canvas, [np.array(vertices)], False, (0, 255, 0), 2)

    # Mostrar la imagen con los vértices y el polígono
    cv2.imshow("Arrastrar Vértices", canvas)

    # Esperar la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cerrar todas las ventanas
cv2.destroyAllWindows()