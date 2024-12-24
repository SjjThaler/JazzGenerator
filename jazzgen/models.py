from django.db import models
import random

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
        the scale as a list of notes, the scale_kind (either major or minor) as a string
        and the tone material of the scale.
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

    
    def progression(self, scale, length):
        '''
        Calculates a random chord progression given a particular scale by (work in progress, lol)
        '''
        scale_c = [[s+q for s, q in zip(scale[0], ["min", "dim", "maj", "min", "min", "maj", "maj"])],
                    [s+q for s, q in zip(scale[0], ["maj", "min", "min", "maj", "maj", "min", "dim"])]
        ]
        if scale[1] == "min":
            scale_c_i = 0
            start = random.choice([0, 3, 4])
        if scale[1] == "maj":
            scale_c_i = 1
            start = random.choice([0, 1, 3, 4])

        progression = [scale_c[scale_c_i][start]]
        for _ in range(length-2):
            chord = random.choice(scale_c[scale_c_i])
            progression.append(chord)
        progression.append(scale_c[scale_c_i][0])
        cleaned_progression = self.filter(progression)
        return progression, scale_c, scale_c_i, scale[2], cleaned_progression


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
