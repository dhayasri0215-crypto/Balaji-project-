import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title='AI Internship Recommendation Engine', page_icon='🎓', layout='wide')
DATA_FILE = Path(__file__).parent / 'data' / 'resources.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    required = {'title', 'category', 'skill_level', 'description', 'url'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing columns: {', '.join(sorted(missing))}")
    return df.fillna('')

st.title('🎓 AI Internship Recommendation Engine')
st.write('Find internships, projects, and learning resources that match your skill level.')
try:
    data = load_data()
except Exception as exc:
    st.error(f'Could not load dataset: {exc}')
    st.stop()

c1, c2 = st.columns(2)
with c1:
    level = st.selectbox('Choose your skill level', ['Beginner', 'Intermediate', 'Advanced'])
with c2:
    category = st.selectbox('Choose a resource category', ['All', 'Internship', 'Project', 'Learning Resource'])

matches = data[data['skill_level'].str.lower() == level.lower()]
if category != 'All':
    matches = matches[matches['category'].str.lower() == category.lower()]
st.subheader(f'Recommended for you ({len(matches)})')
if matches.empty:
    st.info('No matching resources found. Try another skill level or category.')
else:
    for _, item in matches.iterrows():
        with st.container(border=True):
            st.markdown(f"### {item['title']}")
            st.caption(f"{item['category']} • {item['skill_level']}")
            st.write(item['description'])
            if str(item['url']).strip():
                st.link_button('Open resource', str(item['url']))
with st.expander('View complete dataset'):
    st.dataframe(data, use_container_width=True)
st.caption('Demo project. Replace sample CSV records with verified opportunities and learning resources.')
