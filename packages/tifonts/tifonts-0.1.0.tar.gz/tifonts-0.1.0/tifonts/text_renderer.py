import taichi as ti
import numpy as np
from .font_loader import Font # Import the Font class

@ti.kernel
def _render_text_kernel(canvas: ti.template(), text_indices: ti.template(),
                       start_x: ti.i32, start_y: ti.i32,
                       pixel_size: ti.i32, color: ti.math.vec3,
                       char_width: ti.i32, char_height: ti.i32,
                       font_data_field: ti.template()):
    for i in ti.ndrange(text_indices.shape[0]):
        char_idx = text_indices[i]
        if char_idx == -1: # Skip unknown characters
            continue

        # Calculate the starting position for the current character independently
        char_start_x = start_x + i * char_width * pixel_size
        char_start_y = start_y # Assuming single line for now, y doesn't change per char

        # Render each pixel of the character
        for y_offset, x_offset in ti.ndrange(char_height, char_width):
            # Access flattened font data
            if font_data_field[char_idx, y_offset * char_width + x_offset] == 1:
                # Draw a square for each 'on' pixel
                for py, px in ti.ndrange(pixel_size, pixel_size):
                    canvas_x = char_start_x + x_offset * pixel_size + px
                    canvas_y = char_start_y + (char_height - 1 - y_offset) * pixel_size + py
                    # Ensure coordinates are within canvas bounds
                    if (0 <= canvas_x < canvas.shape[0] and
                        0 <= canvas_y < canvas.shape[1]):
                        canvas[canvas_x, canvas_y] = color

def text(canvas, text_str, x, y, size, color, font: Font):
    """
    Renders text on a Taichi canvas.

    Args:
        canvas (ti.field or ti.ndarray): The Taichi field/ndarray representing the canvas.
        text_str (str): The text string to render.
        x (int): The x-coordinate of the top-left corner of the text.
        y (int): The y-coordinate of the top-left corner of the text.
        size (int): The scaling factor for the font pixels.
        color (tuple): RGB color as a tuple (r, g, b), where each component is between 0.0 and 1.0.
        font (Font): The loaded Font object from tifonts.load().
    """
    # Access font data directly from the Font object
    char_width = font.char_width
    char_height = font.char_height
    font_chars_map = font._font_chars_map
    font_data_field = font._font_data_field

    # Convert text_str to a list of character indices
    text_indices_list = [font_chars_map.get(char, -1) for char in text_str] # -1 for unknown chars
    text_indices_ti = ti.field(ti.i32, len(text_indices_list))
    text_indices_ti.from_numpy(np.array(text_indices_list, dtype=np.int32))

    # Convert color tuple to ti.math.vec3
    ti_color = ti.math.vec3(color[0], color[1], color[2])

    _render_text_kernel(canvas, text_indices_ti, x, y, size, ti_color,
                       char_width, char_height, font_data_field)