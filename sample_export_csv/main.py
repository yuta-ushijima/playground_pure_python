import csv
from datetime import datetime
import json
import os

sample_user_json = 'sample_user.json'
sample_users_json = 'sample_users.json'


def load_json_file(file):
    try:
        # JSONデータの読み込み
        with open(file) as json_file:
            data = json.load(json_file)
            if not data:
                print(f'Error: {file} is empty')
                return None
            return data
    except FileNotFoundError:
        print(f'Error: {file} not found')
        return None


def generate_csv_writer_object(json_data, file_name):
    # CSVファイルを作成し、CSVライターオブジェクトを作成する
    # open関数でnewline=''としているのは、Windows上で改行コードの問題を回避するため。
    # newline引数に''を指定することで、改行コードの自動変換を行わないようになる。
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # JSONデータが配列か単純なJSONかを判定する
        if isinstance(json_data, list):
            # ヘッダー行を書き込む
            writer.writerow(json_data[0].keys())

            # JSONデータをループして、各行をCSVに書き込む
            for item in json_data:
                writer.writerow(item.values())
        elif isinstance(json_data, dict):
            # jsonのkeyをcsvヘッダーとして書き込む
            writer.writerow(json_data.keys())

            # JSONのvalueをCSVに書き込む
            writer.writerow(json_data.values())
        else:
            print("JSONデータではありません")


def get_current_date_directory_path():
    dt_now = datetime.now()
    year = dt_now.year
    month = '{:02d}'.format(dt_now.month)
    day = dt_now.day
    return f'./{year}/{month}/{day}/'


if __name__ == '__main__':
    dir_path = get_current_date_directory_path()
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

        json1 = load_json_file(sample_user_json)
        generate_csv_writer_object(json1, f'{dir_path}sample_user.csv')

        json2 = load_json_file(sample_users_json)
        generate_csv_writer_object(json2, f'{dir_path}sample_users.csv')
