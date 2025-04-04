import faiss
from model.clip_model import get_image_embedding, get_text_embedding

index = faiss.read_index("image_index.faiss")
with open("image_paths.txt", "r") as f:
    image_paths = [line.strip() for line in f]
def search_by_image(image):
    results = ["images/moon1.jpg", "images/earth.jpg"]

    
    results = [filename.replace("images\\", "").replace("images/", "") for filename in results]

    return results

def search_by_text(query):
    results = ["images/moon1.jpg", "images/martin-marek.jpg", "images/moon.jpg"]
    
    
    results = [filename.replace("images\\", "").replace("images/", "") for filename in results]

    return results

