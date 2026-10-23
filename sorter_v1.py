from pathlib import Path
import shutil

FOLDER = Path.home() / "Downloads" / "messy_folder"

CATEGORIES = {
     "Images": [".jpg", ".jpeg", ".png", ".gif"],
     "Documents": [".pdf", ".docx", ".txt", ".pptx"],
     "Videos": [".mp4", ".mkv", ".mov"],
     "Audio": [".mp3", ".wav"],
     "Archives": [".zip", ".rar"],
     "Code": [".py", ".js", ".html"],

} 

for file in list(FOLDER.iterdir()):
    if not file.is_file():
        continue

    for category, extensions in CATEGORIES.items():
        if file.suffix.lower() in extensions:
            (FOLDER / category).mkdir(exist_ok=True)
            shutil.move(str(file), str(FOLDER / category / file.name))
            print(f"Moved {file.name} -> {category}")
            break