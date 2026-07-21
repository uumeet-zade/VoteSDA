import os
import json
from bs4 import BeautifulSoup
import re

files = ["index.html", "platform.html", "events.html", "candidates.html"]

# Classes of elements we want to ensure are translated
target_classes = {
    'zigzag-title', 'zigzag-desc',
    'event-title', 'event-location', 'event-time', 'event-desc', 'event-date-month', 'event-date-day', 'event-action',
    'candidate-name', 'candidate-role', 'candidate-bio', 'candidate-constituency',
    'hero-title', 'hero-subtitle', 'hero-eyebrow',
    'bento-item-title', 'bento-item-desc', 'stat-label', 'stat-number',
    'btn-primary', 'btn-outline', 'category-btn',
    'footer-name', 'footer-motto', 'footer-copy',
    'nav-name', 'lang-option', 'section-title', 'section-desc'
}

source_dict = {}

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Counter for new keys
    counter = 1
    file_prefix = filename.split('.')[0]

    # First pass: collect existing data-i18n tags
    for el in soup.find_all(attrs={"data-i18n": True}):
        key = el['data-i18n']
        content = "".join(str(c) for c in el.contents).strip()
        content = re.sub(r'\s+', ' ', content)
        source_dict[key] = content

    # Second pass: find target classes without data-i18n
    for el in soup.find_all(class_=True):
        classes = set(el.get('class', []))
        if classes.intersection(target_classes) and not el.has_attr('data-i18n'):
            # Only tag if there's actual text
            if el.get_text(strip=True):
                new_key = f"auto-{file_prefix}-{counter}"
                counter += 1
                el['data-i18n'] = new_key
                content = "".join(str(c) for c in el.contents).strip()
                content = re.sub(r'\s+', ' ', content)
                source_dict[new_key] = content

    # Check headers and paragraphs inside page-header and other un-classed blocks
    for el in soup.select('.page-header h1, .page-header p, nav a:not(.nav-brand), .event-rsvp'):
        if not el.has_attr('data-i18n') and el.get_text(strip=True):
            new_key = f"auto-{file_prefix}-{counter}"
            counter += 1
            el['data-i18n'] = new_key
            content = "".join(str(c) for c in el.contents).strip()
            content = re.sub(r'\s+', ' ', content)
            source_dict[new_key] = content

    # Save modified HTML
    # Use formatter=None to avoid BeautifulSoup corrupting scripts or SVGs
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"Processed {filename}: added tags up to {counter-1}.")

for f in files:
    process_file(f)

# Save the master source dictionary
with open('data/new_source.json', 'w', encoding='utf-8') as f:
    json.dump(source_dict, f, indent=2, ensure_ascii=False)

print(f"Extraction complete. Total keys: {len(source_dict)}")
