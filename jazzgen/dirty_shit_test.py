import random
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

    qcircel = ["Cmaj", "Amin", "Gmaj", "Emin", "Dmaj", "Bmin", "Amaj", "F#min", "Emaj", "C#min", "Bmaj", "G#min", "F#maj", "D#min"]

    def generate_progression_random(self, length=8):
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
        if root+scale_name in self.qcircel:
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
        # bezieht das scale_pattern aus dem dict
        scale_pattern = self.scales[scale_name]

        # fügt jene noten aus den gewählten notes(sharp/flat) mit dem scale_pattern in eine liste
        for i in scale_pattern:
            index = root_index + i
            if index <= 11:
                scale.append(notes[index])
            else:
                scale.append(notes[index-12])
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
        return scale,scale_name,notes

    def progression(self, scale, length):
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
        return progression, scale_c, scale_c_i, scale[2]


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
        return sub_prog







generate = ChordGenerator()
#print(generate.generate_progression_random())
skala = generate.scale()
#print(skala)
pro = generate.progression(skala, 8)
print("Progression: ",pro[0])
p = generate.substitute(pro)
new_p = []
for i in p:
    new_p.append(i + random.choice(["", "6", "7", "9", "11"]))
print("sub1:        ", new_p)
p = generate.substitute(pro)
new_p = []
for i in p:
    new_p.append(i + random.choice(["", "6", "7", "9", "11"]))
print("sub2:        ", new_p)
