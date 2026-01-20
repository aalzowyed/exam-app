import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="منظم الاختبارات", layout="wide")

st.title("📅 منظم الاختبارات السنوي")
st.write("مرحباً بك! هذا هو الإصدار الأول من تطبيقك على الويب.")

# إضافة تجريبية للتأكد من عمل الموقع
date = st.date_input("اختر تاريخ الاختبار")
subject = st.text_input("اسم المادة")

if st.button("حفظ"):
    st.success(f"تم حفظ اختبار {subject} في تاريخ {date}")