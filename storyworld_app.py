import os
import json
import streamlit as st
import jsonschema
from jsonschema import validate, ValidationError

CHAR_FOLDER = "characters"
SCENE_FOLDER = "scenes"
LOCATION_FOLDER = "locations"
SCHEMAS_FOLDER = "schemas"
SETTINGS_FILE = "streamlit_app_settings.json"

# --- Load UI settings ---
settings = {
    "show_download": True,
    "json_indent": 2,
    "enable_editing": True,
    "validate_schema": True
}
if os.path.exists(SETTINGS_FILE):
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        try:
            user_settings = json.load(f)
            settings.update(user_settings)
        except:
            st.warning("⚠️ Couldn't load settings — using defaults.")

# --- Load schemas ---
schemas = {}
if os.path.exists(SCHEMAS_FOLDER):
    schema_files = {
        "character": "character-schema.json",
        "region": "region-schema.json",
    }

    for schema_type, filename in schema_files.items():
        schema_path = os.path.join(SCHEMAS_FOLDER, filename)
        if os.path.exists(schema_path):
            with open(schema_path, "r", encoding="utf-8") as f:
                try:
                    schemas[schema_type] = json.load(f)
                except Exception as e:
                    st.sidebar.warning(f"⚠️ Couldn't load {schema_type} schema: {e}")

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

def validate_against_schema(data, schema_type):
    """Validate data against the appropriate schema"""
    if schema_type not in schemas:
        return True, "No schema available for validation"

    try:
        validate(instance=data, schema=schemas[schema_type])
        return True, "✅ Valid schema"
    except ValidationError as e:
        return False, f"❌ Schema validation error: {e.message}"

def display_character_details(char_data):
    """Display character data in a more structured way"""
    cols = st.columns(2)

    # Left column for basic info
    with cols[0]:
        if "name" in char_data:
            st.subheader(char_data["name"])

        if "pronouns" in char_data:
            st.write(f"**Pronouns:** {char_data['pronouns']}")

        if "groups" in char_data:
            st.write("**Groups:**")
            for group in char_data["groups"]:
                st.write(f"- {group}")

        if "other_names" in char_data:
            st.write("**Also known as:**")
            for name in char_data["other_names"]:
                st.write(f"- {name}")

        if "personality" in char_data:
            st.write("**Personality:**")
            st.write(char_data["personality"])

    # Right column for background and details
    with cols[1]:
        if "background" in char_data:
            st.write("**Background:**")
            st.write(char_data["background"])

        if "physical_description" in char_data:
            st.write("**Physical Description:**")
            st.write(char_data["physical_description"])

        if "dialogue_style" in char_data:
            st.write("**Dialogue Style:**")
            st.write(char_data["dialogue_style"])

    # Relationships section
    if "relationships" in char_data:
        st.write("### Relationships")
        for person, relationship in char_data["relationships"].items():
            st.write(f"**{person}:** {relationship}")

    # Attributes section
    if "static_attributes" in char_data:
        st.write("### Static Attributes")
        attrs = char_data["static_attributes"]
        attr_cols = st.columns(2)

        with attr_cols[0]:
            if "birthdate" in attrs:
                st.write(f"**Birthdate:** {attrs['birthdate']}")
            if "role" in attrs:
                st.write(f"**Role:** {attrs['role']}")
            if "nationality" in attrs:
                st.write(f"**Nationality:** {attrs['nationality']}")

        with attr_cols[1]:
            if "augmentation_level" in attrs:
                st.write(f"**Augmentation:** {attrs['augmentation_level']}")
            if "economic_viability_rating" in attrs:
                st.write(f"**Economic Rating:** {attrs['economic_viability_rating']}/10")

    # Dynamic attributes (timeline)
    if "dynamic_attributes" in char_data and char_data["dynamic_attributes"]:
        st.write("### Character Timeline")
        for i, period in enumerate(char_data["dynamic_attributes"]):
            with st.expander(f"Time Period: {period.get('time', f'Period {i+1}')}"):
                if "personality" in period:
                    for trait, value in period["personality"].items():
                        st.write(f"**{trait}:** {value}")

def display_location_details(loc_data):
    """Display location data in a structured way"""
    if "region_name" in loc_data:
        st.subheader(loc_data["region_name"])

    cols = st.columns(2)

    with cols[0]:
        if "tone" in loc_data:
            st.write(f"**Tone:** {loc_data['tone']}")
        if "tech_level" in loc_data:
            st.write(f"**Tech Level:** {loc_data['tech_level']}")
        if "elevation" in loc_data:
            st.write(f"**Elevation:** {loc_data['elevation']}")

    with cols[1]:
        if "problems" in loc_data:
            st.write("**Problems:**")
            for problem in loc_data["problems"]:
                st.write(f"- {problem}")

    if "infrastructure" in loc_data:
        st.write("### Infrastructure")
        infra_items = loc_data["infrastructure"]
        st.write(", ".join(infra_items))

    if "youth_trends" in loc_data:
        st.write("### Youth Trends")
        for trend in loc_data["youth_trends"]:
            st.write(f"- {trend}")

    if "notes" in loc_data:
        st.write("### Notes")
        st.write(loc_data["notes"])

def display_json_editor(filename, data, folder, schema_type=None):
    if settings["validate_schema"] and schema_type:
        is_valid, message = validate_against_schema(data, schema_type)
        if is_valid:
            st.success(message)
        else:
            st.warning(message)

    default_str = json.dumps(data, indent=settings["json_indent"], ensure_ascii=False)
    edited = st.text_area("Edit JSON", default_str, height=400)

    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"💾 Save changes to {filename}"):
            try:
                new_data = json.loads(edited)

                # Validate before saving if enabled
                if settings["validate_schema"] and schema_type:
                    is_valid, message = validate_against_schema(new_data, schema_type)
                    if not is_valid:
                        st.error(f"Cannot save: {message}")
                        return

                with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
                    json.dump(new_data, f, indent=2, ensure_ascii=False)
                st.success(f"✅ {filename} updated.")
            except json.JSONDecodeError as e:
                st.error(f"❌ Invalid JSON: {e}")

    with col2:
        if settings["show_download"]:
            st.download_button("⬇️ Download JSON", default_str, file_name=filename, mime="application/json")

# === MAIN VIEW ===

if section == "Characters":
    st.header("🧬 Character Files")

    # Add a new character option
    if st.button("➕ Create New Character"):
        # Template based on character schema
        char_template = {
            "name": "New Character",
            "pronouns": "they/them",
            "groups": [],
            "other_names": [],
            "personality": "",
            "background": "",
            "physical_description": "",
            "dialogue_style": "",
            "relationships": {},
            "static_attributes": {
                "birthdate": "",
                "role": "",
                "nationality": "",
                "augmentation_level": "",
                "economic_viability_rating": 5
            },
            "dynamic_attributes": []
        }

        new_filename = "new_character.json"
        with open(os.path.join(CHAR_FOLDER, new_filename), "w", encoding="utf-8") as f:
            json.dump(char_template, f, indent=2, ensure_ascii=False)
        st.success(f"✅ Created {new_filename}")

    characters = load_json_files(CHAR_FOLDER)
    for filename, char_data in characters.items():
        with st.expander(filename):
            if "error" in char_data:
                st.error(f"❌ {char_data['error']}")
                continue

            tab1, tab2 = st.tabs(["Character View", "Raw JSON"])

            with tab1:
                display_character_details(char_data)

            with tab2:
                st.json(char_data, expanded=False)
                if settings["enable_editing"]:
                    display_json_editor(filename, char_data, CHAR_FOLDER, "character")

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

    # Add a new location o