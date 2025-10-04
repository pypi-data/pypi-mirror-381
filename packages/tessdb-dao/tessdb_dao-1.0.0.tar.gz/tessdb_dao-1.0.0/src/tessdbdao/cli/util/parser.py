# ----------------------------------------------------------------------
# Copyright (c) 2024 Rafael Gonzalez.
#
# See the LICENSE file for details
# ----------------------------------------------------------------------

# --------------------
# System wide imports
# -------------------

import os
from datetime import datetime
from argparse import ArgumentParser

# ---------------------------
# Third-party library imports
# ----------------------------

from lica.validators import vdate

# --------------
# local imports
# -------------

START_DATE = datetime(year=2000, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
END_DATE = datetime(year=2050, month=12, day=31, hour=23, minute=59, second=59, microsecond=99999)


def since() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-s",
        "--since",
        type=vdate,
        default=START_DATE,
        metavar="<YYYY-MM-DD>",
        help="Start date for Date dimension (default %(default)s)",
    )
    return parser


def until() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-u",
        "--until",
        type=vdate,
        default=END_DATE,
        metavar="<YYYY-MM-DD>",
        help="End date for Date dimension (default %(default)s)",
    )
    return parser


def seconds() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-e",
        "--seconds",
        type=int,
        choices=[i for i in range(1,61)],
        default=1,
        help="Default seconds resolution (default %(default)s)",
    )
    return parser

def batch() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-b",
        "--batch-size",
        type=int,
        default=10000,
        help="Date/Time database transaction batch size (default %(default)s)",
    )
    return parser
