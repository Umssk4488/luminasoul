import streamlit as st
import random
import requests
from datetime import datetime

st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮")

# 📍 ลิงก์ Web App URL ที่คุณอุ้มเพิ่งได้มา
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzjNIr948oDKixAVajbf7me-kuABFyRopjKVmdx-PmMkYpFL8WbXAraMMJkPy2lMKLJNg/exec"

st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")

with st.form("lumina_v_final"):
    st.info("✨ ทุกรหัสชีวิตมี 'พรสวรรค์' ซ่อนอยู่เสมอ")
    name = st.text_input("ชื่อของคุณ (หรือชื่อเล่น)")
    contact = st.text_input("ID Line (เพื่อรับผลวิเคราะห์ฉบับเต็ม)")
    
    col1, col2, col3 = st.columns(3)
    with col1: date = st.number_input("วันที่เกิด", min_value=1, max_value=31, value=1)
    with col2: month = st.selectbox("เดือนเกิด", ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"])
    with col3: year = st.number_input("ปี พ.ศ. เกิด", min_value=2450, max_value=2600, value=2535)

    category = st.selectbox("เรื่องที่ต้องการให้ช่วยเช็กพลังงาน:", ["การงานและเส้นทางชีวิต", "ความรักและความสัมพันธ์", "โชคลาภและกระแสการเงิน"])
    st.markdown("**ระบุสิ่งที่ติดค้างในใจ หรือความกังวลที่ต้องการทางออก**")
    question = st.text_area("", placeholder="เช่น ตอนนี้ติดขัดเรื่องงาน...", label_visibility="collapsed")
    submitted = st.form_submit_button("🔮 เริ่มกระบวนการถอดรหัสพลังงาน")

if submitted:
    if name and contact and question:
        st.balloons()
        strengths = [
            "คุณมี 'พลังแห่งการเยียวยา' อยู่ในคำพูดโดยที่คุณอาจไม่รู้ตัว",
            "คุณมี 'สัญชาตญาณ' แม่นยำมาก หากเชื่อในเสียงข้างในชีวิตจะพุ่งทะยาน",
            "คุณมี 'บารมีแห่งผู้นำ' พลังงานของคุณดึงดูดผู้คนได้ง่าย",
            "คุณมี 'รหัสความมั่งคั่ง' ที่จะงอกเงยทุกครั้งที่คุณส่งต่อความสุข",
            "คุณมี 'เกราะคุ้มกันภัย' ที่แข็งแกร่ง อุปสรรคจะทำอะไรคุณไม่ได้"
        ]
        gift = random.choice(strengths)

        # ส่งข้อมูลเข้า Google Sheets
        requests.post(GOOGLE_SCRIPT_URL, json={
            "name": name, "line_id": contact, "birthdate": f"{date} {month} {year}",
            "category": category, "question": question, "result": gift
        })

        st.markdown("---")
        st.success(f"### ✨ ของขวัญจากจิตวิญญาณสำหรับคุณ {name}")
        st.markdown(f"#### 💎 **ข้อดีที่ถูกซ่อนไว้ของคุณคือ:** \n > **{gift}**")
        st.markdown("---")
        st.warning("### ⚠️ สารลับถึงคุณจาก LUMINA SOUL")
        st.markdown(f"**สิ่งที่คุณกังวลใจ...** แท้จริงแล้วคือสัญญาณจากตัวตนภายในค่ะ แอดไลน์ส่งชื่อ **'{name}'** เพื่อรับคำชี้แนะฉบับเต็มได้เลย")
        st.link_button("👉 ติดต่อรับคำปรึกษาฉบับเต็ม", "https://lin.ee/jmI4z6G")
    else:
        st.error("⚠️ โปรดระบุข้อมูลให้ครบถ้วนนะคะ")
