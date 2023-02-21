### 讀取 adult.csv 檔案，取得其中各種種族和其收入大於或小於等於50K，個別的人數，並依照>50K的人數由大至小排序。

import csv

with open('adult.csv', 'r') as fin:
    race = []
    race_num = [0] * 10
    n = 0


    h = fin.readline().replace('\n', '')
    headers = h.split(',')


    ### find race row
    for i, ln in enumerate(headers):
        if ln == 'race':
            race_row = i
        if ln == 'income':
            income_row = i


    reader = csv.reader(fin)

    ### find all race
    for i, ln in enumerate(reader):
        if ln[race_row] in race:
            idx = race.index(ln[race_row])
            if '>50K' in ln[income_row]:   
                race_num[idx * 2] += 1

            else:
                race_num[idx * 2 + 1] += 1

        else:
            race.append(ln[race_row])
            idx = race.index(ln[race_row])
            if '>50K' in ln[income_row]:
                race_num[idx * 2] += 1
                #### 檢查
#                 if(idx * 2 + 1 == 5):
#                     print(ln[race_row])
#                     print('{}'.format(ln[income_row]))
#                     print(str(race_num[idx * 2 + 1]))
            else:
                race_num[idx * 2 + 1] += 1 
                #### 檢查
#                 if(idx * 2 + 1 == 5):
#                     print(ln[race_row], race_num)
#                     print(idx)
#                     print('first {}'.format(ln[income_row]))
#                     print(str(race_num[idx * 2 + 1]))
#                     print(print('{:12s} {:2s} {:6s} {:17s} {}'.format(ln[0], ln[3], ln[4], ln[5], ln[6])))
#             race_num[len(race)] += 1
#             print(ln[race_row] + race_num[race.index[ln[race_row]]])

#     print(race)
#     print(race_num)

#     ###### 未排序
#     print('{:<20s} {:>10s} {:>10s}'.format('Race', '>50K', '<=50K'))
#     print('-------------------------------------------')
#     for i in range(len(race)):
#         print('{:<20} {:>10} {:>10}'.format(race[i], race_num[i*2], race_num[i*2+1]))
#     ######


    ####### 根據 >50 的數據排序 由大到小
    income_list = []
    for i in range(len(race)):
        income_list.append((race[i], race_num[i*2], race_num[i*2+1]))
    income_list.sort(key = lambda x:x[1], reverse = True)
#     print(income_list)

    print('{:<20s} {:>10s} {:>10s}'.format('Race', '>50K', '<=50K'))
    print('-------------------------------------------')
    for i in income_list:
        l1, l2, l3 = i
        print('{:<20} {:>10} {:>10}'.format(l1, l2, l3))
