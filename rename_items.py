#!/usr/bin/env python3
"""
Rename Items_Equipment folders and update README files
"""

import os
import json
import shutil
from pathlib import Path

ITEMS_PATH = Path("/home/kaktak/sphere_scripts/ultima_online_scripts/Items_Equipment")

def rename_folders_and_update_readme():
    """Rename all Item_Unkn folders and update README files"""

    # Load rename map
    with open('/tmp/item_rename_map.json', 'r') as f:
        rename_map = json.load(f)

    os.chdir(ITEMS_PATH)

    print("Начинаю переименовывать папки Items_Equipment...")
    print(f"Всего папок для переименования: {len(rename_map)}\n")

    renamed_count = 0
    for old_name, new_name in sorted(rename_map.items()):
        old_path = ITEMS_PATH / old_name
        new_path = ITEMS_PATH / new_name

        if not old_path.exists():
            print(f"⚠ Папка не найдена: {old_name}")
            continue

        try:
            # Rename folder
            os.rename(str(old_path), str(new_path))
            renamed_count += 1

            # Update README if exists
            readme_path = new_path / "README.md"
            if readme_path.exists():
                try:
                    with open(readme_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Replace old folder name with new one in README
                    updated_content = content.replace(old_name, new_name)

                    with open(readme_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                except Exception as e:
                    print(f"Ошибка при обновлении README для {new_name}: {e}")

            if (renamed_count % 50) == 0:
                print(f"✓ Переименовано {renamed_count}/{len(rename_map)} папок...")

        except Exception as e:
            print(f"✗ Ошибка при переименовании {old_name}: {e}")

    print(f"\n✓ Переименовано {renamed_count} папок в Items_Equipment категории")
    return renamed_count

if __name__ == '__main__':
    count = rename_folders_and_update_readme()
    print(f"\nИтого: переименовано {count} папок")
