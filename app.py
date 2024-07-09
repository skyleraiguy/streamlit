import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data based on the provided pricing information
data = {
    "Venue": [
        "Delta Center", "Delta Center", "Delta Center", "Delta Center", "Delta Center", "Delta Center",
        "Delta Center", "Delta Center", "Delta Center", "Delta Center", "Delta Center", "Delta Center",
        "Salt Palace", "Salt Palace", "Salt Palace", "Salt Palace", "Salt Palace", "Salt Palace",
        "Salt Palace", "Salt Palace", "Salt Palace", "Salt Palace", "Salt Palace", "Salt Palace",
        "Mountain America Expo Center", "Mountain America Expo Center", "Mountain America Expo Center", 
        "Mountain America Expo Center", "Mountain America Expo Center", "Mountain America Expo Center",
        "Mountain America Expo Center", "Mountain America Expo Center", "Mountain America Expo Center",
        "Mountain America Expo Center", "Mountain America Expo Center", "Mountain America Expo Center"
    ],
    "Crowd Size": [
        1000, 2000, 4000, 1000, 2000, 4000, 1000, 2000, 4000, 1000, 2000, 4000,
        1000, 2000, 4000, 1000, 2000, 4000, 1000, 2000, 4000, 1000, 2000, 4000,
        1000, 2000, 4000, 1000, 2000, 4000, 1000, 2000, 4000, 1000, 2000, 4000
    ],
    "Type": [
        "Weekday", "Weekday", "Weekday", "Weekend", "Weekend", "Weekend", "Weekday", "Weekday", "Weekday", "Weekend", "Weekend", "Weekend",
        "Weekday", "Weekday", "Weekday", "Weekend", "Weekend", "Weekend", "Weekday", "Weekday", "Weekday", "Weekend", "Weekend", "Weekend",
        "Weekday", "Weekday", "Weekday", "Weekend", "Weekend", "Weekend", "Weekday", "Weekday", "Weekday", "Weekend", "Weekend", "Weekend"
    ],
    "Min Price": [
        20000, 26000, 29000, 25000, 31000, 34000, 15000, 21000, 26000, 20000, 26000, 31000,
        15000, 21000, 26000, 20000, 26000, 31000, 15000, 21000, 26000, 20000, 26000, 31000,
        18000, 24000, 29000, 23000, 29000, 34000, 18000, 24000, 29000, 23000, 29000, 34000
    ],
    "Max Price": [
        30000, 36000, 39000, 35000, 41000, 44000, 25000, 31000, 36000, 30000, 36000, 41000,
        25000, 31000, 36000, 30000, 36000, 41000, 25000, 31000, 36000, 30000, 36000, 41000,
        28000, 34000, 39000, 33000, 39000, 44000, 28000, 34000, 39000, 33000, 39000, 44000
    ]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Conference Cost Analysis")

# Sidebar filters
selected_venue = st.sidebar.selectbox("Select Venue", df["Venue"].unique())
selected_type = st.sidebar.radio("Select Day Type", ["Weekday", "Weekend"])

# Filter data based on user selection
filtered_data = df[(df["Venue"] == selected_venue) & (df["Type"] == selected_type)]

st.write(f"### {selected_venue} - {selected_type} Pricing")

# Set the style of the visualization
sns.set(style="whitegrid")

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(filtered_data["Crowd Size"] - 100, filtered_data["Min Price"], width=200, label="Min Price", align='center')
ax.bar(filtered_data["Crowd Size"] + 100, filtered_data["Max Price"], width=200, label="Max Price", align='center')

ax.set_title(f"{selected_venue} - {selected_type} Pricing")
ax.set_xlabel("Crowd Size")
ax.set_ylabel("Price ($)")
ax.legend()

st.pyplot(fig)

# Display the data table
st.write("### Pricing Data")
st.write(filtered_data)
