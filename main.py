from pathlib import Path

from mutagen.id3 import APIC, ID3, TIT2, TPE1
from mutagen.mp3 import MP3

MUSIC_DIRECTORY = Path(r"D:\Music\For YandexMusic")
IMAGES_DIRECTORY = Path(r"D:\Music\For YandexMusic\Images")
MUSIC_EXTENSION = ".mp3"
IMAGE_EXTENSION = ".jpg"
ARTIST_NAME = "DEVOURING"


def update_mp3_metadata(file_name, music_directory, images_directory):
    """Обновление метаданных MP3"""

    # Проверяем расширение файла
    if not file_name.endswith(MUSIC_EXTENSION):
        return

    image_path = images_directory / (
        file_name.replace(MUSIC_EXTENSION, IMAGE_EXTENSION)
    )

    # Проверяем, существует ли изображение
    if not image_path.exists():
        print(f"Изображение для {file_name} не найдено")
        return

    track_path = music_directory / file_name

    audio = MP3(track_path, ID3=ID3)

    # добавляем теги если их не было
    if not audio.tags:
        audio.add_tags()

    # Добавление изображения в теги аудиофайла
    audio.tags.add(
        APIC(
            encoding=3,
            mime="image/jpeg",
            type=3,
            desc="Cover",
            data=image_path.read_bytes(),
        ),
    )

    # Добавление информации о названии и исполнителе
    audio.tags.add(
        TIT2(encoding=3, text=file_name.replace(MUSIC_EXTENSION, "")),
    )
    audio.tags.add(TPE1(encoding=3, text=ARTIST_NAME))

    # Сохранение обновленных метаданных
    try:
        audio.save(v2_version=3)
        print(f"Обновлены метаданные для {file_name}")
    except Exception as e:
        print(f"Не удалось обновить метаданные для {file_name}: {e}")


# Обработка каждого файла в директории с музыкой
for file_name in MUSIC_DIRECTORY.iterdir():
    if file_name.is_file():
        update_mp3_metadata(file_name.name, MUSIC_DIRECTORY, IMAGES_DIRECTORY)
