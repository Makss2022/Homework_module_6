import sys
from pathlib import Path
from cleaner import arrange_folder, delet_folders


def main():
    try:
        preassigned_path = Path(sys.argv[1])
        if not preassigned_path.exists():
            print(f"Folder '{preassigned_path}' does not exist")
            return
        destination_folder = preassigned_path
        arrange_folder(preassigned_path, destination_folder)
        delet_folders(preassigned_path)
    except IndexError as err:
        print(err)


if __name__ == "__main__":
    main()
