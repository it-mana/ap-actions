import anchorpoint as ap
import apsync as aps

import subprocess
import sys

from keyframe_pro.keyframe_pro_client import KeyframeProClient

ctx = ap.get_context()
# api = ap.get_api()
settings = aps.Settings(name="keyframe")

selected_files = ctx.selected_files

exe = settings.get("keyframe_root") + "/bin/KeyframePro.exe"

# launch houdini
process = subprocess.Popen([exe])

kpro_client = KeyframeProClient()

if kpro_client.connect() and kpro_client.initialize():
    kpro_client.new_project(empty=True)

    paths = selected_files
    # Import sources
    sources = []
    for path in paths:
        sources.append(kpro_client.import_file(path))

    for index, source in enumerate(sources):
        kpro_client.set_active_in_viewer(source["id"], index)

    kpro_client.set_viewer_layout(layout="horizontal")


# # To quickly create a task (and a task list) call
# task = api.tasks.create_task(ctx.path, "Todo List", "Create Rig")

# # You can access a task list by name
# tasklist = api.tasks.get_task_list(ctx.path, "Todo List")

# # And get all tasks
# all_tasks = api.tasks.get_tasks(tasklist)
# for task in all_tasks:
#     print(f"Task: {task.name}")

# # Set an icon for the task. To get the path of an icon right click the icon in the icon picker
# api.tasks.set_task_icon(task, aps.Icon("qrc:/icons/multimedia/setting.svg", "blue"))

# # Set a status on the task
# api.attributes.set_attribute_value(task, "Status", aps.AttributeTag("Done", "green"))


# ui = ap.UI()
# ui.show_success("Tasks created")
