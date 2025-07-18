
# streamlit_dashboard_updated.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="RetailRocket EDA", layout="wide")

# Section: Top 3-Step Interaction Sequences

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

st.markdown("### Top 3-Step Interaction Patterns")
st.dataframe(df_patterns.style.format({"Count": "{:,}"}))

# Horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 5))
df_patterns[::-1].plot(kind="barh", x="Interaction Pattern", y="Count", ax=ax, color="steelblue", legend=False)
ax.set_title("Top 3-Step Interaction Sequences")
ax.set_xlabel("Count")
ax.set_ylabel("Interaction Pattern")
st.pyplot(fig)

# Interpretation
st.markdown("#### Interpretation")
st.write(
    "The most frequent pattern `view ➝ view ➝ view` reflects a strong browsing tendency, "
    "which is a common user behavior in ecommerce platforms (Moe, 2003). Patterns like "
    "`view ➝ addtocart ➝ transaction` reflect goal-directed behavior indicative of "
    "purchase intent. Modeling such sequences can inform customer intent classification, "
    "segment design, and sequence-aware recommendation strategies (Montgomery et al., 2004)."
)

# References
st.markdown("### References")
st.markdown(
    "- Moe, W. W. (2003). Buying, searching, or browsing: Differentiating between online shoppers using in-store navigational clickstream. *Journal of Consumer Psychology*, 13(1-2), 29–39.
"
    "- Montgomery, A. L., Li, S., Srinivasan, K., & Liechty, J. (2004). Modeling online browsing and path analysis using clickstream data. *Marketing Science*, 23(4), 579–595."
)

# Note: This block is isolated for demonstration purposes. Additional EDA views should be added above.
