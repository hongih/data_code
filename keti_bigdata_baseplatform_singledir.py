import os
import numpy as np
import pandas as pd
from numpy import nan as NULL


dir = 'D:\keti_bigdata_platform\csv_file_1차_test'
new_dir = dir + '/'

file_list = os.listdir(dir)
file_list_csv = [file for file in file_list if file.endswith(".csv")]

# sub dir 파일 크기가 0 이 아닌 목록 추출
real_file_list_csv = []

for filename in file_list_csv:
    file_size = os.path.getsize(new_dir+filename)
    if file_size != 0:
        real_file_list_csv.append(filename)

file_cnt = 0
first_df_columns_cnt = 0
second_df_columns_cnt = 0
third_df_columns_cnt = 0
fourth_df_columns_cnt = 0
fiveth_df_columns_cnt = 0
other_df_columns_cnt = 0

for csv_file in real_file_list_csv:
    new_csv_file = new_dir+csv_file
    df = pd.read_csv(new_csv_file, encoding='utf-8')

    if file_cnt == 0:
        first_df_columns = df.columns
        file_cnt += 1
        first_df_columns_cnt += 1
        print("first_df_one")
        print("file_cnt", file_cnt)
    elif file_cnt == 1:
        if first_df_columns.equals(df.columns):
            file_cnt += 1
            first_df_columns_cnt += 1
            print("first_df_two")
            print("file_cnt", file_cnt)
        elif first_df_columns.equals(df.columns) == False:
            second_df_columns = df.columns
            file_cnt += 1
            second_df_columns_cnt += 1
            print("second_df_one")
            print("file_cnt", file_cnt)
        else:
            pass
    elif file_cnt == 2:
        if first_df_columns.equals(df.columns):
            file_cnt += 1
            first_df_columns_cnt += 1
            print("first_df_two")
            print("file_cnt", file_cnt)
        elif second_df_columns.equals(df.columns):
            file_cnt += 1
            second_df_columns_cnt += 1
            print("second_df_one")
            print("file_cnt", file_cnt)
        elif second_df_columns.equals(df.columns) == False:
            third_df_columns = df.columns
            file_cnt += 1
            third_df_columns_cnt += 1
            print("third_df_one")
            print("file_cnt", file_cnt)
        else:
            pass
    elif file_cnt == 3:
        if first_df_columns.equals(df.columns):
            file_cnt += 1
            first_df_columns_cnt += 1
            print("first_df_two")
            print("file_cnt", file_cnt)
        elif second_df_columns.equals(df.columns):
            file_cnt += 1
            second_df_columns_cnt += 1
            print("second_df_one")
            print("file_cnt", file_cnt)
        elif third_df_columns.equals(df.columns):
            file_cnt += 1
            third_df_columns_cnt += 1
            print("second_df_one")
            print("file_cnt", file_cnt)
        elif third_df_columns.equals(df.columns) == False:
            fourth_df_columns = df.columns
            file_cnt += 1
            fourth_df_columns_cnt += 1
            print("fourth_df_one")
            print("file_cnt", file_cnt)
        else:
            pass
    elif file_cnt == 4:
        if first_df_columns.equals(df.columns):
            file_cnt += 1
            first_df_columns_cnt += 1
            print("first_df_two")
            print("file_cnt", file_cnt)
        elif second_df_columns.equals(df.columns):
            file_cnt += 1
            second_df_columns_cnt += 1
            print("second_df_one")
            print("file_cnt", file_cnt)
        elif third_df_columns.equals(df.columns):
            file_cnt += 1
            third_df_columns_cnt += 1
            print("second_df_one")
            print("file_cnt", file_cnt)
        elif fourth_df_columns.equals(df.columns):
            file_cnt += 1
            fourth_df_columns_cnt += 1
            print("fourth_df_one")
            print("file_cnt", file_cnt)
        elif fourth_df_columns.equals(df.columns) == False:
            fiveth_df_columns = df.columns
            file_cnt += 1
            fiveth_df_columns_cnt += 1
            print("fiveth_df_one")
            print("file_cnt", file_cnt)
        else:
            pass
    else:
        if first_df_columns.equals(df.columns):
            file_cnt += 1
            first_df_columns_cnt += 1
            print("first_df_two")
            print("file_cnt", file_cnt)
        elif second_df_columns.equals(df.columns):
            file_cnt += 1
            second_df_columns_cnt += 1
            print("second_df_one")
            print("file_cnt", file_cnt)
        elif third_df_columns.equals(df.columns):
            file_cnt += 1
            third_df_columns_cnt += 1
            print("second_df_one")
            print("file_cnt", file_cnt)
        elif fourth_df_columns.equals(df.columns):
            file_cnt += 1
            fourth_df_columns_cnt += 1
            print("fourth_df_one")
            print("file_cnt", file_cnt)
        elif fourth_df_columns.equals(df.columns) == False:
            fiveth_df_columns = df.columns
            file_cnt += 1
            fiveth_df_columns_cnt += 1
            print("fiveth_df_one")
            print("file_cnt", file_cnt)
        else:
            other_df_columns_cnt += 1
            print("other_df")
            print("file_cnt", file_cnt)

    # df 저장
    w_df = new_csv_file.split('.')
    w_df_name = w_df[0]+'_df.' + w_df[1]
    df.to_csv(w_df_name, encoding='utf-8')

    # 결측치 제거
    missing_del_df = df.dropna(axis=1, how='all')
    missing_del_csv = new_csv_file.split('.')
    missing_dell_csv_file_wname = missing_del_csv[0] + \
        '_nulldel_'+'df.' + missing_del_csv[1]
    missing_del_df.to_csv(missing_dell_csv_file_wname,
                          sep=',', encoding='utf-8')


print("first_df", first_df_columns_cnt)
print("second_df", second_df_columns_cnt)
print("third_df", third_df_columns_cnt)
print("fourth_df", fourth_df_columns_cnt)
print("fiveth_df", fiveth_df_columns_cnt)
print("other_df", other_df_columns_cnt)

print("end")
