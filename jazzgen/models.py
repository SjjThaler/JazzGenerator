from django.db import models
import random
import pdb

class ChordProgression(models.Model):
    progression = models.TextField()  # Stores the progression as a comma-separated string
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when saved

    def __str__(self):
        return self.progression
    
class ChordRandom:
    CHORDS = ['C', 'C#', 'D', 'D#', 'Db', 'E', 'Eb', 'F', 'F#', 'G', 'Gb', 'G#', 'A', 'Ab', 'A#', 'B', 'Bb']
    QUALITIES = ['maj', 'min', 'dim', 'aug', 'm(M7)', 'm7', '7', 'm6', '6', '9', '11']

    def generate_progression(self, length=8):
        """Generate a random chord progression."""
        progression = [
            f"{random.choice(self.CHORDS)}{random.choice(self.QUALITIES)}"
            for _ in range(length)
        ]
        return progression

class ChordCombiner:
    CHORDS = ['C', 'C#', 'D', 'D#', 'Db', 'E', 'Eb', 'F', 'F#', 'G', 'Gb', 'G#', 'A', 'Ab', 'A#', 'B', 'Bb']
    QUALITIES = ['maj', 'min', 'dim', 'aug', 'm(M7)', 'm7', '7', 'm6', '6', '9', '11']
    notes = [["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"],
             ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
             ]


    scales = {
        "maj":[0,2,4,5,7,9,11],
        "min":[0,2,3,5,7,8,10]

    }
    scales_kind = ["maj", "min"]

    circel_of_sharps = ["Cmaj", "Amin", "Gmaj", "Emin", "Dmaj", "Bmin", "Amaj", "F#min", "Emaj", "C#min", "Bmaj", "G#min", "F#maj", "D#min"]

    def generate_progression(self, length=8):
        """Generate a diatonic and a complex jazz chord progression and return them as a two sublists within a list."""
        #print(generate.generate_progression_random())
        skala = self.scale()
        diatonic_progression = self.progression(skala, 8)

        simple_jazz_progression = self.substitute(diatonic_progression)
        complex_jazz_progression = []
        for i in simple_jazz_progression:
            complex_jazz_progression.append(i + random.choice(["", "6", "7", "9", "11"]))

        return diatonic_progression[4], complex_jazz_progression
    
    
    def scale(self):
        '''
        Calculates the notes of a particular major or minor scale and returns
        the scale as a list of notes, the scale_kind (either major or minor) as a string. 
        Also returns the full chromatic scale either in sharps or in flats. 
        For example: ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'])
        '''

        scale = []
        # wählt random eine root_note aus der sharp oder flat scale
        root = random.choice(random.choice(self.notes))
        # wählt random eine scale (minor/major)
        scale_kind = random.choice(self.scales_kind)
        # prüft welche scale (falt/sharp) passt, je nach root und tonart
        if root + scale_kind in self.circel_of_sharps:
            chromatic_scale = self.notes[0]
        else:
            chromatic_scale = self.notes[1]
        # wandelt chromatischeverwechslung um. z.B C#maj ist nicht im qcircle -> flat_scale ->
        # -> C# ist nicht in der flat_scale -> error ->
        try:
            # wählt den startpunkt
            root_index = chromatic_scale.index(root)
        # -> nutzt den index aus der anderen scale(sharp)
        except:
            notes_i = self.notes[self.notes.index(chromatic_scale)-1]
            root_index = notes_i.index(root)
        
        # bezieht das scale_pattern aus dem dict
        scale_pattern = self.scales[scale_kind]

        # fügt jene noten aus den gewählten notes(sharp/flat) mit dem scale_pattern in eine liste
        for i in scale_pattern:
            index = root_index + i
            if index <= 11:
                scale.append(chromatic_scale[index])
            else:
                scale.append(chromatic_scale[index-12])
        if root == "F#" and scale_kind == "maj":
            scale[-1] = "E#"
        if root == "D#" and scale_kind == "min":
            scale[1] = "E#"
        if root == "Gb" and scale_kind == "maj":
            scale[3] = "Cb"
        if root == "Gb" and scale_kind == "min":
            scale[2] = "Bbb"
            scale[3] = "Cb"
            scale[5] = "Ebb"
            scale[6] = "Fb"
        if root == "Eb" and scale_kind == "min":
            scale[5] = "Cb"
        return scale,scale_kind,chromatic_scale

    
    def progression(self, scale_material, length):
        '''
        Calculates a random chord progression given a particular scale.
        Returns the following:
        1. The chord progression as a list of chords with a defined starting chord, some random chords and the tonic as the end
        2. The scale_chords list which currently contains both the minor and major chords for the tones of the scale as sublists
            => Example: [['Abmin', 'Bbdim', 'Cmaj', 'Dbmin', 'Ebmin', 'Fmaj', 'Gmaj'], ['Abmaj', 'Bbmin', 'Cmin', 'Dbmaj', 'Ebmaj', 'Fmin', 'Gdim']]
        3. The scale_kind_index as a number (0 = minor vs. 1 = major) which is both used in this method but also in substitute
            => could possibly be removed in the future to simplify the code
        4. The chromatic scale which was originally returned by the scale method (see scale method comment for explanation and example)
        5. The cleaned progression as a list of chords which match the standard naming convetions for each chord
        '''

        # Extracting the different sublists from the scale_material
        scale_tones = scale_material[0]
        scale_kind = scale_material[1]
        chromatic_scale = scale_material[2]
        
        # Concatenating the scale_tones with both major and minor scale chords by first creating tuples with zip and then iterating through each tuple
        scale_chords = [[s+q for s, q in zip(scale_tones, ["min", "dim", "maj", "min", "min", "maj", "maj"])],
                    [s+q for s, q in zip(scale_tones, ["maj", "min", "min", "maj", "maj", "min", "dim"])]
        ]

        # Choosing the correct chords depending on whether scale kind is major or minor. Also chooses a common
        # start for the chord progression. Common starting chords are here defined as 
        # either the tonic, the supertonic, the subdominant or the dominant function of the scale
        if scale_kind == "min":
            scale_kind_index = 0
            start = random.choice([0, 3, 4])
        if scale_kind == "maj":
            scale_kind_index = 1
            start = random.choice([0, 1, 3, 4])

        # Create the progression list and immediately add the starting chord as defined above.
        progression = [scale_chords[scale_kind_index][start]]

        # Add length-2 chords from either the minor or major chord. Why length -2? Because the start and end
        # of the chord progression are not supposed to be random chords.
        for _ in range(length-2):
            chord = random.choice(scale_chords[scale_kind_index])
            progression.append(chord)
        
        # Add the tonic chord to the end of the chord progression
        progression.append(scale_chords[scale_kind_index][0])

        # Clean the names of each of the chords to match standard chord naming convents.
        # Examples: 
        # Cmin7 is changed into Cm7
        # Gmaj is changed into G
        cleaned_progression = self.filter(progression)

        # Return all of the material because the substitue method is dependant on it...
        return progression, scale_chords, scale_kind_index, chromatic_scale, cleaned_progression


    def substitute(self, progression_material):
        '''
        Substitutes chords within the chord progression from the progression method and returns a list containing a new chord progression.
        This chord progression differs from the original chord progression by:
        1. Diatonic / functional substitutions
        2. Tritonus substitutions
        3. Borrowed chords
        '''
        # Unpacking the material returned from the progression method, see progression method docstring for explanation
        progression = progression_material[0]
        scale_chords = progression_material[1]
        scale_kind_index = progression_material[2]
        chromatic_scale = progression_material[3]
        cleaned_progression = progression_material[4] # not used in this method but needed in the generate_progression method

        # Create the list which will be filled with the chord progression modified with substitutions
        sub_prog = []

        # Define the substitution_kind list which additionally weighs 
        # the probability of each substitution (i.e. 0 is more probable than 1 and 2)
        # 0 = diatonic / functional substitution
        # 1 = tritonus substitution
        # 2 = borrowed chords
        
        substitution_kind = [0, 0, 0, 0, 1, 1, 2, 2, 2]
        
        # For each chord in the progression choose a random substitution kind
        for chords in progression:
            substitution = random.choice(substitution_kind)
            # ======================================
            #       Functional substitution
            # ======================================
            # Firstly define functional groups for major and minor scales
            if "maj" in scale_chords[scale_kind_index][0]:
                functional_substitutions = [[0, 2, 5], # tonic group 
                                        [1, 3], # subdominant group
                                        [4, 6]] # dominant group
            else:
                functional_substitutions = [[0, 2, 4], # tonic group
                                        [5, 3], # subdominant group
                                        [1, 6]] # dominant group
                # => needs revision! Not sure whether the functional groups in the minor keys are correct!
            if substitution == 0:
                for subs in functional_substitutions:
                    if scale_chords[scale_kind_index].index(chords) in subs: # Check if the scale function of chord is any of [0, 2, 5], [1,3], or [4,6]
                        sub_prog.append(scale_chords[scale_kind_index][random.choice(subs)]) # If yes, choose a random item within the tonic, subdominant or dominant sub-lists (could lead to choosing the original function leading to no substitution)
            # ======================================
            #       Tritonus substitution
            # ======================================
            elif substitution == 1:
                # Remove 'maj' or 'min' and find index of the chord root in the chromatic scale
                # Then add six semitones to calculate the index of the name of the chord root one tritonus away
                try:
                    tritonus_index = chromatic_scale.index(chords[:-3])+6
                
                except ValueError: # Some values are not in the chromatic_scale (Ebb, Bbb, E# etc.)
                    continue

                # Append the tritonus chord root determined above and re-concatenate 'maj' or 'min' onto it again
                if tritonus_index <= 11:
                    sub_prog.append(chromatic_scale[tritonus_index] + chords[-3::]) # Simply append the note that represents the tritonus_index within the chromatic scale
                else:
                    sub_prog.append(chromatic_scale[tritonus_index-12] + chords[-3::]) # Handle exceeding the index when going beyond the octave within the chromatic scale
            # =======================================
            # Borrowed chords
            # =======================================
            elif substitution == 2:
                chord_index = scale_chords[scale_kind_index].index(chords) # Determine the current position of the chord within the scale's chords
                sub_prog.append(scale_chords[scale_kind_index-1][chord_index]) # Change the scale kind to choose the corresponding chord within the parallel scale
        
        # Rename the chords in sub_prog with standard names for chords
        cleaned_substitute_progression = self.filter(sub_prog)
        
        # Finally return everything...
        return cleaned_substitute_progression
    
    def filter(self, progression):
        '''
        Clean the names of each of the chords to match standard chord naming convents.
        Examples: 
        Cmin7 is changed into Cm7
        Gmaj is changed into G
        '''
        cleaned_progression = []
        for chord in progression:
            if "maj" in chord:
                reduced_chord = chord[:-3]
                cleaned_progression.append(reduced_chord)
            if "min" in chord:
                reduced_chord = chord[:-2]
                cleaned_progression.append(reduced_chord)
            if "dim" in chord:
                reduced_chord = chord
                cleaned_progression.append(reduced_chord)
        return cleaned_progression
