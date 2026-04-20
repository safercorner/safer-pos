import streamlit as st
import pandas as pd
import random
from datetime import datetime

# إعدادات واجهة ركن صافر
st.set_page_config(page_title="ركن صافر للتجارة", page_icon="🏪", layout="wide")

# تصميم مخصص لدعم اللغة العربية والطباعة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stButton>button { background-color: #2196F3; color: white; width: 100%; border-radius: 10px; }
    @media print { .no-print { display: none !important; } .print-only { display: block !important; } }
    .print-only { display: none; }
    </style>
    """, unsafe_allow_html=True)

# قاعدة بيانات وهمية (سيتم تطويرها لربطها بملف دائم لاحقاً)
if 'products' not in st.session_state:
    st.session_state.products = [
        {"id": 1, "name": "قاطع كهربائي 16A", "sar": 20.0, "yer": 3000.0, "stock": 50, "loc": "A1"},
        {"id": 2, "name": "لمبة LED 9W", "sar": 10.0, "yer": 1500.0, "stock": 100, "loc": "B2"},
        {"id": 3, "name": "سلك نحاس 2.5mm", "sar": 180.0, "yer": 27000.0, "stock": 20, "loc": "الكابلات"}
    ]
if 'sales' not in st.session_state:
    st.session_state.sales = []

# القائمة الجانبية
st.sidebar.image("https://github.com/safercorner.png", width=100) # سيظهر شعارك آلياً
st.sidebar.title("إدارة ركن صافر")
menu = st.sidebar.radio("انتقل إلى:", ["الرئيسية & المخزن", "عملية بيع جديدة", "تقارير الأرباح"])

if menu == "الرئيسية & المخزن":
    st.header("📦 حالة المخزن الحالي")
    df = pd.DataFrame(st.session_state.products)
    st.table(df.rename(columns={'name': 'الصنف', 'sar': 'سعر (سعودي)', 'yer': 'سعر (يمني)', 'stock': 'المخزون', 'loc': 'الموقع'}))

elif menu == "عملية بيع جديدة":
    st.header("🛒 كاشير ركن صافر")
    
    col1, col2 = st.columns(2)
    with col1:
        product_names = [p['name'] for p in st.session_state.products]
        selected_item = st.selectbox("اختر الصنف", product_names)
    with col2:
        qty = st.number_input("الكمية", min_value=1, value=1)

    if st.button("إصدار الفاتورة"):
        inv_no = f"INV-{random.randint(1000, 9999)}"
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # عرض الفاتورة للتأكيد
        st.success(f"تم تسجيل العملية بنجاح! رقم: {inv_no}")
        
        # نموذج الفاتورة القابلة للطباعة
        invoice_html = f"""
        <div style="border: 2px solid #333; padding: 20px; text-align: center; background: white; color: black;">
            <h2>ركن صافر للتجارة</h2>
            <p>رقم الفاتورة: {inv_no}</p>
            <p>التاريخ: {time_now}</p>
            <hr>
            <h4>الصنف: {selected_item}</h4>
            <h4>الكمية: {qty}</h4>
            <hr>
            <p>شكراً لزيارتكم!</p>
        </div>
        """
        st.markdown(invoice_html, unsafe_allow_html=True)
        st.button("🖨️ اضغط هنا للطباعة", on_click=lambda: st.write('<script>window.print();</script>', unsafe_allow_html=True))

elif menu == "تقارير الأرباح":
    st.header("📊 إحصائيات المبيعات")
    st.info("سيتم هنا عرض الرسوم البيانية للأرباح اليومية والشهرية.")
