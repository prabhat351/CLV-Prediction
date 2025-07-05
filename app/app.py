import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Load model
model = joblib.load("../models/xgb_model.pkl")

st.set_page_config(page_title="CLV Predictor", layout="wide")
st.title("🛍️ Customer Lifetime Value (CLV) Predictor")

option = st.radio("Select input method:", ["📂 Upload CSV", "✍️ Enter manually"])

def get_segment(clv):
    if clv >= 15000:
        return 'High'
    elif clv >= 5000:
        return 'Medium'
    else:
        return 'Low'

if option == "📂 Upload CSV":
    uploaded_file = st.file_uploader("Upload customer RFM data (.csv)", type="csv")
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            data.columns = data.columns.str.strip()
            if not all(col in data.columns for col in ['Recency', 'Frequency', 'Monetary']):
                st.error("CSV must contain columns: Recency, Frequency, Monetary")
            else:
                X = data[['Recency', 'Frequency', 'Monetary']]
                data['Predicted_CLV'] = model.predict(X)
                data['Segment'] = data['Predicted_CLV'].apply(get_segment)

                st.subheader("📊 CLV Predictions")
                st.dataframe(data)

                st.download_button("📥 Download Results", data.to_csv(index=False), file_name="clv_results.csv")

                col1, col2 = st.columns(2)

                with col1:
                    fig = px.histogram(data, x="Predicted_CLV", color="Segment", nbins=20, title="CLV Distribution")
                    st.plotly_chart(fig, use_container_width=True)

                with col2:
                    segment_counts = data['Segment'].value_counts().reset_index()
                    segment_counts.columns = ['Segment', 'Count']
                    fig2 = px.bar(segment_counts, x='Segment', y='Count', color='Segment', title="Customer Segments")
                    st.plotly_chart(fig2, use_container_width=True)

                st.subheader("🏅 Top 10 Customers by CLV")
                top_customers = data.sort_values(by="Predicted_CLV", ascending=False).head(10)
                st.dataframe(top_customers)

        except Exception as e:
            st.error(f"❌ Error reading file: {e}")

elif option == "✍️ Enter manually":
    st.subheader("🔢 Manually enter RFM values")
    recency = st.number_input("Recency (days)", min_value=0)
    frequency = st.number_input("Frequency (number of purchases)", min_value=0)
    monetary = st.number_input("Monetary (total spend)", min_value=0.0)

    if st.button("🔮 Predict CLV"):
        input_df = pd.DataFrame({
            'Recency': [recency],
            'Frequency': [frequency],
            'Monetary': [monetary]
        })

        predicted_clv = model.predict(input_df)[0]
        segment = get_segment(predicted_clv)

        st.success(f"🎯 Predicted CLV: ₹{predicted_clv:.2f}")
        st.info(f"📊 Customer Segment: {segment}")
