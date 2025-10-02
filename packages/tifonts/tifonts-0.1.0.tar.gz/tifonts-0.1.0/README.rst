TiFonts: Taichi-Lang Font Rendering Library
===========================================

`tifonts` is a Python library designed to render pixel-based fonts within the `taichi-lang` environment. It allows users to display text on a Taichi canvas with customizable fonts, sizes, colors, and positions.

Features
--------

*   Load custom pixel fonts from JSON files.
*   Render text on a Taichi `ti.field` or `ti.ndarray`.
*   Control text position (x, y), size, and color.
*   Uses `pixels5x7` as the default font if no font is specified.

Installation
------------

This project uses `uv` for dependency management.

1.  **Install uv**: If you don't have `uv` installed, you can install it via `pipx`:

    .. code-block:: bash

        $ pipx install uv

2.  **Install dependencies**: Navigate to the project root directory and install the dependencies:

    .. code-block:: bash

        $ uv sync

Usage
-----

The `tifonts` library provides a simple API for loading fonts and rendering text.

**API:**

.. code-block:: python

    import tifonts

    # Load a specific font
    font = tifonts.load('path/to/your/font')

    # Render text using a specific font
    tifonts.text(canvas, text_string, x, y, size, color, font)

    # Render text using the default font (pixels5x7)
    tifonts.text(canvas, text_string, x, y, size, color)

*   ``canvas``: A Taichi `ti.field` or `ti.ndarray` (e.g., `ti.Vector.field(3, dtype=ti.f32, shape=(WIDTH, HEIGHT))`) to render the text onto.
*   ``text_string``: The string of text to be rendered.
*   ``x``, ``y``: The bottom-left coordinates (in canvas pixels) where the text rendering should start.
*   ``size``: An integer scaling factor for the font pixels. A `size` of 1 means each font pixel is 1x1 canvas pixel, `size` of 2 means 2x2, and so on.
*   ``color``: An RGB tuple (e.g., `(1.0, 1.0, 1.0)` for white), where each component is between 0.0 and 1.0.
*   ``font``: (Optional) The font object returned by `tifonts.load()`. If not provided, the default `pixels5x7` font will be used.

**Example:**

See `main.py` for a complete example.

.. code-block:: python

    import taichi as ti
    import tifonts

    ti.init(arch=ti.cpu)

    WIDTH, HEIGHT = 800, 600
    canvas = ti.Vector.field(3, dtype=ti.f32, shape=(WIDTH, HEIGHT))

    @ti.kernel
    def clear_canvas():
        for i, j in canvas:
            canvas[i, j] = ti.math.vec3(0.0, 0.0, 0.0) # Black background

    def main():
        clear_canvas()

        # --- Example 1: Using the default font ---
        tifonts.text(canvas, "Default Font!", 50, 50, 5, (1.0, 1.0, 1.0))

        # --- Example 2: Loading a specific font ---
        my_font = tifonts.load('tifonts/fonts/pixels5x7')
        tifonts.text(canvas, "Explicit Font!", 50, 150, 3, (0.0, 1.0, 0.0), my_font)

        gui = ti.GUI("Taichi Text Renderer", res=(WIDTH, HEIGHT))
        while gui.running:
            gui.set_image(canvas)
            gui.show()

    if __name__ == '__main__':
        main()

Font Structure
--------------

Fonts are now located within the `tifonts/fonts/` directory. Each font should be organized in a subdirectory like this:

.. code-block::

    tifonts/
    └── fonts/
        └── your_font_name/
            ├── your_font_name.json
            ├── char_set_1.json
            └── char_set_2.json

**`your_font_name.json` (main configuration file):**

.. code-block:: json

    {
        "your_font_name": {
            "char_width": 5,
            "char_height": 7,
            "chars": [
                "char_set_1.json",
                "char_set_2.json"
            ]
        }
    }

*   ``char_width``: The width of a single character in pixels.
*   ``char_height``: The height of a single character in pixels.
*   ``chars``: A list of JSON filenames, each containing pixel data for a set of characters.

**`char_set_1.json` (example character set file):**

.. code-block:: json

    {
        "char_set_1": {
            "A": {
                "char": "A",
                "pixels": [
                    0, 1, 1, 1, 0,
                    1, 0, 0, 0, 1,
                    ... (char_width * char_height pixels)
                ]
            },
            "B": {
                "char": "B",
                "pixels": [
                    ...
                ]
            }
        }
    }

*   Each key (e.g., "A", "B") represents a character.
*   The value is an object containing a "char" field (the character itself) and a "pixels" field, which is a flat list of integers (0 or 1) representing the pixel data for the character. The list should contain `char_width * char_height` elements.

Running the Example
-------------------

To run the provided example:

.. code-block:: bash

    $ uv run main.py

This will open a Taichi GUI window displaying the rendered text.

Documents
--------------

.. code-block:: bash

    $ uv run sphinx-build -b html docs/source <output_directory>
    $ uv run sphinx-autobuild docs/source <output_directory>
