from pathlib import Path
from django.conf import settings

IMAGE_EXTENSIONS = {
    '.avif',
    '.bmp',
    '.gif',
    '.jfif',
    '.jpeg',
    '.jpg',
    '.pjpeg',
    '.pjp',
    '.png',
    '.svg',
    '.webp',
}


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
            image_dir = Path(settings.BASE_DIR) / 'bracelets' / 'static' / 'bracelets' / 'images'
            if not image_dir.exists():
                continue
            image_path = image_dir / filename
            if image_path.is_file():
                mapping[name] = f'bracelets/images/{filename}'
            else:
                for alt_path in image_dir.iterdir():
                    if (
                        alt_path.is_file()
                        and alt_path.stem.lower() == image_path.stem.lower()
                        and alt_path.suffix.lower() in IMAGE_EXTENSIONS
                    ):
                        mapping[name] = f'bracelets/images/{alt_path.name}'
                        break
    return mapping
