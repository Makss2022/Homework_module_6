from pathlib import Path
import shutil
from typing import Dict, List
from transformer import normalize_filename

CATEGORIES: Dict[str, List[str]] = {
    "images": ["jpeg", "png", "jpg", "svg"],
    "videos": ["avi", "mp4", "mov", "mkv"],
    "documents": ["doc", "docx", "txt", "pdf", "xlsx", "pptx"],
    "music": ["mp3", "ogg", "wav", "amr"],
    "archives": ["zip", "gz", "tar"],
    "unknown": [],
}


def arrange_folder(preassigned_path: Path, destination_folder: Path):
    for file_path in preassigned_path.iterdir():
        if file_path.is_dir():
            arrange_folder(file_path, destination_folder)
        elif file_path.is_file():
            move_to_category_folder(file_path, destination_folder)


def define_category(file_path: Path) -> str:
    extension: str = file_path.name.split('.')[-1]
    for category, ext in CATEGORIES.items():
        if extension in ext:
            return category
    CATEGORIES["unknown"].append(extension)
    return "unknown"


def delet_folders(preassigned_path: Path):
    for folder in preassigned_path.iterdir():
        if folder.name not in list(CATEGORIES.keys()):
            shutil.rmtree(folder)


def move_to_category_folder(file_path: Path, destination_folder: Path):
    category = define_category(file_path)
    destination_category = destination_folder / category
    destination_category.mkdir(exist_ok=True)
    if category == "archives":
        folder_unpack = destination_category / file_path.name.split(".")[0]
        folder_unpack.mkdir()
        shutil.unpack_archive(file_path, folder_unpack)
        return
    destination_path = destination_category / normalize_filename(file_path.name)
    shutil.move(file_path, destination_path)
