import shutil

def save_uploaded_wav(uploaded_file, output_path: str):
    """
    Saves uploaded WAV file to disk
    """
    with open(output_path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)
