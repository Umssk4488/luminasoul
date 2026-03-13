import streamlit as st
import requests

# --- 🎨 1. ตั้งค่าดีไซน์ Premium Lavender Gradient ---
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(135deg, #fdfcfb 0%, #e2d1f9 40%, #fdfbfb 70%, #fff1eb 100%);
    }
    /* ปรับแต่ง Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.4);
        border-right: 1px solid rgba(255, 255, 255, 0.5);
    }
    div.stButton > button:first-child {
        background: linear-gradient(to right, #ba68c8 0%, #f06292 100%);
        color: white; border: none; border-radius: 25px;
        font-weight: bold; width: 100%; transition: 0.3s;
    }
    div.stButton > button:first-child:hover { transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# 📍 ลิงก์รับข้อมูลเดิม (ห้ามเปลี่ยน)
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzjNIr948oDKixAVajbf7me-kuABFyRopjKVmdx-PmMkYpFL8WbXAraMMJkPy2lMKLJNg/exec"

# --- 📂 2. สร้างแถบเมนู (Sidebar) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3594/3594210.png", width=100)
    st.title("เมนูหลัก")
    page = st.radio("เลือกหน้าที่ต้องการชม:", ["🔮 ถอดรหัสพลังงาน", "💖 เกี่ยวกับเรา & บริการ", "📲 ติดต่อเรา"])
    st.markdown("---")
    st.write("LUMINA SOUL | พื้นที่สะท้อนชีวิต")

# --- 🔮 หน้าที่ 1: ถอดรหัสพลังงาน (หน้าเดิมที่คุณต้องการ) ---
if page == "🔮 ถอดรหัสพลังงาน":
    st.title("🔮 LUMINA SOUL")
    st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")
    
    with st.form("main_form"):
        st.info("✨ รหัสลับจิตวิญญาณ... เมื่อคุณเริ่มเข้าใจพลังงานตัวเอง ประตูสู่ความเป็นไปได้ใหม่ๆ จะเปิดออก")
        name = st.text_input("ชื่อ-นามสกุล")
        contact = st.text_input("ID Line")
        col1, col2, col3 = st.columns(3)
        with col1: date = st.number_input("วันที่เกิด", 1, 31, 1)
        with col2: month = st.selectbox("เดือนเกิด", ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"])
        with col3: year = st.number_input("ปี พ.ศ. เกิด", 2450, 2600, 2535)
        
        category = st.selectbox("เลือกด้านที่ต้องการรับพลังงาน:", ["ความรักและความสัมพันธ์", "การงานและเส้นทางชีวิต", "โชคลาภและกระแสการเงิน"])
        question = st.text_area("✨ เรื่องที่กังวลใจที่สุดตอนนี้:", placeholder="แชร์รายละเอียดเรื่องที่ติดค้างในใจ..")
        submitted = st.form_submit_button("🔮 ถอดรหัสพันธสัญญาจิตวิญญาณ")

    if submitted:
        if len(name.strip()) < 2 or len(contact.strip()) < 3:
            st.error("⚠️ รบกวนระบุข้อมูลให้ครบถ้วนนะคะ")
        else:
            st.balloons()
            # ระบบสุ่มคำตอบตามวันที่เกิดเดิม
            res_list = ["พลังงานของคุณกำลังบอกว่า... (ชุดคำตอบเดิมของคุณอุ้ม)"]
            gift = res_list[0] # ตรงนี้ผมใส่ตัวอย่างไว้ คุณอุ้มสามารถเอาชุดคำตอบเดิมมาวางต่อได้เลยครับ
            
            # ส่งข้อมูลเข้า Sheets
            requests.post(GOOGLE_SCRIPT_URL, json={
                "name": name, "line_id": contact, "birthdate": f"{date} {month} {year}",
                "category": category, "question": question, "result": gift
            })
            
            st.success(f"### ✨ ผลถอดรหัส: คุณ {name}")
            st.markdown(f"#### 💎 **สะท้อนพลังงานจากวันเกิด: สัญญาณจากภายในที่อยากบอกอะไรบางอย่างกับคุณ...** \n > **{gift}**")
            st.link_button("👉 คุยเชิงลึกกับที่ปรึกษา", "https://lin.ee/jmI4z6G")

# --- 💖 หน้าที่ 2: เกี่ยวกับเรา ---
elif page == "💖 เกี่ยวกับเรา & บริการ":
    st.title("💖 เกี่ยวกับ LUMINA SOUL")
    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://cdn-icons-png.flaticon.com/512/6529/6529804.png") # เปลี่ยนเป็นรูปคุณอุ้มได้ครับ
    with col_text:
        st.subheader("ยินดีที่ได้รู้จักค่ะ ฉันคือ 'อุ้ม' (Lumina)")
        st.write("ผู้ก่อตั้งพื้นที่สะท้อนชีวิต เพื่อช่วยให้ทุกคนกลับมาตื่นรู้และเห็นคุณค่าในตัวเองอีกครั้ง ผ่านพลังงานจาก Oversoul และรหัสลับจากวันเกิด")
    
    st.markdown("---")
    st.subheader("✨ ผลงาน & บริการของเรา")
    st.write("• **E-book:** เยียวยาหัวใจจาก Oversoul")
    st.write("• **LUMINA SOAP:** สบู่พลังงานบวกเพื่อการชำระล้างใจ")
    st.write("• **Digital Reading:** บริการวิเคราะห์รหัสวิญญาณเชิงลึก")

# --- 📲 หน้าที่ 3: ติดต่อเรา ---
elif page == "📲 ติดต่อเรา":
    st.title("📲 ติดต่อเรา")
    st.write("คุณสามารถติดตามและพูดคุยกับเราได้ผ่านช่องทางต่างๆ ดังนี้ค่ะ")
    
    st.link_button("🟢 LINE Official Account", "https://lin.ee/jmI4z6G")
    st.link_button("⚫ TikTok: พื้นที่สะท้อนชีวิต", "https://www.tiktok.com/@your_tiktok") # ใส่ลิงก์จริงได้เลยครับ
    st.link_button("🔵 Facebook Page", "https://www.facebook.com/your_page")
