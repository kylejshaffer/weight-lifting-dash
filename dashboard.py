import streamlit as st
import pandas as pd

url = f"https://docs.google.com/spreadsheets/d/1AQVcWeRl2E8XBl7gF3MJRT9A1RW_XybAaKSZ1drtI4g/gviz/tq?tqx=out:csv&sheet=0"

df = pd.read_csv(url)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%y")

st.header("Weightlifting Dashboard 🏋️")
option = st.selectbox("Select a Category", ["All","Squat and Pull",
                                                   "Push and Hinge",
                                                   "Core and Cardio",
                                                   "Measurements"])

option_map = {
    "Squat and Pull": df[df["Category"] == "Squat and Pull"]["Movement"].unique().tolist(),
    "Push and Hinge": df[df["Category"] == "Push and Hinge"]["Movement"].unique().tolist(),
    "Core and Cardio": df[df["Category"] == "Core and Cardio"]["Movement"].unique().tolist(),
    # "Measurements": df[df["Category"] == "Measurements"]["Movement"].unique().tolist(),
}
c1, c2 = st.columns(2)

if option == "All":
    sub_df = df[df["Category"].isin(list(option_map.keys()))]
else:
    sub_df = df[df["Category"] == option]

print(option)

y_label = "Weight (lbs.)" if option != "Measurements" else "Measurement (cm)"
for ix, movement in enumerate(sub_df["Movement"].unique()):
    if ix % 2 == 0:
        with c1:
            plot_df = df[df["Movement"] == movement]
            st.subheader(f"{plot_df['Movement'].tolist()[0]}")
            st.line_chart(plot_df.set_index("Date"),
                          y="Metric",
                          x_label="Date",
                          y_label=y_label,
                          height="content")
    else:
        with c2:
            plot_df = df[df["Movement"] == movement]
            st.subheader(f"{plot_df['Movement'].tolist()[0]}")
            st.line_chart(plot_df.set_index("Date"),
                          y="Metric",
                          x_label="Date",
                          y_label=y_label,
                          height="content")


# st.table(sub_df)
