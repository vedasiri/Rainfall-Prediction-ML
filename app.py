import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Rainfall Prediction AI",
    page_icon="🌧️",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("rainfall_model.pkl")

# Batch Prediction Section

st.markdown("---")
st.header("📂 Batch Prediction Using CSV")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    batch_df = pd.read_csv(uploaded_file)

    predictions = model.predict(batch_df)

    batch_df["Prediction"] = [
        "🌧️ Rainfall"
        if p == 1
        else "☀️ No Rainfall"
        for p in predictions
    ]

    st.success("Prediction Completed")

    st.dataframe(
        batch_df,
        use_container_width=True
    )

    csv = batch_df.to_csv(index=False)

    st.download_button(
        label="⬇ Download Prediction Results",
        data=csv,
        file_name="predictions.csv",
        mime="text/csv"
    )



# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 40%,
        #0f172a 100%
    );
}

.main-title {
    text-align:center;
    font-size:55px;
    font-weight:800;
    color:white;
    margin-bottom:0px;
}

.subtitle {
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:30px;
}

.glass {
    background: rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,0.1);
}

.stButton > button {
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    font-size:22px;
    font-weight:bold;
    background: linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6
    );
    color:white;
}

.stButton > button:hover {
    transform:scale(1.02);
}

.metric-card {
    background: rgba(255,255,255,0.08);
    padding:15px;
    border-radius:15px;
    text-align:center;
}

.result-rain {
    background: linear-gradient(
        90deg,
        #14532d,
        #16a34a
    );
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:30px;
    color:white;
    font-weight:bold;
}

.result-no-rain {
    background: linear-gradient(
        90deg,
        #78350f,
        #f59e0b
    );
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:30px;
    color:white;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="main-title">
🌧️ Rainfall Prediction AI
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Machine Learning Powered Weather Forecast System
</div>
""", unsafe_allow_html=True)

# -----------------------------
# INPUT SECTION
# -----------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    pressure = st.number_input(
        "Pressure",
        900.0, 1100.0, 1010.0
    )

    humidity = st.number_input(
        "Humidity (%)",
        0.0, 100.0, 60.0
    )

    sunshine = st.number_input(
        "Sunshine Hours",
        0.0, 15.0, 5.0
    )

    windspeed = st.number_input(
        "Wind Speed",
        0.0, 100.0, 10.0
    )

with col2:
    dewpoint = st.number_input(
        "Dew Point",
        -20.0, 40.0, 20.0
    )

    cloud = st.number_input(
        "Cloud Cover (%)",
        0.0, 100.0, 50.0
    )

    winddirection = st.number_input(
        "Wind Direction",
        0.0, 360.0, 180.0
    )

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("🚀 Predict Rainfall"):

    sample = pd.DataFrame({
        "pressure": [pressure],
        "dewpoint": [dewpoint],
        "humidity": [humidity],
        "cloud": [cloud],
        "sunshine": [sunshine],
        "winddirection": [winddirection],
        "windspeed": [windspeed]
    })

    prediction = model.predict(sample)

    try:
        probability = model.predict_proba(sample)
        confidence = max(probability[0]) * 100
    except:
        confidence = 0

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction[0] == 1:
        st.markdown(f"""
        <div class="result-rain">
        🌧️ RAINFALL EXPECTED
        <br><br>
        Confidence: {confidence:.2f}%
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div class="result-no-rain">
        ☀️ NO RAINFALL EXPECTED
        <br><br>
        Confidence: {confidence:.2f}%
        </div>
        """, unsafe_allow_html=True)

    # Confidence Meter
    st.subheader("🎯 Prediction Confidence")
    st.progress(confidence / 100)

    # Weather Dashboard
    st.subheader("📊 Weather Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Humidity", f"{humidity}%")
    c2.metric("Cloud", f"{cloud}%")
    c3.metric("Sunshine", f"{sunshine} hrs")
    c4.metric("Wind", f"{windspeed}")

    # Input Data Table
    st.subheader("📝 Input Data")

    st.dataframe(
        sample,
        use_container_width=True
    )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.markdown(
    """
    <center>
    <h4 style='color:#94a3b8'>
    Built with ❤️ using Python, Scikit-Learn, Streamlit & Random Forest
    </h4>
    </center>
    """,
    unsafe_allow_html=True
)