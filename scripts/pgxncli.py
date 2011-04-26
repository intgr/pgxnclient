#!/usr/bin/env python
"""
pgxn.client -- command line interface
"""

# Copyright (C) 2011 Daniele Varrazzo

# This file is part of the PGXN client

import sys

from pgxn.client.cli import main
from pgxn.client.i18n import _
from pgxn.client.errors import PgxnException, UserAbort

import logging
logging.basicConfig(
    format="%(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger()

if __name__ == '__main__':
    try:
        main(sys.argv[1:])

    except UserAbort, e:
        logger.info("%s", e)
        sys.exit(1)

    except PgxnException, e:
        logger.error("%s", e)
        sys.exit(1)

    except Exception, e:
        logger.error(_("unexpected error: %s - %s"),
            e.__class__.__name__, e, exc_info=True)
        sys.exit(1)

    except BaseException, e:
        # ctrl-c
        sys.exit(1)

