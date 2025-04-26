import os
import shutil

forder1 = r'C:\Users\a5655\Desktop\aaa' # 폴더 경로
forder2 = r'C:\Users\a5655\Desktop\bbb'

def get_mtime(forder): # {파일 이름 : 파일 수정 시간} 리턴
    return {
        i: os.path.getmtime(os.path.join(forder, i))
        for i in os.listdir(forder)
        if os.path.isfile(os.path.join(forder, i))
    }

files1 = get_mtime(forder1)
files2 = get_mtime(forder2)

both_files = set(files1.keys()) & set(files2.keys())
only1_files = set(files1.keys()) - set(files2.keys())
only2_files = set(files2.keys()) - set(files1.keys())

result = []

for i in both_files: # 최근에 수정된 파일 경로 -> result
    src_folder = forder1 if files1[i] > files2[i] else forder2
    result.append(os.path.join(src_folder, i))


if both_files != set(): # 재사용 시 shutil.move 에러 방지
    for i in only1_files: # 최근에 수정된 파일 경로 -> result
        result.append(os.path.join(forder1, i))

    for i in only2_files:
        result.append(os.path.join(forder2, i))
    

os.makedirs('result', exist_ok=True) # 폴더 생성

for i in result: # 파일 이동
    shutil.move(i, os.path.join(os.getcwd(), 'result'))
    