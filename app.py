import streamlit as st
import random
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮")

# --- ฟังก์ชันเชื่อมต่อ Google Sheets (ใช้ข้อมูลเดิมที่คุณอุ้มเคยตั้งไว้ใน Secrets) ---
def connect_sheets():
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
        client = gspread.authorize(creds)
        # ใส่ชื่อไฟล์ Google Sheets ของคุณอุ้มตรงนี้ (ถ้าชื่อเดิมคืออันไหน ใส่ชื่อนั้นเลยครับ)
        sheet = client.open("LUMINA_SOUL_Data").sheet1 
        return sheet
    except Exception as e:
        return None

# --- หัวข้อหลัก ---
st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")

with st.form("lumina_v5"):
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
    question = st.text_area("เล่าสิ่งที่ติดค้างใจ หรือสิ่งที่อยากให้จักรวาลช่วยนำทาง")
    
    submitted = st.form_submit_button("🔮 เริ่มกระบวนการถอดรหัสพลังงาน")

if submitted:
    if name and contact and question:
        st.balloons()
        
        # ส่วนสุ่มข้อดี
        strengths = [
            "คุณมี 'พลังแห่งการเยียวยา' อยู่ในคำพูดโดยที่บางทีคุณก็ไม่รู้ตัว",
            "คุณเป็นคนที่มี 'สัญชาตญาณ' แม่นยำมาก หากคุณเชื่อในเสียงข้างใน ชีวิตจะพุ่งทะยาน",
            "คุณมี 'บารมีแห่งผู้นำ' พลังงานของคุณสามารถดึงดูดผู้คนให้คล้อยตามได้ง่าย",
            "คุณมี 'รหัสความมั่งคั่ง' ที่จะงอกเงยทุกครั้งที่คุณส่งต่อความสุขให้ผู้อื่น",
            "คุณมี 'เกราะคุ้มกันภัย' ที่แข็งแกร่ง อุปสรรคที่เข้ามาจะทำอะไรคุณไม่ได้ถ้าใจคุณนิ่งพอ"
        ]
        gift = random.choice(strengths)

        # --- ส่วนบันทึกข้อมูลลง Google Sheets ---
        sheet = connect_sheets()
        if sheet:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sheet.append_row([now, name, contact, f"{date} {month} {year}", category, question, gift])
        else:
            st.error("ระบบบันทึกข้อมูลขัดข้องชั่วคราว แต่คุณสามารถแคปหน้าจอเพื่อส่งให้คุณอุ้มได้ค่ะ")

        # --- แสดงผลหน้าเว็บ ---
        st.markdown("---")
        st.success(f"### ✨ ของขวัญจากจิตวิญญาณสำหรับคุณ {name}")
        st.subheader(f"💎 ข้อดีที่ถูกซ่อนไว้ของคุณคือ: \n '{gift}'")
        
        st.markdown("---")
        st.warning(f"⚠️ **สารลับถึงคุณจาก LUMINA SOUL**")
        st.write(f"สิ่งที่คุณกำลังกังวลใจ... แท้จริงแล้วคือสัญญาณจากตัวตนภายในที่ต้องการการสื่อสารค่ะ เพื่อให้คุณเข้าถึงคำตอบที่ชัดเจนที่สุด และปลดพันธนาการที่ทำให้ชีวิตติดขัด แนะนำให้คุณรับสรุปผลวิเคราะห์เชิงลึกจากผู้เชี่ยวชาญโดยตรง")
        
        st.markdown("#### **👇 รับกุญแจปลดล็อกรหัสวิญญาณ (ฟรี)**")
        st.write(f"เพียงแอดไลน์ส่งชื่อ **'{name}'** เพื่อรับคำแนะนำสู่ความสำเร็จของคุณได้เลยนะคะ ✨")
        st.link_button("👉 รับการถอดรหัสส่วนบุคคล (Personal Consulting)", "https://lin.ee/jmI4z6G")
    else:
        st.error("⚠️ โปรดระบุข้อมูลให้ครบถ้วนนะคะ")
