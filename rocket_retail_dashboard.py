import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the results folder (relative to this script's location)
results_folder = 'results'

# Configure page layout
st.set_page_config(page_title="Retail Rocket EDA Dashboard", layout="wide")

# Page title
st.title("Exploratory Data Analysis - Retail Rocket Dataset")
st.markdown("This dashboard showcases the first phase of exploratory insights generated from the Retail Rocket ecommerce dataset.")

# Utility to load CSV summaries
def load_summary(filename):
    file_path = os.path.join(results_folder, filename)
    return pd.read_csv(file_path)

# Utility to display plots with correct argument
def display_plot(plot_filename, caption_text):
    file_path = os.path.join(results_folder, plot_filename)
    st.image(file_path, caption=caption_text, use_container_width=True)

# Sidebar navigation
section = st.sidebar.radio("Select Section", (
    "Event Type Distribution",
    "User Activity Distribution",
    "Session Analysis",
    "Time Gap Analysis"
))

# Event Type Distribution
if section == "Event Type Distribution":
    st.header("Event Type Distribution")

    display_plot("event_type_distribution.png", "Distribution of Event Types")

    st.markdown("**Insight:** Majority of user actions are simple 'view' events, while 'addtocart' and 'transaction' events occur far less frequently. This shows a browsing-dominant user base, which is a typical ecommerce behaviour.")

    event_type_summary = load_summary("event_type_counts.csv")
    st.subheader("Summary Table")
    st.dataframe(event_type_summary)

# User Activity Distribution
elif section == "User Activity Distribution":
    st.header("User Activity Distribution (Events per Visitor)")

    display_plot("visitor_event_distribution_full.png", "Full Range Distribution")
    display_plot("visitor_event_distribution_zoomed.png", "Zoomed (0-100 Events)")

    st.markdown("**Insight:** Most visitors perform only a few actions, but a small subset exhibit extremely high activity levels. This highlights the need for behaviour-based segmentation.")

    activity_summary = load_summary("sessions_per_visitor.csv")
    st.subheader("Sessions per Visitor Summary")
    st.dataframe(activity_summary)

# Session Analysis
elif section == "Session Analysis":
    st.header("Events per Session")

    display_plot("events_per_session_distribution_full.png", "Full Range Distribution")
    display_plot("events_per_session_distribution_zoomed.png", "Zoomed (0-50 Events)")

    st.markdown("**Insight:** Sessions are typically short, often consisting of just a few events. However, some sessions are densely packed with hundreds of interactions, indicating either intense user engagement or automated activity.")

    session_length_summary = load_summary("events_per_session.csv")
    st.subheader("Session Length Summary")
    st.dataframe(session_length_summary)

# Time Gap Analysis
elif section == "Time Gap Analysis":
    st.header("Time Gap Between Events")

    display_plot("time_gap_distribution_log.png", "Log Distribution of Time Gaps Between Consecutive Events")

    st.markdown("**Insight:** Most consecutive events occur within a few minutes of each other, but the dataset also shows sessions with long inactivity gaps, which helps inform session timeout thresholds.")

# Footer
st.markdown("---")
st.markdown("_This dashboard is an initial step in preparing the dataset for behavioural segmentation._")
