import csv
import json

sample_user_json = 'sample_user.json'
sample_users_json = 'sample_users.json'


def load_json_file(file):
    # JSONデータの読み込み
    with open(file) as json_file:
        data = json.load(json_file)

    return data


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


if __name__ == '__main__':
    json1 = load_json_file(sample_user_json)
    generate_csv_writer_object(json1, 'sample_user.csv')

    json2 = load_json_file(sample_users_json)
    generate_csv_writer_object(json2, 'sample_users.csv')
