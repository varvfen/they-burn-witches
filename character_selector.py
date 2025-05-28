import streamlit as st
import pandas as pd
import json
from datetime import datetime
from collections import defaultdict
import io

# Set page config
st.set_page_config(
    page_title="Character Selector & Scene Builder",
    page_icon="🎭",
    layout="wide"
)

# Initialize session state
if 'characters_df' not in st.session_state:
    st.session_state.characters_df = None
if 'scene_data' not in st.session_state:
    st.session_state.scene_data = None

def load_sample_data():
    """Load sample data if no CSV is uploaded"""
    sample_data = {
        'Name': ['Saga Lundqvist', 'Mira Nguyen', 'Elin Voss', 'Freja Holm'],
        'Role': ['Chaotic Rising Star', 'Production Queen', 'Team Leader', 'Technical Specialist'],
        'Groups': ['Ghost Trainers Collective', 'Ghost Trainers Collective', 'Ghost Trainers Collective', 'Ghost Trainers Collective'],
        'Personality': ['Impulsive, curious, fearless questioner', 'Technical genius, streaming expert', 'Determined leader, manual pedaling warrior', 'Cynical, experienced, protective'],
        'Dialogue Style': ['Unfiltered, asks hard questions', 'Technical precision, frustrated muttering', 'Terse commands, granite determination', 'Sharp observations, protective warnings']
    }
    return pd.DataFrame(sample_data)

def analyze_name_conflicts(df):
    """Detect name conflicts in the character database"""
    conflicts = []

    # Extract first and last names
    first_names = defaultdict(list)
    last_names = defaultdict(list)

    for _, row in df.iterrows():
        name = str(row.get('Name', ''))
        if name and name != 'nan':
            parts = name.split()
            if parts:
                first_name = parts[0]
                first_names[first_name].append(name)

                if len(parts) > 1:
                    last_name = parts[-1]
                    last_names[last_name].append(name)

    # Find conflicts
    for first_name, names in first_names.items():
        if len(names) > 1:
            conflicts.append({
                'type': 'First Name',
                'name': first_name,
                'characters': names
            })

    for last_name, names in last_names.items():
        if len(names) > 1:
            conflicts.append({
                'type': 'Last Name',
                'name': last_name,
                'characters': names
            })

    return conflicts

def check_scene_conflicts(selected_characters, df):
    """Check for name conflicts in selected scene characters"""
    conflicts = []
    first_names = defaultdict(list)

    for char_name in selected_characters:
        parts = char_name.split()
        if parts:
            first_name = parts[0]
            first_names[first_name].append(char_name)

    for first_name, names in first_names.items():
        if len(names) > 1:
            conflicts.append(f"⚠️ Multiple characters with first name '{first_name}': {', '.join(names)}")

    return conflicts

def generate_scene_output(scene_data):
    """Generate formatted scene output"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    output = f"""=== SCENE BUILDER OUTPUT ===
Generated: {timestamp}

GROUP: {scene_data.get('group', 'Not specified')}
LOCATION: {scene_data.get('location', 'Not specified')}

CHARACTERS IN SCENE:
"""

    for char in scene_data.get('characters', []):
        output += f"""• {char.get('name', 'Unknown')} ({char.get('role', 'No role')})
  Groups: {char.get('groups', 'No group')}
  Personality: {char.get('personality', 'No personality data')}
  Dialogue Style: {char.get('dialogue_style', 'No dialogue style data')}

"""

    output += f"""SCENE CONCEPT:
{scene_data.get('concept', 'No concept provided')}

"""

    if scene_data.get('conflicts'):
        output += f"""NAME CONFLICTS TO WATCH:
{chr(10).join(scene_data['conflicts'])}

"""

    output += f"""=== AI PROMPT SUGGESTION ===
Write a scene with the following characters in {scene_data.get('location', 'an unspecified location')}:
"""

    for char in scene_data.get('characters', []):
        output += f"- {char.get('name', 'Unknown')}: {char.get('personality', 'No personality data')}\n"

    output += f"""
Scene concept: {scene_data.get('concept', 'No concept provided')}

"""

    if scene_data.get('conflicts'):
        output += "NOTE: Be careful with name conflicts - use full names or distinctive descriptors when multiple characters share first names.\n"

    return output

# Main app
st.title("🎭 Character Selector & Scene Builder")
st.markdown("*For the Ann series and They Burn Witches storyworld*")

# Sidebar for file upload and database info
with st.sidebar:
    st.header("📁 Character Database")

    uploaded_file = st.file_uploader("Upload Character CSV", type=['csv'])

    if uploaded_file:
        try:
            st.session_state.characters_df = pd.read_csv(uploaded_file)
            st.success(f"Loaded {len(st.session_state.characters_df)} characters")
        except Exception as e:
            st.error(f"Error loading CSV: {e}")

    if st.button("Use Sample Data"):
        st.session_state.characters_df = load_sample_data()
        st.info("Loaded sample Ghost Trainers Collective data")

    if st.session_state.characters_df is not None:
        st.subheader("Database Info")
        st.write(f"**Total Characters:** {len(st.session_state.characters_df)}")

        # Show unique groups
        if 'Groups' in st.session_state.characters_df.columns:
            groups = st.session_state.characters_df['Groups'].dropna().unique()
            st.write(f"**Groups:** {len(groups)}")
            for group in groups[:5]:  # Show first 5 groups
                st.write(f"• {group}")
            if len(groups) > 5:
                st.write(f"... and {len(groups) - 5} more")

# Main content area
if st.session_state.characters_df is not None:
    df = st.session_state.characters_df

    # Two columns for main content
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("👥 Character Database")

        # Name conflict analysis
        conflicts = analyze_name_conflicts(df)
        if conflicts:
            st.subheader("⚠️ Name Conflicts Detected")
            for conflict in conflicts:
                with st.expander(f"{conflict['type']}: {conflict['name']}"):
                    for char in conflict['characters']:
                        char_data = df[df['Name'] == char].iloc[0]
                        st.write(f"**{char}** ({char_data.get('Role', 'No role')})")
                        if 'Groups' in char_data:
                            st.write(f"Groups: {char_data.get('Groups', 'No group')}")

        # Character list
        st.subheader("All Characters")
        search_term = st.text_input("Search characters:")

        display_df = df.copy()
        if search_term:
            mask = display_df['Name'].str.contains(search_term, case=False, na=False)
            display_df = display_df[mask]

        for _, char in display_df.iterrows():
            with st.expander(f"{char.get('Name', 'Unknown')} ({char.get('Role', 'No role')})"):
                st.write(f"**Groups:** {char.get('Groups', 'No group')}")
                if 'Personality' in char and pd.notna(char['Personality']):
                    st.write(f"**Personality:** {char['Personality']}")
                if 'Dialogue Style' in char and pd.notna(char['Dialogue Style']):
                    st.write(f"**Dialogue Style:** {char['Dialogue Style']}")

    with col2:
        st.header("🎬 Scene Builder")

        # Scene building form
        with st.form("scene_builder"):
            # Group selection
            groups = ['Any Group'] + list(df['Groups'].dropna().unique())
            selected_group = st.selectbox("Select Group:", groups)

            # Character selection
            if selected_group == 'Any Group':
                available_chars = df['Name'].dropna().tolist()
            else:
                available_chars = df[df['Groups'] == selected_group]['Name'].dropna().tolist()

            selected_characters = st.multiselect(
                "Select Characters:",
                available_chars,
                help="Choose characters for your scene"
            )

            # Additional characters
            if selected_group != 'Any Group':
                other_chars = df[df['Groups'] != selected_group]['Name'].dropna().tolist()
                if other_chars:
                    additional_chars = st.multiselect(
                        "Additional Characters (from other groups):",
                        other_chars
                    )
                    selected_characters.extend(additional_chars)

            # Location
            location = st.selectbox(
                "Location:",
                ["Stockholm", "Rwanda", "Burundi", "Lake Kivu", "Houseboat", "Custom"]
            )

            if location == "Custom":
                location = st.text_input("Custom Location:")

            # Scene concept
            scene_concept = st.text_area(
                "Scene Concept:",
                placeholder="Describe what happens in this scene...",
                height=100
            )

            # Theme/mood
            theme = st.selectbox(
                "Scene Theme/Mood:",
                ["Adventure", "Horror", "Comedy", "Drama", "Mystery", "Action", "Philosophical", "Technical"]
            )

            # Build scene button
            build_scene = st.form_submit_button("🎬 Build Scene", type="primary")

        if build_scene and selected_characters:
            # Check for conflicts
            scene_conflicts = check_scene_conflicts(selected_characters, df)

            # Build character data
            character_data = []
            for char_name in selected_characters:
                char_row = df[df['Name'] == char_name].iloc[0]
                character_data.append({
                    'name': char_name,
                    'role': char_row.get('Role', 'No role'),
                    'groups': char_row.get('Groups', 'No group'),
                    'personality': char_row.get('Personality', 'No personality data'),
                    'dialogue_style': char_row.get('Dialogue Style', 'No dialogue style data')
                })

            # Store scene data
            st.session_state.scene_data = {
                'group': selected_group,
                'location': location,
                'characters': character_data,
                'concept': scene_concept,
                'theme': theme,
                'conflicts': scene_conflicts,
                'timestamp': datetime.now().isoformat()
            }

            st.success("Scene built successfully!")

            # Show conflicts if any
            if scene_conflicts:
                st.warning("Name conflicts detected in this scene:")
                for conflict in scene_conflicts:
                    st.write(conflict)

# Scene output section
if st.session_state.scene_data:
    st.header("📝 Scene Output")

    scene_output = generate_scene_output(st.session_state.scene_data)

    col1, col2 = st.columns([3, 1])

    with col1:
        st.text_area("Generated Scene Data:", scene_output, height=400)

    with col2:
        st.download_button(
            "📥 Download Scene",
            scene_output,
            file_name=f"scene_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

        # JSON export
        json_data = json.dumps(st.session_state.scene_data, indent=2)
        st.download_button(
            "📥 Download JSON",
            json_data,
            file_name=f"scene_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

        if st.button("🔄 New Scene"):
            st.session_state.scene_data = None
            st.rerun()

else:
    st.info("👆 Upload a CSV file or use sample data to get started!")

    st.markdown("""
    ## Features:
    - **Name Conflict Detection**: Automatically finds characters with similar names
    - **Scene Builder**: Select characters, location, and concept
    - **AI Prompt Generation**: Creates ready-to-use prompts for co-writing
    - **Export Options**: Download scene data as text or JSON
    - **Mental Abacus Integration**: Perfect for scenes exploring different forms of intelligence

    ## Example Use Cases:
    - Build a scene with the Ghost Trainers Collective in Rwanda
    - Avoid the "Voss problem" by catching name conflicts early
    - Generate AI prompts for co-writing sessions
    - Track scene continuity across chapters
    """)