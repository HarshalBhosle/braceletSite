from pathlib import Path
from django.conf import settings


def load_bracelet_image_map():
    config_path = Path(settings.BASE_DIR) / 'bracelets' / 'bracelet_image_map.txt'
    if not config_path.exists():
        return {}

    mapping = {}
    for line in config_path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '|' not in line:
            continue
        name, filename = [part.strip() for part in line.split('|', 1)]
        if name and filename:
            image_path = Path(settings.BASE_DIR) / 'bracelets' / 'static' / 'bracelets' / 'images' / filename
            if image_path.exists():
                mapping[name] = f'bracelets/images/{filename}'
            else:
                # Try common alternate extensions if the mapped filename is missing.
                base = image_path.stem
                for ext in ['.jpg', '.jpeg', '.png']:
                    alt_path = image_path.with_suffix(ext)
                    if alt_path.exists():
                        mapping[name] = f'bracelets/images/{alt_path.name}'
                        break
    return mapping
