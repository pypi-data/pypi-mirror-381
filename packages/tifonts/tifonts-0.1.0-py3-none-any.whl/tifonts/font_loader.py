import json
import os
import taichi as ti
import numpy as np

class Font:
    def __init__(self, char_width, char_height, chars_data):
        self.char_width = char_width
        self.char_height = char_height
        self._font_chars_map = {}
        self._font_data_field = None
        self._prepare_font_data(chars_data)

    def _prepare_font_data(self, chars_data):
        # Create a mapping from character to an integer index
        char_list = sorted(chars_data.keys())
        self._font_chars_map = {char: i for i, char in enumerate(char_list)}

        num_chars = len(char_list)
        
        # Create a NumPy array to hold all flattened character data
        all_char_pixels_np = np.zeros((num_chars, self.char_width * self.char_height), dtype=np.int32)

        for char, idx in self._font_chars_map.items():
            char_pixel_data = chars_data[char] # This is already a 1D list
            all_char_pixels_np[idx, :] = np.array(char_pixel_data, dtype=np.int32)

        # Initialize _font_data_field and transfer data from NumPy array
        self._font_data_field = ti.field(ti.i32, (num_chars, self.char_width * self.char_height))
        self._font_data_field.from_numpy(all_char_pixels_np)

def load_font(font_path):
    """
    Loads font data from the specified font path.

    Args:
        font_path (str): The path to the font directory (e.g., 'fonts/pixels5x7').

    Returns:
        Font: An instance of the Font class containing font data.
    """
    font_name = os.path.basename(font_path)
    config_file = os.path.join(font_path, f"{font_name}.json")

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Font configuration file not found: {config_file}")

    with open(config_file, 'r') as f:
        config = json.load(f)

    # Access the nested dictionary using font_name as the key
    font_config = config.get(font_name, {})

    char_width = font_config.get('char_width')
    char_height = font_config.get('char_height')
    char_files = font_config.get('chars', [])

    if char_width is None or char_height is None:
        raise ValueError(f"char_width or char_height not found in {config_file}")

    all_chars = {}
    for char_file_name in char_files:
        char_file_path = os.path.join(font_path, char_file_name)
        if not os.path.exists(char_file_path):
            print(f"Warning: Character file not found: {char_file_path}")
            continue
        with open(char_file_path, 'r') as f:
            char_data_from_file = json.load(f)
            char_file_base_name = os.path.splitext(char_file_name)[0]
            if char_file_base_name in char_data_from_file:
                actual_char_data = char_data_from_file[char_file_base_name]
                for char_key, char_info in actual_char_data.items():
                    if "pixels" in char_info:
                        all_chars[char_key] = char_info["pixels"]
            else:
                print(f"Warning: Could not find expected key '{char_file_base_name}' in {char_file_path}")

    return Font(char_width, char_height, all_chars)