import streamlit as st
import numpy as np
import re
import pickle

# Page settings
st.set_page_config(layout="wide")

# Title
st.markdown("""
<div style='text-align:center'>
    <h1 style='color:#009999;'>Industrial Copper Modeling Application</h1>
</div>
""", unsafe_allow_html=True)

# Dropdown options
status_options = ['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
item_type_options = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
country_options = sorted([28., 25., 30., 32., 38., 78., 27., 77., 113., 79., 26., 39., 40., 84., 80., 107., 89.])
application_options = sorted([10., 41., 28., 59., 15., 4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67., 79., 3., 99., 2., 5., 39., 69., 70., 65., 58., 68.])
product_refs = ['611112', '611728', '628112', '628117', '628377', '640400', '640405', '640665', 
                '611993', '929423819', '1282007633', '1332077137', '164141591', '164336407', 
                '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662', 
                '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738', 
                '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']

# -------------------- Utility Functions --------------------
def is_valid_input(inputs):
    pattern = r"^(?:\d+|\d*\.\d+)$"
    return all(re.match(pattern, val) for val in inputs)

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def predict_price(data):
    model = load_pickle("source/model.pkl")
    scaler = load_pickle("source/scaler.pkl")
    ohe = load_pickle("source/t.pkl")
    be = load_pickle("source/s.pkl")

    transformed = np.array([[np.log(float(data['qty'])), data['application'],
                             np.log(float(data['thickness'])), float(data['width']),
                             data['country'], float(data['customer']),
                             int(data['product']), data['item'], data['status']]])

    item_ohe = ohe.transform(transformed[:, [7]]).toarray()
    status_be = be.transform(transformed[:, [8]]).toarray()
    features = np.concatenate((transformed[:, :7], item_ohe, status_be), axis=1)
    features_scaled = scaler.transform(features)
    pred = model.predict(features_scaled)[0]
    return np.exp(pred)

def predict_status(data):
    model = load_pickle("source/cmodel.pkl")
    scaler = load_pickle("source/cscaler.pkl")
    ohe = load_pickle("source/ct.pkl")

    transformed = np.array([[np.log(float(data['qty'])), np.log(float(data['selling_price'])),
                             data['application'], np.log(float(data['thickness'])),
                             float(data['width']), data['country'],
                             int(data['customer']), int(data['product']), data['item']]])

    item_ohe = ohe.transform(transformed[:, [8]]).toarray()
    features = np.concatenate((transformed[:, :8], item_ohe), axis=1)
    features_scaled = scaler.transform(features)
    return model.predict(features_scaled)[0]

# -------------------- Streamlit Tabs --------------------
tab1, tab2 = st.tabs(["PREDICT SELLING PRICE", "PREDICT STATUS"])

# -------------------- Tab 1: Predict Price --------------------
with tab1:
    with st.form("form_price"):
        col1, col2, col3 = st.columns([5, 1, 5])
        with col1:
            status = st.selectbox("Status", status_options, key="status")
            item = st.selectbox("Item Type", item_type_options, key="item")
            country = st.selectbox("Country", country_options, key="country")
            application = st.selectbox("Application", application_options, key="application")
            product = st.selectbox("Product Reference", product_refs, key="product")
        with col3:
            st.markdown('<p style="color:#00999980;">NOTE: Min & Max given for reference, you can enter any value</p>', unsafe_allow_html=True)
            qty = st.text_input("Quantity Tons")
            thickness = st.text_input("Thickness")
            width = st.text_input("Width")
            customer = 15216550
            submit = st.form_submit_button("PREDICT SELLING PRICE")

        if submit:
            inputs = [qty, thickness, width, customer]
            if not is_valid_input(inputs):
                st.error("Invalid input! Ensure all numeric fields are properly filled.")
            else:
                data = {
                    'qty': qty, 'thickness': thickness, 'width': width, 'customer': customer,
                    'status': status, 'item': item, 'country': country,
                    'application': application, 'product': product
                }
                prediction = predict_price(data)
                st.success(f"Predicted Selling Price: ₹ {prediction:,.2f}")

# -------------------- Tab 2: Predict Status --------------------
with tab2:
    with st.form("form_status"):
        col1, col2, col3 = st.columns([5, 1, 5])
        with col1:
            cqty = st.text_input("Quantity Tons")
            cthickness = st.text_input("Thickness")
            cwidth = st.text_input("Width")
            ccustomer = 15216550
            cselling = st.text_input("Selling Price")
        with col3:
            citem = st.selectbox("Item Type", item_type_options, key="citem")
            ccountry = st.selectbox("Country", country_options, key="ccountry")
            capplication = st.selectbox("Application", application_options, key="capplication")
            cproduct = st.selectbox("Product Reference", product_refs, key="cproduct")
            csubmit = st.form_submit_button("PREDICT STATUS")

        if csubmit:
            inputs = [cqty, cthickness, cwidth, ccustomer, cselling]
            if not is_valid_input(inputs):
                st.error("Invalid input! Ensure all numeric fields are properly filled.")
            else:
                data = {
                    'qty': cqty, 'thickness': cthickness, 'width': cwidth, 'customer': ccustomer,
                    'selling_price': cselling, 'item': citem, 'country': ccountry,
                    'application': capplication, 'product': cproduct
                }
                status_pred = predict_status(data)
                if status_pred == 1:
                    st.success("✅ The Status is: WON")
                else:
                    st.warning("❌ The Status is: LOST")

# Footer
st.markdown("""
            ## <span style="font-size: 18px;">:orange[Created By]:</span><br>
            Raghavendran S,<br>
            Data Scientist Aspirant,<br>
            email-id: [raghavendranhp@gmail.com](mailto:raghavendranhp@gmail.com)<br>
            [LinkedIn-Profile](https://www.linkedin.com/in/raghavendransundararajan/),<br>
            [GitHub-Link](https://github.com/raghavendranhp)
        """, unsafe_allow_html=True)
