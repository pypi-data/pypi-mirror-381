import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import xml.etree.ElementTree as ET
from io import StringIO

st.set_page_config(layout="wide")
st.title("📊 Data Analyzer")

if 'df' not in st.session_state:
    st.session_state.df = None

# Sidebar
with st.sidebar:
    st.header("📁 Files")
    
    if st.button("🎲 Sample Data"):
        st.session_state.df = pd.DataFrame({
            'ID': range(1, 11), 'Name': [f'User{i}' for i in range(1, 11)],
            'Age': np.random.randint(20, 50, 10), 'Score': np.random.randint(50, 100, 10)
        })
        st.rerun()
    
    up = st.file_uploader("Upload CSV", type='csv')
    if up:
        st.session_state.df = pd.read_csv(up)
    
    if st.session_state.df is not None:
        st.divider()
        fmt = st.radio("Format:", ["Binary", "Text", "XML"])
        
        # WRITE
        st.write("*WRITE*")
        mode = st.radio("Data:", ["Current", "Type"], key='wmode')
        if mode == "Type":
            txt = st.text_area("CSV data:", "ID,Name,Age\n1,Alice,25\n2,Bob,30", height=100, key='wtxt')
            if st.button("Write", key='wbtn'):
                d = pd.read_csv(StringIO(txt))
                if fmt == "Binary": st.download_button("⬇", pickle.dumps(d), "data.bin", key='wd1')
                elif fmt == "Text": st.download_button("⬇", d.to_csv(index=False), "data.txt", key='wd2')
                else: 
                    root = ET.Element("data")
                    for _, r in d.iterrows():
                        row = ET.SubElement(root, "row")
                        for k, v in r.items(): ET.SubElement(row, str(k)).text = str(v)
                    st.download_button("⬇", ET.tostring(root, encoding='unicode'), "data.xml", key='wd3')
        else:
            if st.button("Write", key='wbtn2'):
                d = st.session_state.df
                if fmt == "Binary": st.download_button("⬇", pickle.dumps(d), "data.bin", key='wd4')
                elif fmt == "Text": st.download_button("⬇", d.to_csv(index=False), "data.txt", key='wd5')
                else:
                    root = ET.Element("data")
                    for _, r in d.iterrows():
                        row = ET.SubElement(root, "row")
                        for k, v in r.items(): ET.SubElement(row, str(k)).text = str(v)
                    st.download_button("⬇", ET.tostring(root, encoding='unicode'), "data.xml", key='wd6')
        
        # READ
        st.write("*READ*")
        rf = st.file_uploader("File", type=['bin','txt','xml'], key='rfile')
        if rf and st.button("Read", key='rbtn'):
            if fmt == "Binary": st.session_state.df = pickle.loads(rf.read())
            elif fmt == "Text": st.session_state.df = pd.read_csv(rf)
            else: st.session_state.df = pd.DataFrame([{c.tag: c.text for c in r} for r in ET.parse(rf).getroot()])
            st.rerun()
        
        # APPEND
        st.write("*APPEND*")
        amode = st.radio("Add:", ["Current", "Type"], key='amode')
        af = st.file_uploader("Existing file", type=['bin','txt','xml'], key='afile')
        if amode == "Type":
            atxt = st.text_area("New data:", "ID,Name,Age\n11,Charlie,28", height=80, key='atxt')
            if af and st.button("Append", key='abtn1'):
                new = pd.read_csv(StringIO(atxt))
                if fmt == "Binary": old = pickle.loads(af.read())
                elif fmt == "Text": old = pd.read_csv(af)
                else: old = pd.DataFrame([{c.tag: c.text for c in r} for r in ET.parse(af).getroot()])
                comb = pd.concat([old, new], ignore_index=True)
                if fmt == "Binary": st.download_button("⬇", pickle.dumps(comb), "out.bin", key='ad1')
                elif fmt == "Text": st.download_button("⬇", comb.to_csv(index=False), "out.txt", key='ad2')
                else:
                    root = ET.Element("data")
                    for _, r in comb.iterrows():
                        row = ET.SubElement(root, "row")
                        for k, v in r.items(): ET.SubElement(row, str(k)).text = str(v)
                    st.download_button("⬇", ET.tostring(root, encoding='unicode'), "out.xml", key='ad3')
        else:
            if af and st.button("Append", key='abtn2'):
                d = st.session_state.df
                if fmt == "Binary": old = pickle.loads(af.read())
                elif fmt == "Text": old = pd.read_csv(af)
                else: old = pd.DataFrame([{c.tag: c.text for c in r} for r in ET.parse(af).getroot()])
                comb = pd.concat([old, d], ignore_index=True)
                if fmt == "Binary": st.download_button("⬇", pickle.dumps(comb), "out.bin", key='ad4')
                elif fmt == "Text": st.download_button("⬇", comb.to_csv(index=False), "out.txt", key='ad5')
                else:
                    root = ET.Element("data")
                    for _, r in comb.iterrows():
                        row = ET.SubElement(root, "row")
                        for k, v in r.items(): ET.SubElement(row, str(k)).text = str(v)
                    st.download_button("⬇", ET.tostring(root, encoding='unicode'), "out.xml", key='ad6')

# Main
if st.session_state.df is None:
    st.info("👆 Create or upload data")
    st.stop()

df = st.session_state.df
t1, t2, t3, t4 = st.tabs(["📊 Data", "📈 Stats", "🎨 Plot", "🔧 Tools"])

with t1:
    st.dataframe(df, use_container_width=True)
    c1, c2 = st.columns(2)
    c1.metric("Rows", df.shape[0])
    c2.metric("Cols", df.shape[1])

with t2:
    st.dataframe(df.describe(), use_container_width=True)
    nums = df.select_dtypes(include=np.number).columns.tolist()
    if nums:
        col = st.selectbox("Col:", nums, key='statcol')
        c1, c2, c3 = st.columns(3)
        c1.metric("Mean", f"{df[col].mean():.1f}")
        c2.metric("Min", f"{df[col].min():.1f}")
        c3.metric("Max", f"{df[col].max():.1f}")

with t3:
    nums = df.select_dtypes(include=np.number).columns.tolist()
    cats = df.select_dtypes(include='object').columns.tolist()
    p = st.radio("Type:", ["Bar", "Hist", "Line", "Pie"], horizontal=True, key='ptype')
    
    fig, ax = plt.subplots(figsize=(8, 5))
    if p == "Bar" and nums and cats:
        x = st.selectbox("X:", cats, key='px')
        y = st.selectbox("Y:", nums, key='py')
        df.groupby(x)[y].mean().plot(kind='bar', ax=ax, color='steelblue')
    elif p == "Hist" and nums:
        col = st.selectbox("Col:", nums, key='hcol')
        ax.hist(df[col].dropna(), bins=20, color='coral')
    elif p == "Line" and nums:
        df[nums[:2]].plot(ax=ax)
    elif p == "Pie" and cats:
        col = st.selectbox("Col:", cats, key='pcol')
        df[col].value_counts().head(5).plot(kind='pie', ax=ax, autopct='%1.1f%%')
    st.pyplot(fig)

with t4:
    nums = df.select_dtypes(include=np.number).columns.tolist()
    cats = df.select_dtypes(include='object').columns.tolist()
    
    # Convert Types
    st.write("🔄 Convert Data Types**")
    c1, c2, c3 = st.columns([2, 2, 1])
    ccol = c1.selectbox("Column:", df.columns, key='ccol')
    ctype = c2.selectbox("To Type:", ["int", "float", "str", "datetime"], key='ctype')
    if c3.button("Convert", key='cbtn', use_container_width=True):
        try:
            if ctype == "datetime":
                st.session_state.df[ccol] = pd.to_datetime(df[ccol])
            else:
                st.session_state.df[ccol] = df[ccol].astype(ctype)
            st.success(f"✅ Converted {ccol} to {ctype}")
            st.rerun()
        except Exception as e:
            st.error(f"❌ Error: {e}")
    
    st.divider()
    
    # Sort
    st.write("⬆ Sorting**")
    c1, c2, c3 = st.columns([2, 2, 1])
    scol = c1.selectbox("By:", df.columns, key='scol')
    sasc = c2.checkbox("Ascending", True, key='sasc')
    if c3.button("Sort", key='sbtn', use_container_width=True):
        st.dataframe(df.sort_values(scol, ascending=sasc), use_container_width=True)
    
    st.divider()
    
    # Group By
    st.write("📊 Grouping**")
    if cats and nums:
        c1, c2, c3, c4 = st.columns([2, 2, 2, 1])
        gc = c1.selectbox("Group:", cats, key='gcol')
        ac = c2.selectbox("Agg:", nums, key='acol')
        af = c3.selectbox("Func:", ["mean", "sum", "count", "min", "max"], key='afunc')
        if c4.button("Group", key='gbtn', use_container_width=True):
            result = df.groupby(gc)[ac].agg(af).reset_index()
            st.dataframe(result, use_container_width=True)
    
    st.divider()
    
    # Indexing (loc/iloc)
    st.write("🔢 Indexing (iloc)")
    c1, c2, c3 = st.columns([2, 2, 1])
    idx = c1.number_input("Row Index:", 0, len(df)-1, 0, key='idx')
    idxcol = c2.selectbox("Column:", df.columns, key='idxcol')
    if c3.button("Get", key='idxbtn', use_container_width=True):
        st.success(f"Value: *{df.iloc[idx][idxcol]}*")
    
    st.divider()
    
    # Slicing
    st.write("✂ Slicing**")
    c1, c2, c3 = st.columns([2, 2, 1])
    start = c1.number_input("Start:", 0, len(df), 0, key='sstart')
    end = c2.number_input("End:", 0, len(df), min(10, len(df)), key='send')
    if c3.button("Slice", key='slbtn', use_container_width=True):
        st.dataframe(df.iloc[start:end], use_container_width=True)
    
    st.divider()
    
    # Locating/Filtering
    st.write("🔍 Locating Filters**")
    c1, c2, c3 = st.columns([2, 2, 1])
    fcol = c1.selectbox("Column:", df.columns, key='fcol')
    fval = c2.text_input("Contains:", key='fval')
    if c3.button("Filter", key='fbtn', use_container_width=True) and fval:
        result = df[df[fcol].astype(str).str.contains(fval, case=False, na=False)]
        st.success(f"Found {len(result)} rows")
        st.dataframe(result, use_container_width=True)
    
    # Advanced Locate
    st.write("*Advanced Locate (Condition)*")
    if nums:
        c1, c2, c3, c4 = st.columns([2, 2, 2, 1])
        lcol = c1.selectbox("Column:", nums, key='lcol')
        lop = c2.selectbox("Operator:", [">", "<", ">=", "<=", "=="], key='lop')
        lval = c3.number_input("Value:", value=0.0, key='lval')
        if c4.button("Locate", key='lbtn', use_container_width=True):
            if lop == ">": result = df[df[lcol] > lval]
            elif lop == "<": result = df[df[lcol] < lval]
            elif lop == ">=": result = df[df[lcol] >= lval]
            elif lop == "<=": result = df[df[lcol] <= lval]
            else: result = df[df[lcol] == lval]
            st.success(f"Found {len(result)} rows where {lcol} {lop} {lval}")
            st.dataframe(result, use_container_width=True)
def main():
    import streamlit.web.cli as stcli
    import sys
    sys.argv = ["streamlit", "run", __file__]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()
