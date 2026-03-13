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
        # ใช้ข้อมูลกุญแจที่คุณอุ้มตั้งไว้ใน Secrets
        creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
        client = gspread.authorize(creds)
        # เชื่อมกับไฟล์ชื่อ LuminaSoul_Data (ชื่อต้องตรงเป๊ะ)
        sheet = client.open("LuminaSoul_Data").sheet1 
        return sheet
    except Exception as e:
        return None

# --- หัวข้อหลัก ---
st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")
st.write("ร่วมค้นหา 'ของขวัญจากจิตวิญญาณ' และแนวทางปลดล็อกชีวิตในแบบของคุณ")

with st.form("lumina_vfinal"):
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

    category = st.selectbox("มิติจิตวิญญาณที่คุณต้องการคำชี้แนะ:", ["การงานและเส้นทางชีวิต", "ความรักและความสัมพันธ์", "โชคลาภและกระแสการเงิน"])
    
    # --- อัปเดตช่องคำถามตามสไตล์ที่คุณอุ้มเลือก ---
    question = st.text_area("ระบุข้อความหรือความกังวลใจที่ต้องการสื่อสารถึง Oversoul (จิตสูงของคุณ) เพื่อรับคำชี้แนะในการดึงศักยภาพที่ซ่อนอยู่ของคุณออกมา")
    
    submitted = st.form_submit_button("🔮 เริ่มกระบวนการถอดรหัสพลังงาน")

# --- ส่วนแสดงผล ---
if submitted:
    if name and contact and question:
        st.balloons()
        
        # คลังข้อดี (ของขวัญ)
        strengths = [
            "คุณมี 'พลังแห่งการเยียวยา' อยู่ในคำพูดโดยที่คุณอาจไม่รู้ตัว",
            "คุณเป็นคนที่มี 'สัญชาตญาณ' แม่นยำมาก หากเชื่อในเสียงข้างในชีวิตจะพุ่งทะยาน",
            "คุณเป็นผู้มี 'บารมีแห่งผู้นำ' พลังงานของคุณดึงดูดผู้คนให้คล้อยตามได้ง่าย",
            "คุณมี 'รหัสความมั่งคั่ง' ที่จะงอกเงยทุกครั้งที่คุณส่งต่อความสุขให้ผู้อื่น",
            "คุณมี 'เกราะคุ้มกันภัย' ที่แข็งแกร่ง อุปสรรคจะทำอะไรคุณไม่ได้ถ้าใจคุณนิ่งพอ"
        ]
        gift = random.choice(strengths)

        # บันทึกข้อมูลลง Google Sheets
        sheet = connect_sheets()
        if sheet:
            try:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sheet.append_row([now, name, contact, f"{date} {month} {year}", category, question, gift])
            except:
                pass 

        st.markdown("---")
        st.success(f"### ✨ ของขวัญจากจิตวิญญาณสำหรับคุณ {name}")
        st.subheader(f"💎 ข้อดีที่ถูกซ่อนไว้ของคุณคือ: \n '{gift}'")
        
        st.markdown("---")
        st.info(f"**วิเคราะห์พลังงานด้าน {category}:** \n\n ระบบตรวจพบสัญญาณการเปลี่ยนแปลงที่สำคัญในรหัสชีวิตของคุณ... พลังงานของคุณกำลังปรับตัวเพื่อเปิดรับโอกาสใหม่ๆ ที่สอดคล้องกับจิตวิญญาณค่ะ")
        
        # ส่วน Cliffhanger ที่คุณอุ้มเลือก (ดึงดูดสุดๆ)
        st.warning(f"⚠️ **สารลับถึงคุณจาก LUMINA SOUL**")
        st.write(f"สิ่งที่คุณกำลังกังวลใจ... แท้จริงแล้วคือสัญญาณจากตัวตนภายในที่ต้องการการสื่อสารค่ะ เพื่อให้คุณเข้าถึงคำตอบที่ชัดเจนที่สุด และปลดพันธนาการที่ทำให้ชีวิตติดขัด แนะนำให้คุณรับสรุปผลวิเคราะห์เชิงลึกจากผู้เชี่ยวชาญโดยตรง")
        
        st.markdown("#### **👇 รับกุญแจปลดล็อกรหัสวิญญาณ (ฟรี)**")
        st.write(f"เพียงแอดไลน์ส่งชื่อ **'{name}'** เพื่อเริ่มต้นการเยียวยาและรับคำชี้แนะสู่ความสำเร็จของคุณได้เลยนะคะ ✨")
        
        st.link_button("👉 รับการถอดรหัสส่วนบุคคล (Personal Consulting)", "https://lin.ee/jmI4z6G")
        st.caption("หรือแคปหน้าจอนี้ส่งไปที่เพจ 'พื้นที่สะท้อนชีวิต' ได้เลยค่ะ")
    else:
        st.error("⚠️ เพื่อความแม่นยำ โปรดระบุชื่อ ID Line และความในใจถึงจิตสูงให้ครบถ้วนนะคะ")
