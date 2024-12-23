from django.shortcuts import render
from .models import ChordProgression, ChordRandom, ChordCombiner
from urllib.parse import quote  # Import URL encoding function

def random_chords(request):
    generator = ChordRandom()

    # Check if user wants to save the progression (optional functionality)
    
    progression = generator.generate_progression(length=4)
    chords_with_diagrams = [
        {
            "name": chord,
            "diagram_url": f"/media/chord_diagrams/{quote(chord)}.png"  # Encode chord names
        }
        for chord in progression
    ]

    return render(request, 'chords.html', {'progression': progression, 'diagrams': chords_with_diagrams})

def chosen_chords(request):
    generator = ChordCombiner()
    progression = generator.generate_progression(length=8)
    chords_with_diagrams = [
        {
                "name": chord,
                "diagram_url": f"/media/chord_diagrams/{quote(chord)}.png"  # Encode chord names
            }
            for chord in progression
        ]
    
    substitute = generator.generate_substitute_one(length=8)
    subs_with_diagrams = [
        {
                "name": chord,
                "diagram_url": f"/media/chord_diagrams/{quote(chord)}.png"  # Encode chord names
            }
            for chord in substitute
    ]
    return render(request, 'jazz.html', {'progression': progression, 'diagrams': chords_with_diagrams, 'substitute': substitute, 'substitute_diagrams': subs_with_diagrams})



def display_progressions(request):
    # Fetch all progressions from the database
    progressions = ChordProgression.objects.all()
    return render(request, 'progressions.html', {'progressions': progressions})


