🎶 Vibe-Mate

Vibe-Mate is a music data exploration and analysis project.
It uses a dataset of tracks with features like danceability, energy, tempo, popularity, and genre to explore music trends, visualize patterns, and apply clustering for deeper insights.

📂 Project Structure

dataset.csv → Main dataset (not tracked in GitHub for size/privacy reasons)

Vibe_Mate_Phase1.ipynb → Phase 1 notebook (data preparation)

Vibe_Mate_Phase2.ipynb → Phase 2 notebook (exploratory data analysis)

Vibe_Mate_Phase3.ipynb → Phase 3 notebook (clustering analysis)

.gitignore → Ensures dataset and unnecessary files are not pushed

README.md → Project documentation

🚀 Features by Phase
🔹 Phase 1 – Data Preparation

Loaded and inspected the dataset (dataset.csv).

Displayed dataset structure and summary.

Created a decade column from track metadata for temporal analysis.

🔹 Phase 2 – Exploratory Data Analysis (EDA)

Visualized distribution of tracks across decades.

Analyzed trends of sound features (acousticness, danceability, energy, instrumentalness, liveness, valence) over time.

Explored loudness trends across decades.

Identified top 10 genres and compared their sound profiles.

Generated word clouds for genres and artists.

Highlighted top 10 artists by number of songs and by popularity.

🔹 Phase 3 – Clustering Analysis

Applied K-Means clustering to genres (12 clusters).

Applied K-Means clustering to songs (25 clusters).

Visualized clusters to reveal hidden similarities between genres and songs.

Showed how clustering uncovers relationships beyond genre labels.

📊 Key Insights

Tracks show clear temporal patterns, with distinct shifts in energy, danceability, and loudness across decades.

Popularity is concentrated within a few genres and artists, but sound features provide deeper insights than popularity alone.

Clustering reveals that songs and genres naturally group together, often in ways that transcend standard genre labels.

🔧 Requirements

Python 3.10+
Libraries:

pandas

matplotlib

seaborn

plotly

scikit-learn

wordcloud

Install dependencies:

pip install pandas matplotlib seaborn plotly scikit-learn wordcloud

▶️ Running the Project

Place dataset.csv in the project folder.

Open the relevant notebook (Vibe_Mate_Phase1.ipynb, Vibe_Mate_Phase2.ipynb, or Vibe_Mate_Phase3.ipynb).

Run all cells to reproduce the analysis.
