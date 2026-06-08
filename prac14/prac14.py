import os
import sys

STORAGE_DIR = "snippets_storage"

def init_storage():
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)

def create_snippet(name):
    init_storage()
    file_path = os.path.join(STORAGE_DIR, name)
    if os.path.exists(file_path):
        return
    content = sys.stdin.read()
    if not content.strip():
        return
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def list_snippets():
    init_storage()
    files = os.listdir(STORAGE_DIR)
    for index, file_name in enumerate(files, start=1):
        file_path = os.path.join(STORAGE_DIR, file_name)
        size = os.path.getsize(file_path)
        print(file_name, size)

def delete_snippet(name):
    init_storage()
    file_path = os.path.join(STORAGE_DIR, name)
    if os.path.exists(file_path):
        os.remove(file_path)

def main():
    if len(sys.argv) < 2:
        return
    command = sys.argv[1].lower()
    if command == "create" and len(sys.argv) >= 3:
        create_snippet(sys.argv[2])
    elif command == "list":
        list_snippets()
    elif command == "delete" and len(sys.argv) >= 3:
        delete_snippet(sys.argv[2])

if __name__ == "__main__":
    main()