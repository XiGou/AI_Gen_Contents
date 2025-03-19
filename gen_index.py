import os
import json

def list_files(base_dir):
    file_list = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(('.txt', '.md', '.html')):
                file_list.append(os.path.relpath(os.path.join(root, file), base_dir))
    return file_list

base_dir = '.'  # 运行脚本的目录
files = list_files(base_dir)

with open(os.path.join(base_dir, 'index.json'), 'w', encoding='utf-8') as f:
    json.dump(files, f, ensure_ascii=False, indent=2)

print("索引文件 'index.json' 已生成")
