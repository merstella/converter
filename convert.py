import numpy as np

def remove_whitespace_from_prefix_suffix(input_string):
    result = input_string.strip()
    return result
def find_last_occurrence(input_string, element):
    index = input_string.rfind(element)
    return index

fin = open("input.txt", "r", encoding="utf-8")
fout = open("output.txt", "w", encoding="utf-8")

num_of_cls = 3
num_of_sub = 6
num_of_ch = 5
num_of_dif = 4
num_of_q = 30

classes = np.zeros((num_of_cls), dtype=object)
subjects = np.zeros((num_of_cls, num_of_sub), dtype=object)
chapters = np.zeros((num_of_cls, num_of_sub, num_of_ch), dtype=object)
difficulties = np.zeros((num_of_cls, num_of_sub, num_of_ch, num_of_dif), dtype=object)
questions = np.zeros((num_of_cls, num_of_sub, num_of_ch, num_of_dif, num_of_q), dtype=object)
answers = np.zeros((num_of_cls, num_of_sub, num_of_ch, num_of_dif, num_of_q, 4), dtype=object)
no_cls, no_sub, no_ch, no_dif, no_q = -1, -1, -1, -1, -1

for line in fin:
    line = remove_whitespace_from_prefix_suffix(line)
    sz = len(line)
    if line[0].isdigit():
        cntdot = line.count('.')
        if cntdot == 1:
            no_cls += 1
            no_sub, no_ch, no_dif, no_q = -1, -1, -1, -1
            name_cls = line[line.index('.') + 2:sz]
            classes[no_cls] = name_cls
        elif cntdot == 2:
            no_sub += 1
            no_ch, no_dif, no_q = -1, -1, -1
            name_sub = line[find_last_occurrence(line, '.') + 2:sz]
            subjects[no_cls][no_sub] = name_sub
        elif cntdot == 3:
            no_ch += 1
            no_dif, no_q = -1, -1
            name_ch = line[find_last_occurrence(line, '.') + 2:sz]
            chapters[no_cls][no_sub][no_ch] = name_ch
        else:
            no_dif += 1
            no_q = -1
            name_dif = line[find_last_occurrence(line, '.') + 2:sz]
            difficulties[no_cls][no_sub][no_ch][no_dif] = name_dif
    elif line[0].isalpha() and line[1].isalpha():
        no_q += 1
        pos = line.find(':')
        poss = line.find('.')
        if pos != -1 and poss != -1:
            if (poss < pos): 
                if (line[line.index('.') + 1] == ' '):
                    name_quest = line[line.index('.') + 2:sz]
                else:
                    name_quest = line[line.index('.') + 1:sz]
            else:
                if (line[line.index(':') + 1] == ' '):
                    name_quest = line[line.index(':') + 2:sz]
                else:
                    name_quest = line[line.index(':') + 1:sz]
        else:
            if pos != -1 and pos != (sz - 1):
                if (line[line.index(':') + 1] == ' '):
                    name_quest = line[line.index(':') + 2:sz]
                else:
                    name_quest = line[line.index(':') + 1:sz]
            else:
                if (line[line.index('.') + 1] == ' '):
                    name_quest = line[line.index('.') + 2:sz]
                else:
                    name_quest = line[line.index('.') + 1:sz]
        questions[no_cls][no_sub][no_ch][no_dif][no_q] = name_quest
    else:
        if line.find('@') != -1:
            ans = line[line.index('.') + 2:sz - 1];
        else:
            ans = line[line.index('.') + 2:sz];
        if line[0] == 'A' or line[0] == 'a':
            answers[no_cls][no_sub][no_ch][no_dif][no_q][0] = ans
        elif line[0] == 'B' or line[0] == 'b':
            answers[no_cls][no_sub][no_ch][no_dif][no_q][1] = ans
            if line.find('@') != -1:
                answers[no_cls][no_sub][no_ch][no_dif][no_q][0], answers[no_cls][no_sub][no_ch][no_dif][no_q][1] = answers[no_cls][no_sub][no_ch][no_dif][no_q][1], answers[no_cls][no_sub][no_ch][no_dif][no_q][0]
        elif line[0] == 'C' or line[0] == 'c':
            answers[no_cls][no_sub][no_ch][no_dif][no_q][2] = ans
            if line.find('@') != -1:
                answers[no_cls][no_sub][no_ch][no_dif][no_q][0], answers[no_cls][no_sub][no_ch][no_dif][no_q][2] = answers[no_cls][no_sub][no_ch][no_dif][no_q][2], answers[no_cls][no_sub][no_ch][no_dif][no_q][0]
        else:
            answers[no_cls][no_sub][no_ch][no_dif][no_q][3] = ans
            if line.find('@') != -1:
                answers[no_cls][no_sub][no_ch][no_dif][no_q][0], answers[no_cls][no_sub][no_ch][no_dif][no_q][3] = answers[no_cls][no_sub][no_ch][no_dif][no_q][3], answers[no_cls][no_sub][no_ch][no_dif][no_q][0]

for i in range(len(classes)):
    x = str(classes[i])
    if (x == '0'):
        continue
    fout.write("classes["+str(i)+"] = \""+x+"\";")
    fout.write("\n")
fout.write("\n")
for i in range(len(subjects)):
    for j in range(4):
        x = str(subjects[i][j])
        if (x == '0'):
            continue
        fout.write("subjects["+str(i)+"]["+str(j)+"] = \""+x+"\";")
        fout.write("\n")
fout.write("\n")
for i in range(len(chapters)):
    for j in range(4):
        for k in range(4):
            x = str(chapters[i][j][k])
            if (x == '0'):
                continue
            fout.write("chapters["+str(i)+"]["+str(j)+"]["+str(k)+"] = \""+x+"\";")
            fout.write("\n")
# fout.write("\n")
# for i in range(len(difficulties)):
#     for j in range(len(difficulties[i])):
#         for k in range(len(difficulties[i][j])):
#             for l in range(len(difficulties[i][j][k])):
#                 x = str(difficulties[i][j][k][l])
#                 if (x == '0'):
#                     continue
#                 fout.write("difficulties["+str(i)+"]["+str(j)+"]["+str(k)+"]["+str(l)+"] = \""+x+"\";")
#                 fout.write("\n")
fout.write("\n")
cnt = 0
for i in range(len(questions)):
    for j in range(4):
        for k in range(4):
            cnt = 0
            for l in range(len(questions[i][j][k])):
                for m in range(len(questions[i][j][k][l])):
                    x = str(questions[i][j][k][l][m])
                    if (x == '0'):
                        continue
                    fout.write("questions["+str(i)+"]["+str(j)+"]["+str(k)+"]["+str(cnt)+"] = \""+x+"\";")
                    cnt += 1
                    fout.write("\n")
fout.write("\n")
cnt = 0
for i in range(len(answers)):
    for j in range(4):
        for k in range(4):
            cnt = 0
            for l in range(len(answers[i][j][k])):
                for m in range(len(answers[i][j][k][l])):
                    if str(questions[i][j][k][l][m]) == "0":
                        continue
                    for n in range(4):
                        x = str(answers[i][j][k][l][m][n])
                        if x == "0":
                            continue
                        fout.write("answers["+str(i)+"]["+str(j)+"]["+str(k)+"]["+str(cnt)+"]["+str(n)+"] = \""+x+"\";")
                        fout.write("\n")
                    cnt +=1 

fin.close()
fout.close()

