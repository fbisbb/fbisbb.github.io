import csv

# 打开原始CSV文件和新CSV文件
with open('merged_data.csv', mode='r') as input_csv_file, \
        open('merged_dataok.csv', mode='w', newline='') as output_csv_file:

    # 创建CSV读取器和写入器
    csv_reader = csv.DictReader(input_csv_file)
    fieldnames = csv_reader.fieldnames

    # 创建CSV写入器并写入标题行
    csv_writer = csv.DictWriter(output_csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    # 遍历原始CSV文件的行
    for row in csv_reader:
        # 检查'alive'列是否为1，如果是，将行写入新CSV文件
        if row['alive'] == '1':
            csv_writer.writerow(row)
