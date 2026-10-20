"""Wrap src/index.html (artifact-style body) into a standalone docs/index.html for GitHub Pages."""
from pathlib import Path

root = Path(__file__).parent
body = (root / "src" / "index.html").read_text(encoding="utf-8")
head = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
)
# Head-level tags (title, meta, link, style) stay in <head>; the rest goes in <body>.
split = body.index("</style>") + len("</style>")
out = head + body[:split] + "\n</head>\n<body>\n" + body[split:] + "\n</body>\n</html>\n"
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "index.html").write_text(out, encoding="utf-8")
print("wrote docs/index.html", len(out), "bytes")
