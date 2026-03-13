import streamlit as st
import random
import requests  # ใช้ตัวนี้แทน gspread เพื่อส่งข้อมูลผ่านท่อ Apps Script
from datetime import datetime

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮")

# --- 📍 จุดสำคัญ: ใส่ลิงก์ Apps Script ของคุณอุ้มที่นี่ ---
# วางลิงก์ที่ก๊อปมาจาก Google Sheets (Deployment URL)
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbz_ZEwOWxaK3V-tfUgSSSV10EEF8WkHA7ZbyPNYgIp0IdazB3K1gCLpAtpPohAM2vKd2w/exec"

# --- ส่วนหัวข้อเว็บ ---
st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")

with st.form("lumina_v_final"):
    st.info("✨ ทุกรหัสชีวิตมี 'พรสวรรค์' ซ่อนอยู่เสมอ")
    name = st.text_input("ชื่อของคุณ (หรือชื่อเล่น)")
    contact = st.text_input("ID Line (เพื่อรับผลวิเคราะห์ฉบับเต็ม)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        date = st.number_input("วันที่เกิด", min_value=1, max_value=31, value=1)
    with col2:
        month = st.selectbox("เดือนเกิด", ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"])
    with col3:
        year = st.number_input("ปี พ.ศ. เกิด", min_value=2450, max_value=2600, value=2535)

    category = st.selectbox("เรื่องที่ต้องการให้ช่วยเช็กพลังงาน:", ["การงานและเส้นทางชีวิต", "ความรักและความสัมพันธ์", "โชคลาภและกระแสการเงิน"])
    
    st.markdown("**ระบุสิ่งที่ติดค้างในใจ หรือความกังวลที่ต้องการทางออก**")
    st.caption("(เพื่อรับคำชี้แนะจาก Oversoul ในการดึงศักยภาพที่ซ่อนอยู่ของคุณออกมา)")
    question = st.text_area("", placeholder="เช่น ตอนนี้ติดขัดเรื่องงาน...", label_visibility="collapsed")
    
    submitted = st.form_submit_button("🔮 เริ่มกระบวนการถอดรหัสพลังงาน")

if submitted:
    if name and contact and question:
        st.balloons()
        
        strengths = [
            "คุณมี 'พลังแห่งการเยียวยา' อยู่ในคำพูดโดยที่คุณอาจไม่รู้ตัว",
            "คุณเป็นคนที่มี 'สัญชาตญาณ' แม่นยำมาก หากเชื่อในเสียงข้างในชีวิตจะพุ่งทะยาน",
            "คุณมี 'บารมีแห่งผู้นำ' พลังงานของคุณดึงดูดผู้คนให้คล้อยตามได้ง่าย",
            "คุณมี 'รหัสความมั่งคั่ง' ที่จะงอกเงยทุกครั้งที่คุณส่งต่อความสุขให้ผู้อื่น",
            "คุณมี 'เกราะคุ้มกันภัย' ที่แข็งแกร่ง อุปสรรคจะทำอะไรคุณไม่ได้ถ้าใจคุณนิ่งพอ"
        ]
        gift = random.choice(strengths)

        # --- ส่วนส่งข้อมูลเข้า Google Sheets ผ่าน Apps Script ---
        data_to_send = {
            "name": name,
            "line_id": contact,
            "birthdate": f"{date} {month} {year}",
            "category": category,
            "question": question,
            "result": gift
        }

        try:
            # ยิงข้อมูลเข้าท่อส่งที่คุณอุ้มสร้างไว้
            response = requests.post(GOOGLE_SCRIPT_URL, json=data_to_send)
            if response.status_code == 200:
                st.toast("✅ บันทึกข้อมูลเข้า Google Sheets เรียบร้อย!")
            else:
                st.toast("⚠️ บันทึกข้อมูลไม่สำเร็จ แต่คุณยังดูผลได้ค่ะ")
        except:
            st.toast("❌ เชื่อมต่อ Google Sheets ไม่ได้")

        # --- แสดงผลหน้าจอ ---
        st.markdown("---")
        st.success(f"### ✨ ของขวัญจากจิตวิญญาณสำหรับคุณ {name}")
        st.markdown(f"#### 💎 **ข้อดีที่ถูกซ่อนไว้ของคุณคือ:** \n > **{gift}**")
        
        st.markdown("---")
        st.warning(f"### ⚠️ สารลับถึงคุณจาก LUMINA SOUL")
        st.markdown(f"""
        **สิ่งที่คุณกำลังกังวลใจ...** แท้จริงแล้วคือสัญญาณจากตัวตนภายในที่ต้องการการสื่อสารค่ะ เพื่อให้คุณเข้าถึงคำตอบที่ชัดเจนที่สุด และปลดพันธนาการที่ทำให้ชีวิตติดขัด
        
        **แนะนำให้คุณรับ "สรุปผลวิเคราะห์เชิงลึก" โดยตรง เพื่อ:**
        * 🗝️ **ปลดล็อกรหัสพันธสัญญา:** เข้าใจสาเหตุที่แท้จริงของอุปสรรค
        * 🧭 **รับเข็มทิศนำทาง:** รู้วิธีใช้พรสวรรค์แก้ปัญหาปัจจุบัน
        * 📈 **เปิดรับพลังงานใหม่:** พลิกชีวิตสู่ความสำเร็จในแบบของคุณเอง
        
        ---
        #### **👇 รับกุญแจปลดล็อกรหัสวิญญาณ (ฟรี)**
        เพียงแอดไลน์แล้วส่งชื่อ **'{name}'** เพื่อรับคำชี้แนะสู่ความสำเร็จได้ทันทีค่ะ ✨
        """)
        
        st.link_button("👉 ติดต่อรับคำปรึกษาฉบับเต็ม (Personal Consulting)", "https://lin.ee/jmI4z6G")
    else:
        st.error("⚠️ โปรดระบุชื่อ ID Line และความกังวลใจให้ครบถ้วนนะคะ")
