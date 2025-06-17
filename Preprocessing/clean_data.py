import os
import json
from bs4 import BeautifulSoup
from markdown import markdown

# Input directories
DISCOURSE_DIR = "discourse_posts"
MARKDOWN_DIR = "tools-in-data-science-public"
# Output directory
OUTPUT_DIR = "clean_required_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Convert cooked HTML or Markdown to plain text
def clean_text(text, is_markdown=False):
    if is_markdown:
        html = markdown(text)
    else:
        html = text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text(separator=' ', strip=True)

# Clean and save Discourse JSON content
def clean_discourse_json():
    for filename in os.listdir(DISCOURSE_DIR):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(DISCOURSE_DIR, filename), "r", encoding="utf-8") as f:
            data = json.load(f)

        posts = data.get("post_stream", {}).get("posts", [])
        cleaned_posts = []

        for post in posts:
            raw_html = post.get("cooked", "")
            cleaned = clean_text(raw_html)
            if cleaned:
                cleaned_posts.append(cleaned)

        full_text = "\n\n".join(cleaned_posts)
        out_path = os.path.join(OUTPUT_DIR, filename.replace(".json", ".txt"))
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(full_text)

# Clean and save Markdown files
def clean_markdown_files():
    for filename in os.listdir(MARKDOWN_DIR):
        if not filename.endswith(".md"):
            continue
        with open(os.path.join(MARKDOWN_DIR, filename), "r", encoding="utf-8") as f:
            md_content = f.read()

        cleaned = clean_text(md_content, is_markdown=True)
        out_path = os.path.join(OUTPUT_DIR, filename.replace(".md", ".txt"))
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(cleaned)

if __name__ == "__main__":
    clean_discourse_json()
    clean_markdown_files()
