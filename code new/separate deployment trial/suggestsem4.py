# Add ranges for OOP for all Clusters


# suggest Functions compares the value of each int_feature value and give a suggestion accordingly
def suggest(int_features, output):
    # dict = {key: values}
    # key = Cluster Number
    # values = Range of that particular Cluster
    # int_features = Marks Obtained
    dict = {0: [63, 16.5, 21, 20.5],
            1: [47.5, 13, 20.5, 19],
            2: [56, 14.5, 21, 20],
            3: [68.5, 17.5, 22.5, 22.5],
            4: [45.5, 12.5, 19, 19],
            5: [35, 11, 18.5, 17]}
  #The cluster used here is Cluster 0.
  # The list will be appened for each Suggestion.
    list = []
    for x in range(0,9,2):
        if int_features[x] < dict[output][0]:
           # print('this is suggestion for SE', int_features[x])
            list.append(f'this is negative suggestion for SE {int_features[x]}')
           # return 'this is suggestion for SE'

        elif int_features[x] >= dict[output][0]:
            #print('this is suggestion for SE2', int_features[x])
            list.append(f'this is a positive suggestion for SE {int_features[x]}')
           # return 'this is suggestion for SE2'

    for y in range(1,10,2):
        if int_features[y] < dict[output][1]:
            #print('this is suggestion for IA', int_features[y])
            list.append(f'this is negative suggestion for IA {int_features[y]}')
           # return 'this is suggestion for IA'
        elif int_features[y] >= dict[output][1]:
            #print('this is suggestion for IA2', int_features[y])
            list.append(f'this is a positive suggestion for IA {int_features[y]}')
           # return 'this is suggestion for IA2'

    for z in range(10,19,2):
        if int_features[z] < dict[output][2]:
            #print('this is suggestion for TW', int_features[z])
            list.append(f'this is a negative suggestion for TW {int_features[z]}')
           # return 'this is suggestion for TW'
        elif int_features[z] >= dict[output][2]:
            #print('this is suggestion for TW2', int_features[z])
            list.append(f'this is a positive suggestion for TW2 {int_features[z]}')
           # return 'this is suggestion for IA2'

    for w in range(11,20,2):
        if int_features[w] < dict[output][3]:
            #print('this is suggestion for OP', int_features[w])
            list.append(f'this is a negative suggestion for OP {int_features[w]}')
           # return 'this is suggestion for TW'
        elif int_features[w] >= dict[output][3]:
            #print('this is suggestion for OP2', int_features[w])
            list.append(f'this is a positive suggestion for OP2 {int_features[w]}')
           # return 'this is suggestion for IA2'
    return list