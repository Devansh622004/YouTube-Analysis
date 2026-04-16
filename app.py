import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
import wordcloud
from collections import Counter

# Set page config for better UI
st.set_page_config(page_title="YouTube Videos Analysis", page_icon="📈", layout="wide")

st.title("📈 YouTube Trending Videos Analysis")
st.markdown("This dashboard converts the Jupyter Notebook analysis into a fully interactive Streamlit application.")

PLOT_COLORS = ["#268bd2", "#0052CC", "#FF5722", "#b58900", "#003f5c"]
pd.options.display.float_format = '{:.2f}'.format

# Apply seaborn styling
sns.set_theme(style="ticks")
plt.rc('figure', figsize=(8, 5), dpi=100)
plt.rc('axes', labelpad=20, facecolor="#ffffff", linewidth=0.4, grid=True, labelsize=14)
plt.rc('patch', linewidth=0)
plt.rc('xtick.major', width=0.2)
plt.rc('ytick.major', width=0.2)
plt.rc('grid', color='#9E9E9E', linewidth=0.4)
plt.rc('font', family='Arial', weight='400', size=10)
plt.rc('text', color='#282828')
plt.rc('savefig', pad_inches=0.3, dpi=300)

@st.cache_data
def load_data():
    # Make sure USvideos.csv is in the same directory
    try:
        df = pd.read_csv("USvideos.csv")
        df["description"] = df["description"].fillna(value="")
        return df
    except FileNotFoundError:
        st.error("Dataset 'USvideos.csv' not found. Please ensure it is in the same directory.")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    st.sidebar.header("📊 Dashboard Options")
    # Sidebar input
    show_raw_data = st.sidebar.checkbox("Show Raw Data", False)
    
    if show_raw_data:
        st.subheader("Raw Data Preview")
        st.dataframe(df.head())

        st.subheader("Data Description")
        st.dataframe(df.describe())

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Do Video Titles Contain Capitalized Words?")
        def contains_capitalized_word(s):
            if not isinstance(s, str):
                return False
            for w in str(s).split():
                if w.isupper():
                    return True
            return False

        df["contains_capitalized"] = df["title"].apply(contains_capitalized_word)
        value_counts = df["contains_capitalized"].value_counts().to_dict()
        
        fig1, ax1 = plt.subplots()
        ax1.pie([value_counts.get(False, 0), value_counts.get(True, 0)], labels=['No', 'Yes'], 
                   colors=['#003f5c', '#ffa600'], textprops={'color': '#040204'}, startangle=45)
        ax1.axis('equal')
        st.pyplot(fig1)

    with col2:
        st.subheader("Title Length Distribution")
        df["title_length"] = df["title"].apply(lambda x: len(str(x)))
        
        fig2, ax2 = plt.subplots()
        # Using histplot as distplot is deprecated in newer seaborn versions
        sns.histplot(df["title_length"], kde=False, color=PLOT_COLORS[4], ax=ax2)
        ax2.set(xlabel="Title Length", ylabel="No. of videos", xticks=range(0, 110, 10))
        st.pyplot(fig2)

    st.markdown("---")
    st.subheader("Views vs Title Length")
    
    # Use Streamlit slider to add interactivity
    max_length = st.slider("Filter by Maximum Title Length", min_value=10, max_value=100, value=100)
    filtered_df = df[df["title_length"] <= max_length]
    
    fig3, ax3 = plt.subplots()
    ax3.scatter(x=filtered_df['views'], y=filtered_df['title_length'], color=PLOT_COLORS[2], edgecolors="#000000", linewidths=0.5)
    ax3.set(xlabel="Views", ylabel="Title Length")
    # Adding tick formatter for views to avoid scientific notation
    ax3.get_xaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.xticks(rotation=45)
    st.pyplot(fig3)

    st.markdown("---")
    # Because word cloud generation can take time, let's put it on its own or add a button
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Correlation Heatmap")
        
        # Select numeric and bool types only
        num_bool_df = df.select_dtypes(include=['number', 'bool'])
        h_labels = [x.replace('_', ' ').title() for x in list(num_bool_df.columns.values)]
        
        fig4, ax4 = plt.subplots(figsize=(8,6))
        sns.heatmap(num_bool_df.corr(), annot=True, 
                    xticklabels=h_labels, yticklabels=h_labels, cmap=sns.cubehelix_palette(as_cmap=True), ax=ax4)
        st.pyplot(fig4)

    with col4:
        st.subheader("Title Word Cloud")
        
        if st.button("Generate Word Cloud (Takes time)"):
            with st.spinner("Generating..."):
                title_words = list(df["title"].apply(lambda x: str(x).split()))
                title_words = [x for y in title_words for x in y]
                wc = wordcloud.WordCloud(width=800, height=500, 
                                         collocations=False, background_color="white", 
                                         colormap="tab20b").generate(" ".join(title_words))
                fig5, ax5 = plt.subplots(figsize=(8, 5))
                ax5.imshow(wc, interpolation='bilinear')
                ax5.axis("off")
                st.pyplot(fig5)
