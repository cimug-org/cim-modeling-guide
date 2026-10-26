"""Per-rule anchors and rule cross-links for the CIM Modeling Guide site.

MkDocs hook (MkDocs 1.4+ `hooks:` setting; no plugin to install). It changes the
rendered HTML only; the guide's Markdown, and so its rules and the PDF text, are
untouched.

1. Every rule ID cell in a rules table (`<td>Rule049</td>`, from either the HTML
   tables or the Markdown pipe tables) gets `id="Rule049"`, so
   https://cim-mg.ucaiug.io/latest/<section>/#Rule049 lands on that rule. The
   anchor is the rule ID exactly as written, so a link is "#" plus the ID.
   The ID itself is the permalink: clicking or tapping it puts the rule's URL in
   the address bar (works on phones, where there is no hover).
2. Every mention of a rule in running text ("Rule049", "Rule 124", "[Rule 124]")
   becomes a link to that rule's anchor, on the same page or on another page.

The anchor is the rule number, so a link to #Rule049 resolves in every published
version (the rule numbers are the same in all versions).
"""

import logging
import re

from mkdocs.utils import get_relative_url

log = logging.getLogger("mkdocs.hooks.rule_anchors")

# A rule ID cell as it appears in the Markdown source (HTML table or pipe table).
_SRC_CELL = re.compile(r"<td>\s*Rule(\d{3})\s*</td>|^\|\s*Rule(\d{3})\s*\|", re.M)

# The same cell in the rendered HTML (pipe tables may add align/style attributes).
_HTML_CELL = re.compile(r"<td(?P<attrs>[^>]*)>\s*Rule(?P<num>\d{3})\s*</td>")

# A rule mention in running text: Rule049, Rule 49, Rule 124.
_MENTION = re.compile(r"\bRule ?(\d{1,3})\b")

# Split rendered HTML into tags and text so only text outside links/code is linked.
_TOKENS = re.compile(r"(<[^>]+>)")
_SKIP_TAGS = ("a", "code", "pre", "script", "style")

_rule_pages = {}  # "049" -> page URL of the page that defines Rule049


def _anchor(num):
    return f"Rule{num}"


def on_files(files, config):
    """Map every rule number to the page whose rules table defines it."""
    _rule_pages.clear()
    for f in files.documentation_pages():
        with open(f.abs_src_path, encoding="utf-8") as fh:
            src = fh.read()
        for m in _SRC_CELL.finditer(src):
            num = m.group(1) or m.group(2)
            if num in _rule_pages and _rule_pages[num] != f.url:
                log.warning("Rule%s is defined on %s and %s", num, _rule_pages[num], f.url)
            _rule_pages.setdefault(num, f.url)
    log.info("rule_anchors: %d rules indexed", len(_rule_pages))
    return files


def _link_mentions(text, page):
    def repl(m):
        num = m.group(1).zfill(3)
        target = _rule_pages.get(num)
        if target is None:
            log.warning("%s mentions Rule%s, which no rules table defines", page.file.src_uri, num)
            return m.group(0)
        href = "#" + _anchor(num)
        if target != page.url:
            href = get_relative_url(target, page.url) + href
        return f'<a class="cmm-rule-ref" href="{href}">{m.group(0)}</a>'

    return _MENTION.sub(repl, text)


def on_page_content(html, page, config, files):
    # 1. Rule mentions in running text become links. A text node that is nothing
    #    but a rule ID is the ID cell itself, and is anchored in step 2 instead.
    out, skip_depth = [], 0
    for tok in _TOKENS.split(html):
        if tok.startswith("<"):
            name = re.match(r"</?\s*([a-zA-Z0-9]+)", tok)
            if name and name.group(1).lower() in _SKIP_TAGS and not tok.endswith("/>"):
                skip_depth += -1 if tok.startswith("</") else 1
                skip_depth = max(skip_depth, 0)
            out.append(tok)
        elif skip_depth or not _MENTION.search(tok) or re.fullmatch(r"\s*Rule\d{3}\s*", tok):
            out.append(tok)
        else:
            out.append(_link_mentions(tok, page))
    html = "".join(out)

    # 2. Each rule ID cell gets an id, and its ID text becomes a link to itself
    #    (the permalink). The hover "¶" is drawn by extra.css, so no extra text
    #    reaches the search index or the PDF.
    def cell(m):
        num = m.group("num")
        a = _anchor(num)
        attrs = m.group("attrs")
        if re.search(r'\bclass="', attrs):
            attrs = re.sub(r'\bclass="', 'class="cmm-rule-id ', attrs, count=1)
        else:
            attrs += ' class="cmm-rule-id"'
        return (
            f'<td{attrs} id="{a}"><a class="cmm-rule-permalink" href="#{a}"'
            f' title="Permanent link to Rule{num}">Rule{num}</a></td>'
        )

    return _HTML_CELL.sub(cell, html)
