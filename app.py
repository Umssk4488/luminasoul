import streamlit as st
import requests

# -----------------------------
# 1. Page Configuration
# -----------------------------
st.set_page_config(
    page_title="LUMINA SOUL",
    page_icon="🔮",
    layout="centered"
)

# -----------------------------
# 2. CSS Styling (Cyber-Mystic & Luxury)
# -----------------------------
st.markdown("""
<style>
html, body, [class*="css"] { color: #2f1f38 !important; }
.stApp {
    background-image: linear-gradient(135deg, #fdfcfb 0%, #e7d7fb 38%, #fdfbfb 68%, #fff2ec 100%);
}
div.stButton > button:first-child, div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(to right, #ba68c8 0%, #f06292 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 0.78rem 1.3rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    box-shadow: 0 6px 18px rgba(186, 104, 200, 0.28) !important;
}
.result-card {
    background: rgba(255,255,255,0.85);
    padding: 22px;
    border-radius: 20px;
    box-shadow: 0 10px 28px rgba(126, 87, 194, 0.12);
    margin-bottom: 15px;
}
.ebook-promo {
    background: linear-gradient(135deg, #6a1b9a 0%, #ad1457 100%);
    color: white !important;
    padding: 25px;
    border-radius: 24px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0 12px 30px rgba(173, 20, 87, 0.3);
}
.ebook-promo h3, .ebook-promo p { color: white !important; }
.lang-box { margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 3. Bilingual Dictionary (TEXTS)
# -----------------------------
TEXTS = {
    "TH": {
        "title": "🔮 LUMINA SOUL",
        "subtitle": "พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด",
        "welcome": "ยินดีต้อนรับสู่พื้นที่แห่งการตื่นรู้และเยียวยาใจ",
        "name": "ชื่อ-นามสกุล",
        "contact": "ID Line (เพื่อรับสิทธิ์อ่านเชิงลึก)",
        "b_day": "วันที่เกิด",
        "b_month": "เดือนเกิด",
        "b_year": "ปี พ.ศ. เกิด",
        "cat": "ด้านที่ต้องการรับพลังงานนำทาง:",
        "q": "เรื่องที่กังวลใจที่สุด:",
        "placeholder": "แชร์เรื่องที่ติดค้างในใจแบบสั้น ๆ...",
        "btn": "🔮 ถอดรหัสพันธสัญญาจิตวิญญาณ",
        "lp_label": "เลขเส้นทางชีวิต (Life Path)",
        "be_label": "เลขพลังงานวันเกิด (Birthday Energy)",
        "ebook_h": "📘 พิมพ์เขียววิญญาณของคุณ (Deep Dive)",
        "ebook_d": "ปลดล็อกความลับ 9 พลังงาน และวิธีแก้ปมชีวิตใน E-book 'The Soul Blueprint'",
        "ebook_btn": "สั่งซื้อผ่าน LINE (ราคา 259.-)",
        "months": ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"],
        "cats": ["ความรักและความสัมพันธ์", "การงานและเส้นทางชีวิต", "โชคลาภและกระแสการเงิน"],
        "m1": "คุณคือผู้บุกเบิก มีพลังสร้างสรรค์ และไม่ควรถูกตีกรอบ",
        "m11": "คุณคือผู้ตื่นรู้ มีสัญชาตญาณแรงกล้า และเป็นแสงนำทางให้ผู้คน",
        # ... (เพิ่มให้ครบตามระบบเดิมของคุณได้เลย)
    },
    "EN": {
        "title": "🔮 LUMINA SOUL",
        "subtitle": "Soul Reflection | Decoding Your Birth Energy",
        "welcome": "Welcome to a space of awakening and spiritual clarity.",
        "name": "Full Name",
        "contact": "WhatsApp / Email / Social ID",
        "b_day": "Day",
        "b_month": "Month",
        "b_year": "Year (B.E.)",
        "cat": "Area of Guidance:",
        "q": "Current Concerns:",
        "placeholder": "Briefly share what's on your heart...",
        "btn": "🔮 Decode Your Soul Contract",
        "lp_label": "Life Path Number",
        "be_label": "Birthday Energy",
        "ebook_h": "📘 Your Soul Blueprint (Full Report)",
        "ebook_d": "Unlock the secrets of your 9 energies and soul lessons in our E-book.",
        "ebook_btn": "Get E-book via LINE/WhatsApp ($15)",
        "months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "cats": ["Love & Relationships", "Career & Life Path", "Wealth & Abundance"],
        "m1": "The Pioneer: You are a creator with a drive to lead and innovate.",
        "m11": "The Master Teacher: High intuition and a mission to illuminate others.",
        # ... (เพิ่มให้ครบ)
    }
}

# -----------------------------
# 4. Numerology Logic
# -----------------------------
def reduce_number(n: int) -> int:
    while n > 9 and n not in (11, 22, 33):
        n = sum(int(d) for d in str(n))
    return n

def life_path_number(day: int, month_num: int, year_be: int) -> int:
    digits = f"{day:02d}{month_num:02d}{year_be}"
    total = sum(int(d) for d in digits)
    return reduce_number(total)

# -----------------------------
# 5. UI Rendering
# -----------------------------
# Language Selection
lang = st.radio("Select Language / เลือกภาษา", ["TH", "EN"], horizontal=True)
T = TEXTS[lang]

# Header
st.markdown(f"""
<div style="text-align:left; margin-top:10px;">
    <div style="font-size:2.8rem; font-weight:800; color:#3f234f; line-height:1.1;">{T['title']}</div>
    <div style="font-size:1.4rem; font-weight:600; color:#3f234f; opacity:0.8;">{T['subtitle']}</div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Input Form
with st.form("lumina_form"):
    name = st.text_input(T["name"])
    contact = st.text_input(T["contact"])
    
    col1, col2, col3 = st.columns(3)
    with col1: b_day = st.number_input(T["b_day"], 1, 31, 1)
    with col2: b_month_name = st.selectbox(T["b_month"], T["months"])
    with col3: b_year = st.number_input(T["b_year"], 2450, 2600, 2535)
    
    cat = st.selectbox(T["cat"], T["cats"])
    question = st.text_area(T["q"], placeholder=T["placeholder"])
    
    submitted = st.form_submit_button(T["btn"])

# Result Processing
if submitted:
    m_idx = T["months"].index(b_month_name) + 1
    lp = life_path_number(b_day, m_idx, b_year)
    be = reduce_number(b_day)
    
    # ดึงคำแปลตามภาษาที่เลือก (ตัวอย่างเลข 1 และ 11)
    msg = T.get(f"m{lp}", "Your unique energy is unfolding. / พลังงานของคุณกำลังเริ่มต้นการเดินทาง")
    
    st.balloons()
    st.markdown(f"### ✨ {T['name']}: {name}")
    
    st.markdown(f"""
    <div class="result-card">
        <p><b>{T['lp_label']}:</b> {lp}</p>
        <p><b>{T['be_label']}:</b> {be}</p>
        <hr>
        <p style="font-size:1.1rem; line-height:1.6;">{msg}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # --- E-BOOK PROMO HOOK ---
    st.markdown(f"""
    <div class="ebook-promo">
        <h3>{T['ebook_h']}</h3>
        <p>{T['ebook_d']}</p>
        <a href="https://lin.ee/jmI4z6G" style="text-decoration:none;">
            <div style="background:white; color:#ad1457; padding:12px 25px; border-radius:50px; display:inline-block; font-weight:bold; margin-top:15px; box-shadow: 0 4px 15px rgba(0,0,0,0.15);">
                {T['ebook_btn']}
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Google Sheets Integration (Optional - ใช้ URL เดิมของคุณได้)
    # requests.post("YOUR_GOOGLE_SCRIPT_URL", json={...})

# Footer
st.write("---")
st.markdown("<p style='text-align:center; font-size:0.8rem; opacity:0.5;'>© 2026 LUMINA SOUL | Spiritual Awakening Space</p>", unsafe_allow_html=True)
