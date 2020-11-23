import re

CLEAN_UP_PATTERNS = [
    ('-<br />', '<lb break="no"/>'),
    ('<br />', '<lb />'),
    ('\n', ''),
]


def clean_markup(source, patterns=CLEAN_UP_PATTERNS):
    """ applies search and replace
    :param source: A string to clean
    :type source: string
    :param patterns: a list of tuples `[('-<br />', '<lb break="no"/>'),`]
    :type patterns: list

    :return: the cleaned string
    :rtype: string

    """
    for x in patterns:
        source = source.replace(x[0], x[1])
    return source


def extract_page_nr(some_string):
    """ extracts the page number from a string like `Seite 21`

    :param some_string: e.g. `Seite 21`
    :type some_string: string

    :return: The page number e.g. `21`
    :rtype: string
    """

    page_nr = re.findall(r'\d+', some_string)
    if len(page_nr) > 0:
        return "-".join(page_nr)
    else:
        return some_string
