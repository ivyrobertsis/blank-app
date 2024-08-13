import pandas as pd
import seaborn as sns

import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

sns.relplot(df)
st.line_chart()
st.write(df)