import os
import json
import streamlit as st

# Base folders
CHAR_FOLDER = "characters"
SCENE_FOLDER = "scenes"
LOCATION_FOLDER = "locations"

st.set_page_config(page_title="They Burn Witches", layout="wide")

st.title("🧙‍♀️ They Burn Witches: Storyworld Explorer")

st.sidebar.header("Navigation")
view = st.sidebar.selectbox("Choose section", ["Characters", "Scenes", "Locations"])

def load_json_files(folder):
    data = []
    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            with open(os.path.join(folder, filename), encoding="utf-8") as f:
                try:
                    data.append(json.load(f))
                except Exception as e:
                    st.error(f"❌ Error loading {filename}: {e}")
    return data

if view == "Characters":
    st.header("🧬 Characters")
    chars = load_json_files(CHAR_FOLDER)
    for char in chars:
        with st.expander(f"{char.get('name', 'Unnamed')}"):
            st.json(char)

elif view == "Scenes":
    st.header("🎭 Scenes")
    scenes = load_json_files(SCENE_FOLDER)
    for scene in scenes:
        with st.expander(f"{scene.get('title', 'Untitled')}"):
            st.json(scene)

elif view == "Locations":
    st.header("🗺️ Locations")
    locs = load_json_files(LOCATION_FOLDER)
    for loc in locs:
        with st.expander(f"{loc.get('name', 'Unknown')}"):
            st.json(loc)
