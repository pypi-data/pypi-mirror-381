# ----------------------------------------------------------------------
# Copyright (c) 2024 Rafael Gonzalez.
#
# See the LICENSE file for details
# ----------------------------------------------------------------------

# --------------------
# System wide imports
# -------------------

import logging
import asyncio
from argparse import Namespace, ArgumentParser

# -------------------
# Third party imports
# -------------------

from lica.sqlalchemy import sqa_logging
from lica.asyncio.cli import execute
from lica.asyncio.photometer import Role

# --------------
# local imports
# -------------

from .. import __version__
from ..controller.photometer import Reader
from .util import parser as prs
from .util.misc import log_phot_info, log_messages

# ----------------
# Module constants
# ----------------

DESCRIPTION = "TESS-W Reader tool"

# -----------------------
# Module global variables
# -----------------------

# get the module logger
log = logging.getLogger(__name__.split(".")[-1])
controller = None

# ------------------
# Auxiliar functions
# ------------------

# -----------------
# Auxiliary classes
# -----------------


# -------------------
# Auxiliary functions
# -------------------


async def cli_read_ref(args: Namespace) -> None:
    global controller
    ref_params = {
        "model": args.ref_model,
        "sensor": args.ref_sensor,
        "endpoint": args.ref_endpoint,
        "old_proto": args.ref_old_proto,
        "log_level": logging.INFO if args.ref_raw_message else logging.WARN,
    }
    controller = Reader(
        ref_params=ref_params,
    )
    await controller.init()
    await log_phot_info(controller, Role.REF)
    if args.info:
        return
    await log_messages(controller, Role.REF, args.num_messages)


async def cli_read_test(args: Namespace) -> None:
    global controller
    test_params = {
        "model": args.test_model,
        "sensor": args.test_sensor,
        "endpoint": args.test_endpoint,
        "old_proto": args.test_old_proto,
        "log_level": logging.INFO if args.test_raw_message else logging.WARN,
    }
    controller = Reader(
        test_params=test_params,
    )
    await controller.init()
    await log_phot_info(controller, Role.TEST)
    if args.info:
        return
    await log_messages(controller, Role.TEST, args.num_messages)


async def cli_read_both(args: Namespace) -> None:
    global controller
    ref_params = {
        "model": args.ref_model,
        "sensor": args.ref_sensor,
        "endpoint": args.ref_endpoint,
        "old_proto": args.ref_old_proto,
        "log_level": logging.INFO if args.ref_raw_message else logging.WARN,
    }
    test_params = {
        "model": args.test_model,
        "sensor": args.test_sensor,
        "endpoint": args.test_endpoint,
        "old_proto": args.test_old_proto,
        "log_level": logging.INFO if args.test_raw_message else logging.WARN,
    }
    controller = Reader(
        ref_params=ref_params,
        test_params=test_params,
    )
    try:
        await controller.init()
        async with asyncio.TaskGroup() as tg:
            tg.create_task(log_phot_info(controller, Role.REF))
            tg.create_task(log_phot_info(controller, Role.TEST))
        if args.info:
            return
        async with asyncio.TaskGroup() as tg:
            tg.create_task(log_messages(controller, Role.REF, args.num_messages))
            tg.create_task(log_messages(controller, Role.TEST, args.num_messages))
    except* Exception as eg:
        for e in eg.exceptions:
            if args.trace:
                log.exception(e)
            else:
                log.error(e)
        raise RuntimeError("Could't continue execution, check errors above")


# -----------------
# CLI API functions
# -----------------


def add_args(parser: ArgumentParser):
    subparser = parser.add_subparsers(dest="command", required=True)
    p = subparser.add_parser(
        "ref", parents=[prs.info(), prs.nmsg(), prs.ref()], help="Read reference photometer"
    )
    p.set_defaults(func=cli_read_ref)
    p = subparser.add_parser(
        "test", parents=[prs.info(), prs.nmsg(), prs.test()], help="Read test photometer"
    )
    p.set_defaults(func=cli_read_test)
    p = subparser.add_parser(
        "both",
        parents=[
            prs.info(),
            prs.nmsg(),
            prs.ref(),
            prs.test(),
        ],
        help="read both photometers",
    )
    p.set_defaults(func=cli_read_both)


async def cli_main(args: Namespace) -> None:
    sqa_logging(args)
    await args.func(args)


def main():
    """The main entry point specified by pyproject.toml"""
    execute(
        main_func=cli_main,
        add_args_func=add_args,
        name=__name__,
        version=__version__,
        description=DESCRIPTION,
    )


if __name__ == "__main__":
    main()
