import streamlit as st
import requests

# -----------------------------
# 🎨 ตั้งค่าหน้าเว็บ
# -----------------------------
st.set_page_config(page_title="LUMINA SOUL", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(135deg, #fdfcfb 0%, #e2d1f9 40%, #fdfbfb 70%, #fff1eb 100%);
    }

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

    div.stButton > button:first-child,
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(to right, #ba68c8 0%, #f06292 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.7rem 2.5rem;
        font-weight: bold;
        font-size: 1.05rem;
        transition: 0.3s all ease;
        box-shadow: 0 4px 15px rgba(186, 104, 200, 0.3);
        width: 100%;
        margin-top: 10px;
    }

    div.stButton > button:first-child:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(186, 104, 200, 0.4);
        color: white;
    }

    .stTextInput>div>div>input,
    .stSelectbox>div>div>div,
    .stTextArea>div>div>textarea,
    .stNumberInput>div>div>input {
        border-radius: 12px !important;
        border: 1px solid #e0e0e0 !important;
        background-color: rgba(255,255,255,0.88);
    }

    .stAlert {
        border-radius: 12px;
        border: none;
    }

    .result-card {
        background: rgba(255,255,255,0.78);
        padding: 22px;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(126, 87, 194, 0.12);
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .mini-card {
        background: rgba(255,255,255,0.72);
        padding: 14px 16px;
        border-radius: 16px;
        box-shadow: 0 4px 14px rgba(126, 87, 194, 0.10);
        margin-bottom: 12px;
    }

    .center-text {
        text-align: center;
        color: #5a3d5c;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 📍 Google Sheets URL
# -----------------------------
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzjNIr948oDKixAVajbf7me-kuABFyRopjKVmdx-PmMkYpFL8WbXAraMMJkPy2lMKLJNg/exec"

# -----------------------------
# 🔢 ฟังก์ชันคำนวณเลข
# -----------------------------
def reduce_number(n):
    while n > 9 and n not in (11, 22, 33):
        n = sum(int(d) for d in str(n))
    return n

def life_path_number(day, month_num, year_be):
    # ใช้ปี พ.ศ. ตามที่ผู้ใช้กรอก
    digits = f"{day:02d}{month_num:02d}{year_be}"
    total = sum(int(d) for d in digits if d.isdigit())
    return reduce_number(total)

def birth_day_energy(day):
    return reduce_number(day)

# -----------------------------
# 🔮 คำอธิบายเลขชีวิต
# -----------------------------
life_path_meanings = {
    1: "คุณมีพลังของผู้เริ่มต้น กล้าตัดสินใจ และเกิดมาเพื่อสร้างเส้นทางของตัวเอง ไม่ได้มาเพื่อเดินตามใคร",
    2: "คุณมีพลังของผู้ประสานใจ อ่อนไหว ลึกซึ้ง รับรู้ความรู้สึกคนอื่นได้ดี และมีพรสวรรค์ด้านความสัมพันธ์",
    3: "คุณมีพลังแห่งการสื่อสาร ความคิดสร้างสรรค์ เสน่ห์ และการแสดงออก เมื่อคุณเป็นตัวเอง โลกจะได้ยินเสียงของคุณ",
    4: "คุณมีพลังแห่งความมั่นคง เป็นคนสร้างรากฐาน เก่งเรื่องการจัดระบบ ความรับผิดชอบ และความสม่ำเสมอ",
    5: "คุณมีพลังแห่งอิสรภาพ การเปลี่ยนแปลง การเรียนรู้ผ่านประสบการณ์ และการเติบโตอย่างรวดเร็ว",
    6: "คุณมีพลังของผู้ดูแล ผู้เยียวยา และผู้มอบความรักให้ผู้อื่น หัวใจของคุณมีพลังปลอบประโลมสูงมาก",
    7: "คุณมีพลังของนักค้นหาความจริง ลึกซึ้ง ชอบตั้งคำถาม และมีสายเชื่อมต่อกับโลกภายในอย่างชัดเจน",
    8: "คุณมีพลังด้านการบริหาร ความสำเร็จ การเงิน และการผลักดันเป้าหมายให้เกิดผลจริงในโลกวัตถุ",
    9: "คุณมีพลังของผู้ให้ เมตตา วิสัยทัศน์กว้าง และมีภารกิจด้านจิตวิญญาณหรือการช่วยเหลือผู้คน",
    11: "คุณมีพลังของผู้ตื่นรู้ มีสัญชาตญาณแรง รับรู้อะไรลึกกว่าคนทั่วไป และเป็นแสงนำทางให้ผู้อื่นได้",
    22: "คุณมีพลังของผู้สร้างสิ่งใหญ่ให้เป็นจริง มีวิสัยทัศน์กว้างและสามารถเปลี่ยนความฝันให้กลายเป็นระบบที่จับต้องได้",
    33: "คุณมีพลังของครูผู้เยียวยา เปี่ยมเมตตา อ่อนโยน และมีภารกิจในการส่งต่อความรักและแสงสว่าง"
}

birth_day_meanings = {
    1: "วันเกิดของคุณสะท้อนพลังนักบุกเบิก คุณมักไม่ชอบเดินในกรอบเดิม และมีแรงผลักดันจากภายในสูง",
    2: "วันเกิดของคุณสะท้อนพลังความอ่อนโยน การรับรู้ และความสามารถในการเชื่อมใจคนรอบตัว",
    3: "วันเกิดของคุณสะท้อนพลังความสดใส ความคิดสร้างสรรค์ และคำพูดที่มีอิทธิพลต่อผู้คน",
    4: "วันเกิดของคุณสะท้อนพลังความมั่นคง การรับผิดชอบ และความจริงจังกับสิ่งที่คุณให้คุณค่า",
    5: "วันเกิดของคุณสะท้อนพลังการเปลี่ยนแปลง การเรียนรู้ การเคลื่อนไหว และความกล้าลองสิ่งใหม่",
    6: "วันเกิดของคุณสะท้อนพลังผู้ดูแล ผู้เยียวยา และคนที่ให้ความสำคัญกับหัวใจและครอบครัว",
    7: "วันเกิดของคุณสะท้อนพลังนักสังเกต นักค้นหาความหมาย และผู้ที่มีโลกภายในลึกกว่าที่คนอื่นเห็น",
    8: "วันเกิดของคุณสะท้อนพลังความมุ่งมั่น อำนาจภายใน และศักยภาพในการสร้างความสำเร็จ",
    9: "วันเกิดของคุณสะท้อนพลังแห่งเมตตา ความเข้าใจมนุษย์ และการเรียนรู้เรื่องการปล่อยวาง",
    11: "วันเกิดของคุณสะท้อนพลังญาณรู้ ความละเอียดทางพลังงาน และการเชื่อมต่อกับสิ่งที่มองไม่เห็น",
    22: "วันเกิดของคุณสะท้อนพลังผู้สร้างสิ่งใหญ่ มีศักยภาพทำเรื่องที่มีผลกระทบต่อผู้คนจำนวนมาก",
    33: "วันเกิดของคุณสะท้อนพลังแห่งการเยียวยา การสอน และการรับใช้ด้วยหัวใจ"
}

# -----------------------------
# 🔮 คำทำนายแยกตามหมวด
# -----------------------------
love_responses = [
    "หัวใจของคุณมีบารมีสูง ความเจ็บปวดที่พบเจอคือการคัดกรองพลังงานที่ไม่คู่ควรออกไป เพื่อเปิดทางให้ความสัมพันธ์ที่จริงแท้เข้ามาในเวลาที่เหมาะสม",
    "สิ่งที่จบลงอาจไม่ใช่ความล้มเหลว แต่มันคือการถอนพันธะเก่าที่ฉุดรั้งคุณไว้ ความรักครั้งใหม่จะเริ่มเมื่อคุณกลับมาเห็นคุณค่าของตัวเองอย่างแท้จริง",
    "ความรักที่คุณตามหาไม่ได้อยู่ไกลตัว แต่มันถูกบดบังด้วยบาดแผลเดิม เมื่อคุณให้อภัยตัวเองและปล่อยความกลัวลง พลังดึงดูดความรักที่บริสุทธิ์จะเริ่มทำงาน"
]

work_responses = [
    "การติดขัดในตอนนี้ไม่ใช่จุดจบ แต่เป็นสัญญาณว่าคุณกำลังถูกพากลับสู่เส้นทางที่ตรงกับพรสวรรค์จริงของตัวเองมากขึ้น",
    "อุปสรรคที่คุณเผชิญไม่ใช่สิ่งที่มาทำลายคุณ แต่มันกำลังปลุกพลังผู้นำและความกล้าหาญในตัวคุณให้ตื่นขึ้น",
    "อย่ากลัวการเริ่มต้นใหม่ รหัสชีวิตของคุณมีพลังของผู้บุกเบิก สิ่งที่เสียไปอาจกำลังถูกแทนที่ด้วยโอกาสที่ใหญ่กว่าเดิม"
]

money_responses = [
    "กระแสเงินของคุณเหมือนสายน้ำที่กำลังถูกกักด้วยความกังวล เมื่อใจเริ่มคลายและหันกลับมาเห็นคุณค่าของสิ่งที่มี พลังความมั่งคั่งจะเริ่มไหลอีกครั้ง",
    "สิ่งที่เกิดขึ้นเรื่องการเงินคือบทเรียนเรื่องความสมดุล รหัสชีวิตของคุณยังมีพลังแห่งการสร้างตัว เพียงต้องจัดลำดับพลังงานและการตัดสินใจใหม่",
    "คุณมีโชคซ่อนอยู่ในรหัสชีวิต แต่พลังลบรอบตัวอาจกำลังบดบังมันอยู่ เมื่อคุณเริ่มดูแลใจให้สะอาด ช่องทางดี ๆ จะเริ่มเปิดอย่างไม่คาดฝัน"
]

# -----------------------------
# 🪄 ตัวช่วย
# -----------------------------
month_names = [
    "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
    "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
]
month_map = {name: i + 1 for i, name in enumerate(month_names)}

category_advice = {
    "ความรักและความสัมพันธ์": "ความรักไม่ได้มีไว้เพื่อเติมเต็มส่วนที่ขาด แต่มีไว้เพื่อแบ่งปันส่วนที่เต็มจากข้างใน",
    "การงานและเส้นทางชีวิต": "ความสำเร็จไม่ได้วัดที่ความเร็ว แต่วัดที่ความสม่ำเสมอและความศรัทธาในตัวเอง",
    "โชคลาภและกระแสการเงิน": "เงินคือพลังงานที่ไหลตามความชัดเจน ความเชื่อมั่น และความสุขที่คุณอนุญาตให้ตัวเองรับ"
}

# -----------------------------
# 🌌 ส่วนหัวเว็บ
# -----------------------------
st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")

st.write("---")
st.markdown(
    "<p class='center-text'>ยินดีต้อนรับสู่พื้นที่แห่งการตื่นรู้และเยียวยาใจ ผ่านสัญญาณจาก Oversoul และรหัสลับวันเกิด เพื่อปลดล็อกศักยภาพในตัวคุณ</p>",
    unsafe_allow_html=True
)

# -----------------------------
# 📝 ฟอร์มกรอกข้อมูล
# -----------------------------
with st.form("lumina_single_page_form"):
    st.info("✨ รหัสลับจิตวิญญาณ... เมื่อคุณเริ่มเข้าใจพลังงานตัวเอง ประตูสู่ความเป็นไปได้ใหม่ ๆ จะเปิดออก")

    name = st.text_input("ชื่อ-นามสกุล")
    contact = st.text_input("ID Line (เพื่อรับสิทธิ์วิเคราะห์ปมชีวิตเชิงลึกฟรี)")

    col1, col2, col3 = st.columns(3)
    with col1:
        birth_day = st.number_input("วันที่เกิด", min_value=1, max_value=31, value=1, step=1)
    with col2:
        birth_month_name = st.selectbox("เดือนเกิด", month_names)
    with col3:
        birth_year = st.number_input("ปี พ.ศ. เกิด", min_value=2450, max_value=2600, value=2535, step=1)

    category = st.selectbox(
        "ด้านที่คุณต้องการรับพลังงานนำทางในวันนี้:",
        ["ความรักและความสัมพันธ์", "การงานและเส้นทางชีวิต", "โชคลาภและกระแสการเงิน"]
    )

    st.markdown("**✨ เรื่องที่คุณกังวลใจที่สุดในตอนนี้คืออะไร?**")
    question = st.text_area("", placeholder="แชร์รายละเอียดเรื่องที่ติดค้างในใจ..", height=120)

    submitted = st.form_submit_button("🔮 ถอดรหัสพันธสัญญาจิตวิญญาณ")

# -----------------------------
# ⚙️ ประมวลผล
# -----------------------------
if submitted:
    name_clean = name.strip()
    contact_clean = contact.strip()
    question_clean = question.strip()

    if len(name_clean) < 2 or len(contact_clean) < 3 or len(question_clean) < 5:
        st.error("⚠️ รบกวนระบุข้อมูลให้ครบถ้วน เพื่อให้เราสื่อสารกับพลังงานของคุณได้แม่นยำนะคะ")
    else:
        month_num = month_map[birth_month_name]
        day_num = int(birth_day)
        year_num = int(birth_year)

        life_number = life_path_number(day_num, month_num, year_num)
        birth_energy = birth_day_energy(day_num)

        # ใช้ day + life number เพื่อกระจายผลลัพธ์ให้มีความเฉพาะมากขึ้น
        idx = (day_num + life_number) % 3

        if category == "ความรักและความสัมพันธ์":
            main_result = love_responses[idx]
        elif category == "การงานและเส้นทางชีวิต":
            main_result = work_responses[idx]
        else:
            main_result = money_responses[idx]

        life_meaning = life_path_meanings.get(life_number, "คุณมีพลังเฉพาะตัวที่น่าสนใจและควรใช้เวลาเรียนรู้เพิ่มเติม")
        birth_meaning = birth_day_meanings.get(birth_energy, "วันเกิดของคุณสะท้อนพลังเฉพาะตัวที่น่าสนใจ")

        soul_message = f"""
{name_clean} เป็นคนที่มีพลังภายในเฉพาะตัวและไม่ได้เดินมาไกลขนาดนี้โดยบังเอิญ
สิ่งที่กำลังเกิดขึ้นในชีวิตตอนนี้อาจเป็นช่วงเปลี่ยนผ่านสำคัญ
เพื่อพาคุณกลับมาเข้าใจตัวเองลึกขึ้น ปล่อยสิ่งที่ไม่ใช่
และเลือกเส้นทางที่สอดคล้องกับหัวใจของตัวเองมากกว่าเดิม
""".strip()

        advice = category_advice.get(category, "จงเชื่อมั่นในจังหวะชีวิตของตัวเอง")

        birthdate_text = f"{day_num} {birth_month_name} {year_num}"

        # ส่งข้อมูลเข้า Google Sheets
        try:
            requests.post(
                GOOGLE_SCRIPT_URL,
                json={
                    "name": name_clean,
                    "line_id": contact_clean,
                    "birthdate": birthdate_text,
                    "birth_day": day_num,
                    "birth_month": birth_month_name,
                    "birth_year_be": year_num,
                    "life_path_number": life_number,
                    "birth_day_energy": birth_energy,
                    "category": category,
                    "question": question_clean,
                    "result": main_result,
                    "life_meaning": life_meaning,
                    "birth_meaning": birth_meaning,
                    "soul_message": soul_message,
                    "advice": advice
                },
                timeout=10
            )
        except Exception:
            pass

        st.balloons()
        st.markdown("---")

        st.success(f"### ✨ ผลถอดรหัสพลังงานชีวิต: คุณ {name_clean}")

        st.markdown(
            f"""
            <div class="result-card">
                <h4 style="color:#7b1fa2; margin-top:0;">🔢 เลขพลังงานของคุณ</h4>
                <p><b>เลขเส้นทางชีวิต (Life Path):</b> {life_number}</p>
                <p><b>เลขพลังงานวันเกิด:</b> {birth_energy}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="mini-card">
                <h4 style="color:#8e24aa; margin-top:0;">🌙 ความหมายเลขเส้นทางชีวิต</h4>
                <p>{life_meaning}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="mini-card">
                <h4 style="color:#8e24aa; margin-top:0;">💎 พลังงานจากวันเกิด</h4>
                <p>{birth_meaning}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="result-card">
                <h4 style="color:#ad1457; margin-top:0;">🔮 สะท้อนพลังงานในด้าน{category}</h4>
                <p>{main_result}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(f"💡 ข้อคิดนำทาง: {advice}")

        st.markdown(
            f"""
            <div class="mini-card">
                <h4 style="color:#6a1b9a; margin-top:0;">✨ ข้อความจาก Lumina Soul</h4>
                <p>{soul_message}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("#### 👇 หากอยากรับคำชี้แนะเชิงลึกเพิ่มเติม")
        st.write("สามารถทักมาคุยกับที่ปรึกษา LUMINA SOUL ได้โดยตรงนะคะ ✨")
        st.link_button("👉 คุยกับที่ปรึกษา LUMINA SOUL", "https://lin.ee/jmI4z6G")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 0.8rem; color: #888;'>© 2026 LUMINA SOUL | พื้นที่สะท้อนชีวิตและการตื่นรู้</p>",
    unsafe_allow_html=True
)
