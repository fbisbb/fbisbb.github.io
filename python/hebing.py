import os
import csv

# 获取当前工作目录
current_directory = os.getcwd()

# 查找当前目录下的所有CSV文件
csv_files = [f for f in os.listdir(current_directory) if f.endswith('.csv')]

# 如果没有CSV文件，退出
if not csv_files:
    print("在当前目录中找不到任何CSV文件。")
    exit()

# 创建一个合并后的CSV文件
merged_csv_file = 'merged_data.csv'

# 打开合并后的CSV文件以写入模式
with open(merged_csv_file, 'w', newline='', encoding='utf-8') as merged_file:
    csv_writer = csv.writer(merged_file)

    # 遍历每个CSV文件并将其内容写入合并后的文件
    for csv_file in csv_files:
        csv_file_path = os.path.join(current_directory, csv_file)

        # 打开当前CSV文件以读取模式，使用'latin-1'编码方式
        with open(csv_file_path, 'r', newline='', encoding='latin-1') as current_csv:
            csv_reader = csv.reader(current_csv)

            # 逐行将数据从当前CSV文件写入合并后的CSV文件
            for row in csv_reader:
                csv_writer.writerow(row)

print(f"已将所有CSV文件合并到 '{merged_csv_file}' 文件中。")
