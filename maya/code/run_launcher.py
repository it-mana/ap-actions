import anchorpoint as ap
import apsync as aps

import os
import subprocess

# get context and metadata
ui = ap.UI()
ctx = ap.Context.instance()
project = aps.get_project(ctx.path)


settings = aps.Settings(name="maya")


def run_maya():

    # maya settings
    exe = settings.get("maya_root") + "/bin/maya.exe"

    # launch maya
    store_sys = os.getenv("PYTHONPATH")
    # res_env = []
    # for x in os.getenv("PYTHONPATH").split(os.pathsep):
    #     print(x)
    #     if "C:/Users/mike/AppData/Local/Anchorpoint/app-1.16.0/plugins/python" != x:
    #         res_env.append(x)
    os.environ["PYTHONPATH"] = ""
    # res_env = [
    #     "C:/Users/mike/AppData/Local/Anchorpoint/app-1.16.0/scripts",
    #     "C:/Users/mike/AppData/Roaming/Anchorpoint Software/Anchorpoint/python",
    #     "C:/Users/mike/AppData/Local/Anchorpoint/app-1.16.0/plugins/python",
    #     "C:/Users/mike/AppData/Local/Anchorpoint/app-1.16.0/plugins/python/Python39.zip",
    #     "C:/Users/mike/AppData/Local/Anchorpoint/app-1.16.0/plugins/python/Lib/",
    #     "C:/Users/mike/AppData/Local/Anchorpoint/app-1.16.0/plugins/python/Lib/lib-dynload",
    #     "C:/Users/mike/AppData/Local/Anchorpoint/app-1.16.0/plugins/python/Lib/site-packages",
    #     "C:/Users/mike/AppData/Local/Anchorpoint/app-1.16.0/plugins/python/DLLs/",
    # ]
    # os.environ["PYTHONPATH"] = ";".join(res_env)

    process = subprocess.Popen([exe, ctx.path])
    os.environ["PYTHONPATH"] = store_sys


run_maya()
