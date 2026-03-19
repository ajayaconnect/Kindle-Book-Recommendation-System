# 📚 Kindle Book Recommendation System

> **Unsupervised Learning · NLP · Collaborative Filtering · Streamlit Deployment**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-4B9CD3?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Joblib](https://img.shields.io/badge/Model-Joblib%20%7C%20Pickle-4CAF50?style=flat-square)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ajaya210/Kindle-Book-Recommendation-System/blob/main/Copy_of_Book_Recommendation_System_(Unsupervised_Learning_Project).ipynb)

---

## 📌 Project Overview

With millions of books across genres, readers often face discovery paralysis. This project builds a **multi-strategy book recommendation engine** that leverages the power of unsupervised learning to provide personalised recommendations — modelled on how platforms like Amazon and Netflix serve content.

Three complementary recommendation strategies were implemented, evaluated, and compared. The best-performing model was serialised and deployed as an **interactive Streamlit web application**.

**Key business applications:**
- Help readers discover books aligned with their preferences
- Reduce time-to-discovery on digital reading platforms
- Power personalised homepage and "You may also like" features
- Increase engagement, session time, and repeat visits

---

## 📊 Model Performance Summary

| Model | Strategy | Recall@5 | Recall@10 | Hit Rate |
|-------|----------|----------|-----------|---------|
| **Collaborative Filtering ⭐ Deployed** | User behaviour patterns | **95.76%** | **95.76%** | High |
| Content-Based Filtering | TF-IDF + cosine similarity | ~0.15% | ~0.15% | Low |
| k-NN (Cosine Similarity) | Book-to-book similarity | — | — | Evaluated |

> **Primary metric: Recall@N** — measures whether the relevant book appears in the top-N recommendations for a user.

---

## 🗂️ Datasets

Three interconnected CSV files were used:

### `Books.csv`
| Column | Description |
|--------|-------------|
| `ISBN` | Unique book identifier |
| `Book-Title` | Title of the book |
| `Book-Author` | Author name |
| `Year-Of-Publication` | Publication year |
| `Publisher` | Publishing company |

### `Users.csv`
| Column | Description |
|--------|-------------|
| `User-ID` | Unique user identifier |
| `Location` | User's country/region |
| `Age` | User age (positively skewed; outliers treated) |

### `Ratings.csv`
| Column | Description |
|--------|-------------|
| `User-ID` | Reviewer's user ID |
| `ISBN` | ISBN of rated book |
| `Book-Rating` | Rating (1–10) |

### Final Merged Dataset
After filtering (users with ≥200 ratings + books with ≥50 ratings):

```
Rows: 59,850 | Columns: 10 | Qualified Users: 900 | Total Ratings: 5.2 Lakh
```

---

## ⚙️ ML Pipeline

```
Load 3 CSVs (Books / Users / Ratings)
        ↓
Data Cleaning: column renaming, type conversion, replace_df_value()
        ↓
Data Filtering: users ≥200 ratings | books ≥50 ratings
        ↓
EDA (15 Charts): distributions, top authors/publishers/books, correlations
        ↓
Hypothesis Testing: 3 × T-tests (age, ratings, engagement)
        ↓
NLP Text Preprocessing (for Content-Based model):
  Expand Contractions → Remove Punctuation → Remove URLs
  → Remove Stopwords → Lemmatization → TF-IDF Vectorization
        ↓
Model 1: Collaborative Filtering
Model 2: Content-Based Filtering (TF-IDF + Cosine Similarity)
Model 3: k-NN with Cosine Distance
        ↓
Evaluation: Recall@5, Recall@10, Hit Rate
        ↓
Best Model Serialisation → FastAPI → Streamlit Deployment
```

---

## 🤖 Models in Detail

### Model 1 — Collaborative Filtering ⭐ Best
Leverages collective user behaviour — users who have rated books similarly in the past receive similar recommendations.

- **Recall@5**: 95.76%
- **Recall@10**: 95.76%
- Recommends from a pool of 900 qualified users × 5.2L ratings
- **Selected for deployment** due to outstanding recall performance

### Model 2 — Content-Based Filtering
Builds a TF-IDF vector profile for each book and each user (weighted average of interacted book profiles). Recommends books with highest cosine similarity to the user's profile.

- Text preprocessing pipeline: contraction expansion → punctuation removal → URL removal → stopword removal → lemmatization → TF-IDF (5000 features)
- **Limitation**: Very low recall (~0.15%) due to sparse content overlap in this dataset

### Model 3 — k-NN with Cosine Similarity
k-Nearest Neighbours in a high-dimensional space defined by book features. Distance metric: cosine similarity. Evaluated using **Hit Rate** (at least one relevant book in top-k recommendations).

---

## 🔍 Key EDA Insights (15 Charts)

| Insight | Finding |
|---------|---------|
| Most rated book | Wild Animus |
| Most popular book (2nd) | The Lovely Bones: A Novel |
| Most prolific author | Nora Roberts |
| Top publisher | Ballantine Books |
| Peak publication year | 2000 (with sharp decline in 2004) |
| Core user age group | 25–35 years (positively skewed) |
| Most frequent ratings | 7–10 (positive bias in dataset) |
| Top author countries | USA · UK · Canada |
| Multicollinearity | None detected (correlation heatmap) |
| User engagement trend | Upward over time (line plot) |

---

## 🧪 Hypothesis Testing

Three T-tests were performed on independent group comparisons:

1. **USA vs Canada average user age** — tested for regional demographic difference
2. **Age of high-raters (≥5) vs low-raters (<5)** — tested age-engagement relationship
3. **Number of ratings for high-rated vs low-rated books** — tested popularity-quality link

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.x |
| **Data** | Pandas, NumPy |
| **ML** | Scikit-learn (k-NN, Collaborative Filtering) |
| **NLP** | NLTK, TF-IDF Vectorizer, Cosine Similarity |
| **Text Norm** | WordNetLemmatizer, PorterStemmer |
| **Statistics** | Scipy (T-test), Statsmodels |
| **Visualization** | Matplotlib, Seaborn |
| **Model Saving** | Joblib, Pickle |
| **Backend** | FastAPI |
| **Frontend** | Streamlit |

---

## 📦 Quickstart — Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Ajaya210/Kindle-Book-Recommendation-System
cd Kindle-Book-Recommendation-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Streamlit App
```bash
streamlit run streamlit_app.py
```

### 4. Or Run FastAPI Backend
```bash
uvicorn app.main:app --reload
```
API docs: `http://localhost:8000/docs`

---

## 📁 Project Structure

```
Kindle-Book-Recommendation-System/
│
├── Book_Recommendation_System.ipynb      # Main notebook
├── best_model_collaborative.joblib       # Saved model
├── streamlit_app.py                      # Streamlit frontend
├── app/
│   └── main.py                           # FastAPI backend
├── data/
│   ├── Books.csv
│   ├── Users.csv
│   └── Ratings.csv
├── requirements.txt
└── README.md
```

---

## 🏁 Conclusion

Across three recommendation strategies, **Collaborative Filtering** emerged as the clear winner — achieving a 95.76% Recall@10, meaning the system successfully included at least one relevant book in the top-10 list for nearly every user. This directly translates to higher user satisfaction and discovery success rates on reading platforms. The deployed Streamlit app brings this capability to real-time interactive use.

---

## 👤 Author

**Ajaya Kumar Pradhan**  
Data Analyst · Power BI Developer · ML Engineer  
📍 Bhubaneswar, Odisha, India

[![GitHub](https://img.shields.io/badge/GitHub-ajayaconnect-181717?style=flat-square&logo=github)](https://github.com/ajayaconnect)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/)

---

*Built as part of AlmaBetter Full Stack Data Science certification — Unsupervised Learning Capstone.*
