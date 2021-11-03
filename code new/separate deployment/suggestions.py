
dict = {0:[17, 60, 21, 21],
        1:[12, 43, 20, 20],
        2:[14.6, 55, 21, 21],
        3:[14.6,55, 21, 21],
        4:[13.8, 51, 20.667, 19.9],
        5:["To be decided"]}



def suggest(int_features, output):
    if output == 5:  #this is clsuter 0
        for x in range(0,9,2):
            if int_features[x] < 60:
                print('this is suggestion for SE', int_features[x])
               # return 'this is suggestion for SE'

            elif int_features[x] >= 60:
                print('this is suggestion for SE2', int_features[x])
               # return 'this is suggestion for SE2'

        for y in range(1,10,2):
            if int_features[y] < 17:
                print('this is suggestion for IA', int_features[y])
               # return 'this is suggestion for IA'
            elif int_features[y] >= 17:
                print('this is suggestion for IA2', int_features[y])
               # return 'this is suggestion for IA2'

        for z in range(10,15,2):
            if int_features[z] < 17:
                print('this is suggestion for TW', int_features[z])
               # return 'this is suggestion for TW'
            elif int_features[z] >= 17:
                print('this is suggestion for TW2', int_features[z])
               # return 'this is suggestion for IA2'

        for w in range(11,16,2):
            if int_features[w] < 17:
                print('this is suggestion for OP', int_features[w])
               # return 'this is suggestion for TW'
            elif int_features[w] >= 17:
                print('this is suggestion for OP2', int_features[w])
               # return 'this is suggestion for IA2'


        if int_features[16] < 17:
            print('this is suggestion for OOPTW', int_features[16])
            # return 'this is suggestion for TW'
        elif int_features[16] >= 17:
            print('this is suggestion for OOPTW2', int_features[16])
            # return 'this is suggestion for IA2'

        if int_features[17] < 17:
            print('this is suggestion for OOPOP', int_features[17])
            # return 'this is suggestion for TW'
        elif int_features[17] >= 17:
            print('this is suggestion for OOPOP2', int_features[17])
            # return 'this is suggestion for IA2'