#!/usr/bin/env python
###############################################################################
# (c) Copyright 2018 CERN                                                     #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "LICENSE".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
"""
Generate and print the environment banner
"""


def _center(txt, width):
    """
    Return a string of length `width` with the string `txt` centered

    >>> _center('abc', 14)
    '     abc      '
    """
    left = " " * int((width - len(txt)) / 2)
    right = " " * (width - len(txt) - len(left))
    return f"{left}{txt}{right}"


def generate(width=80, env=None):
    """
    Return the environment banner string.
    """
    from os import environ, pathsep

    if env is None:
        env = environ

    lines = []
    lines.append("*" * width)
    lines.append("*{}*".format(_center("---- LbEnv ----", width - 2)))
    if "BINARY_TAG" in env:
        lines.append(
            "*{}*".format(
                _center(
                    "using platform id {}".format(env["BINARY_TAG"]),
                    width - 2,
                )
            )
        )

    lines.append("*" * width)
    if "User_release_area" in env:
        lines.append(
            " --- User_release_area is set to {}".format(env["User_release_area"])
        )
    if env.get("CMAKE_PREFIX_PATH"):
        lines.append(" --- CMAKE_PREFIX_PATH is set to:")
        lines.extend(f"    {item}" for item in env["CMAKE_PREFIX_PATH"].split(pathsep))
    else:
        lines.append(" --- CMAKE_PREFIX_PATH is NOT set!")
    lines.append("-" * width)
    return "\n".join(lines)


if __name__ == "__main__":
    print(generate())
