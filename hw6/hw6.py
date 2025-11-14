import os

# ex1
# def create(path):
#     try:
#       os.makedirs(path,exist_ok=True)
#       print(f"directory '{path}'successfully")
#     except Exception as e:
#         print(f"Error '{e}'")

# ex2
# def empty(path):
#     try:
#      os.rmdir(path)
#      print(f" successfully'{path}'")
#     except OSError  as e:
#         print(f"error'{e}'")

# ex3
# def new_file(file_path):
#     try:
#         with open(file_path,'w') as file:
#           file.write('')
#           print(f" successfully'{file_path}'")
#     except OSError as e:
#         print(f"error'{e}'")

# ex4
# def write(file_path, content, append=False):
#     mode = 'a' if append else 'w'
#     try:
#         with open(file_path,mode) as file:
#           file.write(content)
#           print(f"successfully '{file_path}' ")
#     except OSError as e:
#         print(f"error'{e}'")

# ex5
# def delete(file_path):
#     try:
#         os.remove(file_path)
#         print(f"successfully'{file_path}'")
#     except OSError as e:
#         print(f"error'{e}'")

# ex6
# def list(directory_path):
#     try:
#         with open(directory_path) as entries:
#             for i in entries:
#               print(i.name)
#     except FileNotFoundError:
#         print(f" not found'{directory_path}'")

# ex7
# def show():
#     show_file=os.getcwd()
#     print(f"directory: {show_file}")
