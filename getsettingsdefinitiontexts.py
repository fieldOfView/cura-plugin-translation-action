from pathlib import Path
from settingspot import write_setting_text

import logging

def main():
    setting_json_paths = [path for path in Path(".").rglob("*.def.json") if "test" not in str(path)]
    for path in setting_json_paths:
        logging.info(f"Processing {path}...")
        write_setting_text(path, "i18n-temp")

if __name__=="__main__":
    main()
