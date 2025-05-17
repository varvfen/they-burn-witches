import os
import json
import subprocess
from datetime import datetime

# Folders to ensure exist
FOLDERS = [
    "characters", "locations", "scenes", "arcs",
    "relationships", "items", "metadata"
]

def ensure_folders():
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)

def write_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def init_repo():
    readme = """# They Burn Witches – Storyworld Repository

This is a collaborative, JSON-driven story structure for the speculative fiction series by Gunnar Sandström.

- `characters/` – Profiles with static and dynamic attributes
- `scenes/` – Dialogue + setting snapshots
- `locations/` – Geopolitical, digital or physical places
- `relationships/` – Connections and tensions between people
- `arcs/` – Storylines that span multiple scenes
- `items/` – AI tools, symbolic objects, tech artifacts
- `metadata/` – Versioning, contributors, logs
"""
    with open("README.md", "w") as f:
        f.write(readme)

    with open(".gitignore", "w") as f:
        f.write("__pycache__/\n*.pyc\n.DS_Store\n")

    versioning = {
        "version": "0.1.0",
        "maintainer": "Gunnar Sandström",
        "last_updated": datetime.today().strftime("%Y-%m-%d"),
        "contributors": ["Gunnar", "ChatGPT"],
        "changelog": [
            {
                "version": "0.1.0",
                "date": datetime.today().strftime("%Y-%m-%d"),
                "changes": "Initial repo setup with folders and samples"
            }
        ]
    }
    write_json("metadata/versioning.json", versioning)

def create_sample_files():
    ann = {
        "name": "Ann Charlotte",
        "static_attributes": {
            "birthdate": "1994-03-12",
            "height_cm": 172,
            "eye_color": "hazel",
            "nationality": "Swedish"
        },
        "dynamic_attributes": [
            {
                "time": "before China trip",
                "personality": {
                    "confidence": "quiet",
                    "openness": "moderate",
                    "curiosity": "latent"
                }
            },
            {
                "time": "after China trip",
                "personality": {
                    "confidence": "growing",
                    "openness": "high",
                    "curiosity": "expressive"
                }
            }
        ]
    }
    write_json("characters/ann_charlotte.json", ann)

    scene = {
        "scene_id": "034",
        "title": "Ann Returns to Stockholm",
        "location": "Ann's apartment",
        "time": "2033-10-14T18:32+02:00",
        "tags": ["character_reunion", "post-China"],
        "characters_present": ["Ann Charlotte", "Mary"],
        "summary": "Ann returns after her China trip to find Mary has turned the apartment into chaos.",
        "dialogue": [
            {
                "speaker": "Mary",
                "line": "Surprise! You’re not hallucinating, that’s a fireman’s pole.",
                "tone": "playful"
            },
            {
                "speaker": "Ann",
                "line": "Mary, is that… did you actually put a hole in the floor?",
                "tone": "curious"
            }
        ]
    }
    write_json("scenes/034_ann_returns_stockholm.json", scene)

def add_new_character():
    name = input("Character name: ").strip()
    height = input("Height in cm: ").strip()
    eye_color = input("Eye color: ").strip()
    nationality = input("Nationality: ").strip()

    dynamic_trait = input("Trait to track over time (e.g., openness): ").strip()
    time_1 = input("Time 1 label (e.g., 'before training'): ").strip()
    level_1 = input(f"{dynamic_trait} at {time_1}: ").strip()
    time_2 = input("Time 2 label (e.g., 'after training'): ").strip()
    level_2 = input(f"{dynamic_trait} at {time_2}: ").strip()

    char_data = {
        "name": name,
        "static_attributes": {
            "height_cm": int(height),
            "eye_color": eye_color,
            "nationality": nationality
        },
        "dynamic_attributes": [
            {
                "time": time_1,
                "personality": {
                    dynamic_trait: level_1
                }
            },
            {
                "time": time_2,
                "personality": {
                    dynamic_trait: level_2
                }
            }
        ]
    }

    filename = f"characters/{name.lower().replace(' ', '_')}.json"
    write_json(filename, char_data)
    print(f"✅ Character saved: {filename}")

def add_new_scene():
    scene_id = input("Scene ID (e.g., 035): ").strip()
    title = input("Scene title: ").strip()
    location = input("Location: ").strip()
    char_1 = input("Character 1: ").strip()
    char_2 = input("Character 2 (or leave blank): ").strip()

    summary = input("One-line summary of the scene: ").strip()

    dialogue = []
    while True:
        speaker = input("Speaker (or leave blank to stop): ").strip()
        if not speaker:
            break
        line = input("Line of dialogue: ").strip()
        tone = input("Tone (e.g., anxious, flirty): ").strip()
        dialogue.append({"speaker": speaker, "line": line, "tone": tone})

    scene_data = {
        "scene_id": scene_id,
        "title": title,
        "location": location,
        "time": datetime.today().isoformat(),
        "characters_present": [char_1] + ([char_2] if char_2 else []),
        "summary": summary,
        "dialogue": dialogue
    }

    filename = f"scenes/{scene_id}_{title.lower().replace(' ', '_')}.json"
    write_json(filename, scene_data)
    print(f"✅ Scene saved: {filename}")

def git_commit_push():
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Updated storyworld files"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("✅ Changes pushed to GitHub.")

# MAIN
print("📦 Initializing storyworld repo...")
ensure_folders()
init_repo()
create_sample_files()

# Optional interactive part
while True:
    choice = input("\nWhat would you like to do?\n[1] Add new character\n[2] Add new scene\n[3] Push to GitHub\n[Enter] Quit\n> ").strip()
    if choice == "1":
        add_new_character()
    elif choice == "2":
        add_new_scene()
    elif choice == "3":
        git_commit_push()
    else:
        break

print("✨ All done.")
