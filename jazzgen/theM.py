import random

class theM:
    #circel = ["Cmaj", "Amin", "Gmaj", "Emin", "Dmaj", "Bmin", "Amaj", "F#min", "Emaj", "C#min", "Bmaj", "G#min",
    #          "F#maj", "D#min"]
    notes_pattern = [["A", 0], ["B", 2], ["C", 3], ["D", 5], ["E", 7], ["F", 8], ["G", 10]]
    notes = ["A", "B", "C", "D", "E", "F", "G"]


    scales = {
        "maj":[0,2,4,5,7,9,11],
        "min":[0,2,3,5,7,8,10],
        "harm":[0,2,3,5,7,8,11]

    }
    def scale_root_patter(self, root):
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
        r_p_scale = self.scale_root_patter(root)
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

    def scale_mode(self, root, mode):
        if mode == "ion":
            m = "C"
        if mode == "dor":
            m = "D"
        if mode == "phr":
            m = "E"
        if mode == "lyd":
            m = "F"
        if mode == "myx":
            m = "G"
        if mode == "aeo":
            m = "A"
        if mode == "lok":
            m = "B"
        r_p_scale = self.scale_root_patter(root)
        scale_with_pattern = []
        for note, s_pattern in zip(r_p_scale, [i[1] for i in self.scale_root_patter(m)]):
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

        r_p_scale = self.scale_root_patter(root[0])

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
        delta = self.scale_root_patter("C")[stufe-1][1]-seminotes

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
        #if n == "5":
        #    n = 2
        #if n == "7":
        #    n = 3
        #if n == "9":
        #    n = 4
        for i, note in enumerate(scale_with_root_pattern):
            #add = [scale_with_root_pattern[i][1]]
            intervall = []
            for _ in range(2):
                i += 2
                if i == 7:
                    i = 0
                if i > 6:
                    i = -6
                #add.append(scale_with_root_pattern[i][1])
                intervall.append(self.intervall_ident(note[0], scale_with_root_pattern[i][0]))

            chord_scale.append([note[0], intervall]) # optional semitones add,
        #if len(chord_scale[0][1]) >= 4:
        #    new = []
        #    for i, v in chord_scale:
        #        add = ""
        #        if "b" in v[-1]:
        #            c = v[-1].count("b")
        #            v[-1] = v[-1][-1]
        #            if c == 1:
         #               add = "b"
         #           if c == 2:
          #              add = "bb"
           #     if "#" in v[-1]:
            #        c = v[-1].count("b")
             #       v[-1] = v[-1][-1]
              #      if c == 1:
               #         add = "#"
                #    if c == 2:
                 #       add = "##"
            #    v[-1] = add+str(int(v[-1])+7)
             #   new.append([i, v])
           # return new

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

    def chord_scale(self, chord_scale_intervall):
        #chord_scale_intervall = self.chord_scale_intervall(root, skala)
        chord_scale = []
        for r_note, interv in chord_scale_intervall:
            add = r_note
            if "b3" in interv and "5" in interv:
                add+= "m"
            if "b5" in interv and "b3" in interv:
                add+="dim"
            if "b7" in interv:
                add+="7"
            if "7" in interv:
                add+="M7"
            if "b5" in interv and not "b3" in interv:
                add += "b5"
            if "#5" in interv:
                add+="#5"
            if "b3" in interv and "b5" in interv and "bb7" in interv:
                add = r_note
                add += "dim7"
            if "b3" in interv and "b5" in interv and "b7" in interv:
                add = r_note
                add += "m7b5"
            if "9" in interv and not ("b7" in interv or "7" in interv):
                add += "add9"
            if "b9" in interv and not ("b7" in interv or "7" in interv):
                add += "add-b9"
            if "9" in interv and ("b7" in interv or "7" in interv):
                add = r_note
                add += "9"
            if "b9" in interv and ("b7" in interv or "7" in interv):
                add = r_note
                add += "-b9"
            chord_scale.append(add)
        return chord_scale

    def add_chord_quality(self, chord_scale_intervall, stufe, quality):
        new_chord_scale = chord_scale_intervall
        quality-=1
        i = (stufe  + quality)%7 -1
        intervall = self.intervall_ident(chord_scale_intervall[stufe-1][0], chord_scale_intervall[i][0])
        add = ""
        if "b" in intervall:
            c = intervall.count("b")
            intervall = intervall[-1]
            if c == 1:
                add = "b"
            if c == 2:
                add = "bb"
        if "#" in intervall:
            c = intervall.count("b")
            intervall = intervall[-1]
            if c == 1:
                add = "#"
            if c == 2:
                add = "##"
        intervall = add + str(int(intervall))
        if quality+1 > 7:
            #new = new_chord_scale[stufe-1][1]
            add = ""
            if "b" in intervall:
                c = intervall.count("b")
                intervall = intervall[-1]
                if c == 1:
                    add = "b"
                if c == 2:
                    add = "bb"
            if "#" in intervall:
                c = intervall.count("b")
                intervall = intervall[-1]
                if c == 1:
                    add = "#"
                if c == 2:
                    add = "##"
            intervall = add + str(int(intervall) + 7)

        new_chord_scale[stufe - 1][1].append(intervall)
        return new_chord_scale

    def add_2nd_d(self, chord_scale_intervall, index):
        chord_scale_intervall.insert(index, [self.intervall_gen(chord_scale_intervall[index][0], "5"), ["3", "5", "b7"]])
        return chord_scale_intervall
    def add_251(self, chord_scale_intervall, index):
        chord_scale_intervall.insert(index, [self.intervall_gen(chord_scale_intervall[index][0], "5"), ["3", "5", "b7"]])
        chord_scale_intervall.insert(index, [self.intervall_gen(chord_scale_intervall[index+1][0], "2"), ["b3", "5", "b7"]])
        return chord_scale_intervall

    def find_index(self, chord_scale_intervall, note):
        return [i[0] for i in chord_scale_intervall].index(note)
    def functional(self, root, p):
        functions_dic = {"T": ["1", "6", "3"], "SD": ["4", "2", "b2"], "D": ["b2", "5", "7"]}
        pattern = {1: ["T", "SD", "D", "T"], 2: ["T", "SD", "D", "SD", "T"]}
        chord_scale_intervall = self.chord_scale_intervall(root, "maj")
        result = []
        for i in pattern[p]:
            choice = random.choice(functions_dic[i])
            chord_position = int(choice[-1])-1
            chord = chord_scale_intervall[chord_position]
            if choice == "b2":
                chord = [self.intervall_gen(root, "b2"), ["3", "5", "b7"]]
            result.append(chord)

        return result
    def tritone_sub(self, chord_scale_intervall, index):
        #index = self.find_index(chord_scale_intervall, chord)
        chord_scale_intervall[index] = [self.intervall_gen(chord_scale_intervall[index][0], "b5"), chord_scale_intervall[index][1]]
        return chord_scale_intervall

    def stufen_ident(self, chord_scale_intervall, root):
        result = []
        min_dic = {"1": "i", "b2": "bii", "2": "ii", "b3": "biii", "3": "iii", "b4": "iii", "4": "iv", "#4": "#iv", "b5": "bv", "5": "v", "b6": "bvi", "6": "vi", "bb7": "vi", "b7": "bvii", "7": "vii", "b1": "vii"}
        maj_dic = {"1": "I", "b2": "bII", "2": "II", "b3": "bIII", "3": "III", "b4": "III", "4": "IV", "#4": "#IV", "b5": "bV", "5": "V", "b6": "bVI", "6": "VI", "bb7": "VI", "b7": "bVII", "7": "VII", "b1": "VII"}
        for chord, interv in chord_scale_intervall:
            if "3" in interv:
                result.append(maj_dic[self.intervall_ident(root, chord)])
            if "b3" in interv:
                result.append(min_dic[self.intervall_ident(root, chord)])
        return result
    
    def stufen_gen(self, root, stufe):
        result = []
        min_dic = {'i': '1', 'bii': 'b2', 'ii': '2', 'biii': 'b3', 'iii': '3', 'iv': '4', '#iv': '#4', 'bv': 'b5', 'v': '5', 'bvi': 'b6', 'vi': '6', 'bvii': 'b7', 'vii': '7'}
        maj_dic = {'I': '1', 'bII': 'b2', 'II': '2', 'bIII': 'b3', 'III': '3', 'IV': '4', '#IV': '#4', 'bV': 'b5', 'V': '5', 'bVI': 'b6', 'VI': '6', 'bVII': 'b7', 'VII': '7'}

        try:
            interv = min_dic[stufe]
            return [self.intervall_gen(root, interv), ["b3", "5"]]
        except:
            interv = maj_dic[stufe]
            return [self.intervall_gen(root, interv), ["3", "5"]]
            







x = theM()
print(x.scale("C", "maj"))
print(x.intervall_gen("C#", "b5"))
print(x.intervall_ident("B", "G"))
print(x.scale_root_patter("C"))
chord_scale_intervall = x.chord_scale_intervall("C", "maj")
print(chord_scale_intervall)
#print(x.chord_scale_notes("E", "maj"))

#print(x.scale_mode("C", "lok"))
x.add_chord_quality(chord_scale_intervall, 7, 7)
x.add_chord_quality(chord_scale_intervall, 1, 7)
print(x.add_chord_quality(chord_scale_intervall, 2, 9))

chord_scale = x.chord_scale(chord_scale_intervall)
print(chord_scale)
test = x.add_2nd_d(chord_scale_intervall, 1)
print(test)
print(x.add_2nd_d(test, 1))
print(x.chord_scale(test))
print(x.find_index(test, "F"))
f = x.functional("C", 2)

f = x.add_2nd_d(f, -1)
x.tritone_sub(f, -2)
x.add_2nd_d(f, -3)
x.add_2nd_d(f, 1)
x.add_251(f, 1)
print(x.stufen_ident(f, f[0][0]))

print(x.chord_scale(f))
print(x.stufen_gen("C", "iv"))
