from theM import theM  # Assuming theM class is in the theM.py file

# Initialize the music theory helper
music = theM()

# 1. Generate the root pattern for a scale
# Explain: This generates a list of notes and their semitone values starting from the root note.
root = "C"
root_pattern = music.scale_root_patter(root)
print(f"Root Pattern for {root}: {root_pattern}")

# 2. Generate a major scale
# Explain: The 'scale' function applies a scale pattern (e.g., major) to the root note.
scale_type = "min"
major_scale = music.scale(root, scale_type)
print(f"{root} {scale_type.capitalize()} Scale: {major_scale}")

# 3. Identify a specific interval
# Explain: 'intervall_ident' calculates the interval (e.g., "b3", "5") between two notes.
note1 = "C"
note2 = "E"
interval = music.intervall_ident(note1, note2)
print(f"Interval between {note1} and {note2}: {interval}")

# 4. Generate chords for a major scale
# Explain: 'chord_scale_intervall' determines chord intervals for each note in the scale.
chord_intervals = music.chord_scale_intervall(root, scale_type)
print(f"Chord Intervals for {root} {scale_type.capitalize()} Scale: {chord_intervals}")

# 5. Add a 2nd dominant chord
# Explain: 'add_2nd_d' adds a dominant chord based on the 2nd of the chord scale.
chord_intervals_with_2nd_d = music.add_2nd_d(chord_intervals, 1)  # Adding a dominant chord after the first chord
print(f"Chord Intervals with 2nd Dominant: {chord_intervals_with_2nd_d}")

# 6. Identify functional degrees (stufen) of chords
# Explain: 'stufen_ident' determines the functional role (e.g., "I", "ii") of each chord.
functional_roles = music.stufen_ident(chord_intervals, root)
print(f"Functional Roles in {root} {scale_type.capitalize()} Scale: {functional_roles}")

# 7. Generate a random progression
# Explain: 'rand_prog' creates a random chord progression of the given length.
progression_length = 4
random_progression = music.rand_prog(root, progression_length)
print(f"Random Chord Progression in {root}: {random_progression}")

# 8. Enhance the progression with ii-V-I
# Explain: 'add_251' adds a ii-V-I progression at the specified position.
enhanced_progression = music.add_251(random_progression, -1)  # Adding ii-V-I at the end
print(f"Enhanced Progression with ii-V-I: {enhanced_progression}")

# 9. Perform a tritone substitution
# Explain: 'tritone_sub' substitutes a chord with its tritone equivalent.
tritone_substituted = music.tritone_sub(enhanced_progression, 2)  # Substituting the 3rd chord
print(f"Progression after Tritone Substitution: {tritone_substituted}")
