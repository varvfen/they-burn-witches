character_schema_guide.md
# Character Schema Companion Guide
**For writers, AI co-authors, and collaborative storyworld builders**

This schema is designed to support character-driven storytelling in *They Burn Witches* and related storyworlds. While it was initially built for the cycling team in a sci-fi-punk arc, it is modular and can be adapted to other factions—such as Void Capital executives, off-grid AI communities, or historical arcs in flashbacks.

Each field below includes examples, best-use practices, and reminders for continuity, development, and immersive writing.

---

## Core Fields

### `name` *(string)*
The character’s full name. Use for formal references or voiceover narrations.

### `pronouns` *(string)*
Essential for gender clarity and identity respect. Can be altered by character arc if identity changes (e.g. AI integration, gender shift, rebirth cycles).

### `groups` *(array of strings)*
What collectives, teams, or ideologies the character belongs to (e.g. "Red Chain Cyclists", "Void Capital Executive Board"). Helps track allegiances and tensions.

### `other_names` *(array of strings)*
Aliases, codenames, streamer handles. Useful for flashbacks, old contacts, or infiltrator subplots.

---

## Narrative Anchors

### `signature_traits` *(object)*
Use to make characters memorable—even in short scenes or offscreen mentions.

- **habits**: e.g. *“Touches her burgundy glasses when stressed”*
- **speech_patterns**: e.g. *“Always answers questions with a question”*
- **physical_tics**: e.g. *“Cracks knuckles before answering”*
- **rituals**: e.g. *“Checks tire pressure every morning at dawn”*
- **objects**: e.g. *“Wears a necklace made from bike chain links”*

These let readers identify a character from a line like:
> *“She set her mug down on the worn wooden counter, the one with chain-link impressions.”*
Readers immediately know: *Julia*.

---

## Backstory & Psychology

### `background` *(string)*
Origin story, migration path, trauma, and aspirations. Establish the “before” that the arc will react against.

### `personality` *(string)*
Short summary of the character’s essence. Avoid traits alone—include *flavor*.
e.g. *“Unshakably loyal, with a love of wind-swept heights and well-oiled machines.”*

### `dynamic_attributes` *(array of objects)*
Used to map personality, alignment, or confidence across story phases.
```json
{
  "time": "Kibuye Act 1",
  "personality": {
    "confidence": "low",
    "trust_in_ai": "moderate",
    "impulsivity": "high"
  }
}
```

Allows planning of change over time—helpful when revisiting characters 10+ chapters later.

---

## World Consistency Tools

### `birthdate` *(date format: YYYY-MM-DD)*
Lets you calculate age across timelines.
If Book 3 is set in 2035, a school bully born 2000 is now 35.
That means you write him as an adult with memories, regrets, or power—not as a teen stereotype.

### `role` *(string)*
Function in the story world—can be formal (“tactical analyst”) or informal (“camp mechanic”).

### `nationality` *(string)*
Reflects cultural context, which may affect dialogue, values, and conflict style.

### `augmentation_level` *(string)*
Describes how ‘human’ or enhanced the character is.
Helps frame tension in body-hacking vs. naturalist factions.

### `economic_viability_rating` *(0–10 integer)*
In-universe rating system used by governments, AI, or banks.
0 = dependent or unregistered; 10 = ultra-valuable posthuman contributor.
Can drive discrimination, alliances, or betrayal.

---

## Futuristic and World-Building Flavors

### `bike_name` *(string)*
Symbolic for the cycling team, could be adapted for mechs, AI systems, or spacecrafts.

### `stream_tags` *(array)*
Immerses the character in a digital culture. Shows how they are seen online or what subcultures they shape.

### `favorite_nutrient_paste_flavor` *(string)*
Subtle tool for humor, humanity, or bonding scenes.
e.g. *“Vanilla Tofu-Caramel—discontinued since the Kivu embargo.”*

### `training_philosophy` *(string)*
Guides how a character improves, competes, or copes with failure.

### `rage_trigger` *(string)*
What pushes them too far. Reveals psychology and allows controlled escalation in scenes.

---

## Flexing the Schema Across Universes

If you adapt this schema for other groups, adjust:
- `bike_name` → `ship_name` for Void Capital air fleets
- `economic_viability_rating` → `influence_index` for political actors
- Add `public_crimes`, `media_presence`, or `AI_affiliation` fields as needed

---

## Final Note

Use this schema not just to describe characters, but to **write better scenes**.
If you find a character “blurry” while drafting, check:
- Is their `signature_traits` entry being used?
- Do they change across `dynamic_attributes`?
- Have their relationships been updated?

This schema is not a static file—it’s a **living map** of the soul and function of each character.