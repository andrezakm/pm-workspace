import streamlit as st
import pandas as pd

st.set_page_config(page_title="Backlog Prioritizer", layout="wide")

st.title("Feature Backlog Prioritizer")

# CSV laden
csv_path = st.text_input("CSV-Pfad", value="input/case/data/backlog.csv", label_visibility="collapsed")

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"Datei nicht gefunden: {csv_path}")
    st.stop()

# Score berechnen
fit_map = {"hoch": 3, "mittel": 2, "niedrig": 1}
aufwand_map = {"S": 4, "M": 3, "L": 2, "XL": 1}

df["fit_num"] = df["strategischer_fit"].map(fit_map).fillna(1)
df["aufwand_inv"] = df["aufwand"].map(aufwand_map).fillna(1)
df["score"] = (df["kundenwunsche"] * 0.5 + df["fit_num"] * 0.3 + df["aufwand_inv"] * 0.2).round(2)

# Filter als Tabs
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    status_optionen = ["alle"] + sorted(df["status"].unique().tolist())
    status_filter = st.selectbox("Status", status_optionen)

with col_f2:
    fit_optionen = ["alle"] + sorted(df["strategischer_fit"].unique().tolist())
    fit_filter = st.selectbox("Strategischer Fit", fit_optionen)

with col_f3:
    st.markdown("**Scoring-Formel**")
    st.caption("score = (Kundenwünsche × 0.5) + (Fit × 0.3) + (1/Aufwand × 0.2)")

# Filter anwenden
gefiltert = df.copy()
if status_filter != "alle":
    gefiltert = gefiltert[gefiltert["status"] == status_filter]
if fit_filter != "alle":
    gefiltert = gefiltert[gefiltert["strategischer_fit"] == fit_filter]

gefiltert = gefiltert.sort_values("score", ascending=False)

if gefiltert.empty:
    st.warning("Keine Features entsprechen den gewählten Filtern.")
    st.stop()

# Chart zuerst — Hauptnavigation
st.subheader(f"Score-Übersicht — {len(gefiltert)} Features")
chart_data = gefiltert.set_index("feature")[["score"]]
st.bar_chart(chart_data, height=350)

# Drill-down: Feature auswählen
st.markdown("---")
st.subheader("Detail-Ansicht")

ausgewaehlt = st.selectbox(
    "Feature auswählen für Details",
    options=gefiltert["feature"].tolist(),
    index=0
)

detail = gefiltert[gefiltert["feature"] == ausgewaehlt].iloc[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Score", detail["score"])
col2.metric("Kundenwünsche", detail["kundenwunsche"])
col3.metric("Strategischer Fit", detail["strategischer_fit"])
col4.metric("Aufwand", detail["aufwand"])

st.markdown(f"**Beschreibung:** {detail['beschreibung']}")
st.markdown(f"**Status:** `{detail['status']}`")

# Tabelle als Referenz darunter
st.markdown("---")
st.subheader("Alle Features")
anzeige = gefiltert[["feature", "kundenwunsche", "strategischer_fit", "aufwand", "score"]].copy()
anzeige.columns = ["Feature", "Kundenwünsche", "Strategischer Fit", "Aufwand", "Score"]
st.dataframe(anzeige, use_container_width=True, hide_index=True)
