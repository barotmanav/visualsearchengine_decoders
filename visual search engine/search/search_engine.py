# search.py

import faiss
import numpy as np

# FAISS index for 512-dimensional vectors
vector_dim = 512
index = faiss.IndexFlatL2(vector_dim)
image_paths = []  # Will store the paths/URLs for images

# Add image with its feature vector
def add_image(vector, image_path):
    """
    Add an image's vector and path to the index.
    :param vector: list or np.array of shape (512,)
    :param image_path: string (URL or path)
    """
    global image_paths
    if not isinstance(vector, np.ndarray):
        vector = np.array(vector, dtype=np.float32)
    if vector.ndim == 1:
        vector = np.expand_dims(vector, axis=0)
    index.add(vector)
    image_paths.append(image_path)

# Search similar images
def search_image(query_vector, top_k=5):
    """
    Search for top_k similar images.
    :param query_vector: list or np.array of shape (512,)
    :return: list of image paths
    """
    if not isinstance(query_vector, np.ndarray):
        query_vector = np.array(query_vector, dtype=np.float32)
    if query_vector.ndim == 1:
        query_vector = np.expand_dims(query_vector, axis=0)
    
    distances, indices = index.search(query_vector, top_k)
    return [image_paths[i] for i in indices[0]]

# Example usage (only for testing purpose)
if __name__ == "__main__":
    # Simulate adding 5 image vectors
    for i in range(5):
        fake_vector = np.random.rand(512).astype(np.float32)
        add_image(fake_vector, f"/static/image_{i}.jpg")

    # Simulate searching with a new random query vector
    query = np.random.rand(512).astype(np.float32)
    results = search_image(query)
    
    print("Top matching images:")
    for path in results:
        print(path)


