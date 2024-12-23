import json
from collections import defaultdict

# 直辖市列表
municipalities = ["北京市", "天津市", "上海市", "重庆市"]


def parse_admdvs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 构建一个字典来存储区域信息
    areas = defaultdict(list)
    province = None
    city = None

    for line in lines:
        # 清除行首尾的空白字符，并跳过空行或注释行（如果有的话）
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith('#'):
            continue

        parts = stripped_line.split('\t')
        if len(parts) != 2:
            print(f"Warning: Line format is incorrect - '{stripped_line}'")
            continue

        code, name = parts

        if len(code) == 6 and code.endswith('0000'):
            # 省级单位
            province = {'name': name.strip(), 'value': code.strip(), 'children': []}
            areas[code[:2]].append(province)

            # 如果是直辖市，则添加同名的地市级区划
            if name in municipalities:
                city_code = code[:-2] + '01'
                city = {'name': "直辖市", 'value': city_code.strip(), 'children': []}
                province['children'].append(city)
            else:
                city = None  # Reset city when a new province starts
        elif len(code) == 6 and code.endswith('00'):
            # 地市级单位
            city = {'name': name.strip(), 'value': code.strip(), 'children': []}
            if province is not None:
                province['children'].append(city)
            else:
                print(f"Warning: City found before a province - '{name}'")
        else:
            # 区县级单位
            district = {'name': name.strip(), 'value': code.strip(), 'children': []}
            if city is not None:
                city['children'].append(district)
            elif province is not None:
                province['children'].append(district)
            else:
                print(f"Warning: District found without a parent city or province - '{name}'")

    # 将所有省份的信息合并成一个列表
    result = []
    for _, provinces in areas.items():
        for province in provinces:
            result.append(province)

    return result


def main():
    # 文件路径
    file_path = 'admdvs.txt'

    # 解析文件并生成JSON
    try:
        parsed_data = parse_admdvs(file_path)

        # 输出JSON到文件
        with open('admdvs.json', 'w', encoding='utf-8') as json_file:
            json.dump(parsed_data, json_file, ensure_ascii=False, indent=4)
        print("JSON file created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()