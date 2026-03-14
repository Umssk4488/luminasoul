import streamlit as st
import requests

# --- 🎨 1. ตั้งค่าดีไซน์ Premium Lavender & Pink Pastel (Single Page) ---
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮")

st.markdown("""
    <style>
    /* พื้นหลังไล่สีพรีเมียม */
    .stApp {
        background-image: linear-gradient(135deg, #fdfcfb 0%, #e2d1f9 40%, #fdfbfb 70%, #fff1eb 100%);
    }
    /* หัวข้อหลัก LUMINA SOUL */
    h1 {
        color: #4a148c;
        font-family: 'Sarabun', sans-serif;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0px;
    }
    h3 {
        color: #7e57c2;
        text-align: center;
        font-weight: 400;
        margin-top: 0px;
    }
    /* ปุ่มกด Gradient หรูหรา */
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
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(186, 104, 200, 0.4);
    }
    /* ปรับแต่งกล่อง Input/TextArea ให้โค้งมนนุ่มนวล */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea, .stNumberInput>div>div>input {
        border-radius: 12px !important;
        border: 1px solid #e0e0e0 !important;
        background-color: rgba(255,255,255,0.8);
    }
    /* ปรับปรุงกล่อง Info/Success */
    .stAlert {
        border-radius: 12px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 📍 ลิงก์เชื่อมต่อ Google Sheets (คงเดิมห้ามเปลี่ยน)
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzjNIr948oDKixAVajbf7me-kuABFyRopjKVmdx-PmMkYpFL8WbXAraMMJkPy2lMKLJNg/exec"

# --- 🔮 ส่วนเนื้อหาหน้าเดียว (Single Page) ---
st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")

# ส่วนแนะนำแบรนด์สั้นๆ ให้ดูพรีเมียม
st.write("---")
st.markdown("<p style='text-align: center; color: #5a3d5c;'>ยินดีต้อนรับสู่พื้นที่แห่งการตื่นรู้และเยียวยาใจ ผ่านสัญญาณจาก Oversoul และรหัสลับวันเกิดเพื่อปลดล็อกศักยภาพในตัวคุณ</p>", unsafe_allow_html=True)

with st.form("lumina_single_page_form"):
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
    question = st.text_area("", placeholder="แชร์รายละเอียดเรื่องที่ติดค้างในใจ..", height=120)
    
    submitted = st.form_submit_button("🔮 ถอดรหัสพันธสัญญาจิตวิญญาณ")

if submitted:
    if len(name.strip()) < 2 or len(contact.strip()) < 3 or len(question.strip()) < 5:
        st.error("⚠️ รบกวนระบุข้อมูลให้ครบถ้วน เพื่อให้เราสื่อสารกับพลังงานของคุณได้แม่นยำนะคะ")
    else:
        st.balloons()
        idx = (date % 3)
        
        # ชุดคำตอบสะท้อนพลังงาน
        if category == "ความรักและความสัมพันธ์":
            res = ["หัวใจของคุณมีบารมีสูงนัก ความเจ็บปวดที่พบเจอคือการ 'คัดกรอง' พลังงานที่ไม่คู่ควรออกไป เพื่อเปิดทางให้คู่แท้ตามคำมั่นสัญญาได้เข้ามาหาคุณในจังหวะที่เหมาะสมค่ะ", 
                   "อย่าเสียดายรักที่จากไป เพราะรหัสวันเกิดคุณบอกว่ามันคือการถอนพันธนาการเก่าที่ฉุดรั้งคุณไว้ ความโสดในตอนนี้คือช่วงเวลาที่คุณจะได้กลับมา 'กอดตัวเอง' ให้แข็งแรงที่สุด", 
                   "ความรักที่คุณตามหาไม่ได้อยู่ไกลตัว แต่มันถูกบดบังด้วยความกลัวในอดีต เมื่อคุณให้อภัยตัวเองได้ พลังงานดึงดูดความรักที่บริสุทธิ์จะทำงานทันทีค่ะ"]
            advice = "ความรักไม่ได้มีไว้เพื่อเติมเต็มส่วนที่ขาด แต่มีไว้เพื่อแบ่งปันส่วนที่เต็มจากข้างในค่ะ"
        elif category == "การงานและเส้นทางชีวิต":
            res = ["การติดขัดในตอนนี้ไม่ใช่จุดจบ แต่เป็นสัญญาณจาก Oversoul ว่าคุณกำลังเดินผิดทางจาก 'รหัสพรสวรรค์' ของคุณ ลองหยุดนิ่งแล้วฟังเสียงข้างใน คุณจะพบช่องทางที่ง่ายและรุ่งเรืองกว่าเดิม", 
                   "ความมืดมนที่คุณเผชิญคือช่วงก่อนรุ่งสาง พลังสิงโตในตัวคุณกำลังถูกปลุกขึ้นมา อุปสรรคนี้มาเพื่อสอนให้คุณเป็น 'ผู้นำ' ที่เข้มแข็ง ไม่ใช่คนที่คอยวิ่งตามใคร", 
                   "อย่ากังวลเรื่องการเริ่มต้นใหม่ รหัสชีวิตคุณคือผู้บุกเบิก สิ่งที่เสียไปจะถูกแทนที่ด้วยโอกาสที่ใหญ่กว่าเดิมหลายเท่า ขอเพียงใจคุณกล้าที่จะก้าวข้ามกรอบเดิมๆ"]
            advice = "ความสำเร็จไม่ได้วัดที่ความเร็ว แต่วัดที่ความสม่ำเสมอและความศรัทธาในตัวเองค่ะ"
        else: # การเงิน
            res = ["กระแสเงินของคุณเปรียบเสมือนสายน้ำที่กำลังถูกกักด้วยความกังวล เมื่อคุณเปลี่ยนจากความกลัวเป็นความ 'ขอบคุณ' ในสิ่งที่มี ท่อแห่งความมั่งคั่งจะเริ่มไหลเวียนอีกครั้งค่ะ", 
                   "หนี้สินเป็นเพียง 'บทเรียน' ที่มาสอนเรื่องความสมดุล รหัสวันเกิดคุณมีพลังแห่งการสร้างตัว เพียงแต่ต้องจัดลำดับความสำคัญของใจใหม่ แล้วช่องทางรายได้จะเปิดออกอย่างมหัศจรรย์", 
                   "คุณมีโชคลาภซ่อนอยู่ในรหัสวิญญาณ แต่พลังงานลบรอบตัวกำลังบดบังมันอยู่ ให้เริ่มชำระล้างใจให้ใสสะอาด แล้วสิ่งดีๆ ที่คุณรอคอยจะมาหาแบบไม่คาดฝัน"]
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
        
        st.markdown("#### **👇 ให้แสงสว่างนำทางชีวิตคุณต่อ...**")
        st.write("หากต้องการคำชี้แนะที่เจาะลึกจากสัญญาณนี้ ทักมาพูดคุยกับเราโดยตรงได้เลยนะคะ ✨")
        st.link_button("👉 คุยกับที่ปรึกษา LUMINA SOUL", "https://lin.ee/jmI4z6G")

# ส่วนท้ายหน้าเว็บ (Footer)
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #888;'>© 2026 LUMINA SOUL | พื้นที่สะท้อนชีวิต</p>", unsafe_allow_html=True)
