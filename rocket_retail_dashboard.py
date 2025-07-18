import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

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

# Set Streamlit page layout and title
st.set_page_config(page_title="RetailRocket EDA", layout="wide")

# --------------------------------------------
# Section: Top 3-Step Interaction Sequences
# --------------------------------------------

# Defining common interaction sequences
top_patterns = [
    ("view ➝ view ➝ view", 503814),
    ("view ➝ view ➝ addtocart", 23297),
    ("view ➝ addtocart ➝ view", 20610),
    ("addtocart ➝ view ➝ view", 12608),
    ("view ➝ addtocart ➝ transaction", 10492),
    ("addtocart ➝ view ➝ addtocart", 5281),
    ("addtocart ➝ addtocart ➝ addtocart", 5213),
    ("view ➝ addtocart ➝ addtocart", 4702),
    ("addtocart ➝ transaction ➝ view", 4658),
    ("transaction ➝ view ➝ view", 4474)
]

df_patterns = pd.DataFrame(top_patterns, columns=["Interaction Pattern", "Count"])

# Display table of top patterns
st.markdown("### Top 3-Step Interaction Patterns")
st.dataframe(df_patterns.style.format({"Count": "{:,}"}))

# Horizontal bar chart for visual clarity
fig, ax = plt.subplots(figsize=(8, 5))
df_patterns[::-1].plot(
    kind="barh",
    x="Interaction Pattern",
    y="Count",
    ax=ax,
    color="steelblue",
    legend=False
)
ax.set_title("Top 3-Step Interaction Sequences", fontsize=14)
ax.set_xlabel("Count")
ax.set_ylabel("Interaction Pattern")
st.pyplot(fig)

# --------------------------------------------
# Interpretation of Findings
# --------------------------------------------

st.markdown("#### Interpretation")
st.markdown(
    "The most frequent pattern `view ➝ view ➝ view` reflects a strong browsing tendency, "
    "which is commonly observed in ecommerce user behavior (Moe, 2003). "
    "Patterns involving transitions like `view ➝ addtocart ➝ transaction` signify purposeful, goal-directed sessions "
    "which likely end in purchase. Identifying such sequences is important for customer segmentation, "
    "conversion prediction, and session-based recommendation models (Montgomery et al., 2004)."
)

# --------------------------------------------
# References (Harvard Style)
# --------------------------------------------

st.markdown("### References")
st.markdown("""
- Moe, W. W. (2003). Buying, searching, or browsing: Differentiating between online shoppers using in-store navigational clickstream. *Journal of Consumer Psychology*, 13(1-2), 29–39.
- Montgomery, A. L., Li, S., Srinivasan, K., & Liechty, J. (2004). Modeling online browsing and path analysis using clickstream data. *Marketing Science*, 23(4), 579–595.
""")

# Closing note
st.markdown('---')
st.success("EDA dashboard prepared for behavioural session analysis and downstream modelling. All insights reflect the organic patterns of online retail customer engagement.")
