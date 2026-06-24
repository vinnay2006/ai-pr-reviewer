import re

def diff_parser(state):

    diff = state["diff"]

    files = re.findall(
        r"diff --git a/(.*?) b/",
        diff
    )

    return {
        "files_changed": files
    }