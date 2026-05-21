from django.db import migrations

BRACELET_DEMO_DATA = [
    {
        'name': 'Amethyst Harmony',
        'description': 'A calming amethyst bracelet designed to bring balance and clarity to your mind.',
        'price': '59.00',
        'material': 'Amethyst & Sterling Silver',
        'color': 'Purple',
        'size': '7.0 inches',
        'stock': 18,
        'image_url': 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80',
    },
    {
        'name': 'Rose Quartz Glow',
        'description': 'Soft and elegant rose quartz beads to support self-love and gentle joyful energy.',
        'price': '64.00',
        'material': 'Rose Quartz & Gold-Plated',
        'color': 'Blush Pink',
        'size': '7.2 inches',
        'stock': 14,
        'image_url': 'https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=900&q=80',
    },
    {
        'name': 'Citrine Sunrise',
        'description': 'Bright citrine energy for abundance, optimism, and a cheerful everyday look.',
        'price': '69.00',
        'material': 'Citrine & Gold-Tone Metal',
        'color': 'Golden Yellow',
        'size': '7.1 inches',
        'stock': 12,
        'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80',
    },
    {
        'name': 'Labradorite Moon',
        'description': 'A mystical labradorite bracelet that shimmers with every movement and supports intuition.',
        'price': '74.00',
        'material': 'Labradorite & Leather',
        'color': 'Grey Blue',
        'size': '7.3 inches',
        'stock': 16,
        'image_url': 'https://images.unsplash.com/photo-1516910817561-5ada8b3247c0?auto=format&fit=crop&w=900&q=80',
    },
    {
        'name': 'Clear Quartz Clarity',
        'description': 'A clear quartz design for focus, energy amplification, and versatile styling.',
        'price': '52.00',
        'material': 'Clear Quartz & Silver',
        'color': 'Crystal Clear',
        'size': '7.0 inches',
        'stock': 20,
        'image_url': 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=900&q=80',
    },
    {
        'name': 'Black Onyx Luxe',
        'description': 'A bold black onyx bracelet with a modern luxe finish for day-to-night elegance.',
        'price': '66.00',
        'material': 'Black Onyx & Stainless Steel',
        'color': 'Black',
        'size': '7.2 inches',
        'stock': 9,
        'image_url': 'https://images.unsplash.com/photo-1530519430397-efcfb6f06f80?auto=format&fit=crop&w=900&q=80',
    },
    {
        'name': 'Moonstone Mist',
        'description': 'A dreamy moonstone bracelet with pearly shimmer, ideal for evening glamour.',
        'price': '72.00',
        'material': 'Moonstone & Rose Gold',
        'color': 'Iridescent White',
        'size': '7.1 inches',
        'stock': 11,
        'image_url': 'https://images.unsplash.com/photo-1518617968098-1e6a7c1f1d01?auto=format&fit=crop&w=900&q=80',
    },
    {
        'name': 'Turquoise Dream',
        'description': 'A statement turquoise bracelet with vivid color and grounding energy.',
        'price': '71.00',
        'material': 'Turquoise & Brass',
        'color': 'Turquoise',
        'size': '7.0 inches',
        'stock': 13,
        'image_url': 'https://images.unsplash.com/photo-1509223197845-458d87318791?auto=format&fit=crop&w=900&q=80',
    },
    {
        'name': 'Jade Serenity',
        'description': 'A serene jade bracelet crafted for harmony and a polished everyday look.',
        'price': '62.00',
        'material': 'Jade & Gold-Plated',
        'color': 'Emerald Green',
        'size': '7.2 inches',
        'stock': 10,
        'image_url': 'https://images.unsplash.com/photo-1465406325906-3f1fa28383f6?auto=format&fit=crop&w=900&q=80',
    },
]


def create_demo_bracelets(apps, schema_editor):
    Bracelet = apps.get_model('bracelets', 'Bracelet')
    for item in BRACELET_DEMO_DATA:
        Bracelet.objects.get_or_create(name=item['name'], defaults=item)


def reverse_seed(apps, schema_editor):
    Bracelet = apps.get_model('bracelets', 'Bracelet')
    Bracelet.objects.filter(name__in=[item['name'] for item in BRACELET_DEMO_DATA]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('bracelets', '0003_category_product'),
    ]

    operations = [
        migrations.RunPython(create_demo_bracelets, reverse_seed),
    ]
