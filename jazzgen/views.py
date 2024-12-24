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

    # Add chord diagrams to the diatonic progression (= index 0)
    chords_with_diagrams = [
        {
                "name": chord,
                "diagram_url": f"/media/chord_diagrams/{quote(chord)}.png"  # Encode chord names
            }
            for chord in progression[0]
        ]
    # Add chord diagrams to the jazz progression (= index 1)
    subs_with_diagrams = [
        {
                "name": chord,
                "diagram_url": f"/media/chord_diagrams/{quote(chord)}.png"  # Encode chord names
            }
            for chord in progression[1]
    ]
    return render(request, 'jazz.html', {'diagrams': chords_with_diagrams, 'substitute_diagrams': subs_with_diagrams})



#######################################
#             OBSOLETE                #
#######################################
def display_progressions(request):
    # Fetch all progressions from the database
    progressions = ChordProgression.objects.all()
    return render(request, 'progressions.html', {'progressions': progressions})


