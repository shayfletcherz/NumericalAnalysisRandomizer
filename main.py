# https://github.com/shayfletcherz/NumericalAnalysisRandomizer.git

import datetime
def random (id_list):

    now = datetime.datetime.now()

    print(now)

    qs_1 = (sum(id_list[(now.second+now.minute+now.hour)%4]) * now.second)%9 + 1

    print(qs_1)

    now = datetime.datetime.now()

    qs_2 = (sum(id_list[(now.second+now.minute+now.hour)%4])* now.second)%9 + 1

    now = datetime.datetime.now()

    qs_2_2 = (sum(id_list[(now.second + now.minute + now.hour+now.year) % 4])* now.minute) % 9 + 1

    print(qs_2 + 9, qs_2_2 + 9)

    now = datetime.datetime.now()

    qs_3 = (sum(id_list[(now.second+now.minute+now.hour)%4])* now.second)%12 + 1

    now = datetime.datetime.now()

    qs_3_3 = (sum(id_list[(now.second + now.minute + now.hour+now.year) % 4])* now.hour) % 12 + 1

    print(qs_3 + 18, qs_3_3 + 18)

    now = datetime.datetime.now()

    qs_4 = (sum(id_list[(now.second+now.minute+now.hour)%4])* now.second)%5 + 1

    print(qs_4 + 30)



list = [[3,2,7,2,4,8,6,0,5], [3,2,1,7,3,5,4,3,3], [3,1,8,7,2,7,6,4,1] , [2,0,3,3,4,2,6,2,1]]

random(list)



