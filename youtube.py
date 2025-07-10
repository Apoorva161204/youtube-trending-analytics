import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

df = pd.read_csv(r"C:\Users\Apoorva P\Downloads\US_youtube_trending_larger_sample.csv")

#Perform Sentiment Analysis on video titles
def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

df["sentiment_score"] = df["title"].apply(get_sentiment)

#Classify Sentiment as Positive / Neutral / Negative
def classify_sentiment(score):
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"

df["sentiment_label"] = df["sentiment_score"].apply(classify_sentiment)

#Trending Date Pattern (Line Chart)
df["trending_date"] = pd.to_datetime(df["trending_date"])
trending_counts = df["trending_date"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
trending_counts.plot(kind="line", marker="o", color="blue")
plt.title("Trending Video Count by Date")
plt.xlabel("Date")
plt.ylabel("Number of Trending Videos")
plt.grid(True)
plt.tight_layout()
plt.show()

# Views vs Likes Scatter Plot by Sentiment
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="views",
    y="likes",
    hue="sentiment_label",
    palette={"Positive": "green", "Neutral": "gray", "Negative": "red"}
)
plt.title("Views vs Likes Colored by Sentiment")
plt.xlabel("Views")
plt.ylabel("Likes")
plt.legend(title="Sentiment")
plt.tight_layout()
plt.show()

#Sentiment Distribution (Pie Chart)
df["sentiment_label"].value_counts().plot.pie(
    autopct="%1.1f%%",
    colors=["green", "gray", "red"],
    startangle=90
)
plt.title("Sentiment Distribution of Video Titles")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Export Cleaned Dataset for Dashboard Use
df.to_csv(r"C:\Users\Apoorva P\Downloads\final_youtube_analytics_cleaned.csv", index=False)
print("✅ Cleaned file saved successfully!")
