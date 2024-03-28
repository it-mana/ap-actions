import anchorpoint as ap
import apsync as aps

import os
import sys

ui = ap.UI()
ctx = ap.Context.instance()

project = aps.get_project(ctx.path)
meta = project.get_metadata()

KEYFRAME_DEFAULT = "C:/PROGRA~1/KEYFRA~1"

settings = aps.Settings(name="keyframe")

if not settings.contains("keyframe_root"):
    settings.set("keyframe_root", KEYFRAME_DEFAULT)
    settings.store()


def create_dialog():
    dialog = ap.Dialog()

    dialog.title = "Keyframe Settings"

    dialog.add_text("Install Folder").add_input(
        default=settings.get("keyframe_root"),
        placeholder="path/to/keyframe/directory",
        var="keyframe_root",
        browse=ap.BrowseType.Folder,
        browse_path=settings.get("keyframe_root"),
        width=500,
    )

    dialog.add_info(text="Keyframe installation directory")

    dialog.add_button("Apply", press_apply)

    dialog.show()


def press_apply(dialog):
    maya_root = dialog.get_value("keyframe_root")

    settings = aps.Settings(name="keyframe")
    settings.set("keyframe_root", maya_root)

    settings.store()

    ui.show_success("Keyframe", "Update Keyframe settings successfully.")

    dialog.close()


create_dialog()
