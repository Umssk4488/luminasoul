import streamlit as st
import requests

# -----------------------------
# ตั้งค่าหน้าเว็บ
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
}

h3 {
    color: #7e57c2;
    text-align: center;
}

div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(to right, #ba68c8 0%, #f06292 100%);
    color: white;
    border-radius: 25px;
    padding: 0.7rem 2.5rem;
    font-weight: bold;
    width: 100%;
}

.result-card {
    background: rgba(255,255,255,0.85);
    padding: 22px;
    border-radius: 18px;
    margin-top: 10px;
}

.mini-card {
    background: rgba(255,255,255,0.75);
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
}

.center-text {
    text-align:center;
    color:#5a3d5c;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Google Sheet
# -----------------------------
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzjNIr948oDKixAVajbf7me-kuABFyRopjKVmdx-PmMkYpFL8WbXAraMMJkPy2lMKLJNg/exec"

# -----------------------------
# ฟังก์ชันคำนวณเลข
# -----------------------------
def reduce_number(n):
    while n > 9 and n not in (11,22,33):
        n = sum(int(d) for d in str(n))
    return n

def life_path_number(day,month,year):
    digits = f"{day:02d}{month:02d}{year}"
    total = sum(int(d) for d in digits)
    return reduce_number(total)

def birth_energy(day):
    return reduce_number(day)

# -----------------------------
# ข้อมูลคำอธิบาย
# -----------------------------
life_meanings = {
1:"คุณมีพลังของผู้เริ่มต้น กล้าตัดสินใจ และมักถูกผลักให้สร้างเส้นทางของตัวเอง",
2:"คุณมีพลังของผู้ประสานใจ เข้าใจความรู้สึกคนอื่นได้ลึก และมีความละเอียดอ่อนสูง",
3:"คุณมีพลังแห่งการสื่อสาร ความคิดสร้างสรรค์ และเสน่ห์ตามธรรมชาติ",
4:"คุณมีพลังแห่งความมั่นคง เป็นคนสร้างรากฐานและระบบได้ดี",
5:"คุณมีพลังแห่งการเปลี่ยนแปลง การเรียนรู้ และการเติบโตผ่านประสบการณ์",
6:"คุณมีพลังของผู้เยียวยาและผู้ดูแล หัวใจของคุณมีพลังปลอบประโลมสูง",
7:"คุณมีพลังของนักค้นหาความจริง ชอบเข้าใจชีวิตในระดับลึก",
8:"คุณมีพลังด้านความสำเร็จ การบริหาร และการสร้างผลลัพธ์",
9:"คุณมีพลังของผู้ให้ มีความเมตตาและเข้าใจผู้คน",
11:"คุณมีพลังของผู้ตื่นรู้ สัญชาตญาณแรงและรับพลังงานได้ลึก",
22:"คุณมีพลังของผู้สร้างสิ่งใหญ่ให้เป็นจริง",
33:"คุณมีพลังของครูผู้เยียวยา"
}

birth_meanings = {
1:"พลังนักบุกเบิก กล้าเริ่มต้น",
2:"พลังความอ่อนโยนและการรับรู้",
3:"พลังการแสดงออกและความคิดสร้างสรรค์",
4:"พลังความมั่นคงและความรับผิดชอบ",
5:"พลังการเปลี่ยนแปลงและอิสระ",
6:"พลังความรักและการดูแล",
7:"พลังการค้นหาความหมายชีวิต",
8:"พลังความมุ่งมั่นและความสำเร็จ",
9:"พลังเมตตาและการปล่อยวาง"
}

# -----------------------------
# หัวเว็บ
# -----------------------------
st.title("🔮 LUMINA SOUL")
st.markdown("### พื้นที่สะท้อนชีวิต | ถอดรหัสลับพลังงานวันเกิด")
st.write("---")

st.markdown(
"<p class='center-text'>พื้นที่สะท้อนชีวิต ผ่านพลังงานวันเกิดและสัญญาณจาก Oversoul เพื่อเข้าใจตัวเองลึกขึ้น</p>",
unsafe_allow_html=True
)

# -----------------------------
# ฟอร์ม
# -----------------------------
with st.form("form"):

    name = st.text_input("ชื่อ-นามสกุล")
    line = st.text_input("ID LINE")

    col1,col2,col3 = st.columns(3)

    with col1:
        day = st.number_input("วันที่เกิด",1,31,1)

    with col2:
        month = st.number_input("เดือนเกิด",1,12,1)

    with col3:
        year = st.number_input("ปีเกิด พ.ศ.",2450,2600,2535)

    category = st.selectbox(
        "เรื่องที่อยากสะท้อนพลังงาน",
        ["ความรัก","การงาน","การเงิน"]
    )

    question = st.text_area("เรื่องที่คุณกังวลใจตอนนี้")

    submitted = st.form_submit_button("🔮 ถอดรหัสพลังงานชีวิต")

# -----------------------------
# ประมวลผล
# -----------------------------
if submitted:

    if len(name)<2 or len(line)<2:
        st.error("กรุณากรอกข้อมูลให้ครบ")

    else:

        life = life_path_number(day,month,year)
        birth = birth_energy(day)

        life_text = life_meanings.get(life,"คุณมีพลังชีวิตเฉพาะตัวที่น่าสนใจ")
        birth_text = birth_meanings.get(birth,"วันเกิดของคุณสะท้อนพลังชีวิตเฉพาะตัว")

        result = f"""
พลังชีวิตของคุณกำลังอยู่ในช่วงเปลี่ยนผ่านบางอย่าง

เหตุการณ์หลายอย่างที่เกิดขึ้นในชีวิตช่วงนี้
อาจกำลังผลักให้คุณกลับมาเข้าใจตัวเองลึกขึ้น

บางสิ่งที่คุณเจอไม่ใช่ความบังเอิญ
แต่มันคือบทเรียนที่กำลังพาคุณเข้าใกล้เส้นทางชีวิตจริงของคุณมากขึ้น
"""

        # ส่งข้อมูลเข้า Google Sheet (เงียบ)
        try:
            requests.post(
                GOOGLE_SCRIPT_URL,
                json={
                    "name":name,
                    "line":line,
                    "birthdate":f"{day}/{month}/{year}",
                    "question":question,
                    "life_number":life
                }
            )
        except:
            pass

        st.markdown("---")

        st.success(f"✨ ผลสะท้อนพลังงานของ {name}")

        st.markdown(f"""
<div class="result-card">

🔢 เลขพลังชีวิต : {life}  
🔢 พลังวันเกิด : {birth}

</div>
""",unsafe_allow_html=True)

        st.markdown(f"""
<div class="mini-card">

🌙 ความหมายพลังชีวิต  
{life_text}

</div>
""",unsafe_allow_html=True)

        st.markdown(f"""
<div class="mini-card">

💎 พลังจากวันเกิด  
{birth_text}

</div>
""",unsafe_allow_html=True)

        st.markdown(f"""
<div class="result-card">

🔮 ข้อความสะท้อนพลังงาน  
{result}

</div>
""",unsafe_allow_html=True)

        # -----------------------------
        # ข้อความปิดการขาย
        # -----------------------------

        st.markdown("### ✨ ข้อความจาก Lumina Soul")

        st.markdown("""
สิ่งที่คุณเห็นข้างต้น เป็นเพียง **การสะท้อนพลังงานเบื้องต้นจากวันเกิดของคุณ**

หลายครั้ง รหัสชีวิตของคนเรา  
ไม่ได้เปิดเผยทั้งหมดในครั้งเดียว

ยังมีรายละเอียดที่ลึกกว่า เช่น

• บทเรียนชีวิตที่เกิดซ้ำ  
• ความสัมพันธ์ที่เข้ามาในชีวิต  
• จังหวะการเปลี่ยนแปลงของเส้นทางชีวิต  

หากคุณรู้สึกว่า **บางส่วนของข้อความนี้สะท้อนชีวิตคุณจริง**

คุณสามารถทักเข้ามาเพื่อรับ  
**การอ่านพลังงานเชิงลึกแบบเฉพาะตัว**

Lumina Soul จะช่วยสะท้อนสิ่งที่ชีวิตของคุณกำลังพยายามบอกคุณอยู่ ✨
""")

        st.link_button("👉 คุยกับที่ปรึกษา Lumina Soul", "https://lin.ee/jmI4z6G")

# footer
st.markdown("---")
st.markdown(
"<p style='text-align:center;font-size:0.8rem;color:#888;'>© 2026 LUMINA SOUL</p>",
unsafe_allow_html=True
)
