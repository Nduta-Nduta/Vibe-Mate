# 🎶 Vibe-Mate  

Vibe-Mate is a music data exploration and analysis project.  
It uses a dataset of tracks with features like danceability, energy, tempo, popularity, and genre to explore music trends and patterns.  

---

## 📂 Project Structure  
- `vibe_mate.py` → Phase 1 script (data loading & first transformations)  
- `Vibe_Mate_Phase2.ipynb` → Phase 2 notebook (exploratory data analysis)  
- `dataset.csv` → Main dataset (**not tracked in GitHub**)  
- `.gitignore` → Ensures dataset and unnecessary files are not pushed  

---

## 🚀 Features  

### Phase 1 – Data Preparation  
- Load the main dataset (`dataset.csv`)  
- Display first rows for inspection  
- Generate dataset info summary  
- Create a **decade column** from track release year (if available)  

### Phase 2 – Exploratory Data Analysis (EDA)  
- **Genre distribution** plots  
- Trends in audio features (`danceability`, `energy`, `acousticness`, `valence`)  
- **Loudness comparison** across genres  
- **Popularity analysis** for top genres  
- **Word clouds** of genres and artists  
- **Top artists** by track count and popularity  

---

## 📝 Insights  

- Dataset is **balanced across genres** (~1000 tracks per genre).  
- Acoustic genres are softer and more acoustic, while electronic/dance genres are louder and more energetic.  
- Popularity analysis highlights **listener preferences**, not just raw dataset counts.  
- Top artists differ depending on whether we measure by **track count** or **popularity**.  
- Word clouds give a quick **visual overview** of genre and artist diversity.  

---

## 🔧 Requirements  
- Python 3.10+  
- Libraries:  
  - `pandas`  
  - `matplotlib`  
  - `seaborn`  
  - `wordcloud`  

Install dependencies:  
```bash
pip install pandas matplotlib seaborn wordcloud
