import pandas as pd
import json


def suggest_cal(int_features, cluster, sem_number):  # Import the csv file and fetch the names of each subject
    df = pd.read_csv(
        f'Z:/College/Third year/mini project/S-MINI PROJECT/Student-Analysis/code new/separate clustering/cluster{sem_number}_{cluster}.csv')

    del df['Unnamed: 0']
    del df['cluster']
    if 'GPA_SEM_4' in df.columns:
        del df['GPA_SEM_4']  # change the output number

    else:
        del df['GPA']

    names_of_subject = df.columns.tolist()
    SE = []
    IA = []
    TW = []
    OP = []
    OOPM_TW = []
    OOPM_OP = []
    Compare_list = []
    for x in names_of_subject:
        if '_SE' in x:
            SE.append(x)

        if '_IA' in x:
            IA.append(x)

        if 'OOPM_TW' in x:
            OOPM_TW.append(x)

        if 'OOPM_OP' in x:
            OOPM_OP.append(x)

        if 'OOPM' in x:
            break

        if '_TW' in x:
            TW.append(x)

        if '_OP' in x:
            OP.append(x)

    A = df[SE].mean().astype(int)
    Compare_list.append(int(A.mean()))
    B = df[IA].mean().astype(int)
    Compare_list.append(int(B.mean()))
    C = df[TW].mean().astype(int)
    Compare_list.append(int(C.mean()))
    D = df[OP].mean().astype(int)
    Compare_list.append(int(D.mean()))
    if 'OOPM_TW' and 'OOPM_OP' in names_of_subject:
        E = df[OOPM_TW].mean().astype(int)
        Compare_list.append(int(E.mean()))
        F = df[OOPM_TW].mean().astype(int)
        Compare_list.append(int(F.mean()))


    compare_limit = {3: 15, 4: 19}  # Limits for 3rd and 4th for loop

    Responses = json.loads(open('intents.json').read())
    check_list = ['Positive', 'Negative']
    Subjects = Responses['Subject']  # meaning for each list in intents  # The subject here stands for the subjects present in the json file

    def Subject(Subject_name, positive_negative, cluster):  # Function to return the required output
        return (f'{names_of_subject[Subject_name]}: \t{Subjects[0][names_of_subject[Subject_name]][check_list[positive_negative]][cluster]}')
    list = []
    for x in range(0, 9, 2):
        if int_features[x] < Compare_list[0]:
            list.append(Subject(x, 1, cluster))




        elif int_features[x] >= Compare_list[0]:
            list.append(Subject(x, 0, cluster))

    for y in range(1, 10, 2):
        if int_features[y] < Compare_list[1]:
            list.append(Subject(y, 1, cluster))

        elif int_features[y] >= Compare_list[1]:
            list.append(Subject(y, 0, cluster))

    for z in range(10, compare_limit[sem_number], 2):
        if int_features[z] < Compare_list[2]:
            list.append(Subject(z, 1, cluster))

        elif int_features[z] >= Compare_list[2]:
            list.append(Subject(z, 0, cluster))

    for w in range(11, compare_limit[sem_number] + 1, 2):
        if int_features[w] < Compare_list[3]:
            list.append(Subject(w, 1, cluster))

        elif int_features[w] >= Compare_list[3]:
            list.append(Subject(w, 0, cluster))

    if sem_number == 3:
        if int_features[16] < Compare_list[4]:
            list.append(Subject(16, 1, cluster))

        elif int_features[16] >= Compare_list[4]:
            list.append(Subject(16, 0, cluster))

        if int_features[17] < Compare_list[5]:
            list.append(Subject(17, 1, cluster))

        elif int_features[17] >= Compare_list[5]:
            list.append(Subject(17, 0, cluster))

        return list

    else:
        return list

