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
    scales_name = ["maj", "min"]

    qcircle = ["Cmaj", "Amin", "Gmaj", "Emin", "Dmaj", "Bmin", "Amaj", "F#min", "Emaj", "C#min", "Bmaj", "G#min", "F#maj", "D#min"]


    def generate_progression(self, length=8):
        """Generate a random chord progression."""
        scale_result = self.scale()
        progression = [
            f"{random.choice(scale_result[0])}{random.choice(self.QUALITIES)}"
            for _ in range(length)
        ]
        return progression

    def scale(self):
        scale = []
        # wählt random eine root_note aus der sharp oder flat scale
        root = random.choice(random.choice(self.notes))
        # wählt random eine scale (minor/major)
        scale_name = random.choice(self.scales_name)
        # prüft welche notes (falt/sharp) passen, je nach root und tonart
        if root+scale_name in self.qcircle:
            notes = self.notes[0]
        else:
            notes = self.notes[1]
        # wandelt chromatischeverwechslung um. z.B C#maj ist nicht im qcircle -> flat_notes -> 
        # -> C# ist nicht in der flat_notes_liste -> error -> 
        try:
            # wählt den startpunkt
            root_index = notes.index(root)
        # -> nutzt den index aus der anderen notes_liste(sharp)
        except:
            notes_i = self.notes[self.notes.index(notes)-1]
            root_index = notes_i.index(root)
        # bezieht das scale_pattern aus dem dict. muss nicht über den scale_name bestimmt werden. scale_name dient als basis
        scale_pattern = self.scales[scale_name]
    
        # fügt jene noten aus den gewählten notes(sharp/flat) mit dem scale_pattern in eine liste
        for i in scale_pattern:
            index = root_index + i
            if index <= 11:
                scale.append(notes[index])
            else:
                scale.append(notes[index-12])
        # anpassung
        if root == "F#" and scale_name == "maj":
            scale[-1] = "E#"
        if root == "D#" and scale_name == "min":
            scale[1] = "E#"
        if root == "Gb" and scale_name == "maj":
            scale[3] = "Cb"
        if root == "Gb" and scale_name == "min":
            scale[2] = "Bbb"
            scale[3] = "Cb"
            scale[5] = "Ebb"
            scale[6] = "Fb"
        if root == "Eb" and scale_name == "min":
            scale[5] = "Cb"
        return scale,scale_name,root
