import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE), str(HERE.parent)]

from lamin_sphinx import *  # noqa
from lamin_sphinx import html_theme_options, html_context  # noqa

project = "Lamin Legal"
html_title = f"{project}"
html_context["github_repo"] = "lamin-legal"  # noqa

ogp_site_url = "https://legal.lamin.ai"
ogp_site_name = project

html_theme_options["logo"] = {
    "link": "/",
    "text": project,
    "root": "https://legal.lamin.ai",
}
html_theme_options["icon_links"] = [
    {
        "name": "GitHub",
        "url": "https://github.com/laminlabs/lamin-legal",
        "icon": "fa-brands fa-github",
    },
]
