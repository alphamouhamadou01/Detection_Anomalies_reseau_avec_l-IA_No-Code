import streamlit as st
import pandas as pd
import requests
from streamlit.components.v1 import html

# === CONFIGURATION API DATAROBOT ===
API_KEY = "Njg3MDA3OTFiZTc2MmFiZTA0OTQwMTZhOnBialNEUlRYa1JaenBOb2R5bzNGakVOUFdiUUhpc0dlMk9iQVluTkVBdm89"
DATAROBOT_KEY = "796da197-5b1a-4a7b-9470-62358d5f3e46"
DEPLOYMENT_ID = "686da8de4de70953550d572c"
API_URL = f"https://app.datarobot.com/api/v2/deployments/686da8de4de70953550d572c/predictions"

# === CONFIGURATION DE LA PAGE ===
st.set_page_config(
    page_title="Détection des Anomalies Réseau avec l’IA No-Code",
    layout="centered"
)

# === PERSONNALISATION CSS ===
st.markdown("""
    <style>
    body {
        background-color: white;
    }
    .main, .block-container {
        background-color: white;
        color: #003366;
        border: 3px solid #cce6ff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    .title {
        text-align: center;
        color: #003366;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #444;
        margin-bottom: 30px;
    }
    .info-box {
        border: 2px solid #007acc;
        border-radius: 10px;
        background-color: white;
        padding: 15px;
        margin-bottom: 30px;
    }
    .logo-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .logo-container img {
        width: 180px;
    }
    </style>
""", unsafe_allow_html=True)

# === LOGO IA EN HAUT ===
st.markdown("""
<div class="logo-container">
    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" alt="Logo IA">
</div>
""", unsafe_allow_html=True)

# === EN-TÊTE DE PRÉSENTATION ===
st.markdown('<div class="title">Détection des anomalies réseau avec l’IA No-Code</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Projet présenté par <b>Mouhamadou Alpha BA</b> & <b>Mansor FALL</b><br>Encadré par <b>Dr Alla LÔ</b></div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <b>Université :</b> Université Alioune Diop de Bambey<br>
    <b>UFR :</b> Sciences Appliquées et Technologies de l'Information et de la Communication (SATIC)<br>
    <b>Département :</b> Technologies de l'Information et de la Communication (TIC)<br>
    <b>Filière :</b> Systèmes Réseaux et Télécommunications (SRT)
</div>
""", unsafe_allow_html=True)

# === INTERFACE FONCTIONNELLE ===
st.markdown("""<h4 style='color:#003366;'>Choisissez une méthode :</h4>""", unsafe_allow_html=True)
choix = st.selectbox("", ["Prédiction manuelle", "Prédiction via fichier CSV"])

# === MODE MANUEL ===
if choix == "Prédiction manuelle":
    st.subheader("📝 Entrée manuelle des données :")

    with st.form("manual_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            ifInOctets11 = st.number_input("ifInOctets11", min_value=0)
            ifOutOctets11 = st.number_input("ifOutOctets11", min_value=0)
            ifoutDiscards11 = st.number_input("ifoutDiscards11", min_value=0)
            ifInUcastPkts11 = st.number_input("ifInUcastPkts11", min_value=0)
            ifInNUcastPkts11 = st.number_input("ifInNUcastPkts11", min_value=0)
            ifInDiscards11 = st.number_input("ifInDiscards11", min_value=0)
            ifOutUcastPkts11 = st.number_input("ifOutUcastPkts11", min_value=0)
            ifOutNUcastPkts11 = st.number_input("ifOutNUcastPkts11", min_value=0)
            tcpOutRsts = st.number_input("tcpOutRsts", min_value=0)

        with col2:
            tcpInSegs = st.number_input("tcpInSegs", min_value=0)
            tcpOutSegs = st.number_input("tcpOutSegs", min_value=0)
            tcpPassiveOpens = st.number_input("tcpPassiveOpens", min_value=0)
            tcpRetransSegs = st.number_input("tcpRetransSegs", min_value=0)
            tcpEstabResets = st.number_input("tcpEstabResets", min_value=0)
            tcpCurrEstab = st.number_input("tcpCurrEstab", min_value=0)
            tcp_question_active_opens = st.number_input("tcp?ActiveOpens", min_value=0)
            udpInDatagrams = st.number_input("udpInDatagrams", min_value=0)
            udpOutDatagrams = st.number_input("udpOutDatagrams", min_value=0)
            udpInErrors = st.number_input("udpInErrors", min_value=0)

        with col3:
            udpNoPorts = st.number_input("udpNoPorts", min_value=0)
            ipInReceives = st.number_input("ipInReceives", min_value=0)
            ipInDelivers = st.number_input("ipInDelivers", min_value=0)
            ipOutRequests = st.number_input("ipOutRequests", min_value=0)
            ipOutDiscards = st.number_input("ipOutDiscards", min_value=0)
            ipInDiscards = st.number_input("ipInDiscards", min_value=0)
            ipForwDatagrams = st.number_input("ipForwDatagrams", min_value=0)
            ipOutNoRoutes = st.number_input("ipOutNoRoutes", min_value=0)
            ipInAddrErrors = st.number_input("ipInAddrErrors", min_value=0)
            icmpInMsgs = st.number_input("icmpInMsgs", min_value=0)
            icmpInDestUnreachs = st.number_input("icmpInDestUnreachs", min_value=0)
            icmpOutMsgs = st.number_input("icmpOutMsgs", min_value=0)
            icmpOutDestUnreachs = st.number_input("icmpOutDestUnreachs", min_value=0)
            icmpInEchos = st.number_input("icmpInEchos", min_value=0)

        submit_button = st.form_submit_button("🔎 Lancer la prédiction")

    if submit_button:
        ligne = pd.DataFrame([{  # toutes les variables ici comme dans la version initiale
            "ifInOctets11": ifInOctets11,
            "ifOutOctets11": ifOutOctets11,
            "ifoutDiscards11": ifoutDiscards11,
            "ifInUcastPkts11": ifInUcastPkts11,
            "ifInNUcastPkts11": ifInNUcastPkts11,
            "ifInDiscards11": ifInDiscards11,
            "ifOutUcastPkts11": ifOutUcastPkts11,
            "ifOutNUcastPkts11": ifOutNUcastPkts11,
            "tcpOutRsts": tcpOutRsts,
            "tcpInSegs": tcpInSegs,
            "tcpOutSegs": tcpOutSegs,
            "tcpPassiveOpens": tcpPassiveOpens,
            "tcpRetransSegs": tcpRetransSegs,
            "tcpEstabResets": tcpEstabResets,
            "tcpCurrEstab": tcpCurrEstab,
            "tcp?ActiveOpens": tcp_question_active_opens,
            "udpInDatagrams": udpInDatagrams,
            "udpOutDatagrams": udpOutDatagrams,
            "udpInErrors": udpInErrors,
            "udpNoPorts": udpNoPorts,
            "ipInReceives": ipInReceives,
            "ipInDelivers": ipInDelivers,
            "ipOutRequests": ipOutRequests,
            "ipOutDiscards": ipOutDiscards,
            "ipInDiscards": ipInDiscards,
            "ipForwDatagrams": ipForwDatagrams,
            "ipOutNoRoutes": ipOutNoRoutes,
            "ipInAddrErrors": ipInAddrErrors,
            "icmpInMsgs": icmpInMsgs,
            "icmpInDestUnreachs": icmpInDestUnreachs,
            "icmpOutMsgs": icmpOutMsgs,
            "icmpOutDestUnreachs": icmpOutDestUnreachs,
            "icmpInEchos": icmpInEchos
        }])

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "DataRobot-Key": DATAROBOT_KEY,
            "Content-Type": "text/csv"
        }

        response = requests.post(API_URL, headers=headers, data=ligne.to_csv(index=False))
        if response.status_code == 200:
            pred = response.json()["data"][0]["prediction"]
            st.success(f"✅ Prédiction : **{pred}**")
        else:
            st.error("Erreur API")

# === MODE CSV ===
elif choix == "Prédiction via fichier CSV":
    st.subheader("📁 Uploader un fichier CSV :")
    fichier = st.file_uploader("Fichier CSV", type="csv")
    if fichier:
        df = pd.read_csv(fichier)
        st.dataframe(df.head())
        if st.button("📤 Envoyer à DataRobot"):
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "DataRobot-Key": DATAROBOT_KEY,
                "Content-Type": "text/csv"
            }
            response = requests.post(API_URL, headers=headers, data=df.to_csv(index=False))
            if response.status_code == 200:
                res = pd.json_normalize(response.json()["data"])
                st.success("✅ Prédictions reçues")
                st.dataframe(res[["rowId", "prediction"]])
            else:
                st.error("❌ Erreur API")
