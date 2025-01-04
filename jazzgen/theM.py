import random

import random

class theM:
    """
    Class to manage musical scales, intervals, and chords.
    """

    notes_pattern = [["A", 0], ["B", 2], ["C", 3], ["D", 5], ["E", 7], ["F", 8], ["G", 10]]
    notes = ["A", "B", "C", "D", "E", "F", "G"]

    scales = {
        "maj": [0, 2, 4, 5, 7, 9, 11],
        "min": [0, 2, 3, 5, 7, 8, 10],
        "harm": [0, 2, 3, 5, 7, 8, 11]
    }

    def scale_root_patter(self, root):
        """
        Generates the pattern of notes and their semitone values based on a given root note.

        Args:
            root (str): The root note (e.g., "C", "C#", "Db").

        Returns:
            list: A list of [note, semitone] pairs representing the scale pattern from the root.
        """
        r_p_scale = []
        add = 0
        if "#" in root:
            add = -root.count("#")
            root = root[0]
        if "b" in root:
            add = root.count("b")
            root = root[0]
        root_index = self.notes.index(root)
        scale_to_root = self.notes_pattern[root_index:] + self.notes_pattern[:root_index]
        tone_subtraction = scale_to_root[0][1]
        for note, v in scale_to_root:
            v -= tone_subtraction
            if v < 0:
                v += 12
            r_p_scale.append([note, v + add])
        return r_p_scale

    def scale(self, root, skala):
        """
        Applies a scale pattern to a root note to generate the scale.

        Args:
            root (str): The root note (e.g., "C").
            skala (str): The scale type (e.g., "maj", "min", "harm").

        Returns:
            list: A list of notes with adjusted pitch based on the scale type.
        """
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
        """
        Generates a scale in a specific mode starting from the given root note.

        Args:
            root (str): The root note of the scale.
            mode (str): The mode of the scale ("ion", "dor", "phr", "lyd", "myx", "aeo", "lok").

        Returns:
            list: The scale notes adjusted for the specified mode.
        """
        mode_roots = {
            "ion": "C", "dor": "D", "phr": "E",
            "lyd": "F", "myx": "G", "aeo": "A", "lok": "B"
        }
        m = mode_roots.get(mode, "C")
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
        """
        Generates a note interval based on the input tone and interval descriptor.

        Args:
            tone (str): The base tone (e.g., "C").
            interv (str): The interval (e.g., "b3", "5").

        Returns:
            str: The note at the specified interval.
        """
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
        scale_to_tone = self.notes_pattern[tone_index:] + self.notes_pattern[:tone_index]
        tones_pattern = []
        tone_subtraction = scale_to_tone[0][1]
        for note, v in scale_to_tone:
            v -= tone_subtraction
            if v < 0:
                v += 12
            tones_pattern.append([note, v+add])
        s = tones_pattern[0][1] - add

        if n > 11:
            n -= 12

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
        """
        Identifies the interval between a root note and another tone.

        Args:
            root (str): The root note.
            tone (str): The target tone.

        Returns:
            str: The interval (e.g., "b3", "5").
        """
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
        delta = self.scale_root_patter("C")[stufe-1][1] - seminotes

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
        """
        Generates a list of chord intervals based on the root note and scale.

        Args:
            root (str): The root note.
            skala (str): The scale type (e.g., "maj").

        Returns:
            list: A list of [note, interval] pairs for each chord in the scale.
        """
        scale_with_root_pattern = self.scale(root, skala)
        chord_scale = []

        for i, note in enumerate(scale_with_root_pattern):
            intervall = []
            for _ in range(2):
                i += 2
                if i == 7:
                    i = 0
                if i > 6:
                    i = -6
                intervall.append(self.intervall_ident(note[0], scale_with_root_pattern[i][0]))
            chord_scale.append([note[0], intervall])

        return chord_scale

    def chord_scale_notes(self, root, skala):
        """
        Generates the notes of the chords in a scale.

        Args:
            root (str): The root note.
            skala (str): The scale type (e.g., "maj").

        Returns:
            list: A list of chords with their constituent notes.
        """
        chord_scale = self.chord_scale_intervall(root, skala)
        chord_scale_notes = []
        for r_note, chord_pattern in chord_scale:
            add = [r_note]
            for i in chord_pattern:
                add.append(self.intervall_gen(r_note, i))
            chord_scale_notes.append(add)
        return chord_scale_notes

    def chord_scale(self, chord_scale_intervall):
        """
        Determines the quality of chords in a scale.

        Args:
            chord_scale_intervall (list): A list of [note, interval] pairs.

        Returns:
            list: A list of chord names with qualities (e.g., "Cmaj7", "Am").
        """
        chord_scale = []
        for r_note, interv in chord_scale_intervall:
            add = r_note
            if "b3" in interv and "5" in interv:
                add += "m"
            if "b5" in interv and "b3" in interv:
                add += "dim"
            if "b7" in interv:
                add += "7"
            if "7" in interv:
                add += "M7"
            if "b5" in interv and not "b3" in interv:
                add += "b5"
            if "#5" in interv:
                add += "#5"
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

    def add_chord_quality_diatonic(self, chord_scale_intervall, stufe, quality):
        """
        funktioniert nur wenn die chord_scale_intervall liste nach einer skala geordnet ist
        Adds an interval to a chord in the scale.

        Args:
            chord_scale_intervall (list): The chord scale intervals.
            stufe (int): The chord degree to modify (1-based index).
            quality (int): The interval to add.

        Returns:
            list: Updated chord scale intervals with the added interval.
        """
        new_chord_scale = chord_scale_intervall
        quality -= 1
        i = (stufe + quality) % 7 - 1
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
        if quality + 1 > 7:
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
        """
        Adds a 2nd dominant chord at the specified index.

        Args:
            chord_scale_intervall (list): The chord scale intervals.
            index (int): The index to insert the new chord.

        Returns:
            list: Updated chord scale intervals with the new chord.
        """
        chord_scale_intervall.insert(index, [self.intervall_gen(chord_scale_intervall[index][0], "5"), ["3", "5", "b7"]])
        return chord_scale_intervall

    def add_251(self, chord_scale_intervall, index):
        """
        Adds a ii-V-I progression at the specified index.

        Args:
            chord_scale_intervall (list): The chord scale intervals.
            index (int): The index to insert the progression.

        Returns:
            list: Updated chord scale intervals with the progression.
        """
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
        """
        Finds the index of a chord in the scale.

        Args:
            chord_scale_intervall (list): The chord scale intervals.
            note (str): The note to find.

        Returns:
            int: The index of the note in the scale.
        """
        return [i[0] for i in chord_scale_intervall].index(note)

    def functional(self, root, p):
        """
        Generates a functional chord progression based on the root.

        Args:
            root (str): The root note.
            p (int): The pattern index (1 or 2).

        Returns:
            list: A list of chords in the progression.
        """
        functions_dic = {"T": ["1", "6", "3"], "SD": ["4", "2", "b2"], "D": ["b2", "5", "7"]}
        pattern = {1: ["T", "SD", "D", "T"], 2: ["T", "SD", "D", "SD", "T"]}
        chord_scale_intervall = self.chord_scale_intervall(root, "maj")
        result = []
        for i in pattern[p]:
            choice = random.choice(functions_dic[i])
            chord_position = int(choice[-1]) - 1
            chord = chord_scale_intervall[chord_position]
            if choice == "b2":
                chord = [self.intervall_gen(root, "b2"), ["3", "5", "b7"]]
            result.append(chord)

        return result

    def tritone_sub(self, chord_scale_intervall, index):
        """
        Performs a tritone substitution at the specified index.

        Args:
            chord_scale_intervall (list): The chord scale intervals.
            index (int): The index to substitute.

        Returns:
            list: Updated chord scale intervals with the substitution.
        """
        chord_scale_intervall[index] = [self.intervall_gen(chord_scale_intervall[index][0], "b5"), chord_scale_intervall[index][1]]
        return chord_scale_intervall

    def stufen_ident(self, chord_scale_intervall, root):
        """
        Identifies the functional stufen (degrees) of chords.

        Args:
            chord_scale_intervall (list): The chord scale intervals.
            root (str): The root note.

        Returns:
            list: A list of stufen (e.g., "I", "ii").
        """
        result = []
        min_dic = {"1": "i", "b2": "bii", "2": "ii", "b3": "biii", "3": "iii", "b4": "iii", "4": "iv", "#4": "#iv", "b5": "bv", "5": "v", "b6": "bvi", "6": "vi", "bb7": "vi", "b7": "bvii", "7": "vii", "b1": "vii"}
        maj_dic = {"1": "I", "b2": "bII", "2": "II", "b3": "bIII", "3": "III", "b4": "III", "4": "IV", "#4": "#IV", "b5": "bV", "5": "V", "b6": "bVI", "6": "VI", "bb7": "VI", "b7": "bVII", "7": "VII", "b1": "VII"}
        for i, chord in enumerate(chord_scale_intervall):

            if "3" in chord[1]:
                if i <= len(chord_scale_intervall) - 2:
                    if self.intervall_ident(chord_scale_intervall[i + 1][0], chord[0]) == "5" and not self.stufen_ident([chord_scale_intervall[i+1]], root)[0] in ["i", "I"]:
                        result.append("V/"+self.stufen_ident([chord_scale_intervall[i+1]], root)[0])

                    else:
                        result.append(maj_dic[self.intervall_ident(root, chord[0])])
                else:
                    result.append(maj_dic[self.intervall_ident(root, chord[0])])
            if "b3" in chord[1]:
                if i <= len(chord_scale_intervall) - 3:
                    if self.intervall_ident(chord_scale_intervall[i + 2][0], chord[0]) == "2" and self.intervall_ident(chord_scale_intervall[i + 2][0], chord_scale_intervall[i + 1][0]) == "5" and "3" in chord_scale_intervall[i + 1][1] and not self.stufen_ident([chord_scale_intervall[i + 2]], root)[0] in ["i", "I"]:
                        result.append("ii/" + self.stufen_ident([chord_scale_intervall[i + 2]], root)[0])
                    else:
                        result.append(min_dic[self.intervall_ident(root, chord[0])])
                else:
                    result.append(min_dic[self.intervall_ident(root, chord[0])])
        return result

    def stufen_gen(self, root, stufe):
        """
        Generates a chord based on its functional stufe.

        Args:
            root (str): The root note.
            stufe (str): The functional stufe (e.g., "I", "ii").

        Returns:
            list: A chord with its intervals.
        """
        min_dic = {'i': '1', 'bii': 'b2', 'ii': '2', 'biii': 'b3', 'iii': '3', 'iv': '4', '#iv': '#4', 'bv': 'b5', 'v': '5', 'bvi': 'b6', 'vi': '6', 'bvii': 'b7', 'vii': '7'}
        maj_dic = {'I': '1', 'bII': 'b2', 'II': '2', 'bIII': 'b3', 'III': '3', 'IV': '4', '#IV': '#4', 'bV': 'b5', 'V': '5', 'bVI': 'b6', 'VI': '6', 'bVII': 'b7', 'VII': '7'}

        add = []
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
            quality.extend(add)
            return [self.intervall_gen(root, interv), quality]
        except:
            interv = maj_dic[stufe]
            quality = ["3", "5"]
            quality.extend(add)
            return [self.intervall_gen(root, interv), quality]

    def rand_prog(self, root, length):
        """
        Generates a random chord progression of a given length.

        Args:
            root (str): The root note.
            length (int): The number of chords in the progression.

        Returns:
            list: A random progression of chords.
        """
        choice = ["i", "I", "bii", "bII", "ii", "II", "biii", "bIII", "iii", "III", "iv", "IV", "bv", "bV", "v", "V", "bvi", "bVI", "vi", "VI", "bvii", "bVII", "vii", "VII"]
        result = []
        for _ in range(length):
            result.append(self.stufen_gen(root, random.choice(choice)))
        return result

    def rand_prog_programms(self):
        root = random.choice(["A", "B", "C", "D", "E", "F", "G"]) + random.choice(["", "", "", "", "b", "#"])

        rand = self.rand_prog(root, 5)
        rand.insert(0, self.stufen_gen(root, random.choice(["i", "I"])))
        rand.append(self.stufen_gen(root, random.choice(["i", "I"])))
        self.add_251(rand, -3)
        self.add_2nd_d(rand, 2)
        self.add_251(rand, -1)
        self.add_chord_quality(rand, random.choice(range(len(rand))), "9")
        stufen = self.stufen_ident(rand, root)
        chords = self.chord_scale(rand)
        return stufen, chords








# x = theM()
# #print(x.scale("C", "maj"))
# #print(x.intervall_gen("C#", "b5"))
# #print(x.intervall_ident("B", "G"))
# #print(x.scale_root_patter("C"))
# chord_scale_intervall = x.chord_scale_intervall("Cb", "maj")
# #print(chord_scale_intervall)
# #print(x.chord_scale_notes("E", "maj"))

# #print(x.scale_mode("C", "lok"))
# x.add_chord_quality(chord_scale_intervall, 7, 7)
# x.add_chord_quality(chord_scale_intervall, 1, 7)
# x.add_chord_quality(chord_scale_intervall, 2, 9)

# chord_scale = x.chord_scale(chord_scale_intervall)
# print(chord_scale)
# test = x.add_2nd_d(chord_scale_intervall, 1)
# print(test)
# print(x.add_2nd_d(test, 1))
# print(x.chord_scale(test))
# #print(x.find_index(test, "F"))
# f = x.functional("Cb", 2)

# f = x.add_2nd_d(f, -1)
# x.tritone_sub(f, -2)
# x.add_2nd_d(f, -3)
# x.add_2nd_d(f, 1)
# x.add_251(f, 1)
# print(x.stufen_ident(f, f[0][0]))

# print(x.chord_scale(f))
# print(x.chord_scale([x.stufen_gen("C", "iv")]))
# root = "G"
# rand = x.rand_prog(root, 5)
# rand.insert(0, x.stufen_gen(root, random.choice(["i", "I"])))
# rand.append(x.stufen_gen(root, random.choice(["i", "I"])))
# x.add_251(rand, -1)
# x.add_2nd_d(rand, -3)
# print(x.stufen_ident(rand, root))
# print(x.chord_scale(rand))
