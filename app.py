
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from langdetect import detect, detect_langs

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn. linear_model import LogisticRegression
from sklearn.model_selection import train test_split
from sklearn.metrics import accuracy_score
import os
import re

# Setup Tesseract
pytesseract.pytesseract.tesseract_cd = r'C: \Program Files \Tesseract-OCR\tesseract.exe'
os. environ["TESSDATA_PREFIX"] = r'C: \Program Files\Tesseract-OCR\tessdata'

@st. cache_resource
def load model_and_accuracy():
    df = pd.read_csv(r"C:/Users/AB Tech/Desktop/Final/Language Detection.csv")
    x = df['Text']
    y = df['Language']
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    pipeline = Pipeline([
    ('tfidf', Tfidfvectorizer()),
    ('classifier', LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(x_train, y_train)
    y_pred = pipeline.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    return pipeline, accuracy

model, accuracy = load model and accuracy()

def preprocess_image (image):
    img = image.convert('L')
    img = img.filter(ImageFilter.SHARPEN)
    enhancer = ImageEnhance.Contrast (img)
    img = enhancer. enhance(2)
    return img

def filter text by_language(text, lang='en"):
    if lang == 'en'
     # Keep only English letters, numbers, and basic punctuation
    return re. sub(r'[^A-Za-20-9\s.,!?|"1"1", ", text)
  # Optionally add filters for other languages (e.g. Hindi, Kannada)
  return text

st. title(" Multi-language OCR & Language Detection"')
st. markdown("Upload an image with text. The app will extract and detect the language.")

st. write(f"**Model Accuracy on Test Data:** {accuracy * 100: 2f)%")
          
or_langs = st.text_input("OCR Languages (e.g. engthin+kan):", "engthin+kan")

uploaded_file = st.file uploader ("Upload an Image", type=["png", 'jpg', 'jpeg'1)

if uploaded_file is not None:
   image = Image.open(uploaded_file)
   st. image (image, caption="Uploaded Image", use_column width=True)

   preprocessed_img = preprocess_image(image)
   with st. spinner("Extracting text..."):
       extracted_text = pytesseract image_to_string(preprocessed_img, lang-ocr_langs)

       st. subheader (" E Extracted Text (Raw):") st. text_area"Text", extracted_text, height=200)
# Filter text to only English
       filtered text = filter text by language(extracted text, lang='en')
# Filter text to only English
filtered_text = filter_text _by_language(extracted_ text, lang='en')
st. subheader(" B Extracted Text (Filtered to English):") 
st. text_area"Filtered Text", filtered_text, height=200)

if filtered text.strip():
    detected model_lang = model.predict([filtered_text])[0]
    st. subheader ("Detected Language (Model):")
    st. write(detected model_Lang)

    try:
       detected_lang = detect (filtered_text)
       lang_probs = detect_langs(filtered_text)
       st. subheader ('Detected Language (Langdetect) for Filtered Text:') 
       st write(f' {detected_lang}  Loading...ininint(Ip) for Ip in lang_ probs'))
    except:
       st. warning("Could not detect language via langdetect.")
else:
    st. warning("No valid text detected in the filtered content. ")
