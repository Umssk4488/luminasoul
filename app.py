import streamlit as st
import requests

# --- 🎨 1. ตั้งค่าดีไซน์ Premium Lavender & Pink Pastel (Gradient) ---
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    /* พื้นหลังไล่สีนุ่มนวล */
    .stApp {
        background-image: linear-gradient(135deg, #fdfcfb 0%, #e2d1f9 40%, #fdfbfb 70%, #fff1eb 100%);
    }
    /* ปรับแต่ง Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.4);
        border-right: 1px solid rgba(255, 255, 255, 0.5);
    }
    /* หัวข้อหลัก */
    h1 {
        color: #4a148c;
        font-family: 'Sarabun', sans-serif;
        text-align: center;
        font-weight: 800;
    }
    /* ปุ่มกด Gradient */
    div.stButton > button:first-child {
        background: linear-gradient(to right, #ba68c8 0%, #f06292 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.7rem 2.5rem;
        font-weight: bold;
        width: 100%;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(186, 104, 200, 0.3);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(186, 104, 200, 0.4);
    }
    /* ปรับแต่งกล่อง Input */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea {
        border-radius: 12px !important;
        background-color: rgba(255,255,255,0.8);
    }
    </style>
    """, unsafe_allow_html=True)

# 📍 ลิงก์เชื่อมต่อ Google Sheets (คงเดิมห้ามเปลี่ยน)
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzjNIr948oDKixAVajbf7me-kuABFyRopjKVmdx-PmMkYpFL8WbXAraMMJkPy2lMKLJNg/exec"

# --- 📂 2. สร้างแถบเมนู (Sidebar) ---
with st.sidebar:
    st.title("MENU")
    page = st.radio("ไปที่หน้า:", ["🔮 ถอดรหัสพลังงาน", "💖 เกี่ยวกับ LUMINA SOUL", "📲 ติดต่อเรา"])
    st.markdown("---")
    st.write("© 2026 LUMINA SOUL")

# --- 🔮 หน้าที่ 1: ถอดรหัสพลังงาน (หน้าหลัก) ---
if page == "🔮 ถอดรหัสพลังงาน":
    st.title("🔮 LUMINA SOUL")
    st.markdown("<h3 style='text-align: center; color: #7e57c2;'>พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด</h3>", unsafe_allow_html=True)
    
    with st.form("main_form"):
        st.info("✨ รหัสลับจิตวิญญาณ... เมื่อคุณเริ่มเข้าใจพลังงานตัวเอง ประตูสู่ความเป็นไปได้ใหม่ๆ จะเปิดออก")
        
        name = st.text_input("ชื่อ-นามสกุล")
        contact = st.text_input("ID Line (เพื่อรับสิทธิ์วิเคราะห์เชิงลึกฟรี)")
        
        col1, col2, col3 = st.columns(3)
        with col1: date = st.number_input("วันที่เกิด", 1, 31, 1)
        with col2: month = st.selectbox("เดือนเกิด", ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"])
        with col3: year = st.number_input("ปี พ.ศ. เกิด", 2450, 2600, 2535)
        
        category = st.selectbox("ด้านที่ต้องการรับพลังงานนำทาง:", ["ความรักและความสัมพันธ์", "การงานและเส้นทางชีวิต", "โชคลาภและกระแสการเงิน"])
        question = st.text_area("✨ เรื่องที่กังวลใจที่สุดตอนนี้:", placeholder="แชร์รายละเอียดเรื่องที่ติดค้างในใจ..")
        
        submitted = st.form_submit_button("🔮 ถอดรหัสพันธสัญญาจิตวิญญาณ")

    if submitted:
        if len(name.strip()) < 2 or len(contact.strip()) < 3 or len(question.strip()) < 5:
            st.error("⚠️ รบกวนระบุข้อมูลให้ครบถ้วน เพื่อให้เราสื่อสารกับพลังงานของคุณได้แม่นยำนะคะ")
        else:
            st.balloons()
            idx = (date % 3)
            if category == "ความรักและความสัมพันธ์":
                res = ["หัวใจของคุณมีบารมีสูงนัก ความเจ็บปวดที่พบเจอคือการ 'คัดกรอง' พลังงานที่ไม่คู่ควรออกไป...", "อย่าเสียดายรักที่จากไป เพราะรหัสวันเกิดคุณบอกว่ามันคือการถอนพันธนาการเก่า...", "ความรักที่คุณตามหาไม่ได้อยู่ไกลตัว แต่มันถูกบดบังด้วยความกลัวในอดีต..."]
                advice = "ความรักไม่ได้มีไว้เพื่อเติมเต็มส่วนที่ขาด แต่มีไว้เพื่อแบ่งปันส่วนที่เต็มจากข้างในค่ะ"
            elif category == "การงานและเส้นทางชีวิต":
                res = ["การติดขัดในตอนนี้ไม่ใช่จุดจบ แต่เป็นสัญญาณจาก Oversoul ว่าคุณกำลังเดินผิดทาง...", "ความมืดมนที่คุณเผชิญคือช่วงก่อนรุ่งสาง พลังสิงโตในตัวคุณกำลังถูกปลุกขึ้นมา...", "อย่ากังวลเรื่องการเริ่มต้นใหม่ รหัสชีวิตคุณคือผู้บุกเบิก..."]
                advice = "ความสำเร็จไม่ได้วัดที่ความเร็ว แต่วัดที่ความสม่ำเสมอและความศรัทธาในตัวเองค่ะ"
            else:
                res = ["กระแสเงินของคุณเปรียบเสมือนสายน้ำที่กำลังถูกกักด้วยความกังวล...", "หนี้สินเป็นเพียง 'บทเรียน' ที่มาสอนเรื่องความสมดุล...", "คุณมีโชคลาภซ่อนอยู่ในรหัสวิญญาณ แต่พลังงานลบรอบตัวกำลังบดบังอยู่..."]
                advice = "เงินทองคือพลังงานที่ไหลตามความสุข ยิ่งคุณมีใจที่เบาสบาย ทรัพย์จะยิ่งเข้าหาคุณค่ะ"
            
            gift = res[idx]
            # ส่งข้อมูลเข้า Sheets
            try:
                requests.post(GOOGLE_SCRIPT_URL, json={
                    "name": name, "line_id": contact, "birthdate": f"{date} {month} {year}",
                    "category": category, "question": question, "result": gift
                })
            except: pass

            st.markdown("---")
            st.success(f"### ✨ ผลถอดรหัสรหัสชีวิต: คุณ {name}")
            st.markdown(f"#### 💎 **สะท้อนพลังงานจากวันเกิด: สัญญาณจากภายในที่อยากบอกอะไรบางอย่างกับคุณ...** \n > **{gift}**")
            st.info(f"💡 **ข้อคิด:** {advice}")
            st.link_button("👉 คุยเชิงลึกกับที่ปรึกษา LUMINA SOUL", "https://lin.ee/jmI4z6G")

# --- 💖 หน้าที่ 2: เกี่ยวกับ LUMINA SOUL ---
elif page == "💖 เกี่ยวกับ LUMINA SOUL":
    st.title("💖 เกี่ยวกับ LUMINA SOUL")
    st.write("พื้นที่สะท้อนชีวิตที่ก่อตั้งขึ้นเพื่อช่วยให้ทุกคนกลับมาตื่นรู้และเห็นคุณค่าในตัวเองอีกครั้ง ผ่านพลังงานจาก Oversoul และรหัสลับจากวันเกิด เพื่อปลดล็อกศักยภาพที่ซ่อนอยู่ภายในตัวคุณ")
    st.markdown("---")
    st.subheader("✨ ผลงาน & บริการของเรา")
    st.write("• **E-book:** เยียวยาหัวใจจาก Oversoul")
    st.write("• **LUMINA SOAP:** สบู่พลังงานบวกเพื่อการชำระล้างและปรับสมดุล")
    st.write("• **Digital Reading:** บริการวิเคราะห์รหัสวิญญาณเชิงลึก")

# --- 📲 หน้าที่ 3: ติดต่อเรา ---
elif page == "📲 ติดต่อเรา":
    st.title("📲 ติดต่อ LUMINA SOUL")
    st.write("ติดตามและพูดคุยกับเราได้ผ่านช่องทางอย่างเป็นทางการ:")
    st.link_button("🟢 LINE Official Account", "https://lin.ee/jmI4z6G")
    st.write("ติดตามคลิปตื่นรู้และพลังงานบวกได้ที่ TikTok และ Facebook ของแบรนด์เร็วๆ นี้ค่ะ")
