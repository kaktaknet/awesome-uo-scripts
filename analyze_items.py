#!/usr/bin/env python3
"""
Analyze Items_Equipment folders and create meaningful rename map
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

# Items_Equipment base path
ITEMS_PATH = Path("/home/kaktak/sphere_scripts/ultima_online_scripts/Items_Equipment")

# Keyword patterns for identifying item types
ITEM_KEYWORDS = {
    'weapon': r'\b(weapon|sword|axe|mace|bow|arrow|blade|hammer|spear|dagger|staff|crossbow|halberd|lute)\b',
    'armor': r'\b(armor|armour|plate|chain|leather|scale|helm|helmet|gauntlet|boots|glove|shield|breast|gorget|sleeves)\b',
    'jewelry': r'\b(ring|necklace|bracelet|earring|pendant|amulet|talisman|jewel|gem|crown|tiara|band)\b',
    'clothing': r'\b(clothing|clothes|robe|gown|dress|tunic|coat|cloak|cape|shirt|pants|skirt|vest|jacket|hood)\b',
    'food': r'\b(food|eat|edible|bread|meat|fish|fruit|potion|drink|beverage|ale|wine|cheese|apple|mushroom)\b',
    'crafting': r'\b(craft|crafting|ingredient|material|ore|ingot|wood|lumber|thread|cloth|silk|leather|hide|skin)\b',
    'alchemy': r'\b(alchemy|alchemist|potion|reagent|herb|mushroom|bottle|vial|ingredients)\b',
    'magery': r'\b(magery|spell|magical|enchant|arcane|rune|scroll|spellbook|grimoire|magic)\b',
    'tool': r'\b(tool|tools|pickaxe|shovel|hammer|saw|chisel|plane|tongs|wrench|axe|hatchet)\b',
    'container': r'\b(container|bag|pack|pouch|box|chest|crate|barrel|container|backpack|satchel)\b',
    'quest': r'\b(quest|quest|item|objective|task|goal|mission|reward)\b',
    'currency': r'\b(gold|coin|currency|money|treasure|gem|valuable|price|cost)\b',
    'decoration': r'\b(decoration|decorat|furniture|chair|table|carpet|painting|statue|vase|rug|curtain|tapestry|lamp|plant)\b',
    'light': r'\b(light|lamp|lantern|torch|candle|brighten|glow|illuminate)\b',
    'music': r'\b(music|instrument|harp|lute|drum|flute|horn|pipe|bell|lyre|organ|tambourine)\b',
    'house': r'\b(house|home|building|structure|door|window|wall|floor|roof|foundation)\b',
    'pet': r'\b(pet|animal|creature|beast|companion|mount|horse|dragon|familiar)\b',
    'boat': r'\b(boat|ship|vessel|sail|anchor|maritime|naval|galleon)\b',
    'scroll': r'\b(scroll|scroll|document|parchment|manuscript|letter|note|deed)\b',
    'book': r'\b(book|books|tome|journal|grimoire|lore|knowledge|wisdom|story)\b',
    'special': r'\b(special|unique|artifact|legendary|rare|powerful|ancient|cursed|blessed)\b',
}

def analyze_folder(folder_path):
    """Analyze a folder to determine its type"""
    matched_types = defaultdict(int)

    # Read README if it exists
    readme_path = folder_path / "README.md"
    if readme_path.exists():
        try:
            with open(readme_path, 'r', encoding='utf-8', errors='ignore') as f:
                readme_content = f.read().lower()
                for item_type, pattern in ITEM_KEYWORDS.items():
                    matches = len(re.findall(pattern, readme_content, re.IGNORECASE))
                    if matches > 0:
                        matched_types[item_type] += matches * 2  # Weight README higher
        except:
            pass

    # Read .scp files if they exist
    try:
        for scp_file in folder_path.glob("*.scp"):
            with open(scp_file, 'r', encoding='utf-8', errors='ignore') as f:
                scp_content = f.read().lower()
                for item_type, pattern in ITEM_KEYWORDS.items():
                    matches = len(re.findall(pattern, scp_content, re.IGNORECASE))
                    if matches > 0:
                        matched_types[item_type] += matches
    except:
        pass

    # Return the type with highest match count
    if matched_types:
        best_type = max(matched_types.items(), key=lambda x: x[1])[0]
        return best_type
    return 'misc'

def main():
    os.chdir(ITEMS_PATH)

    # Get all Item_Unkn folders
    item_folders = []
    for folder in sorted(os.listdir('.')):
        if folder.startswith('Item_Unkn'):
            item_folders.append(folder)

    print(f"Analyzing {len(item_folders)} Item_Unkn folders...")

    # Analyze each folder
    type_counts = defaultdict(list)
    rename_map = {}

    for idx, folder_name in enumerate(item_folders, 1):
        folder_path = ITEMS_PATH / folder_name
        if not folder_path.is_dir():
            continue

        item_type = analyze_folder(folder_path)
        type_counts[item_type].append(folder_name)

        if (idx % 50) == 0:
            print(f"Processed {idx}/{len(item_folders)} folders...")

    # Create rename map with versioning
    print("\nGenerating rename map...")
    for item_type, folders in sorted(type_counts.items()):
        for version, folder_name in enumerate(folders, 1):
            new_name = f"Item_{item_type.title()}_v{version}"
            rename_map[folder_name] = new_name

    # Save rename map
    with open('/tmp/item_rename_map.json', 'w') as f:
        json.dump(rename_map, f, indent=2, sort_keys=True)

    print(f"\nRename map created with {len(rename_map)} entries")
    print(f"Item types found: {len(type_counts)}")
    for item_type, folders in sorted(type_counts.items(), key=lambda x: -len(x[1])):
        print(f"  {item_type}: {len(folders)} folders")

if __name__ == '__main__':
    main()
