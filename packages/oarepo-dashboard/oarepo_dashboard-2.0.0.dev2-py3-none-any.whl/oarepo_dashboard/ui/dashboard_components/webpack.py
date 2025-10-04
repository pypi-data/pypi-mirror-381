"""Oarepo Dashboard dashboard components webpack configuration."""

#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-dashboard (see https://github.com/oarepo/oarepo-dashboard).
#
# oarepo-dashboard is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
from __future__ import annotations

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {"dashboard_components": "./js/dashboard_components/custom-components.js"},
            "dependencies": {},
            "devDependencies": {},
            "aliases": {"@js/dashboard_components": "./js/dashboard_components/search"},
        }
    },
)
