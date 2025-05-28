# Character Schema Companion Guide
**For writers, AI co-authors, and collaborative storyworld builders**

This schema is designed to support character-driven storytelling in *They Burn Witches* and related storyworlds. While it was initially built for the cycling team in a sci-fi-punk arc, it is modular and can be adapted to other factions—such as Void Capital executives, off-grid AI communities, or historical arcs in flashbacks.

Each field below includes examples, best-use practices, and reminders for continuity, development, and immersive writing.

---

## Core Fields

### `id` *(string)* **[IMMUTABLE]**
⚠️ **CRITICAL**: This is an IMMUTABLE unique identifier used as both filename and programmatic reference. Once established, this should NEVER be changed as it breaks external references, file management systems, and data integrity.

Use other fields like `other_names`, `role`, or descriptive text to reflect character evolution. If you need to indicate major character transformation, add it to `other_names` or track it in `worldview_evolution`.

**Example**: `"Saga_Lundqvist_The_chaotic_rising_star"` stays the same even if Saga becomes more thoughtful and curious.

### `name` *(string)*
The character's full name. Use for formal references or voiceover narrations. This can change if the character legally changes their name or adopts a new identity.

### `pronouns` *(string)*
Essential for gender clarity and identity respect. Can be altered by character arc if identity changes (e.g. AI integration, gender shift, rebirth cycles).

### `groups` *(array of strings)*
What collectives, teams, or ideologies the character belongs to (e.g. "Red Chain Cyclists", "Void Capital Executive Board"). Helps track allegiances and tensions. This should evolve as characters join or leave organizations.

### `other_names` *(array of strings)*
Aliases, codenames, streamer handles, evolutionary nicknames. Useful for flashbacks, old contacts, or infiltrator subplots. **Use this field to reflect character growth** - add new names that reflect their evolution without breaking the immutable `id`.

---

## Character Evolution Tracking

### `worldview_evolution` *(object)* **[NEW]**
Maps how the character's understanding of the world changes across story phases. Key for tracking growth arcs and thematic development.

**Example**:
```json
"worldview_evolution": {
  "Stockholm": "Adventure is content, chaos is entertainment",
  "Africa_arrival": "Wait, why is everything expensive if people don't have money?",
  "Lake_Kivu": "What if the important questions don't have comfortable answers?"
}
```

### `signature_questions` *(array)* **[NEW]**
Key questions the character asks that reveal their nature and drive plot/theme development. Especially useful for characters who serve as the story's conscience or philosophical voice.

**Example**: `["But why do we need motors to pedal?", "Are we disaster tourists?"]`

### `dynamic_attributes` *(array of objects)*
Used to map personality, alignment, or confidence across story phases.
```json
{
  "time": "Africa_awakening",
  "personality": {
    "curiosity": "fearless and cutting",
    "empathy": "expanding beyond comfort zone",
    "wisdom": "accidentally profound through honest questions"
  }
}
```

Allows planning of change over time—helpful when revisiting characters 10+ chapters later.

---

## Narrative Anchors

### `signature_traits` *(object)*
Use to make characters memorable—even in short scenes or offscreen mentions.

- **habits**: e.g. *"Touches her burgundy glasses when stressed"*
- **speech_patterns**: e.g. *"Always answers questions with a question"*
- **physical_tics**: e.g. *"Cracks knuckles before answering"*
- **rituals**: e.g. *"Checks tire pressure every morning at dawn"*
- **objects**: e.g. *"Wears a necklace made from bike chain links"*

These let readers identify a character from a line like:
> *"She set her mug down on the worn wooden counter, the one with chain-link impressions."*
Readers immediately know: *Julia*.

---

## Backstory & Psychology

### `background` *(string)*
Origin story, migration path, trauma, and aspirations. Establish the "before" that the arc will react against. This can be updated to reflect new revelations about the character's past.

### `personality` *(string)*
Short summary of the character's essence. Avoid traits alone—include *flavor*. This should evolve to reflect character growth while maintaining core identity.
e.g. *"Unshakably loyal, with a love of wind-swept heights and well-oiled machines."*

---

## World Consistency Tools

### `birthdate` *(date format: YYYY-MM-DD)*
Lets you calculate age across timelines.
If Book 3 is set in 2035, a school bully born 2000 is now 35.
That means you write him as an adult with memories, regrets, or power—not as a teen stereotype.

### `role` *(string)*
Function in the story world—can be formal ("tactical analyst") or informal ("camp mechanic"). **Can evolve** to reflect character growth, but consider the impact on external systems that might use this for categorization.

### `nationality` *(string)*
Reflects cultural context, which may affect dialogue, values, and conflict style.

### `augmentation_level` *(string)*
Describes how 'human' or enhanced the character is.
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
Immerses the character in a digital culture. Shows how they are seen online or what subcultures they shape. Should evolve as character grows or audience perception changes.

### `favorite_nutrient_paste_flavor` *(string)*
Subtle tool for humor, humanity, or bonding scenes.
e.g. *"Vanilla Tofu-Caramel—discontinued since the Kivu embargo."*

### `training_philosophy` *(string)*
Guides how a character improves, competes, or copes with failure. Can evolve as characters learn and grow.

### `rage_trigger` *(string)*
What pushes them too far. Reveals psychology and allows controlled escalation in scenes. May evolve as characters mature or heal from trauma.

---

## Data Management Best Practices

### Immutable vs. Mutable Fields
- **NEVER CHANGE**: `id`, `birthdate`
- **CHANGE CAREFULLY**: `role`, `name` (consider external system impacts)
- **EVOLVE FREELY**: All descriptive text, arrays like `other_names`, `stream_tags`, personality descriptions, relationships

### Version Control for Character Development
When updating character files:
1. Update descriptive fields to reflect current character state
2. Add new phases to `dynamic_attributes` rather than overwriting old ones
3. Add new names/titles to `other_names` rather than changing `id` or `name`
4. Use `worldview_evolution` to track major philosophical changes
5. Update relationships to reflect new dynamics, but preserve relationship history in the text

### Cross-Reference Integrity
Before changing any character data:
- Check if other character files reference this character by `id` or `name`
- Verify that any external tools or databases use these fields as keys
- Update all references consistently if making breaking changes

---

## Flexing the Schema Across Universes

If you adapt this schema for other groups, adjust:
- `bike_name` → `ship_name` for Void Capital air fleets
- `economic_viability_rating` → `influence_index` for political actors
- Add `public_crimes`, `media_presence`, or `AI_affiliation` fields as needed
- Add `thematic_function` to track what role each character plays in the story's larger themes

---

## Final Note

Use this schema not just to describe characters, but to **write better scenes**.
If you find a character "blurry" while drafting, check:
- Is their `signature_traits` entry being used?
- Do they change across `dynamic_attributes`?
- Have their relationships been updated?
- Are their `signature_questions` driving meaningful dialogue?
- Does their `worldview_evolution` reflect their journey?

This schema is not a static file—it's a **living map** of the soul and function of each character. But remember: some parts of this map (like the `id`) are permanent landmarks that other systems depend on. Change thoughtfully, and always consider the ripple effects of your modifications.