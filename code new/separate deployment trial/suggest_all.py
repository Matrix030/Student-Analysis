import pandas as pd

def suggest2(int_features, cluster, sem_number):  # Import the csv file and fetch the names of each subject
    df = pd.read_csv(
        f'G:/SEM 5/mini-project/code new/separate clustering/cluster{sem_number}_{cluster}.csv')      
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
    if sem_number ==3 and cluster == 5:
        Compare_list = []
    print(Compare_list)

    compare_limit = {3: 15, 4: 19}  # Limits for 3rd and 4th for loop

    list = []
    for x in range(0, 9, 2):
        if int_features[x] < Compare_list[0]:
            # print('this is suggestion for SE', int_features[x])
            list.append(f'this is negative suggestion for {names_of_subject[x]}  {int_features[x]}')
        # return 'this is suggestion for SE'

        elif int_features[x] >= Compare_list[0]:
            # print('this is suggestion for SE2', int_features[x])
            list.append(f'this is a positive suggestion for {names_of_subject[x]}  {int_features[x]}')
        # return 'this is suggestion for SE2'

    for y in range(1, 10, 2):
        if int_features[y] < Compare_list[1]:
            # print('this is suggestion for IA', int_features[y])
            list.append(f'this is negative suggestion for {names_of_subject[y]}  {int_features[y]}')
        # return 'this is suggestion for IA'
        elif int_features[y] >= Compare_list[1]:
            # print('this is suggestion for IA2', int_features[y])
            list.append(f'this is a positive suggestion for {names_of_subject[y]}  {int_features[y]}')
        # return 'this is suggestion for IA2'

    for z in range(10, compare_limit[sem_number], 2):
        if int_features[z] < Compare_list[2]:
            # print('this is suggestion for TW', int_features[z])
            list.append(f'this is a negative suggestion for {names_of_subject[z]}  {int_features[z]}')
        # return 'this is suggestion for TW'
        elif int_features[z] >= Compare_list[2]:
            # print('this is suggestion for TW2', int_features[z])
            list.append(f'this is a positive suggestion for {names_of_subject[z]}  {int_features[z]}')
        # return 'this is suggestion for IA2'

    for w in range(11, compare_limit[sem_number] + 1, 2):
        if int_features[w] < Compare_list[3]:
            # print('this is suggestion for OP', int_features[w])
            list.append(f'this is a negative suggestion for {names_of_subject[w]}  {int_features[w]}')
        # return 'this is suggestion for TW'
        elif int_features[w] >= Compare_list[3]:
            # print('this is suggestion for OP2', int_features[w])
            list.append(f'this is a positive suggestion for {names_of_subject[x]}  {int_features[w]}')
        # return 'this is suggestion for IA2'

    if sem_number == 3:
        if int_features[16] < Compare_list[4]:
            # print('this is suggestion for OOPTW', int_features[16])
            list.append(
                f'this is a negative suggestion for {names_of_subject[16]}  {int_features[16]}')  # make changes here
            # return 'this is suggestion for TW'
        elif int_features[16] >= Compare_list[4]:
            # print('this is suggestion for OOPTW2', int_features[16])
            list.append(
                f'this is a positive suggestion for {names_of_subject[16]}  {int_features[16]}')  # make changes here
            # return 'this is suggestion for OOPTW2'

        if int_features[17] < Compare_list[5]:
            # print('this is suggestion for OOPOP', int_features[17])
            list.append(
                f'this is a negative suggestion for {names_of_subject[17]}  {int_features[17]}')  # make changes here
            # return 'this is suggestion for TW'
        elif int_features[17] >= Compare_list[5]:
            # print('this is suggestion for OOPOP2', int_features[17])
            list.append(
                f'this is a positive suggestion for {names_of_subject[17]}  {int_features[17]}')  # make changes here
            # return 'this is suggestion for OOPOP'
        return list

    else:
        return list