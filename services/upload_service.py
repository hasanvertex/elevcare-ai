
import os

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_file(uploaded_file):

    if uploaded_file is None:
        return None

    path = os.path.join(
        UPLOAD_DIR,
        uploaded_file.name
    )

    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return path
