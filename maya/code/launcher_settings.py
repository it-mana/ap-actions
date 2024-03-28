import anchorpoint as ap
import apsync as aps

import os
import sys

ui = ap.UI()
ctx = ap.Context.instance()

project = aps.get_project(ctx.path)
meta = project.get_metadata()

MAYA_DEFAULT = "C:/PROGRA~1/Autodesk/Maya2024"

settings = aps.Settings(name="maya")

# if not settings.contains("maya_root"):
#     settings.set("maya_root", MAYA_DEFAULT)
#     settings.store()


def create_dialog():
    dialog = ap.Dialog()

    dialog.title = "Maya Settings"

    dialog.add_text("MAYA_ROOT").add_input(
        default=settings.get("maya_root"),
        placeholder="path/to/maya/directory",
        var="maya_root",
        browse=ap.BrowseType.Folder,
        browse_path=settings.get("maya_root"),
        width=500,
    )

    dialog.add_info(text="Maya installation directory")

    dialog.add_separator()

    dialog.start_section("Maya Packages", folded=False)

    dialog.add_button("Apply", press_apply)

    dialog.show()


def press_apply(dialog):
    maya_root = dialog.get_value("maya_root")

    settings = aps.Settings(name="maya")
    settings.set("maya_root", maya_root)

    settings.store()

    ui.show_success("Maya", "Update Maya settings successfully.")

    dialog.close()


create_dialog()
