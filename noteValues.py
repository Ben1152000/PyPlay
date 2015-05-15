
# Finds the frequency of each note in hertz

notes = ['b#', 'c#', 'd', 'd#', 'e', 'e#', 'f#', 'g', 'g#', 'a', 'a#', 'b']
octaves = [2, 3, 4, 5, 6, 7]
startValue = 65.406 # c2 freq.
halfStepsAboveStartNote = 0
noteValues = {}

for octaveName in octaves:
    for noteName in notes:
        noteValues[(noteName, octaveName)] = (startValue * (1.059463094) ** halfStepsAboveStartNote)
        halfStepsAboveStartNote += 1

notes = ['c', 'db', 'd', 'eb', 'fb', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'cb']
octaves = [2, 3, 4, 5, 6, 7]
startValue = 65.406 # c2 freq.
halfStepsAboveStartNote = 0

for octaveName in octaves:
    for noteName in notes:
        noteValues[(noteName, octaveName)] = (startValue * (1.059463094) ** halfStepsAboveStartNote)
        halfStepsAboveStartNote += 1

noteValues['*', 0] = 0