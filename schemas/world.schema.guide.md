
# 🌍 World Schema Guide for "They Burn Witches"

This document explains how to use and expand the modular world schema system for all stories set in the **PixelVault Earth** universe. It ensures consistency across characters, locations, and timelines—whether you’re working solo, with AI, or collaborating with human co-authors.

---

## 🧩 Purpose

The `world-schema.json` defines the **global truths** of the world (2034–2042), such as:
- Common technologies
- Climate effects
- Banned genre tropes
- Narrative tone and lens

It references a modular `region-schema.json`, so you can define **regions like Sweden, Rwanda, or Bangladesh** in separate files.

---

## 📁 File Structure Example

```
they-burn-witches/
├── schemas/
│   ├── world-schema.json         ← Canonical global blueprint
│   ├── region-schema.json        ← Regional structure template
├── locations/
│   ├── Sweden.json               ← A validated region file
│   ├── Rwanda.json
│   └── Ann_stockholm_apartment.json
├── docs/
│   └── world.schema.guide.md     ← This file
```

---

## ✅ What to Include in `world-schema.json`

- **`world_name`**: The name of your canonical world (default: "PixelVault Earth").
- **`time_period`**: Main narrative timeframe (default: 2034–2042).
- **`global`**: Planet-wide defaults like energy, AI, internet access, and transportation.
- **`regions`**: Now an array of region files conforming to `region-schema.json`.
- **`rules`**: World constraints and genre filters (e.g., no zombies, no anti-gravity).
- **`narrative_lens`**: Approved tones and storytelling variation options.

---

## 🗺️ What Goes in a `region.json` File

Each region (e.g., `Sweden.json`, `Rwanda.json`) should include:

```json
{
  "$schema": "../schemas/region-schema.json",
  "region_name": "Sweden",
  "tone": "gritty thriller",
  "tech_level": "mid-high",
  "problems": ["rising sea", "tech witch trials", "housing"],
  "youth_trends": ["cycling crews", "underground AI"]
}
```

Other examples:
- Rwanda might have `"tone": "hopepunk"` and `"tech_level": "mid with spiritual AI"`.
- Gabon or Congo could introduce regional airship trade or refugee logistics.

---

## 🧠 For Co-authors and AI Assistants

### Human:
- Use the schemas to propose new regions or edits through pull requests.
- Link `region.json` files to scenes, characters, and arcs.

### AI:
Prompt like this for clarity:
```
Use tone and tech-level from Rwanda.json. Ground story in spiritual AI ecology. Avoid cyberpunk or cityscapes.
```

---

## 🧰 Future Extensions

You may later modularize:
- `location-schema.json` → for buildings, landmarks
- `timeline-schema.json` → global events, tech rollouts
- `faction-schema.json` → political entities, corporations, resistance groups

---

This guide ensures that your world stays **coherent and scalable**, even as stories shift across continents, tones, and timelines.
