import os

def bulk_rename(folder_path, prefix):
    """
    Renames all files in the given folder with a new prefix followed by a number.
    """
    try:
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        print(f"Found {len(files)} files in '{folder_path}'. Renaming...")

        for index, filename in enumerate(files):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}_{index+1}{ext}"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)

        print("✅ Renaming completed successfully!")

    except FileNotFoundError:
        print("❌ Folder not found. Please check the path.")
    except Exception as e:
        print(f"⚠️ Error: {e}")


def main():
    print("📁 Bulk File Re-namer 📁")
    folder_path = input("Enter the folder path: ").strip()
    prefix = input("Enter the new file prefix (e.g., file, image, doc): ").strip()

    bulk_rename(folder_path, prefix)


if __name__ == "__main__":
    main()
