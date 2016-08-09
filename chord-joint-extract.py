__author__ = 'aryo.seto'
import csv

file = open("CHORD_JOINT_JKT.LIS", 'r')
firsttime = True

v_joint = 0
v_chord = 0
v_align = 0
v_temp = 0

result = []

def append_data(result, v_joint, v_chord, v_align):
    if v_joint != 0 and v_chord != 0 and v_align != 0:
        result.append([v_joint, v_chord, v_align])

for line in file:
    if 'Joint ..:' in line:
        if firsttime:
            firsttime = False
        else:
            append_data(result, v_joint, v_chord, v_align)
            v_joint = int(line[line.find(':') + 1:])
            v_chord = 0
            v_align = 0
    elif 'Member ..:' in line:
        v_temp = int(line[line.find(':')+1:])
    elif 'CHORD' in line:
        v_chord = v_temp
        v_temp = 0
    elif 'ALIGN' in line:
        v_align = v_temp
        v_temp = 0

file.close()

# Print list joint into files
with open ("ChordNodes.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(result)
