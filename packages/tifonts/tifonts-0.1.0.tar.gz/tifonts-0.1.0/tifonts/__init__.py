from .font_loader import load_font, Font
from .text_renderer import text as _text_renderer_text

_default_font_path = "tifonts/fonts/pixels5x7"
_default_font_obj = None

def load(font_path=None):
    global _default_font_obj
    if font_path is None:
        if _default_font_obj is None:
            _default_font_obj = load_font(_default_font_path)
        return _default_font_obj
    else:
        return load_font(font_path)

def text(canvas, text_str, x, y, size, color, font=None):
    if font is None:
        # Ensure default font is loaded
        _ = load() # This will load if not already loaded
        font = _default_font_obj
    # Pass the Font object directly to the renderer
    _text_renderer_text(canvas, text_str, x, y, size, color, font)