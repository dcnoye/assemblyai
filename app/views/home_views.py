from pygments.formatters import HtmlFormatter
import markdown
import markdown.extensions.fenced_code
from flask import (
    Blueprint,
)


home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route('/')
def landing_page():
    """Landing page."""
    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()

    readme_file = open("README.md", "r")
    markdown_string = markdown.markdown(
        readme_file.read(),
        extensions=["fenced_code", "codehilite"]
    )
    markdown_css = "<style>" + css_string + "</style>"
    good_stuff = markdown_css + markdown_string

    return good_stuff
