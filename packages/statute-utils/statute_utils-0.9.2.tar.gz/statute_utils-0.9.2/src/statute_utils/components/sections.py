import re
from typing import Iterable, Match, NamedTuple, Optional

from bs4 import BeautifulSoup, Tag
from bs4.element import NavigableString, PageElement
from prelawsql.sanitizer import statute_sanitizer


def slice_unit(item: Tag, source: str) -> str:
    """Slice a snippet from the source based on the item parameter as the start index,
    and its succeeding item as the end index

    Args:
        item (Tag): the section tag
        source (str): the html markup of the entire text

    Returns:
        str: the characters between the item parameter and the next
    """
    s: int = source.index(str(item))
    mark: str = str(end) if (end := item.find_next("section")) else "</body>"
    e: int = source.index(mark)
    return source[s:e]


class Unit(NamedTuple):
    order: int
    item: str
    caption: str | None
    content: str


def caption_content(raw: str):
    # initialize controls
    caption = None
    counter = 0
    soup = BeautifulSoup(raw, "lxml")
    body = soup.body
    if not body:
        raise Exception("Missing html body")

    child_nodes = body.contents
    if not child_nodes:
        raise Exception("Missing child nodes")

    # remove section; cannot use decompose since the section might contain relevant text
    if not soup.section:
        raise Exception("No sections")
    soup.section.unwrap()

    while True:
        try:
            target = child_nodes[counter]
        except Exception:
            break

        # first non-empty string
        if isinstance(target, NavigableString) and str(target).strip():
            break

        # italicized text, extract from child_nodes is done implicitly
        elif isinstance(target, Tag) and target.name == "em":
            caption = target.extract().get_text().strip("–—- ")
            break

        counter += 1

    content = "".join(str(i) for i in child_nodes).strip("–—- ")
    return caption, statute_sanitizer.sanitize(content)


def make_unit(elem: Tag, html_markup: str) -> Optional[Unit]:
    """Using passed section tag, generate a section snippet as a Unit

    Args:
        elem (Tag): [description]
        soup (BeautifulSoup): [description]

    Returns:
        Unit: [description]
    """
    if not (section_number := match_section(elem.get_text())):
        return None
    item = section_number.group().strip()
    uniform_item = uniform_section_phrase(item)
    sliced = slice_unit(elem, html_markup)
    removed_item = re.sub(item, "", sliced).strip()
    caption, content = caption_content(removed_item)
    _id = elem.get("id")
    if not _id or isinstance(_id, list):
        raise Exception(f"Bad id found under {elem=}")

    return Unit(int(_id), uniform_item, caption, content)


def make_units(html: BeautifulSoup) -> Iterable[Unit]:
    """The html object will be used to generate section tags
    For each (pre-marked) section tag, create a unit

    Args:
        html (BeautifulSoup): The marked html

    Returns:
        Iterable[Unit]: named tuple consisting of unit parameters

    Yields:
        Iterator[Iterable[Unit]]: [description]
    """
    revised_html = str(html)
    for section in html("section"):
        if unit := make_unit(section, revised_html):
            yield unit


def match_section(raw: str) -> Match | None:
    """Return matching section text from the raw string, if it exists

    Args:
        raw (str): [description]

    Returns:
        Optional[Match]: [description]
    """
    regex = r"""
        ^\s*
        S
        (
            (
                (EC|ec)
                [\s\.\,]*
                \d+ # any number
                \.
                \s*
            )|
            (
                ECTION
                \s*
                1 # first section
                \.
                \s*
            )
        )
    """
    pattern = re.compile(regex, re.X)
    return pattern.search(raw)


def uniform_section_phrase(raw: str):
    regex = r"""
        ^\s*
        S
        (
            ECTION|
            EC|
            ec
        )
        [\s.,]+
    """
    pattern = re.compile(regex, re.X)
    return pattern.sub("Section ", raw).strip("., ") if pattern.search(raw) else raw


def candidate_unit(el: PageElement):
    """Tag matching the following requisites: (1) the next element is a
    navigable string, (2) the next element is not None, and (3) the string
    version of the next element matche the section pattern to be be considered
    a candidate for a unit.

    Args:
        el (PageElement): Target BeautifulSoup object to flag

    Returns:
        [type]: [description]
    """
    return (
        isinstance(el.next_element, NavigableString)
        and el.next_element is not None
        and match_section(str(el.next_element))
    )


def mark_html_sections(raw: str) -> list[Unit] | None:
    html = BeautifulSoup(raw, "lxml")
    if candidates := html(candidate_unit):  # type: ignore
        for counter, candidate in enumerate(candidates, start=1):
            wrapper = html.new_tag("section")
            target = candidate.next_element
            elem = target.wrap(wrapper)
            elem["id"] = counter
        return list(make_units(html))
    return None


def list_sections(raw: str) -> list[dict]:
    """Based on the markup in html format, generate units.
    For each unit generated, convert into a dictionary.

    Args:
        raw (str): [description]

    Returns:
        list[dict]: [description]
    """
    return [s._asdict() for s in raw_s] if (raw_s := mark_html_sections(raw)) else []
