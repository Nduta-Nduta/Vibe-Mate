#Vibe-Mate  

Vibe-Mate is a music data exploration and analysis project.  
It uses a dataset of tracks with features like **danceability, energy, tempo, popularity, and genre** to explore music trends and patterns.  

## 📂 Project Structure
- `vibe_mate.py` → Main Python script (data loading & first transformations)  
- `dataset.csv` → Main dataset (not tracked in GitHub for size/privacy reasons)  
- `.gitignore` → Ensures dataset and unnecessary files are not pushed  

## 🚀 Features (so far)
- Load the main dataset (`dataset.csv`)  
- Display first rows for inspection  
- Generate dataset info summary  
- Create a `decade` column from track release year (if available)  

## 🔧 Requirements
- Python 3.10+  
- Libraries:  
  - `pandas`  

Install dependencies:
```bash
pip install pandas

▶️ Running the Project

Place dataset.csv in the project folder (same level as vibe_mate.py).

Run the script:

python vibe_mate.py

📌 Next Steps

Add data cleaning (missing values, duplicates)

Explore popularity across decades

Genre-based analysis

Visualizations (Matplotlib/Seaborn/Plotly)

🎧 Vibe-Mate: turning raw data into music insights.


---


