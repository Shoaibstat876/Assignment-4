🧠 Logic Recap: Erase Canvas

Variable              : What It Represents                                : User Input? : Explanation
------------------------------------------------------------------------------------------------------------
CANVAS_WIDTH          : Width of the canvas in pixels                      : ❌ No        : Constant value (400)
CANVAS_HEIGHT         : Height of the canvas in pixels                     : ❌ No        : Constant value (400)
CELL_SIZE             : Size of each blue cell in the grid                : ❌ No        : Each cell is 40x40 px
ERASER_SIZE           : Size of the eraser rectangle                      : ❌ No        : 20x20 px pink box
canvas                : The drawing canvas created using Canvas class     : ❌ No        : Used to draw grid and eraser
eraser                : Pink rectangle controlled by mouse                : ❌ No        : Erases blue cells it touches
mouse_x / mouse_y     : Current mouse coordinates                         : ✅ Yes       : Used to position the eraser
overlapping_objects   : List of items overlapping with the eraser         : ❌ No        : Detected by canvas.find_overlapping
canvas.set_color(...) : Sets any overlapping cell to white                : ❌ No        : Creates erasing effect visually
