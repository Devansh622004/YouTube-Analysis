# 📈 YouTube Trending Videos Analysis Dashboard

An interactive web application built with **Python**, **Streamlit**, and **Pandas** to analyze and visualize YouTube trending data. This project converts a static Jupyter Notebook statistical analysis into a dynamic, user-friendly dashboard.

## ✨ Features
- **Interactive Data Viewing:** Toggle raw datasets and statistical descriptions directly in the UI.
- **Dynamic Visualizations:** Modify chart criteria (e.g., Title Length vs. Views) using real-time sliders and inputs.
- **Data Visualizations:** 
  - Pie charts examining Title Capitalization behavior.
  - Distribution histograms for title lengths.
  - Correlation Heatmaps across various video metrics.
  - Word Clouds revealing the most common terms in trending capabilities.

## 🛠️ Technologies Used
- **Python 3.x**
- **Streamlit** - For the frontend UI and web application framework.
- **Pandas & NumPy** - Data cleaning, preparation, and analysis.
- **Matplotlib & Seaborn** - Charting and advanced statistical graphic generation.
- **WordCloud** - Custom text analysis visualization.

## 🚀 Live Demo
*(Once deployed to Streamlit Cloud, place your public URL here!)*
> [Link to live app]()

## 💻 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Devansh622004/YouTube-Analysis.git
   cd your-repo-name
   ```

2. **Ensure you have the dataset:**
   Make sure `USvideos.csv` is present in the root directory.

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application:**
   ```bash
   python -m streamlit run app.py
   ```

5. **Open in Browser:**
   The application will automatically pop up in your default web browser on `http://localhost:8501`.

## 📁 Repository Structure
```text
.
├── analysis.ipynb      # Original data analysis notebook
├── app.py              # Main Streamlit web application
├── requirements.txt    # Python dependencies
├── USvideos.csv        # Dataset
└── README.md           # Documentation
```

## 📊 Data Source
Dataset used is based on the Kaggle **Trending YouTube Video Statistics**. It provides a daily record of top-trending YouTube videos.
