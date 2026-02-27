import streamlit as st
from ultralytics import YOLO
from PIL import Image
import openai

# 1. Page Config
st.set_page_config(page_title="EcoCycle AI", layout="wide")
st.title("♻️ AI Upcycling Assistant")

# 2. Load Model (YOLOv8)
@st.cache_resource
def load_yolo():
    return YOLO('yolov8n.pt')

model = load_yolo()

# 3. Sidebar for Settings
with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    confidence = st.slider("Detection Confidence", 0.0, 1.0, 0.5)

# 4. Image Upload (Real-time processing)
img_file = st.camera_input("Take a photo of your item")

if img_file:
    img = Image.open(img_file)
    results = model(img, conf=confidence)
    
    # Get detected labels
    names = [model.names[int(c)] for c in results[0].boxes.cls]
    detected_str = ", ".join(set(names))
    
    st.success(f"Detected: {detected_str}")

    # 5. LLM Logic
    if api_key and st.button("Get Upcycling Ideas"):
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"I have {detected_str}. Give 3 creative upcycling ideas."}]
        )
        st.write(response.choices[0].message.content)
