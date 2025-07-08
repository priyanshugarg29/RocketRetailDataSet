
import streamlit as st
import pandas as pd
from pathlib import Path

# Setting results directory
results_folder = Path(__file__).parent / 'results'

# Custom function to load images safely
def load_plot(image_name, caption):
    file_path = results_folder / image_name
    if file_path.exists():
        st.image(str(file_path), use_container_width=True, caption=caption)
    else:
        st.warning(f"Plot not found: {file_path}")

# Custom function to load dataframes safely
def load_summary(csv_name, section_title):
    file_path = results_folder / csv_name
    if file_path.exists():
        st.subheader(section_title)
        df = pd.read_csv(file_path)
        st.dataframe(df, use_container_width=True)
    else:
        st.warning(f"Summary file not found: {file_path}")

# -----------------------------------------
# Streamlit App Layout
# -----------------------------------------

st.title('Exploratory Data Analysis of Retail Rocket Dataset')
st.markdown('---')

# Section 1: Event Type Distribution
st.header("Event Type Distribution")
load_plot('event_type_distribution.png', 'Breakdown of views, add-to-carts, and transactions.')
load_summary('event_type_counts.csv', 'Event Type Count Summary')
st.markdown('**Insight:** This distribution reflects the natural behaviour of ecommerce customers, where most interactions are passive product views, while a small proportion lead to purchase-related actions.')

# Section 2: Visitor Activity Distribution
st.header("Visitor Activity Distribution")
col1, col2 = st.columns(2)
with col1:
    load_plot('visitor_event_distribution_full.png', 'Event counts per visitor (Full Range)')
with col2:
    load_plot('visitor_event_distribution_zoomed.png', 'Event counts per visitor (0-100 Events)')
load_summary('visitor_event_counts.csv', 'Visitor Event Counts Summary')
st.markdown('**Insight:** A vast majority of visitors interact only a handful of times, while a few power users demonstrate unusually high activity — common in ecommerce visitor traffic patterns.')

# Section 3: Sessions per Visitor Distribution
st.header("Sessions per Visitor Distribution")
load_plot('sessions_per_visitor_distribution.png', 'Distribution of number of sessions each visitor has.')
st.markdown('**Insight:** Most users have a single session, but a few highly engaged users or bots initiate hundreds of sessions.')

# Section 4: Events per Session Distribution
st.header("Events per Session Distribution")
col3, col4 = st.columns(2)
with col3:
    load_plot('events_per_session_distribution_full.png', 'Events per session (Full Range)')
with col4:
    load_plot('events_per_session_distribution_zoomed.png', 'Events per session (0-50 Events)')
load_summary('events_per_session.csv', 'Events per Session Summary')
st.markdown('**Insight:** The typical session is short, often involving only 1–3 actions, while a few sessions reflect much deeper engagement, suggesting purchase journeys or automated activity.')

# Section 5: Time Gaps Between Events
st.header("Time Gap Between Consecutive Events")
load_plot('time_gap_distribution_log.png', 'Log-distributed histogram of time gaps between consecutive user events.')
st.markdown('**Insight:** The majority of actions occur within a few minutes of each other, but the right-skewed distribution highlights longer breaks that likely separate user sessions.')

# Closing note
st.markdown('---')
st.success("EDA dashboard prepared for behavioural session analysis and downstream modelling. All insights reflect the organic patterns of online retail customer engagement.")

