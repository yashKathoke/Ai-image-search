import os
import streamlit as st
# from transformers import pipeline
import torch
from diffusers import DiffusionPipeline, StableDiffusionInpaintPipeline
import ctransformers
from transformers import pipeline
from transformers import CLIPTokenizer, CLIPProcessor


@st.cache_resource()
def load_model_pipeline(task, model_path, device='cpu'):
    model = pipeline(task=task, model=model_path, device=device)
    return model


##------------------------------------------------------------------------------------------------------------


@st.cache_resource()
def load_audio_model(model_path, chunk_length_s=30, device='cpu'):
    model = pipeline("automatic-speech-recognition", model=model_path, device=device)
    return model


def save_uploaded_file(uploaded_file):
    try:
        os.makedirs("temp", exist_ok=True)
        file_path = os.path.join("temp", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        return None


def generate_text_from_audio(model, audio_file):
    file_path = save_uploaded_file(audio_file)
    result = model(file_path)["text"]
    return result


# -----------------------------------------------------------------------------------------------------------
@st.cache_resource()
def load_model_image_sdxl(model_path, model_path_lora=None):
    base = DiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16, variant="fp16",
                                             use_safetensors=True)

    if model_path_lora:
        base.load_lora_weights(model_path_lora)

    base.enable_model_cpu_offload()
    return base


def generate_image_sdxl(base, prompt, num_inference_steps=20, guidance_scale=4):
    image = base(prompt=prompt, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale).images[0]

    return image


# -------------------------------------------------------------------------------------------------------------------------------

@st.cache_resource()
def load_model_inpaint(model_path, torch_dtype=torch.float16):
    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        model_path,
        revision="fp16",
        torch_dtype=torch_dtype,
    )
    pipe.enable_model_cpu_offload()
    return pipe


# TEXT GEN WITH LLAMA GGUF

@st.cache_resource()
def load_model_text_llama(model_path, model_file, model_type="llama", gpu_layers=0):
    model = ctransformers.AutoModelForCausalLM.from_pretrained(model_path_or_repo_id=model_path, model_file=model_file,
                                                               model_type=model_type,
                                                               gpu_layers=gpu_layers)

    return model


def generate_text_faster(model, prompt, textarea_placeholder, streamStop, stop=None):
    if stop is None:
        stop = ['\n', "Question:", "Q"]
    generated_text = ""
    for text in model(prompt, stream=True, stop=stop):
        generated_text += text
        textarea_placeholder.markdown(generated_text)
        if streamStop:
            return generated_text
    return generated_text


# -----------------------------------------------------------------------------------------------------------------------------
# Text Encode
def get_text_encoder(model_name="openai/clip-vit-base-patch32"):
    """
  This function loads a pre-trained CLIP model as a text encoder.

  Args:
      model_name (str, optional): Name of the pre-trained CLIP model. Defaults to "openai/clip-vit-base-patch32".

  Returns:
      tuple: A tuple containing the CLIP tokenizer and processor for text encoding.
  """
    tokenizer = CLIPTokenizer.from_pretrained(model_name)
    processor = CLIPProcessor.from_pretrained(model_name)
    return tokenizer, processor


def encode_text(tokenizer, processor, prompt):
    """
  This function encodes a text prompt using the CLIP tokenizer and processor.

  Args:
      tokenizer (transformers.CLIPTokenizer): The CLIP tokenizer.
      processor (transformers.CLIPProcessor): The CLIP processor.
      prompt (str): The text prompt to encode.

  Returns:
      tuple: A tuple containing the positive and negative image embeddings for the prompt.
  """
    encoding = tokenizer(prompt, return_tensors="pt")
    image_embeds = processor(text_input=encoding["input_ids"])["pixel_values"]
    # Assuming negative embeddings are not required, return only positive embeddings
    return image_embeds, None  # Modify this to return negative embeddings if needed


def main():
    pass


if __name__ == '__main__':
    main()
