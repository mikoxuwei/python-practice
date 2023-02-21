### 讀取 adult.csv 檔案，取得其中各種種族和其收入大於或小於等於50K，個別的人數，並依照>50K的人數由大至小排序。

import csv

with open('adult.csv', 'r') as fin:  ## 讀取檔案
    race = []
    race_num = [0] * 10
    n = 0

    ### 取得標題(第一列)
    h = fin.readline().replace('\n', '')  ## 去掉換行
    headers = h.split(',')  ## 因為 csv 檔案以逗號區隔，所以用逗號分開
   
    ### 找到種族、收入的行 col
    for i, ln in enumerate(headers):
        if ln == 'race':
            race_col = i
        if ln == 'income':
            income_col = i

    reader = csv.reader(fin)  ## 透過 csv.reader 取整個檔案內容 
    
    ###  找到所有種族，並計算出每個種族 >50K、<=50K 的人數
    """ 
    例如: race[race_A, race_B, ...]
    race_num[race_A_>50K, race_A_<=50K, race_B_>50K, race_B_<=50K, ...]
    所以如果是 race_C，在 race[2] 的位置，
    >50K、<=50K存的位置分別是 race_num[4]、race_num[5]，
    idx = 2 根據計算分別是 idx*2 = 4、idx*2 + 1 = 5    
    """
    for i, ln in enumerate(reader):
        if ln[race_col] in race:             ## 種族已經存在清單中
            idx = race.index(ln[race_col])   ## 取得此筆資料種族在 race[] 中的位置
            if '>50K' in ln[income_col]:     ## 如果 >50K 存入特定位置
                race_num[idx * 2] += 1
            else:                            ## 如果 <=50K 存入特定位置
                race_num[idx * 2 + 1] += 1
        else:                                ## 如果種族沒有清單中
            race.append(ln[race_col])        ## 先新增此種族進清單中
            idx = race.index(ln[race_col])
            if '>50K' in ln[income_col]:
                race_num[idx * 2] += 1
            else:
                race_num[idx * 2 + 1] += 1 

#     ## 檢查看數據有無錯誤
#     print(race)
#     print(race_num)

#     ###### 未排序
#     print('{:<20s} {:>10s} {:>10s}'.format('Race', '>50K', '<=50K'))
#     print('-------------------------------------------')
#     for i in range(len(race)):
#         print('{:<20} {:>10} {:>10}'.format(race[i], race_num[i*2], race_num[i*2+1]))
#     ######

    ### 根據 >50 的人數數據排序 由大到小
    income_list = []
    for i in range(len(race)):
        income_list.append((race[i], race_num[i*2], race_num[i*2+1]))  ## 把各種族、>50K、<=50K 放入一個 tuple
    income_list.sort(key = lambda x:x[1], reverse = True)
#     print(income_list)

    ### 輸出
    print('{:<20s} {:>10s} {:>10s}'.format('Race', '>50K', '<=50K'))
    print('-------------------------------------------')
    for i in income_list:
        l1, l2, l3 = i
        print('{:<20} {:>10} {:>10}'.format(l1, l2, l3))  ## <20 限制長度為 20 並置左，>10 限制長度為 10 置右
