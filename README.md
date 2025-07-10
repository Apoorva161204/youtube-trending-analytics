# YouTube Trending Analytics 🎥📊

This project explores trending YouTube videos in the US and reveals insights using sentiment analysis and visual exploration. It was developed as part of a 2-week internship project.

## 📌 Objective
Analyze patterns in trending YouTube videos including title sentiment, viewership engagement, and upload timing. The goal is to help content creators and marketers better understand what drives video popularity.

## 🛠️ Tools & Technologies Used
- **Python** (Pandas, TextBlob, Matplotlib, Seaborn)
- **Spyder IDE**
- **CSV dataset** (100 trending videos from the US)
  
## 📂 Project Structure
youtube-trending-analytics/
│
├── data/
│ └── US_youtube_sample.csv # Sample dataset
│
├── visuals/
│ ├── sentiment_pie.png # Sentiment distribution chart
│ ├── views_vs_likes.png # Scatter plot
│ └── trending_over_time.png # Time series chart
│
├── src/
│ └── youtube_analysis.py # Python code for analysis
│
├── report/
│ └── youtube_project1_report.pdf # Final internship report 
│
├── cleaned_data.csv # Exported data after preprocessing
└── README.md # Project documentation


## 🔍 Steps Performed

1. Loaded and cleaned the dataset.
2. Applied **TextBlob** to perform sentiment analysis on video titles.
3. Classified each title as **Positive**, **Neutral**, or **Negative**.
4. Created 3 key visualizations:
   - **Pie Chart**: Sentiment distribution of video titles
   - **Scatter Plot**: Relationship between views and likes
   - **Line Chart**: Trending activity over time
5. Exported cleaned data for further use.

## 📊 Visual Outputs
Find all visualizations in the folder.

- Sentiment Pie Chart  
- Views vs Likes Scatter Plot  
- Trending Videos Over Time Line Chart  

## 📈 Key Insights

- **60%** of video titles were Neutral, **40%** were Positive.
- Videos with **Positive sentiment** received more likes.
- **August 9th** had the highest number of trending videos.
- Regular publishing schedules may improve trending chances.

## 📄 Final Report
The complete  project report is available in youtube_project_report.pdf

## 🚀 Future Improvements
- Integrate YouTube comments sentiment
- Use advanced NLP (e.g., VADER, BERT)
- Analyze data across multiple countries
- Add real-time trend tracking using YouTube API

