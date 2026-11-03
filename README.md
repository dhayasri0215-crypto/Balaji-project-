# AI Internship Recommendation Engine

A beginner-friendly Streamlit application that recommends internships, projects, and learning resources based on a user's selected skill level and category.

## Features
- Select Beginner, Intermediate, or Advanced skill level.
- Filter by Internship, Project, Learning Resource, or All.
- Display matching recommendations from a CSV dataset.
- View the complete dataset in the app.

## Technologies
Python, Pandas, Streamlit, and CSV.

## Run locally
1. Install Python 3.9 or newer.
2. Open a terminal in this project folder.
3. Install dependencies: `pip install -r requirements.txt`
4. Start the app: `streamlit run app.py`

## Dataset
Edit `data/resources.csv` to add your own verified records. Keep the columns `title`, `category`, `skill_level`, `description`, and `url`. Use skill levels Beginner, Intermediate, or Advanced.

## Upload to GitHub
1. Create a new repository on GitHub.
2. Extract this ZIP file.
3. Upload the files and folders inside the extracted project folder.
4. Commit with a message such as `Initial project upload`.

## Note
This ZIP is a working starter implementation based on the project description and weekly reports. The CSV entries are sample data, not verified live internship vacancies. Replace them with your own project dataset before presenting it as a completed recommendation service.
