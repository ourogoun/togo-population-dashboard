import streamlit as st
import pandas as pd

df = pd.read_csv("togo_live_population.csv")
df = df[df['year'] >= 2017]

st.title("Togo Live Population Dashboard")

st.subheader("Children (0–14) vs Elderly (65+)")
st.line_chart(df.set_index("year")[["children_0_14", "elderly_65_plus"]])

st.subheader("Birth Rate")
st.line_chart(df.set_index("year")[["birth_rate"]])

st.subheader("Total Population")
st.line_chart(df.set_index("year")[["total_population"]])
