import os
import shutil
import argparse

def copy_files_recursive(src_dir, dest_dir):
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)

        if os.path.isdir(item_path):
            copy_files_recursive(item_path, dest_dir)

        elif os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lstrip('.').lower()
            if not file_extension:
                file_extension = 'no_extension'

            new_folder = os.path.join(dest_dir, file_extension)
            os.makedirs(new_folder, exist_ok=True)

            dest_file_path = os.path.join(new_folder, item)
            print(f"Copying {item_path} to {dest_file_path}")
            try:
                shutil.copy2(item_path, dest_file_path)
            except Exception as e:
                print(f"Error copying file {item_path}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Recursively copying and sorting files by extension."
        )
    )
    parser.add_argument('src', help="Path to the output directory")
    parser.add_argument(
        'dest',
        nargs='?',
        default='dist',
        help="Path to the destination directory (default 'dist')")
    args = parser.parse_args()

    src_dir = args.src
    dest_dir = args.dest

    if not os.path.exists(src_dir):
        print(f"Output directory {src_dir} does not exist.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copy_files_recursive(src_dir, dest_dir)
    print("Copying complete.")

if __name__ == "__main__":
    main()