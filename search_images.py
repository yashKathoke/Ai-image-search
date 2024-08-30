import struct
import sys
import time
from pathlib import Path
from PIL import Image
import uuid
import os

# sys.path.append(str(Path(__file__).resolve().parents[2]))

from offline_module import *


def rename_and_save(uploaded_file, semantics, upload_folder):
    try:
        new_name = f"{uuid.uuid4()}_{semantics}.jpeg"
        new_path = os.path.join(Path(upload_folder), new_name)
        image = uploaded_file
        image.save(new_path, format='JPEG')
    except Exception as e:
        new_name = f"{uuid.uuid4()}_{semantics}.png"
        new_path = os.path.join(Path(upload_folder), new_name)
        image = uploaded_file
        image.save(new_path, format='PNG')


def get_semantics(uploaded_file):
    semantics = model(images=uploaded_file)[0]["generated_text"]
    return semantics


def save_and_process_files(uploaded_files, upload_folder):
    progress = st.progress(0)
    counter = st.empty()

    for i,uploaded_file in enumerate(uploaded_files):
        image = Image.open(uploaded_file)
        semantics = get_semantics(image)
        rename_and_save(image, semantics, upload_folder)
        counter.text(f"{i+1}/{len(uploaded_files)} images processed")
        progress.progress(int((i+1)/len(uploaded_files)*100))


def get_all_files(upload_folder):
    return [
        os.path.join(upload_folder, filename)
        for filename in os.listdir(upload_folder)
    ]


def filter_files(search_query, upload_folder):
    images = get_all_files(upload_folder)
    if search_query:
        keywords = search_query.lower().split()
        filtered_images = [
            file for file in images
            if all(keyword in file.lower() for keyword in keywords)
        ]
        return filtered_images
    else:
        return images


def display_filetered(filter_files):
    if filter_files:
        num_cols = 3
        cols = st.columns(num_cols)
        for index, file in enumerate(filter_files):
            cols[index % num_cols].image(file, use_column_width=True)




st.title("Image Semantics")

model_path = ("./models/models--Salesforce--blip-image-captioning-large/"
              "snapshots/2227ac38c9f16105cb0412e7cab4759978a8fd90")

model = load_model_pipeline("image-to-text", model_path)

# Directory for uploaded images
upload_folder = "upload_folder"
os.makedirs(upload_folder, exist_ok=True)

# Initializing unique key for session of file uploader
if 'file_upload_key' not in st.session_state:
    st.session_state['file_upload_key'] = str(uuid.uuid4())

uploaded_files = st.file_uploader("Choose an image", accept_multiple_files=True, type=["jpg", "jpeg", "png"],
                                  key=st.session_state['file_upload_key'])


if uploaded_files:
    save_and_process_files(uploaded_files, upload_folder)
    st.session_state['file_upload_key'] = str(uuid.uuid4())

search_query = st.text_input("Search Images", value="")
filter_files = filter_files(search_query, upload_folder)
display_filetered(filter_files)

