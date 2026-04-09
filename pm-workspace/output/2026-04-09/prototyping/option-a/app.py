import streamlit as st
import pandas as pd

st.set_page_config(page_title="Backlog Prioritizer", layout="wide")
st.title("Feature Backlog Prioritizer")

csv_path = st.sidebar.text_input("CSV-Pfad", value="input/case/data/backlog.csv")

try:
    df = pd.read_csv(csv_path, encoding="utf-8")
except FileNotFoundError:
    st.error(f"Datei nicht gefunden: {csv_path}")
    st.stop()

fit_map = {"hoch": 3, "mittel": 2, "niedrig": 1}
aufwand_map = {"S": 4, "M": 3, "L": 2, "XL": 1}
df["fit_num"] = df["strategischer_fit"].map(fit_map).fillna(1)
df["aufwand_inv"] = df["aufwand"].map(aufwand_map).fillna(1)
df["score"] = (df["kundenwunsche"] * 0.5 + df["fit_num"] * 0.3 + df["aufwand_inv"] * 0.2).round(2)

st.sidebar.markdown("---")
st.sidebar.markdown("### Filter")
status_filter = st.sidebar.selectbox("Status", ["alle"] + sorted(df["status"].unique().tolist()))
fit_filter = st.sidebar.selectbox("Strategischer Fit", ["alle"] + sorted(df["strategischer_fit"].unique().tolist()))

st.sidebar.markdown("---")
st.sidebar.markdown("### Scoring-Formel")
st.sidebar.markdown("```\nscore = (kundenwunsche × 0.5)\n      + (fit_num × 0.3)\n      + (aufwand_inv × 0.2)\n```")
st.sidebar.markdown("fit: hoch=3, mittel=2, niedrig=1")
st.sidebar.markdown("aufwand: S=4, M=3, L=2, XL=1")

gefiltert = df.copy()
if status_filter != "alle":
    gefiltert = gefiltert[gefiltert["status"] == status_filter]
if fit_filter != "alle":
    gefiltert = gefiltert[gefiltert["strategischer_fit"] == fit_filter]
gefiltert = gefiltert.sort_values("score", ascending=False)

if gefiltert.empty:
    st.warning("Keine Features entsprechen den gewählten Filtern.")
    st.stop()

col1, col2 = st.columns([3, 2])
with col1:
    st.subheader(f"Features ({len(gefiltert)})")
    anzeige = gefiltert[["feature", "kundenwunsche", "strategischer_fit", "aufwand", "score"]].copy()
    anzeige.columns = ["Feature", "Kundenwünsche", "Strategischer Fit", "Aufwand", "Score"]
    st.dataframe(anzeige.reset_index(drop=True), use_container_width=True, hide_index=True)
with col2:
    st.subheader("Score-Vergleich")
    st.bar_chart(gefiltert.set_index("feature")[["score"]])
