"""
This program implements an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles.
We then create a pink eraser which, when dragged around with the mouse,
sets all the rectangles it touches to white.
"""

from graphics import Canvas
import time

# Constants
CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400
CELL_SIZE: int = 40
ERASER_SIZE: int = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    for obj in overlapping_objects:
        if obj != eraser:
            canvas.set_color(obj, 'white')

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    # Draw the blue grid
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    canvas.wait_for_click()
    click_x, click_y = canvas.get_last_click()

    # Create pink eraser
    eraser = canvas.create_rectangle(
        click_x,
        click_y,
        click_x + ERASER_SIZE,
        click_y + ERASER_SIZE,
        'pink'
    )

    # Live erasing loop
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        canvas.tk.update()  # ✅ Keeps the GUI responsive
        time.sleep(0.05)

if __name__ == '__main__':
    main()
