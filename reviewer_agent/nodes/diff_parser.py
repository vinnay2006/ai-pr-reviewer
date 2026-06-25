import re

def diff_parser(state):

    diff = state["diff"]

    files = re.findall(r"diff --git a/(.*?) b/", diff)

    # Build line map: {filename: [valid new-file line numbers]}
    line_map = {}
    current_file = None
    current_line = 0

    for raw_line in diff.splitlines():

        # new file starting
        file_match = re.match(r"diff --git a/(.*?) b/", raw_line)
        if file_match:
            current_file = file_match.group(1)
            line_map[current_file] = []
            current_line = 0
            continue

        # hunk header: @@ -old_start,old_count +new_start,new_count @@
        hunk_match = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@", raw_line)
        if hunk_match:
            current_line = int(hunk_match.group(1))
            continue

        if current_file is None:
            continue

        # added or context line — exists in new file
        if raw_line.startswith("+") and not raw_line.startswith("+++"):
            line_map[current_file].append(current_line)
            current_line += 1

        elif raw_line.startswith("-") and not raw_line.startswith("---"):
            # removed line — does not exist in new file, don't increment
            pass

        elif not raw_line.startswith("\\"):
            # context line
            current_line += 1

    return {
        "files_changed": files,
        "line_map": line_map
    }