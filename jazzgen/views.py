from django.shortcuts import render
from .models import ChordProgression, ChordRandom, ChordCombiner
from urllib.parse import quote  # Import URL encoding function

def random_chords(request):
    generator = ChordRandom()

    # Check if user wants to save the progression (optional functionality)
    if request.method == "POST":
        progression = generator.generate_progression(length=4)
        saved_progression = ChordProgression.objects.create(progression=", ".join(progression))
        saved_progression.save()
    else:
        progression = generator.generate_progression(length=4)
        chords_with_diagrams = [
            {
                "name": chord,
                "diagram_url": f"/media/chord_diagrams/{quote(chord)}.png"  # Encode chord names
            }
            for chord in progression
        ]

    return render(request, 'chords.html', {'progression': progression, 'diagrams': chords_with_diagrams})


def display_progressions(request):
    # Fetch all progressions from the database
    progressions = ChordProgression.objects.all()
    return render(request, 'progressions.html', {'progressions': progressions})


