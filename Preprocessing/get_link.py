import os
from pathlib import Path

MARKDOWN_DIR = "tools-in-data-science-public"

def slugify(text):
    return text.lower().replace(" ", "-").replace("_", "-").replace(".md", "")

links = []

for md_path in sorted(Path(MARKDOWN_DIR).rglob("*.md")):
    page_name = md_path.stem.replace("_", " ").replace("-", " ").title()
    slug = slugify(md_path.stem)
    url = f"https://tds.s-anand.net/#/{slug}"
    links.append((str(md_path), url))

# Print all links
for file_path, url in links:
    print(f"{file_path} -> {url}")
