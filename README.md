# Image Semantics

This project processes images to generate semantic descriptions using a pre-trained model. It allows users to upload images, process them to extract semantics, and search through the processed images.

**Hugging Face model used:**
(https://huggingface.co/Salesforce/blip-image-captioning-large)



## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv myenv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        .\myenv\Scripts\activate.bat
        ```
    - On macOS/Linux:
        ```sh
        source myenv/bin/activate
        ```

4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```sh
    streamlit run search_images.py
    ```

2. **Upload Images:**
    - Use the file uploader to select and upload multiple images.

3. **Process Images:**
    - The application will process the uploaded images to generate semantic descriptions.

4. **Search Images:**
    - Use the search bar to filter images based on the generated semantics.

## Key Functions

- **[`get_semantics(uploaded_file)`](command:_github.copilot.openSymbolFromReferences?%5B%22get_semantics(uploaded_file)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyashk%5C%5COneDrive%5C%5CDesktop%5C%5CPython%5C%5CGoogle_Photos_Replica%5C%5Csearch_images.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyashk%2FOneDrive%2FDesktop%2FPython%2FGoogle_Photos_Replica%2Fsearch_images.py%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fyashk%2FOneDrive%2FDesktop%2FPython%2FGoogle_Photos_Replica%2Fsearch_images.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A26%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition")**: Extracts semantic description from the uploaded image.
- **`save_and_process_files(uploaded_files, upload_folder)`**: Saves and processes the uploaded images.
- **`rename_and_save(uploaded_file, semantics, upload_folder)`**: Renames and saves the processed images.
- **[`display_filetered(filter_files)`](command:_github.copilot.openSymbolFromReferences?%5B%22display_filetered(filter_files)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyashk%5C%5COneDrive%5C%5CDesktop%5C%5CPython%5C%5CGoogle_Photos_Replica%5C%5Csearch_images.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyashk%2FOneDrive%2FDesktop%2FPython%2FGoogle_Photos_Replica%2Fsearch_images.py%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fyashk%2FOneDrive%2FDesktop%2FPython%2FGoogle_Photos_Replica%2Fsearch_images.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A63%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition")**: Displays the filtered images based on the search query.

## Model

The project uses the [`Salesforce--blip-image-captioning-large`](command:_github.copilot.openSymbolFromReferences?%5B%22Salesforce--blip-image-captioning-large%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyashk%5C%5COneDrive%5C%5CDesktop%5C%5CPython%5C%5CGoogle_Photos_Replica%5C%5Csearch_images.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyashk%2FOneDrive%2FDesktop%2FPython%2FGoogle_Photos_Replica%2Fsearch_images.py%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fyashk%2FOneDrive%2FDesktop%2FPython%2FGoogle_Photos_Replica%2Fsearch_images.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A75%2C%22character%22%3A32%7D%7D%5D%5D "Go to definition") model to generate image captions. The model is loaded from the [`models/models--Salesforce--blip-image-captioning-large/snapshots/2227ac38c9f16105cb0412e7cab4759978a8fd90`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fyashk%2FOneDrive%2FDesktop%2FPython%2FGoogle_Photos_Replica%2Fmodels%2Fmodels--Salesforce--blip-image-captioning-large%2Fsnapshots%2F2227ac38c9f16105cb0412e7cab4759978a8fd90%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yashk\OneDrive\Desktop\Python\Google_Photos_Replica\models\models--Salesforce--blip-image-captioning-large\snapshots\2227ac38c9f16105cb0412e7cab4759978a8fd90") directory.
