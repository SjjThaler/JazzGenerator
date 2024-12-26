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
    # r_p_scale = root, pattern scale
    def scale(self, root, skala):
        r_p_scale = []
        add = 0
        if "#" in root:
            add = -root.count("#")
            root = root[0]
        if "b" in root:
            add = root.count("b")
            root = root[0]
        root_index = self.notes.index(root)
        scale_to_root = self.notes_pattern[root_index::]+self.notes_pattern[:root_index]
        tone_subtraction = scale_to_root[0][1]
        for note, v in scale_to_root:
            v -= tone_subtraction
            if v < 0:
                v+=12
            r_p_scale.append([note, v+add])
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

    def intervall(self, tone, n):
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
        intervall = []
        if n > 11:
            n-= 12
        for note, s_pattern in zip(tones_pattern, self.scales["maj"]):
            if note[1] - s == n:
                intervall.append(note[0])
            if note[1] - s == n-1:
                intervall.append(note[0] + "#")
            #if note[1] - s == n-2:
            #    intervall.append(note[0] + "##")
            if note[1] - s == n+1:
                intervall.append(note[0] + "b")
            #if note[1] - s == n+2:
            #    intervall.append(note[0] + "bb")

        sort_intervall = [i for i in intervall if len(i) == 1]
        for i, c in zip(["#", "b"], intervall):
            if i in c:
                sort_intervall.append(c)

        if len(tone) == 1 or "#" in tone:
            return sort_intervall[0]
        elif "b" in tone:
            return sort_intervall[-1]


x = theM()
print(x.scale("D", "harm"))
print(x.intervall("B", 6))





