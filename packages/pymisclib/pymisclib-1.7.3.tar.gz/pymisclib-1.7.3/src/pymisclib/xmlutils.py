#!/usr/bin/env python3
# vim: fileencoding=utf-8 ts=4
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: © Copyright 2024 by Christian Dönges. All rights reserved.
# SPDXID: SPDXRef-xmlutils-py
"""XML handling utilities."""

import logging
import xml.etree.ElementTree as ET

try:
    from lxml import etree as ET
    _USING_LXM = True
except ImportError:
    import xml.etree.ElementTree as ET
    _USING_LXM = False


def elements_equal(element1: ET.Element | ET.ElementTree,
                   element2: ET.Element | ET.ElementTree,
                   logger: logging.Logger = logging.getLogger(__name__)) -> bool:
    """Check if two XML elements are equal.

    Compares the tags, attributes, children (recursively), tail, and text of
    both *elements*, not their textual representations.

    :param xml.etree.ElementTree.Element element1: First XML element to compare.
    :param xml.etree.ElementTree.Element element2: Second XML element to compare.
    :param logging.Logger logger: Logger for diagnostics.
    :rtype: bool
    :return: True if elements are equal, False otherwise.

    .. versionadded:: 1.6.0
    """
    if isinstance(element1, ET.ElementTree):
        element1 = element1.getroot()
        logger.debug('Converted element <%s> from ElementTree to Element for comparison.', element1.tag)
    if isinstance(element2, ET.ElementTree):
        element2 = element2.getroot()
        logger.debug('Converted element <%s> from ElementTree to Element for comparison.', element2.tag)

    if element1.tag != element2.tag:
        logger.debug('Tag "%s" != "%s"', element1.tag, element2.tag)
        return False
    if element1.text != element2.text:
        logger.debug('Text "%s" != "%s"', element1.text, element2.text)
        return False
    if element1.tail != element2.tail:
        logger.debug('Tail "%s" != "%s"', element1.tail, element2.tail)
        return False
    if element1.attrib != element2.attrib:
        logger.debug('Attribute "%s" != "%s"', element1.attrib, element2.attrib)
        return False
    if len(element1) != len(element2):
        logger.debug('Length %d != %d', len(element1), len(element2))
        return False
    return all(elements_equal(child1, child2) for child1, child2 in zip(element1, element2))


def log_xml(fn_logger: logging.Logger,
            xml_elem: ET.Element | ET.ElementTree,
            level: int = logging.DEBUG,
            indent: int = 0,
            indent_level_start: int = 0,
            indent_spaces: int = 2):
    """Log the XML as one or more log entries.

    :param logging.Logger fn_logger: The logger to log to.
    :param etree._Element xml_elem: The XML element to log.
    :param int level: Level for logging (e.g logging.DEBUG, logging.INFO, ...)
    :param int indent: Number of spaces to indent all entries. This does not
        change the indentation added for nested elements (indent_spaces spaces per level).
    :param int indent_level_start: Start indentation at this level.
        If > 0, the parameter "indent" is ignored.
    :param int indent_spaces: Number of spaces to indent per level.

    .. note:: ``indent`` is the old interface for indenting the entire
        ``xml_element``. In order to be closer to the interface of the Python
        standard library, ``indent_level_start`` and ``indent_spaces`` have been
        introduced. Since there is no compatible way to deprecate ``indent``,
        it will stay but the recommendation is to switch to the new parameters.

    .. versionchanged:: 1.6.0 Moved here from :py:func:`pymisclib.utilities.log_xml`.
    .. versionchanged:: 1.6.2 Formatting improved.
    .. versionchanged:: 1.7.1 Added parameters ``indent_level_start`` and ``indent_spaces``.
    """
    if not fn_logger.isEnabledFor(level):
        # Save lots of processing cycles.
        return

    if indent < 0:
        raise ValueError('indent must be >= 0')
    if indent_level_start < 0:
        raise ValueError('indent_level_start must be >= 0')
    if indent_spaces < 0:
        raise ValueError('indent_space must be >= 0')

    if isinstance(xml_elem, ET.ElementTree):
        xml_elem = xml_elem.getroot()

    # Try to convert indent to an indent_level_start.
    if indent > 0 and indent_level_start == 0:
        if indent_spaces > 0:
            if indent % indent_spaces == 0:
                indent_level_start = int(indent / indent_spaces)
                indent = 0

    try:
        ET.indent(xml_elem, space = ' ' * indent_spaces, level = indent_level_start)
    except Exception as e:
        fn_logger.error('Failed to indent XML element: %s', e)
        fn_logger.debug('    XML element: %s', xml_elem)
        return
    try:
        if _USING_LXM:
            s = ET.tostring(xml_elem, pretty_print=True, encoding='unicode')
        else:
            s = ET.tostring(xml_elem, encoding='unicode')
            # xml.etree.ElementTree.indent() does not correctly indent the first line.
            if indent_level_start > 0:
                s = ' ' * (indent_spaces * indent_level_start) + s
    except Exception as e:
        fn_logger.error('Failed to convert XML element to string: %s', e)
        fn_logger.debug('    XML element: %s', xml_elem)

    if indent == 0:
        fmt = '%s'
    else:
        fmt = f'{" " * indent}%s'
    for line in s.splitlines():
        fn_logger.log(level, fmt, line)
