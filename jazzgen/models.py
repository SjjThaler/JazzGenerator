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

    substitute_progression = []

    def generate_progression(self, length=8):
        """Generate a random chord progression."""
        #print(generate.generate_progression_random())
        skala = self.scale()
        progression = self.progression(skala, 8)

        p = self.substitute(progression)
        new_p = []
        for i in p:
            new_p.append(i + random.choice(["", "6", "7", "9", "11"]))
        self.substitute_progression = new_p

        return progression[4]
    
    def generate_substitute_one(self, length=8):
        return self.substitute_progression

    
    def scale(self):
        '''
        Calculates the notes of a particular major or minor scale and returns
        the scale as a list of notes, the scale_kind (either major or minor) as a string. 
        Also returns the full possible tone material outside of the scale modified
        either by sharps or flats (for example: ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'])
        '''

        scale = []
        # wählt random eine root_note aus der sharp oder flat scale
        root = random.choice(random.choice(self.notes))
        # wählt random eine scale (minor/major)
        scale_kind = random.choice(self.scales_kind)
        # prüft welche scale (falt/sharp) passt, je nach root und tonart
        if root + scale_kind in self.circel_of_sharps:
            tone_material = self.notes[0]
        else:
            tone_material = self.notes[1]
        # wandelt chromatischeverwechslung um. z.B C#maj ist nicht im qcircle -> flat_scale ->
        # -> C# ist nicht in der flat_scale -> error ->
        try:
            # wählt den startpunkt
            root_index = tone_material.index(root)
        # -> nutzt den index aus der anderen scale(sharp)
        except:
            notes_i = self.notes[self.notes.index(tone_material)-1]
            root_index = notes_i.index(root)
        
        # bezieht das scale_pattern aus dem dict
        scale_pattern = self.scales[scale_kind]

        # fügt jene noten aus den gewählten notes(sharp/flat) mit dem scale_pattern in eine liste
        for i in scale_pattern:
            index = root_index + i
            if index <= 11:
                scale.append(tone_material[index])
            else:
                scale.append(tone_material[index-12])
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
        return scale,scale_kind,tone_material

    
    def progression(self, scale_material, length):
        '''
        Calculates a random chord progression given a particular scale.
        Returns the following:
        1. The chord progression as a list of chords with a defined starting chord, some random chords and the tonic as the end
        2. The scale_chords list which currently contains both the minor and major chords for the tones of the scale as sublists
        3. The scale_kind_index as a number (0 = minor vs. 1 = major) which is both used in this method but also in substitute
            => could possibly be removed in the future to simplify the code
        4. The tone material which was originally returned by the scale method (see scale method comment for explanation and example)
        5. The cleaned progression as a list of chords which match the standard naming convetions for each chord
        '''

        # Extracting the different sublists from the scale_material
        scale_tones = scale_material[0]
        scale_kind = scale_material[1]
        tone_material = scale_material[2]
        
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

        # Return all of the material because the substitue method is dependend on it...
        return progression, scale_chords, scale_kind_index, tone_material, cleaned_progression


    def substitute(self, progression):
        if "maj" in progression[1][progression[2]][0]:
            su = [[0, 2, 5], [1, 3], [4, 6]]
        else:
            su = [[0, 2, 4], [5, 3], [1, 6]]

        sub_prog = []
        prob = [0, 0, 0, 0, 1, 1, 2, 2, 2]
        # 0=funktional, 1=tritonus, 2=borow
        for p_chords in progression[0]:
            p = random.choice(prob)
            if p == 0:
                for subs in su:
                    if progression[1][progression[2]].index(p_chords) in subs:
                        sub_prog.append(progression[1][progression[2]][random.choice(subs)])
            elif p == 1:

                index = progression[3].index(p_chords[:-3])+6
                if index <= 11:
                    sub_prog.append(progression[3][index]+p_chords[-3::])
                else:
                    sub_prog.append(progression[3][index-12]+p_chords[-3::])
            elif p == 2:
                index = progression[1][progression[2]].index(p_chords)
                sub_prog.append(progression[1][progression[2]-1][index])
        cleaned_substitute_progression = self.filter(sub_prog)
        return cleaned_substitute_progression
    
    def filter(self, progression):
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
