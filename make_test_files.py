from pathlib import Path
import random
FOLDER = Path.home() / "Downloads" / "messy_folder"
FOLDER.mkdir(parents=True, exist_ok=True)
names = ["holiday", "notes", "report", "song", "lecture", "photo",
 "invoice", "project", "backup", "screenshot", "budget", "demo"]
extensions = [".jpg", ".png", ".pdf", ".docx", ".txt", ".mp4",
 ".mp3", ".zip", ".py", ".html", ".xyz"]
random.seed(1)
for i in range(1, 31):
 name = random.choice(names)
 ext = random.choice(extensions)
 (FOLDER / f"{name}_{i}{ext}").write_text("test file")
print(f"Created test files in {FOLDER}")
