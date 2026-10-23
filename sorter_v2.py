import shutil
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--")]
FOLDER = Path(args[0]) if args else Path.home() / "Downloads" / "messy_folder"
DRY_RUN = "--dry-run" in sys.argv

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".js", ".html"],
}


def category_for(file):
    ext = file.suffix.lower()
    for name, extensions in CATEGORIES.items():
        if ext in extensions:
            return name
    return "Other"


def unique_path(path):
    counter = 1
    new_path = path
    while new_path.exists():
        new_path = path.with_name(f"{path.stem} ({counter}){path.suffix}")
        counter += 1
    return new_path


moved = 0
for file in list(FOLDER.iterdir()):
    if not file.is_file():
        continue
    target_dir = FOLDER / category_for(file)
    destination = unique_path(target_dir / file.name)
    print(f"{file.name} -> {target_dir.name}/{destination.name}")
    if not DRY_RUN:
        target_dir.mkdir(exist_ok=True)
        shutil.move(str(file), str(destination))
        moved += 1

print("Dry run: nothing was moved." if DRY_RUN else f"Done. Moved {moved} files.")
