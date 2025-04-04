import os
import faiss
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from model.clip_model import get_image_embedding



def build_index(image_folder="images"):
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'png'))]
    index = faiss.IndexFlatL2(512)
    image_paths = []

    for file in image_files:
        path = os.path.join(image_folder, file)
        emb = get_image_embedding(path)
        index.add(emb)
        image_paths.append(path)

    faiss.write_index(index, "image_index.faiss")
    with open("image_paths.txt", "w") as f:
        for path in image_paths:
            f.write(path + "\n")

    print("Built index with", len(image_files), "images.")

if __name__ == "__main__":
    build_index()
