import streamlit as st
import random
import requests
from datetime import datetime

st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮")

# 📍 ลิงก์ Web App URL ของคุณอุ้ม (ห้ามลบนะ!)
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzjNIr948oDKixAVajbf7me-kuABFyRopjKVmdx-PmMkYpFL8WbXAraMMJkPy2lMKLJNg/exec"

st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")

with st.form("lumina_v_pro"):
    st.info("✨ รหัสชีวิตของคุณมีคำตอบซ่อนอยู่เสมอ")
    name = st.text_input("ชื่อของคุณ")
    contact = st.text_input("ID Line")
    
    col1, col2, col3 = st.columns(3)
    with col1: date = st.number_input("วันที่เกิด", 1, 31, 1)
    with col2: month = st.selectbox("เดือนเกิด", ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"])
    with col3: year = st.number_input("ปี พ.ศ. เกิด", 2450, 2600, 2535)

    category = st.selectbox("เรื่องที่ต้องการให้ช่วยเช็กพลังงาน:", ["การงานและเส้นทางชีวิต", "ความรักและความสัมพันธ์", "โชคลาภและกระแสการเงิน"])
    question = st.text_area("ระบุสิ่งที่ติดค้างในใจ", placeholder="เช่น อกหักทำใจไม่ได้...")
    submitted = st.form_submit_button("🔮 ถอดรหัสพลังงานส่วนบุคคล")

if submitted:
    if name and contact and question:
        st.balloons()
        
        # --- ระบบคำนวณคำตอบตาม "เลขวันที่เกิด" (ศาสตร์เลขศาสตร์) ---
        base_num = (date % 9) or 9
        responses = {
            1: "คุณคือ 'ผู้เริ่มต้น' พลังงานวันนี้บอกว่าอุปสรรคคือบททดสอบความแข็งแกร่ง",
            2: "คุณคือ 'ผู้เยียวยา' ช่วงนี้จิตใจไวต่อความรู้สึก ให้กลับมาอยู่กับลมหายใจ",
            3: "คุณคือ 'ผู้สร้างสรรค์' พลังงานที่ติดขัดจะคลี่คลายเมื่อคุณเริ่มลงมือทำสิ่งใหม่",
            4: "คุณคือ 'รากฐาน' ความมั่นคงกำลังกลับมา ขอเพียงคุณมีระเบียบกับใจตัวเอง",
            5: "คุณคือ 'ผู้เปลี่ยนแปลง' สิ่งที่เสียไปคือการสลัดสิ่งเก่าเพื่อรับสิ่งที่ดีกว่า",
            6: "คุณคือ 'ผู้ให้' ความรักที่ผิดหวังคือกุญแจที่สอนให้คุณรักตัวเองก่อน",
            7: "คุณคือ 'นักปราชญ์' คำตอบที่คุณตามหาอยู่ในความสงบ ไม่ใช่การวิ่งตาม",
            8: "คุณคือ 'ผู้นำพาความมั่งคั่ง' พลังงานการเงินกำลังหมุนเวียน อย่าเพิ่งท้อ",
            9: "คุณคือ 'ผู้บรรลุ' ทุกตอนจบคือจุดเริ่มต้นของความสำเร็จที่ยิ่งใหญ่กว่า"
        }
        gift = responses[base_num]

        # ส่งข้อมูลเข้า Google Sheets
        requests.post(GOOGLE_SCRIPT_URL, json={
            "name": name, "line_id": contact, "birthdate": f"{date} {month} {year}",
            "category": category, "question": question, "result": gift
        })

        # --- แสดงผลแบบมืออาชีพ ---
        st.markdown("---")
        st.success(f"### ✨ ผลวิเคราะห์รหัสชีวิตคุณ {name}")
        st.markdown(f"#### 💎 **สาส์นจาก Oversoul สำหรับผู้เกิดวันที่ {date}:** \n > **{gift}**")
        
        st.warning("💡 **คำชี้แนะเบื้องต้น:** สิ่งที่คุณเผชิญอยู่ตอนนี้ (เช่น {question}) เป็นเพียงสภาวะชั่วคราว พลังงานของคุณจะเปลี่ยนไปในทางที่ดีขึ้นหากคุณเริ่มปลดล็อกเงื่อนปมในใจค่ะ")
        
        st.info("👇 **รับทางแก้ปัญหาแบบเจาะลึกรายบุคคล (ฟรี)**\nแอดไลน์ส่งชื่อของคุณเพื่อรับเข็มทิศชีวิตค่ะ")
        st.link_button("👉 ปรึกษาเชิงลึกกับ LUMINA SOUL", "https://lin.ee/jmI4z6G")
    else:
        st.error("⚠️ กรุณากรอกข้อมูลให้ครบเพื่อการคำนวณที่แม่นยำค่ะ")
