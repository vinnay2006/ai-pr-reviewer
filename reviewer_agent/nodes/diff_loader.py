def diff_loader(state):

    with open("sample_diffs/security.diff","r") as f:
        diff = f.read()

    return {
        "diff": diff
    }