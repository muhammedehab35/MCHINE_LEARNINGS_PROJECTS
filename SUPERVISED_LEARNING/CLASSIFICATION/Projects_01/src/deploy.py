import streamlit as st
import pandas as pd
import joblib
import base64

# Charger le modèle
model = joblib.load('fraud_detection_model.pkl')

# Fonction pour convertir l'image en base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Fonction pour définir le background
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Appliquer le background (remplacez 'background.jpg' par le nom de votre fichier)
set_png_as_page_bg('background.jpg')

# Titre et description

st.title("Fraud Detection App")
st.write("This app detects fraudulent transactions using a machine learning model.")
st.markdown("## Please enter the transaction details below:")


st.divider()


transaction_type = st.selectbox("Transaction Type", ["CASH_IN", "CASH_OUT", "DEPOSIT", "PAYMENT", "TRANSFER"])

amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0, step=0.01)

oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=5000.0, step=0.01)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=4000.0, step=0.01)
oldbalaceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=1000.0, step=0.01)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=2000.0, step=0.01)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalaceDest],
        'newbalanceDest': [newbalanceDest]
    })

    prediction = model.predict(input_data)[0]

    st.subheader(f"prediction : {int(prediction)}")

    if prediction == 1:
        st.error("This transaction is likely fraudulent.")
    else:
        st.success("This transaction is likely legitimate.")

