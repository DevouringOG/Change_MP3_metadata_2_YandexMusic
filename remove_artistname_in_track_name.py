from pathlib import Path

# Укажите правильный путь к директории
DIRECTORY = Path(r"D:\Music\For YandexMusic\Images")
IMAGE_EXTENSION = ".jpg"
SUBSTRING_TO_REMOVE = "babaew.15 remix – "

for track_path in DIRECTORY.iterdir():
    if track_path.suffix == IMAGE_EXTENSION:

        # Удаляем ненужную подстроку из имени файла
        new_name = track_path.name.replace(SUBSTRING_TO_REMOVE, "")
        new_name = new_name.replace("..", ".")

        new_path = DIRECTORY / new_name

        print(f"OLD: {track_path.name}")
        print(f"NEW: {new_name}\n")

        # Переименовываем файл
        track_path.rename(new_path)
