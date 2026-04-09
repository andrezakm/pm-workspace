import streamlit as st
import pandas as pd

st.set_page_config(page_title="Backlog Prioritizer", layout="wide")
st.title("Was sollen wir als nächstes bauen?")
st.caption("Kein Chart. Keine Tabelle. Nur eine Entscheidung.")

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
st.sidebar.caption("score = (Kundenwünsche × 0.5) + (Fit × 0.3) + (1/Aufwand × 0.2)")
st.sidebar.caption("fit: hoch=3, mittel=2, niedrig=1 | aufwand: S=4, M=3, L=2, XL=1")

gefiltert = df.copy()
if status_filter != "alle":
    gefiltert = gefiltert[gefiltert["status"] == status_filter]
if fit_filter != "alle":
    gefiltert = gefiltert[gefiltert["strategischer_fit"] == fit_filter]
gefiltert = gefiltert.sort_values("score", ascending=False).reset_index(drop=True)

if gefiltert.empty:
    st.warning("Keine Features entsprechen den gewählten Filtern.")
    st.stop()

top3 = gefiltert.head(3)
st.markdown("## Top 3 Kandidaten")
cols = st.columns(3)
rang_labels = ["#1 Empfehlung", "#2 Alternative", "#3 Reserve"]
rang_farben = ["🟢", "🟡", "🔵"]

for i, (col, (_, row)) in enumerate(zip(cols, top3.iterrows())):
    with col:
        st.markdown(f"### {rang_farben[i]} {rang_labels[i]}")
        st.markdown(f"## {row['feature']}")
        st.markdown(f"_{row['beschreibung']}_")
        st.markdown("---")
        st.metric("Score", row["score"])
        c1, c2, c3 = st.columns(3)
        c1.metric("Nachfrage", row["kundenwunsche"])
        c2.metric("Fit", row["strategischer_fit"])
        c3.metric("Aufwand", row["aufwand"])
        st.markdown(f"`{row['status']}`")

if len(gefiltert) > 3:
    st.markdown("---")
    with st.expander(f"Weitere {len(gefiltert) - 3} Features anzeigen"):
        rest = gefiltert.iloc[3:][["feature", "strategischer_fit", "aufwand", "score"]]
        rest.columns = ["Feature", "Fit", "Aufwand", "Score"]
        st.dataframe(rest, use_container_width=True, hide_index=True)
