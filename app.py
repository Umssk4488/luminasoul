import streamlit as st
import random

# ตั้งค่าหน้าเว็บและสี (ธีมมืด/ทอง)
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮", layout="centered")

# --- การตกแต่ง CSS เพื่อความพรีเมียม ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(45deg, #FFD700, #B8860B);
        color: black;
        font-weight: bold;
        border: none;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stTextArea>div>textarea {
        background-color: #1c1f26;
        color: white;
        border: 1px solid #FFD700;
    }
    h1, h2, h3 {
        color: #FFD700 !important;
    }
    .stAlert {
        background-color: #1c1f26;
        border: 1px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ส่วนหัวข้อ ---
st.title("🔮 LUMINA SOUL")
st.markdown("### Spiritual Decoding System")
st.write("ร่วมค้นหา 'ของขวัญจากจิตวิญญาณ' และแนวทางปลดล็อกชีวิตในแบบของคุณ")

# --- ฟอร์มรับข้อมูล ---
with st.form("lumina_premium"):
    st.markdown("#### 📝 ข้อมูลเพื่อเชื่อมต่อรหัสพลังงาน")
    name = st.text_input("ชื่อของคุณ (หรือชื่อเรียก)")
    contact = st.text_input("ID Line (เพื่อรับผลวิเคราะห์ฉบับเต็มและคำแนะนำฟรี)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        date = st.number_input("วันที่เกิด", min_value=1, max_value=31, value=1)
    with col2:
        month = st.selectbox("เดือนเกิด", ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"])
    with col3:
        year = st.number_input("ปี พ.ศ. เกิด", min_value=2450, max_value=2600, value=2535)

    category = st.selectbox("มิติจิตวิญญาณที่คุณต้องการคำชี้แนะ:", ["การงานและเส้นทางชีวิต", "ความรักและความสัมพันธ์", "โชคลาภและกระแสการเงิน"])
    question = st.text_area("เล่าสิ่งที่ติดค้างในใจ หรือสิ่งที่อยากให้จักรวาลช่วยนำทาง")
    
    submitted = st.form_submit_button("🔮 เริ่มกระบวนการถอดรหัสพลังงาน")

if submitted:
    if name and contact and question:
        st.balloons()
        
        # คลังข้อดี (คุณอุ้มมาเพิ่มเองได้เรื่อยๆ ครับ)
        strengths = [
            "คุณมี 'พลังแห่งการเยียวยา' อยู่ในคำพูดโดยที่บางทีคุณก็ไม่รู้ตัว",
            "คุณเป็นคนที่มี 'สัญชาตญาณ' แม่นยำมาก หากคุณเชื่อในเสียงข้างใน ชีวิตจะพุ่งทะยาน",
            "คุณมี 'บารมีแห่งผู้นำ' พลังงานของคุณสามารถดึงดูดผู้คนให้คล้อยตามได้ง่าย",
            "คุณมี 'รหัสความมั่งคั่ง' ที่จะงอกเงยทุกครั้งที่คุณส่งต่อความสุขให้ผู้อื่น",
            "คุณมี 'เกราะคุ้มกันภัย' ที่แข็งแกร่ง อุปสรรคที่เข้ามาจะทำอะไรคุณไม่ได้ถ้าใจคุณนิ่งพอ"
        ]
        gift = random.choice(strengths)

        st.markdown("---")
        st.markdown(f"### ✨ ของขวัญจากจิตวิญญาณสำหรับคุณ {name}")
        st.info(f"💎 **ข้อดีที่ถูกซ่อนไว้ของคุณคือ:** \n\n '{gift}'")
        
        st.markdown("---")
        st.subheader(f"📊 วิเคราะห์พลังงานด้าน {category}")
        st.write("ระบบตรวจพบสัญญาณการเปลี่ยนแปลงที่สำคัญในรหัสชีวิตของคุณ... มีบางอย่างที่กำลังรอการปลดล็อกเพื่อให้พลังงานกลับมาไหลเวียนอย่างสมบูรณ์")
        
        # ส่วน Cliffhanger ที่คุณอุ้มเลือก (ลึกซึ้ง)
        st.warning(f"⚠️ **สารลับถึงคุณจาก LUMINA SOUL**")
        st.write("สิ่งที่คุณกำลังกังวลใจ... แท้จริงแล้วคือสัญญาณจากตัวตนภายในที่ต้องการการสื่อสารค่ะ เพื่อให้คุณเข้าถึงคำตอบที่ชัดเจนที่สุด และปลดพันธนาการที่ทำให้ชีวิตติดขัด แนะนำให้คุณรับสรุปผลวิเคราะห์เชิงลึกจากผู้เชี่ยวชาญโดยตรง")
        
        st.markdown("#### **👇 รับกุญแจปลดล็อกรหัสวิญญาณ (ฟรี)**")
        st.write(f"เพียงแอดไลน์ส่งชื่อ **'{name}'** และแจ้งข้อดีที่คุณได้รับ เพื่อเริ่มต้นการเยียวยาและรับคำชี้แนะสู่ความสำเร็จของคุณได้เลยนะคะ ✨")
        
        st.link_button("👉 รับการถอดรหัสส่วนบุคคล (Personal Consulting)", "https://lin.ee/jmI4z6G")
        st.caption("หรือแคปหน้าจอนี้ส่งไปที่เพจ 'พื้นที่สะท้อนชีวิต' ได้เลยค่ะ")
    else:
        st.error("⚠️ เพื่อความแม่นยำสูงสุด โปรดระบุชื่อ ID Line และคำถามให้ครบถ้วนนะคะ")
