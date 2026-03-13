import streamlit as st
import random
import requests

# --- 🎨 ยกเครื่องดีไซน์แบบพรีเมียม (Premium Pastel Gradient) ---
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮")

st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(135deg, #fdfcfb 0%, #e2d1f9 40%, #fdfbfb 70%, #fff1eb 100%);
    }
    h1 {
        color: #4a148c;
        font-family: 'Sarabun', sans-serif;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        font-weight: 800;
        margin-bottom: 0px;
    }
    h3 {
        color: #7e57c2;
        text-align: center;
        font-weight: 400;
        margin-top: 0px;
        margin-bottom: 30px;
    }
    div[data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid rgba(255, 255, 255, 0.4);
    }
    div.stButton > button:first-child {
        background: linear-gradient(to right, #ba68c8 0%, #f06292 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.7rem 2.5rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: 0.3s all ease;
        box-shadow: 0 4px 15px rgba(186, 104, 200, 0.3);
        width: 100%;
        margin-top: 20px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(to right, #ab47bc 0%, #ec407a 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(186, 104, 200, 0.4);
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea, .stNumberInput>div>div>input {
        border-radius: 12px !important;
        border: 1px solid #e0e0e0 !important;
        padding: 10px;
        background-color: rgba(255,255,255,0.8);
    }
    .stAlert {
        border-radius: 12px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 📍 ลิงก์ Web App URL (เชื่อมต่อ Google Sheets)
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzjNIr948oDKixAVajbf7me-kuABFyRopjKVmdx-PmMkYpFL8WbXAraMMJkPy2lMKLJNg/exec"

st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")

with st.form("lumina_premium_fix"):
    st.info("✨ รหัสลับจิตวิญญาณ... เมื่อคุณเริ่มเข้าใจพลังงานตัวเอง ประตูสู่ความเป็นไปได้ใหม่ๆ จะเปิดออก")
    
    name = st.text_input("ชื่อ-นามสกุล")
    contact = st.text_input("ID Line (เพื่อรับสิทธิ์วิเคราะห์ปมชีวิตเชิงลึกฟรี)")
    
    col1, col2, col3 = st.columns(3)
    with col1: date = st.number_input("วันที่เกิด", 1, 31, 1)
    with col2: month = st.selectbox("เดือนเกิด", ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"])
    with col3: year = st.number_input("ปี พ.ศ. เกิด", 2450, 2600, 2535)

    category = st.selectbox("ด้านที่คุณต้องการรับพลังงานนำทางในวันนี้:", 
                            ["ความรักและความสัมพันธ์", "การงานและเส้นทางชีวิต", "โชคลาภและกระแสการเงิน"])
    
    st.markdown("**✨เรื่องที่คุณกังวลใจที่สุดในตอนนี้คืออะไร?**")
    # แก้ไข placeholder ให้สั้นและเข้าใจง่ายตามสั่งครับ
    question = st.text_area("", placeholder="แชร์รายละเอียดเรื่องที่ติดค้างในใจ..", height=120)
    
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

        try:
            requests.post(GOOGLE_SCRIPT_URL, json={
                "name": name, "line_id": contact, "birthdate": f"{date} {month} {year}",
                "category": category, "question": question, "result": gift
            })
        except: pass

        st.markdown("---")
        st.success(f"### ✨ ผลถอดรหัสรหัสชีวิต: คุณ {name}")
        
        # แก้ไขตัวสะกดจาก สัญญา เป็น สัญญาณ เรียบร้อยครับ
        st.markdown(f"#### 💎 **สะท้อนพลังงานจากวันเกิด: สัญญาณจากภายในที่อยากบอกอะไรบางอย่างกับคุณ...** \n > **{gift}**")
        
        st.info(f"💡 **ข้อคิด:** {advice}")
        st.warning(f"⚠️ **สำหรับเรื่องที่คุณกังวล:** '{question[:60]}...' พลังงานบอกว่านี่คือปมที่รอการปลดล็อก และคุณไม่ได้เผชิญมันเพียงลำพังค่ะ")
        st.markdown("#### **👇 ให้แสงสว่างนำทางชีวิตคุณต่อ...**")
        st.write("สาส์นสั้นๆ นี้อาจยังไม่พอที่จะเยียวยาทุกอย่าง... แต่เราอยากให้คุณรู้ว่าคุณไม่ต้องแบกความทุกข์นี้ไว้เพียงลำพังนะคะ หากต้องการคำชี้แนะที่เจาะลึก ทักมาพูดคุยกับเราได้โดยตรงเลยค่ะ ✨")
        st.link_button("👉 คุยกับที่ปรึกษา LUMINA SOUL", "https://lin.ee/jmI4z6G")
