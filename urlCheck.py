import os
import re
import sys

def check_urls_empty(base_dirs):
    pattern = re.compile(r'url\s*=\s*(["\'])(.*?)\1')
    failed = False

    for base_dir in base_dirs:
        for root, _, files in os.walk(base_dir):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    with open(filepath, "r") as f:
                        for i, line in enumerate(f, 1):
                            match = pattern.search(line)
                            if match:
                                url_value = match.group(2).strip()
                                if url_value:
                                    print(f"[ERROR] Non-empty url in {filepath}:{i} -> {line.strip()}")
                                    failed = True

    return failed

if __name__ == "__main__":
    folders = ["web"]  
    if check_urls_empty(folders):
        sys.exit(1)
    else:
        print("[OK] All url= lines are empty.")
