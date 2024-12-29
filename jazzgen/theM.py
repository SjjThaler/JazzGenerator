import random

class theM:

    notes_pattern = [["A", 0], ["B", 2], ["C", 3], ["D", 5], ["E", 7], ["F", 8], ["G", 10]]
    notes = ["A", "B", "C", "D", "E", "F", "G"]


    scales = {
        "maj":[0,2,4,5,7,9,11],
        "min":[0,2,3,5,7,8,10],
        "harm":[0,2,3,5,7,8,11]

    }
    def scale_mode(self, root):
        r_p_scale = []
        add = 0
        if "#" in root:
            add = -root.count("#")
            root = root[0]
        if "b" in root:
            add = root.count("b")
            root = root[0]
        root_index = self.notes.index(root)
        scale_to_root = self.notes_pattern[root_index::] + self.notes_pattern[:root_index]
        tone_subtraction = scale_to_root[0][1]
        for note, v in scale_to_root:
            v -= tone_subtraction
            if v < 0:
                v += 12
            r_p_scale.append([note, v + add])
        return r_p_scale

    # r_p_scale = root, pattern scale
    def scale(self, root, skala):
        r_p_scale = self.scale_mode(root)
        scale_with_pattern = []

        for note, s_pattern in zip(r_p_scale, self.scales[skala]):
            if note[1] - s_pattern == 0:
                scale_with_pattern.append(note)
            if note[1] - s_pattern == -1:
                scale_with_pattern.append([note[0]+"#", s_pattern])
            if note[1] - s_pattern == -2:
                scale_with_pattern.append([note[0]+"##", s_pattern])
            if note[1] - s_pattern == 1:
                scale_with_pattern.append([note[0]+"b", s_pattern])
            if note[1] - s_pattern == 2:
                scale_with_pattern.append([note[0]+"bb", s_pattern])

        return scale_with_pattern

    def intervall_gen(self, tone, interv):
        inter = {"1":0, "b2":1, "2":2, "#2":3, "b3":3, "3":4, "#3":5, "4":5, "A4":6, "#4":6, "b5":6, "5":7, "#5":8, "b6":8, "6":9, "#6":10, "b7":10, "7":11, "#7":0}
        ind = [["1"], ["b2", "2", "#2"], ["b3", "3", "#3"], ["4", "A4", "#4"], ["b5", "5", "#5"], ["b6", "6", "#6"], ["b7", "7", "#7"]]
        for i, sublist in enumerate(ind):
            if interv in sublist:
                stop = i
                break
        n = inter[interv]
        add = 0
        n_tone = tone
        if "#" in tone:
            add = -tone.count("#")
            n_tone = tone[0]
        if "b" in tone:
            add = tone.count("b")
            n_tone = tone[0]
        tone_index = self.notes.index(n_tone)
        scale_to_tone = self.notes_pattern[tone_index::] + self.notes_pattern[:tone_index]
        tones_pattern = []
        tone_subtraction = scale_to_tone[0][1]
        for note, v in scale_to_tone:
            v -= tone_subtraction
            if v < 0:
                v+=12
            tones_pattern.append([note, v+add])
        s = tones_pattern[0][1]-add

        if n > 11:
            n-= 12

        note = tones_pattern[stop]
        if note[1] - s == n:
            intervall = note[0]
        if note[1] - s == n-1:
            intervall = note[0] + "#"
        if note[1] - s == n-2:
            intervall = note[0] + "##"
        if note[1] - s == n+1:
            intervall = note[0] + "b"
        if note[1] - s == n+2:
            intervall = note[0] + "bb"

        return intervall

    def intervall_ident(self, root, tone):

        r_p_scale = self.scale_mode(root[0])

        add = 0
        if "#" in root:
            add = -root.count("#")
            root = root[0]
        if "b" in root:
            add = root.count("b")
            root = tone[0]
        if "#" in tone:
            add += tone.count("#")
            tone = tone[0]
        if "b" in tone:
            add += -tone.count("b")
            tone = tone[0]

        for i, sublist in enumerate(r_p_scale):
            if tone in sublist:
                tone_ = r_p_scale[i]
                stufe = i + 1
                break

        seminotes = tone_[1] + add
        delta = self.scale_mode("C")[stufe-1][1]-seminotes

        if delta == 0:
            intervall = f"{stufe}"
        if delta == 1:
            intervall = f"b{stufe}"
        if delta == 2:
            intervall = f"bb{stufe}"
        if delta == -1:
            intervall = f"#{stufe}"
        if delta == -2:
            intervall = f"##{stufe}"

        return intervall





    def chord_scale_intervall(self, root, skala):
        scale_with_root_pattern = self.scale(root, skala)
        chord_scale = []
        for i, note in enumerate(scale_with_root_pattern):
            #add = [scale_with_root_pattern[i][1]]
            intervall = []
            for _ in range(3):
                i += 2
                if i == 7:
                    i = 0
                if i > 6:
                    i = -6
                #add.append(scale_with_root_pattern[i][1])
                intervall.append(self.intervall_ident(note[0], scale_with_root_pattern[i][0]))

            chord_scale.append([note[0], intervall]) # optional semitones add,
        return chord_scale

    def chord_scale_notes(self, root, skala):
        chord_scale = self.chord_scale_intervall(root, skala)
        chord_scale_notes = []
        for r_note, chord_pattern in chord_scale:
           add = [r_note]
           for i in chord_pattern:
               add.append(self.intervall_gen(r_note, i))
           chord_scale_notes.append(add)
        return chord_scale_notes

    def chord_scale(self, root, skala):
        chord_scale_intervall = self.chord_scale_intervall(root, skala)
        chord_scale = []
        for r_note, interv in chord_scale_intervall:
            if "b3" in interv:
                r_note+= "m"
            if "b5" in interv:
                r_note+="dim"
            if "b7" in interv:
                r_note+="7"
            if "7" in interv:
                r_note+="M7"
            chord_scale.append(r_note)
        return chord_scale



x = theM()
print(x.scale("C", "maj"))
print(x.intervall_gen("C#", "b5"))
print(x.intervall_ident("B", "G"))
print(x.scale_mode("C"))
print(x.chord_scale_intervall("E", "harm"))
#print(x.chord_scale_notes("E", "maj"))
print(x.chord_scale("A", "harm"))
