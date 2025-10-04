#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-dashboard (see https://github.com/oarepo/oarepo-dashboard).
#
# oarepo-dashboard is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Oarepo Dashboard UI components. It is mainly a wrapper around dashboard from InvenioRDM."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from flask_menu import current_menu
from invenio_i18n import lazy_gettext as _
from oarepo_ui.overrides import (
    UIComponent,
    UIComponentOverride,
)
from oarepo_ui.overrides.components import UIComponentImportMode
from oarepo_ui.proxies import current_ui_overrides
from oarepo_ui.resources import TemplatePageUIResource, TemplatePageUIResourceConfig

if TYPE_CHECKING:
    from flask import Blueprint, Flask
    from flask_resources import ResourceConfig


class ComponentsResourceConfig(TemplatePageUIResourceConfig):
    """Resource config for dashboard components."""

    url_prefix = "/me"
    blueprint_name = "dashboard_components"
    template_folder = "templates"


def init_menu(app: Flask) -> None:
    """Initialize dashboard menu."""
    current_menu.submenu("actions.deposit").register(
        endpoint="invenio_app_rdm_users.uploads",
        text=_("My dashboard"),
        order=1,
    )
    user_dashboard = current_menu.submenu("dashboard")
    # set dashboard-config to its default
    user_dashboard_menu_config = {
        "uploads": {
            "endpoint": "invenio_app_rdm_users.uploads",
            "text": _("Uploads"),
            "order": 1,
        },
        "communities": {
            "endpoint": "invenio_app_rdm_users.communities",
            "text": _("Communities"),
            "order": 2,
        },
        "requests": {
            "endpoint": "invenio_app_rdm_users.requests",
            "text": _("Requests"),
            "order": 3,
        },
    }

    # apply dashboard-config overrides
    for submenu_name, submenu_kwargs in app.config["USER_DASHBOARD_MENU_OVERRIDES"].items():
        if submenu_name not in user_dashboard_menu_config:
            raise ValueError(
                f"attempting to override dashboard's submenu `{submenu_name}`, "
                "but dashboard has no registered submenu of that name"
            )
        user_dashboard_menu_config[submenu_name].update(submenu_kwargs)

    # register dashboard-menus
    for submenu_name, submenu_kwargs in user_dashboard_menu_config.items():
        user_dashboard.submenu(submenu_name).register(**submenu_kwargs)


def _register_dashboard_uploads_result_item(
    ui_overrides: set[UIComponentOverride], schema: str, component: UIComponent
) -> None:
    """Register a result list items for dashboard uploads."""
    dashboard_uploads_result_list_item = UIComponentOverride(
        "invenio_app_rdm_users.uploads",
        f"InvenioAppRdm.DashboardUploads.ResultsList.item.{schema}",
        component,
    )
    if dashboard_uploads_result_list_item not in ui_overrides:
        ui_overrides.add(dashboard_uploads_result_list_item)


def ui_overrides(app: Flask) -> None:  # NOQA: ARG001
    """Define overrides that this library will register."""
    dynamic_result_list_item = UIComponent(
        "DynamicResultsListItem",
        "@js/oarepo_ui/search/DynamicResultsListItem",
        UIComponentImportMode.DEFAULT,
    )
    dynamic_result_list_item_override = UIComponentOverride(
        "invenio_app_rdm_users.uploads",
        "InvenioAppRdm.DashboardUploads.ResultsList.item",
        dynamic_result_list_item,
    )
    if dynamic_result_list_item_override not in current_ui_overrides:
        current_ui_overrides.add(dynamic_result_list_item_override)


def finalize_app(app: Flask) -> None:
    """Finalize the app (registering menu items, or overrides etc...)."""
    init_menu(app)
    ui_overrides(app)


def create_blueprint(app: Flask) -> Blueprint:
    """Register blueprint for this resource."""
    app.config.get("OAREPO_UI_RESULT_LIST_ITEM_REGISTRATION_CALLBACKS", []).append(
        _register_dashboard_uploads_result_item
    )
    return TemplatePageUIResource(cast("ResourceConfig", ComponentsResourceConfig())).as_blueprint()
