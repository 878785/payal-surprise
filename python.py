from PIL import Image
import os

# Payal folder ka path
folder_path = r"C:\Users\sumit\OneDrive\payal"  # apna folder path

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if filename.lower().endswith((".png", ".jpeg")):
        img = Image.open(file_path).convert("RGB")
        new_filename = os.path.splitext(filename)[0] + ".jpg"
        new_path = os.path.join(folder_path, new_filename)
        
        img.save(new_path, "JPEG")
        print(f"Converted: {filename} → {new_filename}")
        
        # Original PNG/JPEG file delete karo
        os.remove(file_path)
        print(f"Deleted original: {filename}")

print("✅ Saari images JPG me convert ho gayi aur originals delete ho gaye!")
