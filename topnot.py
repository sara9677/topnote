import streamlit as st
import json
import os

USERS_FILE = 'users.json'

# تحميل بيانات المستخدمين من ملف json
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

# حفظ بيانات المستخدمين
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

# التحقق من صحة بيانات الدخول
def authenticate(username, password, users):
    return username in users and users[username] == password

st.set_page_config(page_title="المفكرة السرية", layout="centered")
st.title("🔒 المفكرة السرية")

users = load_users()

# واجهة تسجيل الدخول
tab1, tab2 = st.tabs(["تسجيل الدخول", "إنشاء حساب جديد"])

with tab1:
    st.subheader("تسجيل الدخول")
    username = st.text_input("اسم المستخدم")
    password = st.text_input("كلمة المرور", type="password")

    if st.button("دخول"):
        if authenticate(username, password, users):
            st.success(f"أهلاً بك، {username}!")
            st.info("🚀 المفكرة جاهزة! (هنكملها بالخطوة الجاية)")
        else:
            st.error("اسم المستخدم أو كلمة المرور غير صحيحة.")

with tab2:
    st.subheader("إنشاء حساب")
    new_user = st.text_input("اسم المستخدم الجديد")
    new_pass = st.text_input("كلمة المرور الجديدة", type="password")

    if st.button("إنشاء حساب"):
        if new_user in users:
            st.warning("اسم المستخدم مستخدم بالفعل!")
        elif new_user == "" or new_pass == "":
            st.warning("يرجى ملء كل الحقول.")
        else:
            users[new_user] = new_pass
            save_users(users)
            st.success("تم إنشاء الحساب! يمكنك تسجيل الدخول الآن.")

