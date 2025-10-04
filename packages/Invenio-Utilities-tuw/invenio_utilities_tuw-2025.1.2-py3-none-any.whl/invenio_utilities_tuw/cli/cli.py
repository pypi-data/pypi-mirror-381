# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 - 2022 TU Wien.
#
# Invenio-Utilities-TUW is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""CLI commands for Invenio-Utilities-TUW."""

import click

from .drafts import drafts
from .files import files
from .notifications import notifications
from .records import records
from .reports import reports
from .users import users
from .vocabularies import vocabularies


@click.group()
def utilities():
    """Utility commands for InvenioRDM."""


utilities.add_command(drafts)
utilities.add_command(files)
utilities.add_command(notifications)
utilities.add_command(records)
utilities.add_command(reports)
utilities.add_command(users)
utilities.add_command(vocabularies)
