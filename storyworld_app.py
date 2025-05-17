import os
import json
import streamlit as st

CHAR_FOLDER = "characters"
SCENE_FOLDER = "scenes"
LOCATION_FOLDER = "locations"
SETTINGS_FILE = "streamlit_app_settings.json"

# --- Load UI settings ---
settings = {
    "show_download": True,
    "json_indent": 2,
    "enable_editing": True
}
if os.path.exists(SETTINGS_FILE):
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        try:
            user_settings = json.load(f)
            settings.update(user_settings)
        except:
            st.warning("⚠️ Couldn't load settings — using defaults.")

st.set_page_config(page_title="They Burn Witches", layout="wide")

st.title("🧙‍♀️ They Burn Witches: Storyworld Explorer")

section = st.sidebar.radio("Choose section", ["Characters", "Scenes", "Locations"])

def load_json_files(folder):
    items = {}
    if not os.path.exists(folder):
        return items
    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    items[filename] = json.load(f)
                except Exception as e:
                    items[filename] = {"error": str(e)}
    return items

def display_json_editor(filename, data, folder):
    default_str = json.dumps(data, indent=settings["json_indent"], ensure_ascii=False)
    edited = st.text_area("Edit JSON", default_str, height=400)
    if st.button(f"💾 Save changes to {filename}"):
        try:
            new_data = json.loads(edited)
            with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
                json.dump(new_data, f, indent=2, ensure_ascii=False)
            st.success(f"✅ {filename} updated.")
        except json.JSONDecodeError as e:
            st.error(f"❌ Invalid JSON: {e}")

    if settings["show_download"]:
        st.download_button("⬇️ Download JSON", default_str, file_name=filename, mime="application/json")

# === MAIN VIEW ===

if section == "Characters":
    st.header("🧬 Character Files")
    characters = load_json_files(CHAR_FOLDER)
    for filename, char_data in characters.items():
        with st.expander(filename):
            if "error" in char_data:
                st.error(f"❌ {char_data['error']}")
                continue
            st.json(char_data, expanded=False)
            if settings["enable_editing"]:
                display_json_editor(filename, char_data, CHAR_FOLDER)

elif section == "Scenes":
    st.header("🎭 Scenes")
    scenes = load_json_files(SCENE_FOLDER)
    for filename, scene_data in scenes.items():
        with st.expander(filename):
            st.json(scene_data, expanded=False)
            if settings["enable_editing"]:
                display_json_editor(filename, scene_data, SCENE_FOLDER)

elif section == "Locations":
    st.header("🗺️ Locations")
    locs = load_json_files(LOCATION_FOLDER)
    for filename, loc_data in locs.items():
        with st.expander(filename):
            st.json(loc_data, expanded=False)
            if settings["enable_editing"]:
                display_json_editor(filename, loc_data, LOCATION_FOLDER)
