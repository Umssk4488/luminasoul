import streamlit as st
import random
import requests

# --- 🎨 ยกเครื่องดีไซน์แบบพรีเมียม (Premium Pastel Gradient) ---
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮")

st.markdown("""
    <style>
    /* 1. พื้นหลังไล่สีนุ่มนวล (Premium Lavender -> Soft Peach) */
    .stApp {
        background-image: linear-gradient(135deg, #fdfcfb 0%, #e2d1f9 40%, #fdfbfb 70%, #fff1eb 100%);
    }

    /* 2. ปรับปรุงหัวข้อหลักให้โดดเด่น */
    h1 {
        color: #4a148c;
        font-family: 'Sarabun', sans-serif;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        font-weight: 800;
        margin-bottom: 0px;
    }
    
    /* 3. ปรับปรุงหัวข้อรอง */
    h3 {
        color: #7e57c2;
        text-align: center;
        font-weight: 400;
        margin-top: 0px;
        margin-bottom: 30px;
    }

    /* 4. ปรับกล่องฟอร์มให้ดูนุ่มนวล (Glassmorphism style light) */
    div[data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid rgba(255, 255, 255, 0.4);
    }

    /* 5. ปรับแต่งปุ่มกดให้พรีเมียมไล่สี (Gradient Button with Hover effect) */
    div.stButton > button:first-child {
        background: linear-gradient(to right, #ba68c8 0%, #f06292 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.7rem 2.5rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: 0.3s all ease;
        box-shadow: 0 4px 15px rgba(186, 104, 200, 0.3);
        width: 100%;
        margin-top: 20px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(to right, #ab47bc 0%, #ec407a 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(186, 104, 200, 0.4);
    }

    /* 6. ปรับแต่งกล่อง Input/Select/TextArea */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea, .stNumberInput>div>div
