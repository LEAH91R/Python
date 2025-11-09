# def count_words_in_file(file_path):
#     try:
#         with open(file_path,'r',encoding='utf-8')as file:
#             text=file.read()
#             words=text.split()
#             return len(words)
#     except FileNotFoundError:
#         print(f"שגיאה: הקובץ בנתיב '{file_path}' לא נמצא.")
#         return -1
#     except Exception as e:
#         print(f"שגיאה אחרת אירעה: {e}")
#         return -1
#
#
# count = count_words_in_file("my_file.txt")
import json


def func(data):

    with open('data.json','w') as jsonFile:
        json.dump(data,jsonFile)

    with open('data.json','r') as jsonFile:
        data=json.load(jsonFile)
        print(data)


print(func({"name":"david","age":23}))
