from pathlib import Path

p = Path("C:\\Users\\T Kluczlowski\\Dropbox\PYTHON 3\\CHAPTER 17 PYGAME\\PNG-cards-1.3")
file_list = [file.name for file in p.iterdir() if file.is_file()]
print(file_list)