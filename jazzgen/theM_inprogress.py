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
    prog_dic = {1: ["I", "IV", "V"],
                2: ["ii", "V", "I"],
                3: ["I", "IV", "V", "vi", "IV", "V"],
                4: ["I", "V", "ii", "IV"],
                5: ["i", "bVII", "v", "bVI"],
                6: ["i", "bIII", "bVII", "IV"],
                7: ["I", "V", "vi", "IV"],
                8: ["I", "IV", "vi", "V"],
                9: ["vi", "IV", "I", "V"],
                10: ["i", "bVII", "bVI", "V"],
                11: ["i", "bVII", "bVI", "bVII"],
                12: ["I", "vi", "IV", "V"],
                13: ["I", "bVII", "IV", "I"],
                14: ["IV", "V", "iii", "vi"]

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

    def add_chord_quality_orderd_scale(self, chord_scale_intervall, stufe, quality):
        new_chord_scale = chord_scale_intervall
        quality-=1
        i = (stufe + quality)%7 -1
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
    def add_chord_quality(self, chord_scale_intervall, index, quality):
        return chord_scale_intervall[index][1].append(quality)

    def add_2nd_d(self, chord_scale_intervall, index):
        chord_scale_intervall.insert(index, [self.intervall_gen(chord_scale_intervall[index][0], "5"), ["3", "5", "b7"]])
        return chord_scale_intervall
    def add_251(self, chord_scale_intervall, index):
        if index < 0:
            index = len(chord_scale_intervall) + index
        chord_scale_intervall.insert(index, [self.intervall_gen(chord_scale_intervall[index][0], "5"), ["3", "5", "b7"]])
        if "3" in chord_scale_intervall[index+1][1]:
            quality = ["b3", "5", "b7"]
        if "b3" in chord_scale_intervall[index+1][1]:
            quality = ["b3", "b5", "b7"]
        chord_scale_intervall.insert(index, [self.intervall_gen(chord_scale_intervall[index+1][0], "2"), quality])
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
        for i, chord in enumerate(chord_scale_intervall):
            add = ""
            if "7" in chord[1]:
                add = "M7"
            if "b7" in chord[1]:
                add = "7"
            if "3" in chord[1]:
                if i <= len(chord_scale_intervall) - 2:
                    if self.intervall_ident(chord_scale_intervall[i + 1][0], chord[0]) == "5" and not self.stufen_ident([chord_scale_intervall[i+1]], root)[0] in ["i", "I"] and not (chord[0] == root and not "b7" in chord[1]):
                        second_root = self.stufen_ident([chord_scale_intervall[i+1]], root)[0]
                        for q in ["b5", "6", "b6", "M7", "7", "b9", "9", "/"]:
                            if "b" + q in second_root:
                                second_root = second_root.split("b" + q)
                                second_root = "".join(second_root)
                            elif q in second_root:
                                second_root = second_root.split(q)
                                second_root = "".join(second_root)
                        result.append("V"+add+"/"+second_root)

                    else:
                        result.append(maj_dic[self.intervall_ident(root, chord[0])]+add)
                else:
                    result.append(maj_dic[self.intervall_ident(root, chord[0])]+add)
            if "b3" in chord[1]:
                if i <= len(chord_scale_intervall) - 3:
                    if self.intervall_ident(chord_scale_intervall[i + 2][0], chord[0]) == "2" and self.intervall_ident(chord_scale_intervall[i + 2][0], chord_scale_intervall[i + 1][0]) == "5" and "3" in chord_scale_intervall[i + 1][1] and not self.stufen_ident([chord_scale_intervall[i + 2]], root)[0] in ["i", "I"]:
                        second_root = self.stufen_ident([chord_scale_intervall[i + 2]], root)[0]
                        for q in ["b5", "6", "b6", "M7", "7", "b9", "9", "/"]:
                            if "b" + q in second_root:
                                second_root = second_root.split("b" + q)
                                second_root = "".join(second_root)
                            elif q in second_root:
                                second_root = second_root.split(q)
                                second_root = "".join(second_root)
                        result.append("ii"+add+"/" + second_root)
                    else:
                        result.append(min_dic[self.intervall_ident(root, chord[0])]+add)
                else:
                    result.append(min_dic[self.intervall_ident(root, chord[0])]+add)
        return result
    
    def stufen_gen(self, root, stufe):
        result = []
        rom_num_dic = {"i":"1", "I":"1", "bii":"b2", "bII":"b2", "ii":"2", "II":"2", "biii":"b3", "bIII":"b3", "iii":"3", "III":"3", "biv":"b4", "bIV":"bIV", "iv":"4", "IV":"4", "#iv":"#4", "#IV":"#4", "bv":"b5", "bV":"b5", "v":"5", "V":"5", "bvi":"b6", "bVI":"b6", "vi":"6", "VI":"6", "bvii":"b7", "bVII":"b7", "vii":"7", "VII":"7"}
        min_dic = {'i': '1', 'bii': 'b2', 'ii': '2', 'biii': 'b3', 'iii': '3', 'iv': '4', '#iv': '#4', 'bv': 'b5', 'v': '5', 'bvi': 'b6', 'vi': '6', 'bvii': 'b7', 'vii': '7'}
        maj_dic = {'I': '1', 'bII': 'b2', 'II': '2', 'bIII': 'b3', 'III': '3', 'IV': '4', '#IV': '#4', 'bV': 'b5', 'V': '5', 'bVI': 'b6', 'VI': '6', 'bVII': 'b7', 'VII': '7'}
        add = []
        if "/" in stufe:
            stufe = stufe.split("/")
            second_root = stufe[1]
            second_chord = stufe[0]
            stufe = self.stufen_ident([self.stufen_gen(self.intervall_gen(root, rom_num_dic[second_root]), second_chord)], root)[0]
            #print(stufe)
        for i in ["b5", "6", "b6", "M7", "7", "b9", "9"]:

            if "b" + i in stufe:
                stufe = stufe.split("b" + i)
                stufe = "".join(stufe)
                add.append(i)

            elif i in stufe:
                stufe = stufe.split(i)
                stufe = "".join(stufe)
                if i == "7":
                    i = "b7"
                if i == "M7":
                    i = "7"


                #if i == "9":
                #    add.append("b7")
                #if i == "b9":
                #    add.append("b7")
                add.append(i)

        try:
            interv = min_dic[stufe]
            quality = ["b3", "5"]
            if "b5" in add:
                quality = ["b3"]
            quality.extend(add)
            return [self.intervall_gen(root, interv), quality]
        except:
            interv = maj_dic[stufe]
            quality = ["3", "5"]
            if "b5" in add:
                quality = ["3"]
            quality.extend(add)
            return [self.intervall_gen(root, interv), quality]

    def rand_prog(self, root, length):
        choice = ["i", "I", "bii", "bII", "ii", "II", "biii", "bIII", "iii", "III", "iv", "IV", "bv", "bV", "v", "V", "bvi", "bVI", "vi", "VI", "bvii", "bVII", "vii", "VII"]
        result = []
        for _ in range(length):
            result.append(self.stufen_gen(root, random.choice(choice)))
        return result

    def rand_prog_programms(self, programm):
        root = random.choice(["A", "B", "C", "D", "E", "F", "G"]) + random.choice(["", "", "", "", "b", "#"])
        if programm == 1:
            rand = self.rand_prog(root, 5)
            rand.insert(0, self.stufen_gen(root, random.choice(["i", "I"])))
            rand.append(self.stufen_gen(root, random.choice(["i", "I"])))
            self.add_251(rand, 0)
            self.add_251(rand, -3)
            self.add_2nd_d(rand, 5)
            self.add_251(rand, -1)
            self.add_chord_quality(rand, random.choice(range(len(rand))), "7")
            stufen = self.stufen_ident(rand, root)
            chords = self.chord_scale(rand)
        if programm == 2:
            rand_programm = random.randint(1,14)
            rand = self.common_chord_prog(root, rand_programm)
            add = []
            if "I" in self.prog_dic[rand_programm]:
                add = [root, ["3", "5"]]
            if "i" in self.prog_dic[rand_programm]:
                add = [root, ["b3", "5"]]
            rand.extend(rand)
            rand.append(add)
            stufen = self.stufen_ident(rand, root)
            chords = self.chord_scale(rand)
        column_width = max(max(len(str(item)) for item in stufen), max(len(str(item)) for item in chords))
        print(" ".join(f"{str(item):<{column_width}}" for item in stufen))
        print(" ".join(f"{str(item):<{column_width}}" for item in chords))
        return None
    def common_chord_prog(self, root, program):

        result = []
        for stufe in self.prog_dic[program]:
            result.append(self.stufen_gen(root, stufe))
        return result
    def tension_brightness_ident(self, stufen_progression):
        tension = []
        brightness = []
        #hohe tension entsteht
        # an bestimmten stufen wie, b2, 5, 7, 2, 4, 3, 6
        # und durch bestimmte qualities im chord ( intervalle im chord zur root oder chord_root)
        # brightness entsteht
        # durch chord qualitäten wie 3, b3, 7, b7. je nach dem ob 3 oder b3 mit 9 kombiniert ist
        # die root note des chords hat die gröste gewichtung, die 5 die zweitgröste und die 3 die dritt.
        # die intervalle zueinander werden in tension_scores umgewandelt und pto 1, 3, 5 gemittelt und jeweilig mit einer gewichtung multipliziert#
        # diese gewichteten mittel werden ebenfalls gemittelt
        tension_dic = {"1":10, "5":9, "4":8, "3":7, "b3":6, "b5":3, "2":4, "b2":1, "b7":8

        }
        chord_scale_intervall = [self.stufen_gen("C", i) for i in stufen_progression]
        for i in range(len(chord_scale_intervall)):
            chord_scale_intervall[i][1].insert(0, "1")
        root_intervalls = [["C", "E", "G", "Bb"], ["1", "3", "5", "b7"]]
        for root, inter in zip(["C", "E", "G", "Bb"], ["1", "3", "5", "b7"]):
            result = []
            #root = "C"

            for chord, intervall in zip(chord_scale_intervall, stufen_progression):
                add = []
                add2 = []
                for i in chord[1]:
                    add.append(self.intervall_gen(chord[0], i))
                for note in add:
                    add2.append(self.intervall_ident(root, note))
                result.append([intervall, add2])
            print(inter, result)
        return None

    def intervall_tension(self):
        # chord folgen triggern skalen, welche eine bestimmte stimmung erzeugen.
        # grund erzeugter stimmung: spannungsverhältnis der noten/intervalle zur root_reverenz und untereinander (secondary_reverenz) + kulturell erworbene erwartung
        #zB Edur_root (EG#B) und Cdur(CEG) ermöglicht:
        # - ambivalente noten wie F und F#, D und D# da in beiden major skalen vorhanden
        # - eindeutige noten wie C (von E = b6)
        # - überschneidende G und G#
        # so kann man spielen: 1,b2,3,4,5,b6,b7 = PhrD oder 1,2,b3,4,5,b6,b7 = Phr oder 1,2, 3, 4,5,b6,7 = Harm-Maj
        return None

    def functional_new(self, root, p):
        functions_dic_maj = {"T": ["I", "iii", "vi"], "SD": ["IV", "ii"], "D": ["V", "viib5"]}
        functions_dic_min = {"T": ["i", "bIII"], "SD": ["iv", "bVI", "iib5"], "D": ["V", "v", "bVII","bviib5"]}
        pattern = {1: ["T", "SD", "D", "T"], 2: ["T", "SD", "D", "T", "SD", "D", "T"]}
        functions_dic = random.choice([functions_dic_maj, functions_dic_min])
        result = []
        for ind, i in enumerate(pattern[p]):
            choice = random.choice(functions_dic[i])
            if ind == 0 or ind == len(pattern[p])-1:
                choice = functions_dic[i][0]
            result.append(choice)
        print(result)
        return [self.stufen_gen(root, i) for i in result]








x = theM()
#print(x.scale("C", "maj"))
#print(x.intervall_gen("C#", "b5"))
#print(x.intervall_ident("B", "G"))
#print(x.scale_root_patter("C"))
chord_scale_intervall = x.chord_scale_intervall("Cb", "maj")
#print(chord_scale_intervall)
#print(x.chord_scale_notes("E", "maj"))
"""
#print(x.scale_mode("C", "lok"))
x.add_chord_quality_orderd_scale(chord_scale_intervall, 7, 7)
x.add_chord_quality_orderd_scale(chord_scale_intervall, 1, 7)
x.add_chord_quality_orderd_scale(chord_scale_intervall, 2, 9)

chord_scale = x.chord_scale(chord_scale_intervall)
print(chord_scale)
test = x.add_2nd_d(chord_scale_intervall, 1)
print(test)
print(x.add_2nd_d(test, 1))
print(x.chord_scale(test))
#print(x.find_index(test, "F"))
f = x.functional("Cb", 2)

f = x.add_2nd_d(f, -1)
x.tritone_sub(f, -2)
x.add_251(f, -3)
x.add_2nd_d(f, 1)
x.add_251(f, 1)
print(x.stufen_ident(f, f[0][0]))

print(x.chord_scale(f))
xyz = x.stufen_gen("C", "bIII9")
print(xyz)
print(x.chord_scale([x.stufen_gen("C", "bIII9")]))
root = "G"
rand = x.rand_prog(root, 5)
print(rand)
rand.insert(0, x.stufen_gen(root, random.choice(["i", "I"])))
rand.append(x.stufen_gen(root, random.choice(["i", "I"])))
x.add_251(rand, -3)
x.add_2nd_d(rand, 2)
x.add_251(rand, -1)
#rand = [['F', ['3', '5']], ['D', ['b3', '5']], ['F', ['b3', '5']], ['B', ['b3', '5']], ['F', ['3', '5']], ['E', ['b3', '5']], ['A', ['b3', '5']], ['D', ['3', '5']]]
print(x.stufen_ident(rand, root))
#x.add_chord_quality(rand, 0, "7")
print(x.chord_scale(rand))
"""
#print(x.rand_prog_programms(1))
#print(x.chord_scale(x.common_chord_prog("E", 14)))
"""
rand = [["F", ["3", "5"]], ["C", ["3", "5"]], ["F", ["3", "5", "b7"]], ["Bb", ["3", "5"]]]
root = "F"
stufen = x.stufen_ident(rand, root)
chords = x.chord_scale(rand)
column_width = max(max(len(str(item)) for item in stufen), max(len(str(item)) for item in chords))
print(" ".join(f"{str(item):<{column_width}}" for item in stufen))
print(" ".join(f"{str(item):<{column_width}}" for item in chords))
"""
c = []
arab = ["I", "iv", "bVII", "bVI"]
phr = ["i", "iv", "bIII", "bvii", "bIIb5"]
for i in phr:
    c.append(x.stufen_gen("A", i))
print(c)
print(x.stufen_ident(c, "A"))
#print(x.chord_scale(c))
#f = [x.stufen_gen("C", i) for i in ["ii7", "V7", "I", "V7/VII", "VII"]]
print(x.stufen_ident([x.stufen_gen("C", i) for i in ["ii7", "V7", "I", "V7/VII", "VII7"]], "C"))
test2 = ["I7","ii", "iii", "IV", "V7", "vi", "viib5"]
test3 = ["I7"]
print(x.tension_brightness_ident(test3))
print(x.chord_scale(x.functional_new("C", 2)))
