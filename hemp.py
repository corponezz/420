import os
import shutil

user = os.getlogin()

icon_path = r"C:\Windows\hemp\420-279\icon.ico"
target_directory = f"C:\\Users\\{user}\\Desktop"
base_directory = f"C:\Windows\hemp"


for i in range(1, 421):
    filename = f"420-{i}.exe"
    target_path = os.path.join(target_directory, filename)
    shutil.copy(icon_path, target_path)
    
for i in range(1, 421):
    if i == 279:
        continue
    
    folder_name = f"420-{i}"
    folder_path = os.path.join(base_directory, folder_name)
    
    try:
        os.mkdir(folder_path)
        print(f"Папка создана: {folder_path}")
    except FileExistsError:
        print(f"Папка уже существует: {folder_path}")
        
    filename = f"420.exe"
    target_path = os.path.join(base_directory,folder_name, filename)
    shutil.copy(icon_path, target_path)