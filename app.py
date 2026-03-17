import streamlit as st
import requests

# -----------------------------
# 1. Page Config (ต้องอยู่บรรทัดแรกๆ เสมอ)
# -----------------------------
st.set_page_config(
    page_title="LUMINA SOUL",
    page_icon="🔮",
    layout="centered"
)

# -----------------------------
# 2. ส่วนจัดการภาษา (แสดงบนหัวเว็บ)
# -----------------------------
if 'lang' not in st.session_state:
    st.session_state.lang = 'TH'

# สร้างคอลัมน์เพื่อให้ปุ่มสลับภาษาอยู่ชิดขวาบนหัวเว็บ (Mobile Friendly)
c_space, c1, c2 = st.columns([6, 1.2, 1.2]) 
with c1:
    if st.button("🇹🇭 TH"):
        st.session_state.lang = 'TH'
        st.rerun()
with c2:
    if st.button("🇺🇸 EN"):
        st.session_state.lang = 'EN'
        st.rerun()

lang = st.session_state.lang

# -----------------------------
# 3. คลังคำแปล (ใช้แสดงผลตามภาษาที่เลือก)
# -----------------------------
translations = {
    'TH': {
        'hero_title': "LUMINA SOUL",
        'hero_subtitle': "พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด",
        'welcome_msg': "ยินดีต้อนรับสู่พื้นที่แห่งการตื่นรู้และเยียวยาใจ",
        'name_label': "ชื่อ-นามสกุล",
        'contact_label': "ID Line (เพื่อรับผลสะท้อนพลังงาน)",
        'submit_btn': "🔮 ถอดรหัสพันธสัญญาจิตวิญญาณ"
    },
    'EN': {
        'hero_title': "LUMINA SOUL",
        'hero_subtitle': "Life Reflection | Decoding Birth Energy",
        'welcome_msg': "Welcome to a sacred space for awakening and healing",
        'name_label': "Full Name",
        'contact_label': "Line ID / WhatsApp / Email",
        'submit_btn': "🔮 Decode Your Soul Contract"
    }
}
L = translations[lang]

# -----------------------------
# 4. CSS (โค้ดเดิมของคุณจะเริ่มต่อจากตรงนี้)
# -----------------------------

# 3. กำหนดตัวแปรสั้นๆ เพื่อไปใช้ในหน้าเว็บ
lang = st.session_state.lang

# --- จบส่วนที่เพิ่ม จากนั้นจะเป็นบรรทัดที่ 13 (CSS) เดิมของคุณ ---

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    color: #2f1f38 !important;
}

.stApp {
    background-image: linear-gradient(135deg, #fdfcfb 0%, #e7d7fb 38%, #fdfbfb 68%, #fff2ec 100%);
    color: #2f1f38 !important;
}

p, span, div, label, li, small {
    color: #2f1f38 !important;
}

h1, h2, h3, h4, h5, h6 {
    margin: 0 !important;
}

div.stButton > button:first-child,
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(to right, #ba68c8 0%, #f06292 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 0.78rem 1.3rem !important;
    font-weight: 700 !important;
    font-size: 1.02rem !important;
    transition: 0.25s all ease !important;
    box-shadow: 0 6px 18px rgba(186, 104, 200, 0.28) !important;
    width: 100% !important;
    margin-top: 10px !important;
}

div.stButton > button:first-child:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(186, 104, 200, 0.38);
    color: white !important;
}

.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div {
    border-radius: 14px !important;
    border: 1px solid #d9cfe6 !important;
    background-color: rgba(255,255,255,0.94) !important;
    color: #2f1f38 !important;
    -webkit-text-fill-color: #2f1f38 !important;
}

input::placeholder,
textarea::placeholder {
    color: #8d7b9a !important;
    opacity: 1 !important;
    -webkit-text-fill-color: #8d7b9a !important;
}

label, .stMarkdown, .stTextInput label, .stNumberInput label, .stSelectbox label, .stTextArea label {
    color: #4a3557 !important;
}

div[data-baseweb="select"] * {
    color: #2f1f38 !important;
}

.stAlert {
    border-radius: 14px !important;
    border: none !important;
}

.hero-title-wrap {
    text-align: left;
    margin-top: 6px;
    margin-bottom: 12px;
}

.hero-brand {
    font-size: 3.0rem;
    font-weight: 800;
    line-height: 1.02;
    color: #3f234f !important;
    letter-spacing: -1px;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 2.0rem;
    font-weight: 700;
    line-height: 1.22;
    color: #3f234f !important;
}

.hero-card {
    background: rgba(255,255,255,0.58) !important;
    backdrop-filter: blur(6px);
    padding: 20px 18px !important;
    border-radius: 24px !important;
    box-shadow: 0 8px 24px rgba(126, 87, 194, 0.10) !important;
    margin-top: 10px !important;
    margin-bottom: 16px !important;
}

.glow-box {
    background: linear-gradient(135deg, rgba(214,228,255,0.95), rgba(234,223,255,0.95)) !important;
    border-radius: 18px !important;
    padding: 18px !important;
    box-shadow: 0 6px 20px rgba(126, 87, 194, 0.10) !important;
    margin-top: 8px !important;
    margin-bottom: 18px !important;
}

.result-card {
    background: rgba(255,255,255,0.85) !important;
    padding: 22px !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 28px rgba(126, 87, 194, 0.12) !important;
    margin-top: 10px !important;
    margin-bottom: 12px !important;
    color: #2f1f38 !important;
}

.mini-card {
    background: rgba(255,255,255,0.80) !important;
    padding: 16px !important;
    border-radius: 18px !important;
    box-shadow: 0 4px 16px rgba(126, 87, 194, 0.10) !important;
    margin-bottom: 12px !important;
    color: #2f1f38 !important;
}

.stat-card {
    background: rgba(255,255,255,0.78) !important;
    padding: 14px 12px !important;
    border-radius: 18px !important;
    text-align: center !important;
    box-shadow: 0 4px 14px rgba(126, 87, 194, 0.08) !important;
    margin-bottom: 10px !important;
    min-height: 120px;
}

.review-card {
    background: rgba(255,255,255,0.78) !important;
    padding: 16px !important;
    border-radius: 18px !important;
    box-shadow: 0 4px 14px rgba(126, 87, 194, 0.08) !important;
    margin-bottom: 12px !important;
}

.center-text {
    text-align: center !important;
    color: #5a3d5c !important;
}

.soft-note {
    color: #6b5876 !important;
    font-size: 0.95rem !important;
}

hr {
    border: none !important;
    border-top: 1px solid rgba(126, 87, 194, 0.15) !important;
}

* {
    -webkit-text-fill-color: inherit;
}

@media (max-width: 768px) {
    .hero-brand {
        font-size: 2.25rem !important;
        line-height: 1.02 !important;
        letter-spacing: -0.4px !important;
        margin-bottom: 12px !important;
    }

    .hero-subtitle {
        font-size: 1.15rem !important;
        line-height: 1.32 !important;
        font-weight: 700 !important;
    }

    .hero-card {
        padding: 16px 14px !important;
        border-radius: 20px !important;
    }

    .glow-box {
        padding: 15px !important;
        border-radius: 16px !important;
    }

    .result-card, .mini-card, .stat-card, .review-card {
        border-radius: 16px !important;
    }

    .soft-note {
        font-size: 0.92rem !important;
    }
}

@media (prefers-color-scheme: dark) {
    html, body, .stApp {
        color: #2f1f38 !important;
        background-color: transparent !important;
    }

    p, span, div, label, li, small {
        color: #2f1f38 !important;
    }

    .result-card, .mini-card, .stat-card, .review-card, .hero-card, .glow-box {
        color: #2f1f38 !important;
        background: rgba(255,255,255,0.88) !important;
    }

    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: rgba(255,255,255,0.95) !important;
        color: #2f1f38 !important;
        -webkit-text-fill-color: #2f1f38 !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #8d7b9a !important;
        -webkit-text-fill-color: #8d7b9a !important;
    }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Google Sheets endpoint
# -----------------------------
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzjNIr948oDKixAVajbf7me-kuABFyRopjKVmdx-PmMkYpFL8WbXAraMMJkPy2lMKLJNg/exec"

# -----------------------------
# Helpers
# -----------------------------
def reduce_number(n: int) -> int:
    while n > 9 and n not in (11, 22, 33):
        n = sum(int(d) for d in str(n))
    return n

def life_path_number(day: int, month_num: int, year_be: int) -> int:
    digits = f"{day:02d}{month_num:02d}{year_be}"
    total = sum(int(d) for d in digits)
    return reduce_number(total)

def birth_day_energy(day: int) -> int:
    return reduce_number(day)

# -----------------------------
# Meanings
# -----------------------------
life_path_meanings = {
    1: "คุณมีพลังของผู้เริ่มต้น กล้าตัดสินใจ ชอบสร้างเส้นทางของตัวเอง และไม่เหมาะกับการใช้ชีวิตแบบที่ต้องกดตัวตนไว้ตลอดเวลา",
    2: "คุณมีพลังของผู้ประสานใจ ลึกซึ้ง อ่อนโยน รับความรู้สึกคนอื่นได้ดี และมีพรสวรรค์ในการเชื่อมโยงหัวใจผู้คน",
    3: "คุณมีพลังแห่งการสื่อสาร ความคิดสร้างสรรค์ และเสน่ห์ตามธรรมชาติ เมื่อคุณกล้าแสดงออก โลกจะเริ่มตอบรับคุณชัดขึ้น",
    4: "คุณมีพลังแห่งความมั่นคง เป็นคนสร้างรากฐาน เก่งเรื่องระบบ ความรับผิดชอบ และการเปลี่ยนสิ่งเล็ก ๆ ให้กลายเป็นความมั่นคงระยะยาว",
    5: "คุณมีพลังแห่งอิสรภาพ การเปลี่ยนแปลง การเดินทาง และการเรียนรู้ผ่านประสบการณ์ตรง ชีวิตของคุณจะเติบโตมากเมื่อไม่ฝืนตัวเอง",
    6: "คุณมีพลังของผู้ดูแลและผู้เยียวยา หัวใจของคุณมีพลังในการโอบอุ้มคนอื่น แต่บทเรียนสำคัญคืออย่าลืมดูแลหัวใจตัวเองด้วย",
    7: "คุณมีพลังของนักค้นหาความจริง ชอบตั้งคำถาม ชอบเข้าใจชีวิตในระดับลึก และมักมีสายเชื่อมต่อกับโลกภายในอย่างชัดเจน",
    8: "คุณมีพลังด้านการบริหาร การเงิน ความสำเร็จ และการทำสิ่งใหญ่ให้เกิดขึ้นจริง หากใช้พลังอย่างสมดุล คุณมีศักยภาพสร้างความมั่นคงสูงมาก",
    9: "คุณมีพลังของผู้ให้ เมตตา เข้าใจมนุษย์ และมักมีบทบาทเกี่ยวข้องกับการช่วยเหลือหรือส่งต่อบางอย่างที่มีความหมายต่อผู้อื่น",
    11: "คุณมีพลังของผู้ตื่นรู้ สัญชาตญาณแรง รับรู้อะไรลึกกว่าคนทั่วไป และมีศักยภาพเป็นแสงนำทางให้ผู้คนรอบตัว",
    22: "คุณมีพลังของผู้สร้างสิ่งใหญ่ให้เป็นจริง มองภาพกว้างได้ดี และมีศักยภาพเปลี่ยนวิสัยทัศน์ให้เป็นสิ่งที่จับต้องได้",
    33: "คุณมีพลังของครูผู้เยียวยา เปี่ยมเมตตา อ่อนโยน และมีภารกิจในการส่งต่อความรัก ความเข้าใจ และแสงสว่างให้ผู้อื่น"
}

birth_day_meanings = {
    1: "วันเกิดของคุณสะท้อนพลังนักบุกเบิก คุณมักไม่ชอบเดินตามกรอบเดิม และมีแรงขับภายในที่ชัดเจน",
    2: "วันเกิดของคุณสะท้อนพลังความอ่อนโยน การรับรู้ และความสามารถในการเข้าใจความละเอียดอ่อนของผู้คน",
    3: "วันเกิดของคุณสะท้อนพลังความสดใส ความคิดสร้างสรรค์ และคำพูดที่มีอิทธิพลต่อความรู้สึกของคนรอบตัว",
    4: "วันเกิดของคุณสะท้อนพลังความมั่นคง ความรับผิดชอบ และความจริงจังต่อสิ่งที่คุณให้คุณค่า",
    5: "วันเกิดของคุณสะท้อนพลังการเปลี่ยนแปลง การเรียนรู้ ความคล่องตัว และความกล้าลองเส้นทางใหม่",
    6: "วันเกิดของคุณสะท้อนพลังผู้ดูแล ผู้เยียวยา และหัวใจที่ให้ความสำคัญกับความรักและความสัมพันธ์",
    7: "วันเกิดของคุณสะท้อนพลังนักสังเกต นักค้นหาความหมาย และคนที่มีโลกภายในลึกกว่าที่คนอื่นมองเห็น",
    8: "วันเกิดของคุณสะท้อนพลังความมุ่งมั่น อำนาจภายใน และศักยภาพในการสร้างผลลัพธ์ที่จับต้องได้",
    9: "วันเกิดของคุณสะท้อนพลังแห่งเมตตา ความเข้าใจมนุษย์ และการเรียนรู้เรื่องการปล่อยวาง",
    11: "วันเกิดของคุณสะท้อนพลังญาณรู้ ความละเอียดทางพลังงาน และการเชื่อมต่อกับสิ่งที่มองไม่เห็น",
    22: "วันเกิดของคุณสะท้อนพลังผู้สร้างสิ่งใหญ่ มีศักยภาพทำสิ่งที่ส่งผลต่อผู้คนจำนวนมาก",
    33: "วันเกิดของคุณสะท้อนพลังแห่งการเยียวยา การสอน และการรับใช้ด้วยหัวใจ"
}

month_names = [
    "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
    "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
]

month_map = {
    "มกราคม": 1,
    "กุมภาพันธ์": 2,
    "มีนาคม": 3,
    "เมษายน": 4,
    "พฤษภาคม": 5,
    "มิถุนายน": 6,
    "กรกฎาคม": 7,
    "สิงหาคม": 8,
    "กันยายน": 9,
    "ตุลาคม": 10,
    "พฤศจิกายน": 11,
    "ธันวาคม": 12
}

month_energy_meanings = {
    1: "พลังของการเริ่มต้นและความชัดเจน",
    2: "พลังของความสัมพันธ์และความอ่อนโยน",
    3: "พลังของการสื่อสารและความคิดสร้างสรรค์",
    4: "พลังของความมั่นคงและการวางรากฐาน",
    5: "พลังของการเปลี่ยนแปลงและอิสรภาพ",
    6: "พลังของความรัก การดูแล และการเยียวยา",
    7: "พลังของการค้นหาความหมายภายใน",
    8: "พลังของความสำเร็จและการผลักดันเป้าหมาย",
    9: "พลังของการให้ การปล่อยวาง และการเข้าใจชีวิต",
    10: "พลังของจุดเปลี่ยนและการเปิดวงจรใหม่",
    11: "พลังของญาณรู้และการตื่นรู้ภายใน",
    12: "พลังของการปิดวงจรเก่าเพื่อเตรียมสู่การเริ่มต้นใหม่"
}

category_advice = {
    "ความรักและความสัมพันธ์": "นี่คือคำสะท้อนพลังงานเบื้องต้น หากอยากอ่านลึกเฉพาะความสัมพันธ์ของคุณแบบเจาะรายละเอียด สามารถทักเข้ามาได้",
    "การงานและเส้นทางชีวิต": "นี่คือคำสะท้อนเบื้องต้นของเส้นทางชีวิต หากต้องการอ่านลึกเรื่องงานและจังหวะชีวิตเฉพาะตัว สามารถทักเข้ามาได้",
    "โชคลาภและกระแสการเงิน": "นี่คือคำสะท้อนเบื้องต้นของกระแสการเงิน หากต้องการอ่านลึกเฉพาะตัวเรื่องเงินและโอกาส สามารถทักเข้ามาได้"
}

# -----------------------------
# Generate content
# -----------------------------
def generate_main_result(category: str, life_number: int, birth_energy: int, question_text: str) -> str:
    if category == "ความรักและความสัมพันธ์":
        if life_number in [2, 6, 9, 11, 33]:
            return "พลังความรักของคุณเป็นพลังที่ลึกและจริงใจมาก คุณไม่ได้ต้องการแค่ความสัมพันธ์ แต่ต้องการความเชื่อมโยงที่สัมผัสถึงหัวใจจริง ๆ ช่วงนี้บทเรียนสำคัญคือการแยกให้ออกว่าอะไรคือความรัก และอะไรคือการยอมทนเพราะกลัวเสียใครบางคนไป"
        elif life_number in [1, 5, 8, 22]:
            return "ความรักของคุณมักเชื่อมโยงกับบทเรียนเรื่องคุณค่าในตัวเองและขอบเขตที่ชัดเจน คุณมีเสน่ห์และแรงดึงดูดสูง แต่หัวใจจะสงบได้จริงเมื่อคุณเลือกคนที่เคารพตัวตนของคุณ ไม่ใช่คนที่ทำให้คุณต้องเล็กลง"
        return "หัวใจของคุณกำลังเรียนรู้บางอย่างผ่านความสัมพันธ์ที่ผ่านมา สิ่งที่เกิดขึ้นไม่ได้มาเพื่อทำร้ายคุณ แต่มาเพื่อสอนให้คุณกลับมาเข้าใจความต้องการที่แท้จริงของหัวใจ และเปิดพื้นที่ให้ความสัมพันธ์ที่เหมาะสมกว่าเข้ามา"

    if category == "การงานและเส้นทางชีวิต":
        if life_number in [1, 4, 8, 22]:
            return "เส้นทางการงานของคุณไม่ได้ธรรมดา คุณมีพลังในการสร้างบางอย่างให้เกิดขึ้นจริง ช่วงนี้อาจเหมือนถูกกดดันหรือถูกบีบให้ตัดสินใจ แต่แท้จริงแล้วชีวิตกำลังผลักคุณออกจากทางเดิม เพื่อพาไปสู่บทบาทที่ใหญ่และชัดเจนกว่าเดิม"
        elif life_number in [3, 5, 7, 11]:
            return "เส้นทางชีวิตของคุณเด่นเรื่องการค้นหา การสื่อสาร และการใช้ตัวตนที่แท้จริงเป็นเครื่องนำทาง งานที่เหมาะกับคุณคือสิ่งที่ทำแล้วใจไม่ฝืน และยิ่งคุณฟังสัญญาณจากข้างในมากเท่าไร เส้นทางจะยิ่งเปิดชัดขึ้น"
        return "การงานในช่วงนี้อาจดูเหมือนยังไม่ชัด แต่จริง ๆ แล้วคุณกำลังอยู่ในช่วงจัดระเบียบชีวิตใหม่ เพื่อให้สิ่งที่สอดคล้องกับหัวใจมากกว่าเดิมเข้ามาแทนที่ ชีวิตไม่ได้พาคุณหลงทาง มันกำลังพาคุณกลับเข้าหาตัวเอง"

    if life_number in [8, 4, 22]:
        return "พลังการเงินของคุณมีศักยภาพสูงมาก แต่จะเปิดเต็มที่เมื่อคุณจัดระบบความคิดและการตัดสินใจให้ชัดขึ้น เงินของคุณไม่ได้มาเพราะโชคอย่างเดียว แต่มาจากความสามารถในการสร้างมูลค่าและยืนระยะ"
    elif life_number in [5, 3, 1]:
        return "กระแสการเงินของคุณสัมพันธ์กับความกล้าลอง ความคิดสร้างสรรค์ และการขยับตัว หากช่วงนี้เงินนิ่งหรือช้า อาจไม่ใช่เพราะคุณไม่มีโชค แต่เป็นเพราะคุณกำลังต้องเปลี่ยนวิธีคิดหรือวิธีเปิดรับโอกาสใหม่"
    return "การเงินของคุณเชื่อมโยงกับพลังใจอย่างมาก เมื่อใจแบกความกังวลมากเกินไป กระแสทรัพย์จะติดขัดง่าย ช่วงนี้จึงเป็นจังหวะสำคัญในการเคลียร์ความกลัว ความไม่มั่นใจ และกลับมาเชื่อในคุณค่าของตัวเองอีกครั้ง"

def generate_soul_message(name: str, category: str, life_number: int, birth_energy: int, month_num: int) -> str:
    month_energy = month_energy_meanings.get(month_num, "พลังเฉพาะของช่วงเวลาที่คุณเกิด")
    return f"""
{name} เป็นคนที่มีพลังภายในเฉพาะตัว และไม่ได้เดินทางมาถึงจุดนี้โดยบังเอิญ

เลขเส้นทางชีวิตของคุณสะท้อนว่า ชีวิตกำลังสอนให้คุณกลับมาใช้พลังแท้ของตัวเองอย่างมีสติ
ขณะที่พลังวันเกิดของคุณบอกว่า ลึกลงไปแล้วคุณมีศักยภาพบางอย่างที่พร้อมเติบโต หากคุณเลิกสงสัยในคุณค่าของตัวเอง

พลังเดือนเกิดของคุณยังสะท้อนถึง{month_energy}
จึงเป็นไปได้ว่า ชีวิตของคุณไม่ได้มาเพื่ออยู่แบบเดิมไปเรื่อย ๆ
แต่มาเพื่อเรียนรู้ เติบโต และค่อย ๆ เข้าใกล้เส้นทางที่สอดคล้องกับจิตวิญญาณมากขึ้น

นี่คือการอ่านพลังงานเบื้องต้นเท่านั้น
หากต้องการอ่านเชิงลึกแบบเฉพาะตัวในเรื่อง{category} สามารถทักมาพูดคุยต่อได้
""".strip()

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero-title-wrap">
    <div class="hero-brand">🔮 LUMINA SOUL</div>
    <div class="hero-subtitle">พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด</div>
</div>
""", unsafe_allow_html=True)

st.write("---")

st.markdown(
    """
    <div class="hero-card">
        <p class='center-text' style='font-size:1.05rem; margin-bottom:8px;'>
        ยินดีต้อนรับสู่พื้นที่แห่งการตื่นรู้และเยียวยาใจ ผ่านสัญญาณจาก Oversoul และรหัสลับวันเกิด เพื่อปลดล็อกศักยภาพในตัวคุณ
        </p>
        <p class='center-text soft-note' style='margin-bottom:0;'>
        บางคำตอบในชีวิต อาจเริ่มต้นจากการเข้าใจพลังงานของตัวเอง
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="glow-box">
        <p style="margin:0; color:#3576c5 !important; font-weight:600;">
        ✨ รหัสลับจิตวิญญาณ... เมื่อคุณเริ่มเข้าใจพลังงานตัวเอง ประตูสู่ความเป็นไปได้ใหม่ ๆ จะเปิดออก
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Trust section
# -----------------------------
st.markdown("### 🔑 ทำไมหลายคนถึงเริ่มจากการถอดรหัสพลังงานชีวิต")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size:1.15rem; font-weight:700; color:#8e24aa;">เข้าใจตัวเอง</div>
        <div class="soft-note">เห็นจุดแข็ง จุดเปลี่ยน และบทเรียนที่กำลังเกิดขึ้น</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size:1.15rem; font-weight:700; color:#8e24aa;">สะท้อนชีวิต</div>
        <div class="soft-note">ช่วยมองความรัก งาน และการเงินในมุมที่ลึกขึ้น</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size:1.15rem; font-weight:700; color:#8e24aa;">ต่อยอดได้จริง</div>
        <div class="soft-note">หากรู้สึกว่าตรง คุณสามารถอ่านเชิงลึกต่อได้ทันที</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### 🌕 รีวิวความรู้สึกจากผู้ที่เคยสะท้อนพลังงาน💫")

r1, r2 = st.columns(2)
with r1:
    st.markdown("""
    <div class="review-card">
        <div style="font-weight:700; color:#7b1fa2;">“อ่านแล้วเหมือนมีใครอธิบายชีวิตเราได้”</div>
        <div class="soft-note">หลายอย่างตรงแบบรู้สึกได้ว่าไม่ใช่แค่คำทั่วไป</div>
    </div>
    """, unsafe_allow_html=True)

with r2:
    st.markdown("""
    <div class="review-card">
        <div style="font-weight:700; color:#7b1fa2;">“ช่วยให้เข้าใจช่วงชีวิตที่กำลังเปลี่ยน”</div>
        <div class="soft-note">ยิ่งอ่านยิ่งเห็นภาพว่าบางอย่างที่เกิดขึ้นมีเหตุผลของมัน</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### 🔮 ตัวอย่างสิ่งที่คุณอาจค้นพบ")
st.markdown("""
<div class="mini-card">
• ทำไมบางความสัมพันธ์ถึงเกิดซ้ำในชีวิต<br>
• ทำไมช่วงนี้งานหรือการเงินถึงติดบางจุด<br>
• พลังหลักที่ซ่อนอยู่ในตัวคุณ<br>
• เส้นทางชีวิตที่กำลังเรียกให้คุณเปลี่ยนแปลง
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Form
# -----------------------------
with st.form("lumina_single_page_form"):
    name = st.text_input("ชื่อ-นามสกุล")
    contact = st.text_input("ID Line (เพื่อรับผลสะท้อนพลังงานและสิทธิ์อ่านเชิงลึก)")

    col1, col2, col3 = st.columns(3)
    with col1:
        birth_day = st.number_input("วันที่เกิด", min_value=1, max_value=31, value=1, step=1)
    with col2:
        birth_month_name = st.selectbox("เดือนเกิด", month_names)
    with col3:
        birth_year = st.number_input("ปี พ.ศ. เกิด", min_value=2450, max_value=2600, value=2535, step=1)

    category = st.selectbox(
        "ด้านที่คุณต้องการรับพลังงานนำทางในวันนี้:",
        ["ความรักและความสัมพันธ์", "การงานและเส้นทางชีวิต", "โชคลาภและกระแสการเงิน"]
    )

    st.markdown("**⭐️ เรื่องที่คุณกังวลใจที่สุดในตอนนี้คืออะไร?**")
    question = st.text_area("", placeholder="แชร์รายละเอียดเรื่องที่ติดค้างในใจแบบสั้น ๆ", height=120)

    submitted = st.form_submit_button("🔮 ถอดรหัสพันธสัญญาจิตวิญญาณ")

# -----------------------------
# Processing
# -----------------------------
if submitted:
    name_clean = name.strip()
    contact_clean = contact.strip()
    question_clean = question.strip()

    if len(name_clean) < 2:
        st.error("กรุณากรอกชื่อ-นามสกุลให้ครบถ้วน")
    elif len(contact_clean) < 3:
        st.error("กรุณากรอก ID Line ให้ถูกต้อง")
    elif len(question_clean) < 5:
        st.error("กรุณาพิมพ์เรื่องที่กังวลใจสั้น ๆ เพื่อให้คำสะท้อนเหมาะกับคุณมากขึ้น")
    else:
        month_num = month_map[birth_month_name]
        day_num = int(birth_day)
        year_num = int(birth_year)

        life_number = life_path_number(day_num, month_num, year_num)
        birth_energy = birth_day_energy(day_num)

        life_meaning = life_path_meanings.get(
            life_number,
            "คุณมีพลังเฉพาะตัวที่น่าสนใจ และกำลังอยู่ในช่วงเรียนรู้พลังแท้ของตัวเอง"
        )
        birth_meaning = birth_day_meanings.get(
            birth_energy,
            "วันเกิดของคุณสะท้อนพลังเฉพาะตัวที่ควรค่าแก่การทำความเข้าใจ"
        )

        main_result = generate_main_result(category, life_number, birth_energy, question_clean)
        soul_message = generate_soul_message(name_clean, category, life_number, birth_energy, month_num)
        advice = category_advice.get(category, "หากอยากอ่านลึกเฉพาะตัว สามารถทักเข้ามาได้")

        birthdate_text = f"{day_num} {birth_month_name} {year_num}"

        try:
            requests.post(
                GOOGLE_SCRIPT_URL,
                json={
                    "name": name_clean,
                    "line_id": contact_clean,
                    "birthdate": birthdate_text,
                    "birth_day": day_num,
                    "birth_month": birth_month_name,
                    "birth_year_be": year_num,
                    "life_path_number": life_number,
                    "birth_day_energy": birth_energy,
                    "category": category,
                    "question": question_clean,
                    "result": main_result,
                    "life_meaning": life_meaning,
                    "birth_meaning": birth_meaning,
                    "soul_message": soul_message,
                    "advice": advice
                },
                timeout=15
            )
        except Exception:
            pass

        st.balloons()
        st.write("---")
        st.success(f"### 🌟 ผลสะท้อนพลังงานเบื้องต้น: คุณ {name_clean}")

        st.markdown(
            f"""
            <div class="result-card">
                <h4 style="color:#7b1fa2; margin-top:0;">🔢 เลขพลังงานของคุณ</h4>
                <p><b>เลขเส้นทางชีวิต:</b> {life_number}</p>
                <p><b>เลขพลังงานวันเกิด:</b> {birth_energy}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="mini-card">
                <h4 style="color:#8e24aa; margin-top:0;">🌙 ความหมายพลังชีวิต</h4>
                <p>{life_meaning}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="mini-card">
                <h4 style="color:#8e24aa; margin-top:0;">💎 พลังงานจากวันเกิด</h4>
                <p>{birth_meaning}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="result-card">
                <h4 style="color:#ad1457; margin-top:0;">🔮 คำสะท้อนในด้าน{category}</h4>
                <p>{main_result}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(f"💡 {advice}")

        st.markdown(
            f"""
            <div class="mini-card">
                <h4 style="color:#6a1b9a; margin-top:0;">✨ ข้อความจาก Lumina Soul</h4>
                <p>{soul_message}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### ✨ ข้อความจาก Lumina Soul")
        st.markdown("""
สิ่งที่คุณเห็นข้างต้น เป็นเพียง **การสะท้อนพลังงานเบื้องต้นจากวันเกิดของคุณ**

หลายครั้ง รหัสชีวิตของคนเรา  
ไม่ได้เปิดเผยทั้งหมดในครั้งเดียว

ยังมีรายละเอียดที่ลึกกว่า เช่น

• บทเรียนชีวิตที่เกิดซ้ำ  
• ความสัมพันธ์ที่เข้ามาในชีวิต  
• จังหวะการเปลี่ยนแปลงของเส้นทางชีวิต  

หากคุณรู้สึกว่า **บางส่วนของข้อความนี้สะท้อนชีวิตคุณจริง**

คุณสามารถทักเข้ามาเพื่อรับ  
**การอ่านพลังงานเชิงลึกแบบเฉพาะตัว**

Lumina Soul จะช่วยสะท้อนสิ่งที่ชีวิตของคุณกำลังพยายามบอกคุณอยู่ ✨
""")

        st.link_button("✳️👉 คุยกับที่ปรึกษา LUMINA SOUL", "https://lin.ee/jmI4z6G")

# -----------------------------
# Footer
# -----------------------------
st.write("---")
st.markdown(
    "<p style='text-align: center; font-size: 0.82rem; color: #888;'>© 2026 LUMINA SOUL | พื้นที่สะท้อนชีวิตและการตื่นรู้</p>",
    unsafe_allow_html=True
)
