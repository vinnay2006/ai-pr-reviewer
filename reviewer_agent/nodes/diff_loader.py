def diff_loader(state):
    sample_diff = """
- const user = getUser(id);
+ const user = getUser(id);
+ console.log(user.password);
"""

    return {
        "diff": sample_diff
    }