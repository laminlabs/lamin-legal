import sys
from pathlib import Path
from dirsync import sync

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE), str(HERE.parent)]

from lamin_sphinx import *  # noqa
from lamin_sphinx import html_theme_options  # noqa

sync("../lamin-about/about", ".", "sync", exclude=["^.*README.md$"])

project = "Lamin"
html_title = "Company | Lamin"
html_context["github_repo"] = "lamin-about"  # noqa

ogp_site_url = "https://lamin.ai"

html_theme_options["logo"] = {
    "link": "https://lamin.ai",
    "text": project,
    "root": "https://lamin.ai",
}
html_theme_options["icon_links"] = [
    {
        "name": "GitHub",
        "url": "https://github.com/laminlabs/lamin-about",
        "icon": "fa-brands fa-github",
    },
]
