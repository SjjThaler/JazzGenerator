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

    def generate_progression(self, length=8):
        """Generate a random chord progression."""
        progression = [
            f"{random.choice(self.CHORDS)}{random.choice(self.QUALITIES)}"
            for _ in range(length)
        ]
        return progression
