import streamlit as st
import random
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮")

# --- ฟังก์ชันเชื่อมต่อ Google Sheets ---
def connect_sheets():
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
        client = gspread.authorize(creds)
        # ตรวจสอบชื่อไฟล์ให้ตรงกับ LuminaSoul_Data
        sheet = client.open("LuminaSoul_Data").sheet1 
        return sheet
    except Exception as e:
        return None

# --- ส่วนหัวข้อ ---
st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")
st.write("ร่วมค้นหา 'ของขวัญจากจิตวิญญาณ' และแนวทางปลดล็อกชีวิตในแบบของคุณ")

with st.form("lumina_v_final"):
    st.info("✨ ทุกรหัสชีวิตมี 'พรสวรรค์' ซ่อนอยู่เสมอ")
    
    name = st.text_input("ชื่อของคุณ (หรือชื่อเล่น)")
    contact = st.text_input("ID Line (เพื่อรับผลวิเคราะห์ฉบับเต็มและคำแนะนำฟรี)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        date = st.number_input("วันที่เกิด", min_value=1, max_value=31, value=1)
    with col2:
        month = st.selectbox("เดือนเกิด", ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"])
    with col3:
        year = st.number_input("ปี พ.ศ. เกิด", min_value=2450, max_value=2600, value=2535)

    category = st.selectbox("เรื่องที่ต้องการให้ช่วยเช็กพลังงาน:", ["การงานและเส้นทางชีวิต", "ความรักและความสัมพันธ์", "โชคลาภและกระแสการเงิน"])
    
    # --- ปรับแต่งส่วนคำถามให้ สั้น กระชับ และมีตัวอย่างตามที่คุณอุ้มสั่ง ---
    st.markdown("**ระบุสิ่งที่ติดค้างในใจ หรือความกังวลที่ต้องการทางออก**")
    st.caption("(เพื่อรับคำชี้แนะจาก Oversoul ในการดึงศักยภาพที่ซ่อนอยู่ของคุณออกมา)")
    
    # ใส่ placeholder ตัวอย่างสั้นๆ
    question = st.text_area("", placeholder="เช่น ตอนนี้ติดขัดเรื่องงาน, ความสัมพันธ์เริ่มมีปัญหา, อยากรู้วิธีเปิดดวงรับทรัพย์", label_visibility="collapsed")
    
    submitted = st.form_submit_button("🔮 เริ่มกระบวนการถอดรหัสพลังงาน")

if submitted:
    if name and contact and question:
        st.balloons()
        
        # คลังข้อดี (Strengths)
        strengths = [
            "คุณมี 'พลังแห่งการเยียวยา' อยู่ในคำพูดโดยที่คุณอาจไม่รู้ตัว",
            "คุณเป็นคนที่มี 'สัญชาตญาณ' แม่นยำมาก หากเชื่อในเสียงข้างในชีวิตจะพุ่งทะยาน",
            "คุณมี 'บารมีแห่งผู้นำ' พลังงานของคุณดึงดูดผู้คนให้คล้อยตามได้ง่าย",
            "คุณมี 'รหัสความมั่งคั่ง' ที่จะงอกเงยทุกครั้งที่คุณส่งต่อความสุขให้ผู้อื่น",
            "คุณมี 'เกราะคุ้มกันภัย' ที่แข็งแกร่ง อุปสรรคจะทำอะไรคุณไม่ได้ถ้าใจคุณนิ่งพอ"
        ]
        gift = random.choice(strengths)

        # บันทึกข้อมูลลง Sheets
        sheet = connect_sheets()
        if sheet:
            try:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sheet.append_row([now, name, contact, f"{date} {month} {year}", category, question, gift])
            except:
                pass 

        # --- แสดงผลหน้าจอให้ลูกค้า ---
        st.markdown("---")
        st.success(f"### ✨ ของขวัญจากจิตวิญญาณสำหรับคุณ {name}")
        st.subheader(f"💎 ข้อดีที่ถูกซ่อนไว้ของคุณคือ: \n '{gift}'")
        
        st.markdown("---")
        st.warning(f"⚠️ **สารลับถึงคุณจาก LUMINA SOUL**")
        st.write(f"สิ่งที่คุณกำลังกังวลใจ... แท้จริงแล้วคือสัญญาณจากตัวตนภายในที่ต้องการการสื่อสารค่ะ เพื่อให้คุณเข้าถึงคำตอบที่ชัดเจนที่สุด และปลดพันธนาการที่ทำให้ชีวิตติดขัด แนะนำให้คุณรับสรุปผลวิเคราะห์เชิงลึกจากผู้เชี่ยวชาญโดยตรง")
        
        st.markdown("#### **👇 รับกุญแจปลดล็อกรหัสวิญญาณ (ฟรี)**")
        st.write(f"เพียงแอดไลน์ส่งชื่อ **'{name}'** เพื่อเริ่มต้นการเยียวยาและรับคำชี้แนะสู่ความสำเร็จของคุณได้เลยนะคะ ✨")
        st.link_button("👉 รับการถอดรหัสส่วนบุคคล (Personal Consulting)", "https://lin.ee/jmI4z6G")
    else:
        st.error("⚠️ โปรดระบุชื่อ ID Line และความกังวลใจให้ครบถ้วนนะคะ")
