import streamlit as st

st.title("🎈 하 하")
st.info(
    "jjjjjjjjjjjjjjjjjjjj하윙"
)
st.button("지도")
import pandas as pd
df = pd.DataFrame({"lat": [37.5], "lon": [127.0]})
st.map(df, zoom=12)