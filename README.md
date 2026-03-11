# YouTube Trending Insight Pipeline

A machine learning pipeline that predicts the probability of a YouTube video trending using **text embeddings, channel analytics, and ensemble learning**.  
The project also includes an **interactive Streamlit dashboard** for exploring trending patterns across multiple countries.

---

# Project Overview

This project analyzes YouTube video metadata to estimate whether a video is likely to trend.

The prediction system uses information available at upload time such as:

- Video title
- Video description
- Tags
- Channel statistics
- Video duration
- Category
- Country

The model combines **text features, channel engagement metrics, and psychological signals** to generate a **trending probability score**.

---

# Machine Learning Pipeline

The system uses a **stacked ensemble architecture** consisting of three specialized models.

## 1. Text Model

Extracts semantic meaning from video metadata.

Embedding Model: **LaBSE Multilingual Transformer**

Features used:
- Video title
- Description
- Tags
- Channel title

Classifier:
- Logistic Regression

---

## 2. Channel & Numeric Model

Captures creator authority and engagement patterns.

Engineered features include:

- log subscriber count
- log channel view count
- video duration
- channel authority score
- views per video
- subscribers per video
- channel activity bucket

Model used:

**Random Forest (Calibrated)**

---

## 3. Psychological Signals Model

Captures virality-related signals in titles and descriptions.

Features include:

- urgency keywords
- hype words
- emotional language
- numbers in titles
- punctuation signals
- title–description overlap

Model used:

**Logistic Regression**

---

## 4. Stacking Ensemble Architecture

The prediction system is built using a **stacked ensemble learning architecture** that combines multiple machine learning models, each designed to capture different aspects of YouTube video virality. Instead of relying on a single model, the pipeline first generates predictions from three specialized models and then combines those predictions using a **Logistic Regression meta model** to produce the final trending probability.

This design improves performance because each model focuses on a different type of signal: **semantic content, channel authority, and psychological engagement cues**.

---

### Text Model (Content Understanding)

The first model analyzes the **semantic meaning of video metadata** using a multilingual transformer model.

Inputs used for this model include:

- Video Title  
- Video Description  
- Video Tags  
- Channel Title  

These text fields are combined and converted into contextual embeddings using the **LaBSE (Language-agnostic BERT Sentence Embedding) transformer model**. LaBSE captures deep semantic relationships between words and phrases across multiple languages, allowing the system to understand how video titles and descriptions may influence audience interest.

The generated embeddings are normalized and passed to a **Logistic Regression classifier**, which learns patterns between textual content and the probability of a video trending.

Output produced by this model:

```
Text Probability Score
```

This score represents how likely a video is to trend **based on the semantic meaning of its textual metadata**.

---

### Numeric / Channel Model (Channel Authority & Engagement)

The second model captures **channel strength and engagement behavior**, which are strong indicators of whether a video can trend.

This model uses engineered features derived from channel statistics and video characteristics, including:

- Log-transformed video duration  
- Log subscriber count  
- Log channel view count  
- Channel authority score  
- Views per video ratio  
- Subscribers per video ratio  
- Legacy channel indicator  
- Video upload volume bucket  
- Video category  
- Country of upload  

Categorical features such as **video category and country** are encoded using one-hot encoding and combined with the numerical features.

A **Random Forest classifier** is then trained on these features. Random Forest is effective at capturing **nonlinear relationships between channel authority, engagement metrics, and trending probability**.

To improve the reliability of predicted probabilities, the model predictions are calibrated using **probability calibration techniques**.

Output produced by this model:

```
Numeric Probability Score
```

This score represents how likely a video is to trend **based on channel influence and engagement statistics**.

---

### Psychological Signal Model (Virality Signals)

The third model focuses on **content psychology signals** that often drive viral engagement on platforms like YouTube.

This model extracts features from video titles and descriptions that indicate audience engagement triggers such as:

- Urgency keywords (e.g., breaking, update)  
- Hype-related words (e.g., viral, massive)  
- Official announcement signals  
- Emotional tone indicators  
- Presence of numbers in titles  
- Question marks or exclamation marks  
- Overlap between title and description  

These features capture how creators structure content to attract viewer attention.

The extracted features are standardized and used to train a **Logistic Regression classifier**, which outputs a probability score representing the psychological virality potential of the content.

Output produced by this model:

```
Psychology Probability Score
```

---

### Meta Model (Stacking Layer)

The final stage of the pipeline combines the predictions from the three base models.

Each model produces a probability representing its estimate of the video's likelihood of trending:

- Text Model Probability  
- Numeric Model Probability  
- Psychology Model Probability  

These three probability scores are stacked together to form a new feature vector that serves as the input to the **Meta Model**, which is implemented using **Logistic Regression**.

The meta model learns the optimal weighting of each model’s prediction and produces the final output:

```
Text Model Probability
Numeric Model Probability
Psychology Model Probability
           │
           ▼
   Logistic Regression Meta Model
           │
           ▼
     Final Trending Probability
```

This stacking approach allows the system to integrate **semantic content signals, channel authority metrics, and psychological engagement cues**, resulting in a more robust and accurate prediction model.

The final stacked model achieves a **ROC-AUC score of approximately 0.89**, demonstrating strong performance in predicting whether a video is likely to trend.

# Dataset

The dataset contains **YouTube trending videos from multiple countries**.

Countries included:

- Australia
- Canada
- India
- Ireland
- New Zealand
- Singapore
- South Africa
- United Kingdom
- United States

Each dataset contains video metadata, channel statistics, and engagement metrics.

---

# Interactive Dashboard

Dashboard features include:

### Trending Videos by Category
Trending distribution across video categories.

### Category Share
All Categories pie chart

### Country Analytics
Trending patterns across different countries.

### Videos Predicted to Trend by Country
Trending Videos distribution by Country

### Views vs Likes

### Views Distribution

# Prediction
Predicts percentage of the video to get in the trending by using the features

---

# Project Structure

```
youtube-trending-ml-pipeline
│
├── dataset_csv_files
├──accesing_from_database
|  ├── database_accessing.ipynb
├── model
|   ├── final_model.ipynb
|   ├── clip_values.pkl
|   ├── ohe.pkl
|   ├── urgency.pkl
│   ├── text_lr.pkl
│   ├── text_scaler.pkl
│   ├── rf_calibrated.pkl
│   ├── psych_lr.pkl
│   ├── psych_scaler.pkl
│   └── meta_lr.pkl
│
├── pushing_into_database
|   ├── data_ingestion_api_v3.py
├── insert_will_trend.py
│
├── ui
│   ├── app.py
│   ├── data_loader.py
│
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Sentence Transformers
- Streamlit
- Matplotlib
- Seaborn
- Joblib
- Plotly

---

# Running the Project Locally

### Install dependencies

```
pip install -r requirements.txt
```

---

### Run the Streamlit dashboard

```
streamlit run ui/app.py
```

---

### Open the app in your browser

```
http://localhost:8501
```

---

# Example Output

```
Final Probability: 0.86
Text Score: 0.73
Numeric Score: 0.73
Psychology Score: 0.50
```

---

# Future Improvements

Possible future improvements include:

- YouTube API data ingestion
- Real-time trending prediction
- Cloud deployment
- Automated model retraining
- Feature importance visualization

---

# Author

Machine Learning project focused on **content virality prediction and YouTube analytics pipelines**.
