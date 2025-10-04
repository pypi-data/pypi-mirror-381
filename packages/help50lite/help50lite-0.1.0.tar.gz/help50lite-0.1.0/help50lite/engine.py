import re
from help50lite.registry import HELPERS, PREPROCESSORS


def get_help(output, domain="make"):
    # Clean ANSI codes
    output = re.sub(r"\x1B\[[0-?]*[ -/]*[@-~]", "", output)

    # Run preprocessors
    for pre in PREPROCESSORS.get(domain, []):
        output = pre(output)

    lines = output.splitlines()
    for i in range(len(lines)):
        slice_ = lines[i:]
        for helper in HELPERS.get(domain, []):
            result = helper(slice_)
            if result:
                return result
    return None
