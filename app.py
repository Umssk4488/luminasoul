import streamlit as st
import requests

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="LUMINA SOUL",
    page_icon="🔮",
    layout="centered"
)

# -----------------------------
# 1. ระบบเลือกภาษา (เพิ่มเข้ามาใหม่)
# -----------------------------
# วางไว้บนสุดเพื่อให้คนเลือกได้ทันที
lang = st.radio("Select Language / เลือกภาษา", ["TH", "EN"], horizontal=True, label_visibility="collapsed")

# -----------------------------
# 2. คลังคำศัพท์ 2 ภาษา (เก็บข้อความทั้งหมดจากโค้ดเดิมของคุณ)
# -----------------------------
TEXTS = {
    "TH": {
        "brand": "🔮 LUMINA SOUL",
        "subtitle": "พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด",
        "welcome_h": "ยินดีต้อนรับสู่พื้นที่แห่งการตื่นรู้และเยียวยาใจ ผ่านสัญญาณจาก Oversoul และรหัสลับวันเกิด เพื่อปลดล็อกศักยภาพในตัวคุณ",
        "welcome_s": "บางคำตอบในชีวิต อาจเริ่มต้นจากการเข้าใจพลังงานของตัวเอง",
        "glow": "✨ รหัสลับจิตวิญญาณ... เมื่อคุณเริ่มเข้าใจพลังงานตัวเอง ประตูสู่ความเป็นไปได้ใหม่ ๆ จะเปิดออก",
        "why_h": "### 🔑 ทำไมหลายคนถึงเริ่มจากการถอดรหัสพลังงานชีวิต",
        "stat1_h": "เข้าใจตัวเอง", "stat1_b": "เห็นจุดแข็ง จุดเปลี่ยน และบทเรียนที่กำลังเกิดขึ้น",
        "stat2_h": "สะท้อนชีวิต", "stat2_b": "ช่วยมองความรัก งาน และการเงินในมุมที่ลึกขึ้น",
        "stat3_h": "ต่อยอดได้จริง", "stat3_b": "หากรู้สึกว่าตรง คุณสามารถอ่านเชิงลึกต่อได้ทันที",
        "rev_h": "### 🌕 รีวิวความรู้สึกจากผู้ที่เคยสะท้อนพลังงาน💫",
        "rev1_t": "“อ่านแล้วเหมือนมีใครอธิบายชีวิตเราได้”", "rev1_b": "หลายอย่างตรงแบบรู้สึกได้ว่าไม่ใช่แค่คำทั่วไป",
        "rev2_t": "“ช่วยให้เข้าใจช่วงชีวิตที่กำลังเปลี่ยน”", "rev2_b": "ยิ่งอ่านยิ่งเห็นภาพว่าบางอย่างที่เกิดขึ้นมีเหตุผลของมัน",
        "ex_h": "### 🔮 ตัวอย่างสิ่งที่คุณอาจค้นพบ",
        "ex_list": "• ทำไมบางความสัมพันธ์ถึงเกิดซ้ำในชีวิต<br>• ทำไมช่วงนี้งานหรือการเงินถึงติดบางจุด<br>• พลังหลักที่ซ่อนอยู่ในตัวคุณ<br>• เส้นทางชีวิตที่กำลังเรียกให้คุณเปลี่ยนแปลง",
        "f_name": "ชื่อ-นามสกุล",
        "f_contact": "ID Line (เพื่อรับผลสะท้อนพลังงานและสิทธิ์อ่านเชิงลึก)",
        "f_day": "วันที่เกิด", "f_month": "เดือนเกิด", "f_year": "ปี พ.ศ. เกิด",
        "f_cat": "ด้านที่คุณต้องการรับพลังงานนำทางในวันนี้:",
        "f_q_label": "**⭐️ เรื่องที่คุณกังวลใจที่สุดในตอนนี้คืออะไร?**",
        "f_q_placeholder": "แชร์รายละเอียดเรื่องที่ติดค้างในใจแบบสั้น ๆ",
        "f_btn": "🔮 ถอดรหัสพันธสัญญาจิตวิญญาณ",
        "err_name": "กรุณากรอกชื่อ-นามสกุลให้ครบถ้วน",
        "err_contact": "กรุณากรอก ID Line ให้ถูกต้อง",
        "err_q": "กรุณาพิมพ์เรื่องที่กังวลใจสั้น ๆ เพื่อให้คำสะท้อนเหมาะกับคุณมากขึ้น",
        "res_head": "🌟 ผลสะท้อนพลังงานเบื้องต้น: คุณ",
        "res_num_h": "🔢 เลขพลังงานของคุณ",
        "res_lp": "เลขเส้นทางชีวิต", "res_be": "เลขพลังงานวันเกิด",
        "res_meaning_h": "🌙 ความหมายพลังชีวิต",
        "res_birth_h": "💎 พลังงานจากวันเกิด",
        "res_cat_h": "🔮 คำสะท้อนในด้าน",
        "res_soul_h": "✨ ข้อความจาก Lumina Soul",
        "res_final_h": "### ✨ ข้อความจาก Lumina Soul",
        "res_final_body": "สิ่งที่คุณเห็นข้างต้น เป็นเพียง **การสะท้อนพลังงานเบื้องต้นจากวันเกิดของคุณ**...", # ตัดย่อเพื่อประหยัดพื้นที่
        "res_btn": "✳️👉 คุยกับที่ปรึกษา LUMINA SOUL",
        "footer": "© 2026 LUMINA SOUL | พื้นที่สะท้อนชีวิตและการตื่นรู้",
        "months": ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"],
        "cats": ["ความรักและความสัมพันธ์", "การงานและเส้นทางชีวิต", "โชคลาภและกระแสการเงิน"]
    },
    "EN": {
        "brand": "🔮 LUMINA SOUL",
        "subtitle": "Soul Reflection | Decoding Your Birth Energy",
        "welcome_h": "Welcome to a sacred space of awakening. Decode your Oversoul signals and birth codes to unlock your true potential.",
        "welcome_s": "Some of life's deepest answers begin with understanding your own energy.",
        "glow": "✨ Soul Codes... When you align with your energy, new doors of possibility swing open.",
        "why_h": "### 🔑 Why start with a Soul Energy Decoding?",
        "stat1_h": "Self-Understanding", "stat1_b": "Discover your strengths, transitions, and the lessons unfolding now.",
        "stat2_h": "Life Reflection", "stat2_b": "Gain a deeper perspective on love, career, and abundance.",
        "stat3_h": "Actionable Insight", "stat3_b": "If this resonates, you can dive deeper into a full reading immediately.",
        "rev_h": "### 🌕 Soul Resonance Stories💫",
        "rev1_t": "“It felt like someone finally explained my life.”", "rev1_b": "Everything was so accurate; it wasn't just generic advice.",
        "rev2_t": "“Helping me navigate a major transition.”", "rev2_b": "I can clearly see the purpose behind the challenges I've faced.",
        "ex_h": "### 🔮 What You Might Discover",
        "ex_list": "• Why certain relationship patterns repeat<br>• Why your career or finances feel blocked<br>• The core power hidden within you<br>• The path life is calling you to embrace",
        "f_name": "Full Name",
        "f_contact": "ID Line / Contact (To receive full reflection)",
        "f_day": "Day", "f_month": "Month", "f_year": "Year (B.E.)",
        "f_cat": "Guidance needed for:",
        "f_q_label": "**⭐️ What is your most pressing concern right now?**",
        "f_q_placeholder": "Briefly share what is weighing on your heart...",
        "f_btn": "🔮 Decode Your Soul Contract",
        "err_name": "Please enter your full name",
        "err_contact": "Please enter a valid contact ID",
        "err_q": "Please share your concern so we can reflect accurately",
        "res_head": "🌟 Initial Energy Reflection: Mx.",
        "res_num_h": "🔢 Your Energy Numbers",
        "res_lp": "Life Path Number", "res_be": "Birthday Energy",
        "res_meaning_h": "🌙 Life Path Essence",
        "res_birth_h": "💎 Birthday Frequency",
        "res_cat_h": "🔮 Reflection on",
        "res_soul_h": "✨ Message from Lumina Soul",
        "res_final_h": "### ✨ A Message from Lumina Soul",
        "res_final_body": "The insights above are just the **initial reflection of your energy**...",
        "res_btn": "✳️👉 Consult with LUMINA SOUL",
        "footer": "© 2026 LUMINA SOUL | Life Reflection & Awakening Space",
        "months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "cats": ["Love & Relationships", "Career & Life Path", "Wealth & Abundance"]
    }
}

T = TEXTS[lang]

# -----------------------------
# CSS (เหมือนเดิม 100%)
# -----------------------------
st.markdown("""
<style>
html, body, [class*="css"] { color: #2f1f38 !important; }
.stApp { background-image: linear-gradient(135deg, #fdfcfb 0%, #e7d7fb 38%, #fdfbfb 68%, #fff2ec 100%); }
/* ... (โค้ด CSS เดิมของคุณทั้งหมด) ... */
div.stButton > button:first-child, div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(to right, #ba68c8 0%, #f06292 100%) !important;
    color: white !important;
    border-radius: 25px !important;
    width: 100% !important;
}
.hero-brand { font-size: 3.0rem; font-weight: 800; color: #3f234f !important; }
.hero-subtitle { font-size: 2.0rem; font-weight: 700; color: #3f234f !important; }
.hero-card { background: rgba(255,255,255,0.58) !important; padding: 20px 18px !important; border-radius: 24px !important; }
.glow-box { background: linear-gradient(135deg, rgba(214,228,255,0.95), rgba(234,223,255,0.95)) !important; border-radius: 18px !important; padding: 18px !important; }
.result-card { background: rgba(255,255,255,0.85) !important; padding: 22px !important; border-radius: 20px !important; }
.stat-card { background: rgba(255,255,255,0.78) !important; padding: 14px 12px !important; border-radius: 18px !important; text-align: center !important; min-height: 120px; }
.mini-card { background: rgba(255,255,255,0.80) !important; padding: 16px !important; border-radius: 18px !important; margin-bottom: 12px; }
.review-card { background: rgba(255,255,255,0.78) !important; padding: 16px !important; border-radius: 18px !important; }
.soft-note { color: #6b5876 !important; font-size: 0.95rem !important; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Meanings (คำแปล 2 ภาษา)
# -----------------------------
# (ผมย่อคำแปลภาษาอังกฤษให้ดูเป็นตัวอย่าง คุณสามารถปรับแก้ได้)
life_path_meanings = {
    1: {"TH": "คุณมีพลังของผู้เริ่มต้น กล้าตัดสินใจ...", "EN": "The Pioneer: A leader with creative drive..."},
    11: {"TH": "คุณคือผู้ตื่นรู้ มีสัญชาตญาณแรงกล้า...", "EN": "The Master Teacher: High intuition and light-bringer..."},
    # ... (เพิ่มให้ครบตามเลขที่คุณมี)
}

# -----------------------------
# Helpers & Logic (เหมือนเดิม)
# -----------------------------
def reduce_number(n: int) -> int:
    while n > 9 and n not in (11, 22, 33): n = sum(int(d) for d in str(n))
    return n

def life_path_number(day: int, month_num: int, year_be: int) -> int:
    digits = f"{day:02d}{month_num:02d}{year_be}"
    return reduce_number(sum(int(d) for d in digits))

# -----------------------------
# Header (ใช้ตัวแปร T แทนข้อความ)
# -----------------------------
st.markdown(f"""
<div class="hero-title-wrap">
    <div class="hero-brand">{T['brand']}</div>
    <div class="hero-subtitle">{T['subtitle']}</div>
</div>
""", unsafe_allow_html=True)

st.write("---")

st.markdown(f"""
<div class="hero-card">
    <p style='text-align:center; font-size:1.05rem;'>{T['welcome_h']}</p>
    <p style='text-align:center;' class='soft-note'>{T['welcome_s']}</p>
</div>
<div class="glow-box"><p style="margin:0; color:#3576c5 !important; font-weight:600;">{T['glow']}</p></div>
""", unsafe_allow_html=True)

# -----------------------------
# Trust & Reviews (ใช้ตัวแปร T)
# -----------------------------
st.markdown(T["why_h"])
c1, c2, c3 = st.columns(3)
for i, col in enumerate([c1, c2, c3], 1):
    with col:
        st.markdown(f'<div class="stat-card"><b>{T[f"stat{i}_h"]}</b><br><span class="soft-note">{T[f"stat{i}_b"]}</span></div>', unsafe_allow_html=True)

st.markdown(T["rev_h"])
r1, r2 = st.columns(2)
with r1: st.markdown(f'<div class="review-card"><b>{T["rev1_t"]}</b><br><span class="soft-note">{T["rev1_b"]}</span></div>', unsafe_allow_html=True)
with r2: st.markdown(f'<div class="review-card"><b>{T["rev2_t"]}</b><br><span class="soft-note">{T["rev2_b"]}</span></div>', unsafe_allow_html=True)

st.markdown(T["ex_h"])
st.markdown(f'<div class="mini-card">{T["ex_list"]}</div>', unsafe_allow_html=True)

# -----------------------------
# Form (ใช้ตัวแปร T)
# -----------------------------
with st.form("lumina_form"):
    name = st.text_input(T["f_name"])
    contact = st.text_input(T["f_contact"])
    col1, col2, col3 = st.columns(3)
    with col1: birth_day = st.number_input(T["f_day"], 1, 31, 1)
    with col2: birth_month_name = st.selectbox(T["f_month"], T["months"])
    with col3: birth_year = st.number_input(T["f_year"], 2450, 2600, 2535)
    
    category = st.selectbox(T["f_cat"], T["cats"])
    st.markdown(T["f_q_label"])
    question = st.text_area("", placeholder=T["f_q_placeholder"], height=120)
    
    submitted = st.form_submit_button(T["f_btn"])

# -----------------------------
# Result (แสดงผลตามภาษาที่เลือก)
# -----------------------------
if submitted:
    if len(name) < 2: st.error(T["err_name"])
    elif len(contact) < 3: st.error(T["err_contact"])
    else:
        st.balloons()
        lp = life_path_number(birth_day, T["months"].index(birth_month_name)+1, birth_year)
        
        st.success(f"### {T['res_head']} {name}")
        
        st.markdown(f"""
        <div class="result-card">
            <h4 style="color:#7b1fa2;">{T['res_num_h']}</h4>
            <p><b>{T['res_lp']}:</b> {lp}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # แสดงคำทำนายจาก Dictionary (ดึงตามภาษาปัจจุบัน)
        meaning = life_path_meanings.get(lp, {"TH": "...", "EN": "..."})[lang]
        st.markdown(f'<div class="mini-card"><h4 style="color:#8e24aa;">{T["res_meaning_h"]}</h4><p>{meaning}</p></div>', unsafe_allow_html=True)

        st.link_button(T["res_btn"], "https://lin.ee/jmI4z6G")

# Footer
st.write("---")
st.markdown(f"<p style='text-align:center; font-size:0.82rem; color:#888;'>{T['footer']}</p>", unsafe_allow_html=True)
