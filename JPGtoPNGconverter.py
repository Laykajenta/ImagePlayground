import os
from PIL import Image

# Define paths
base_folder = "Pokedex"
new_folder = os.path.join(base_folder, "new")

# Create 'new' folder if it doesn't exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Loop through files in 'Pokedex'
for item in os.listdir(base_folder):
    full_path = os.path.join(base_folder, item)

    # Check if it's a .jpg file (case-insensitive)
    if os.path.isfile(full_path) and item.lower().endswith(".jpg"):
        with Image.open(full_path) as img:
            # Create PNG filename and save in 'new' folder
            png_name = os.path.splitext(item)[0] + ".png"
            png_path = os.path.join(new_folder, png_name)
            img.save(png_path, "PNG")
            print(f"Converted: {item} → new/{png_name}")
