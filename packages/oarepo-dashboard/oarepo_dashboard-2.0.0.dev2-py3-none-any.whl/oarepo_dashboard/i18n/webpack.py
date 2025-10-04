#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-dashboard (see https://github.com/oarepo/oarepo-dashboard).
#
# oarepo-dashboard is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Oarepo Dashboard i18n webpack configuration."""

from __future__ import annotations

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {},
            "dependencies": {},
            "devDependencies": {},
            "aliases": {"@translations/oarepo_dashboard": "translations/oarepo_dashboard/i18next.js"},
        }
    },
)
