"""Build the OrbitGuard pages from the templates in this folder.

    python3 source/build.py

Writes:
  index.html                                  hosted console (textures from jsDelivr, ~180 KB)
  offline/orbitguard-defence-offline.html     self-contained console (textures embedded)
  tracker/index.html                          10,000-object tracker with constellation highlighting
"""
import base64, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
p = lambda *a: os.path.join(HERE, *a)
uri = lambda f, m: f"data:{m};base64," + base64.b64encode(open(f, "rb").read()).decode()
CDN = "https://cdn.jsdelivr.net/npm/three-globe@2.45.3/example/img/"
HEAD = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n')

def page(body, icon=""):
    return HEAD + icon + body.replace("</style>\n", "</style>\n</head>\n<body>\n", 1) + "\n</body>\n</html>\n"

def embed_textures(s):
    return (s.replace("__DAY__", uri(p("textures", "day.jpg"), "image/jpeg"))
             .replace("__NIGHT__", uri(p("textures", "night.jpg"), "image/jpeg"))
             .replace("__WATER__", uri(p("textures", "water.jpg"), "image/jpeg")))

d = open(p("defence.template.html"), encoding="utf-8").read()

hosted = (d.replace("__LOGO__", uri(p("logo-sm.png"), "image/png"))
           .replace("__DAY__", CDN + "earth-blue-marble.jpg")
           .replace("__NIGHT__", CDN + "earth-night.jpg")
           .replace("__WATER__", CDN + "earth-water.png")
           .replace('width="191" height="120"', 'width="140" height="88"'))
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(
    page(hosted, '<link rel="icon" type="image/png" href="favicon.png">\n'))

offline = embed_textures(d.replace("__LOGO__", uri(p("logo.png"), "image/png")))
open(os.path.join(ROOT, "offline", "orbitguard-defence-offline.html"), "w", encoding="utf-8").write(
    page(offline, '<link rel="icon" type="image/png" href="' + uri(p("favicon.png"), "image/png") + '">\n'))

t = embed_textures(open(p("tracker.template.html"), encoding="utf-8").read())
open(os.path.join(ROOT, "tracker", "index.html"), "w", encoding="utf-8").write(page(t))
print("built index.html, offline/orbitguard-defence-offline.html, tracker/index.html")
