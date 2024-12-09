from django.db import models
import random

class ChordProgression(models.Model):
    progression = models.TextField()  # Stores the progression as a comma-separated string
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when saved

    def __str__(self):
        return self.progression

class ChordGenerator:
    CHORDS = ['C', 'C#', 'D', 'D#', 'Db', 'E', 'Eb', 'F', 'F#', 'G', 'Gb', 'G#', 'A', 'Ab', 'A#', 'B', 'Bb']
    QUALITIES = ['maj', 'min', 'dim', 'aug', '7', '6', '9', '11']
    notes = [["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"],
             ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
             ]


    scales = {
        "maj":[0,2,4,5,7,9,11],
        "min":[0,2,3,5,7,8,10]

    }
    scales_name = ["maj", "min"]

    qcircle = ["Cmaj", "Amin", "Gmaj", "Emin", "Dmaj", "Bmin", "Amaj", "F#min", "Emaj", "C#min", "Bmaj", "G#min"]


    def generate_progression(self, length=8):
        """Generate a random chord progression."""
        progression = [
            f"{random.choice(self.CHORDS)}{random.choice(self.QUALITIES)}"
            for _ in range(length)
        ]
        return progression

    def scale(self):
        scale = []
        # wählt random eine root_note aus der sharp oder flat scale
        root = random.choice(random.choice(self.notes))
        # wählt random eine scale (minor/major)
        scale_name = random.choice(self.scales_name)
        # prüft welche scale (falt/sharp) passt, je nach root und tonart
        if root+scale_name in self.qcircle:
            notes = self.notes[0]
        else:
            notes = self.notes[1]
        # wandelt chromatischeverwechslung um. z.B C#maj ist nicht im qcircle -> flat_scale -> 
        # -> C# ist nicht in der flat_scale -> error -> 
        try:
            # wählt den startpunkt
            root_index = notes.index(root)
        # -> nutzt den index aus der anderen scale(sharp)
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
        return scale,scale_name,root
