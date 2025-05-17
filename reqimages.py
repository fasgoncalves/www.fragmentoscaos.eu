import os, re, requests
from pathlib import Path
from bs4 import BeautifulSoup
from html import unescape

site_dir = Path("./")  # ou caminho onde tens o site
img_dir = site_dir / "assets/images"
img_dir.mkdir(parents=True, exist_ok=True)

# Dicionário para evitar downloads duplicados
url_to_local = {}
index = 0

# Encontrar imagens nos ficheiros HTML
for file in site_dir.glob("*.html"):
    if file.name == "index.html":
        continue
    html = file.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    modified = False

    for img in soup.find_all("img"):
        src = img.get("src")
        if not src or src.startswith("assets/images/"):
            continue

        src = unescape(src)
        if src not in url_to_local:
            try:
                ext = Path(src).suffix or ".jpg"
                local_name = f"img_{index}{ext}"
                local_path = img_dir / local_name
                r = requests.get(src, timeout=10)
                if r.status_code == 200:
                    with open(local_path, "wb") as f:
                        f.write(r.content)
                    url_to_local[src] = f"assets/images/{local_name}"
                    index += 1
            except Exception as e:
                print(f"Erro ao descarregar {src}: {e}")
                continue

        if src in url_to_local:
            img["src"] = url_to_local[src]
            modified = True

    if modified:
        file.write_text(str(soup), encoding="utf-8")

