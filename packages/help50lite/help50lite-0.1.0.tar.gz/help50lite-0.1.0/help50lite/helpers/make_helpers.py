import re
from help50lite.registry import helper


@helper("make")
def no_rule_to_make(lines):
    matches = re.search(r"No rule to make target '(.+)'.", lines[0])

    if not matches:
        return
    target = matches.group(1)
    return lines[0:1], [f"Do you actually have a file called `{target}.c`?"]


@helper("make")
def no_target_specified(lines):
    if "No targets specified and no makefile found" not in lines[0]:
        return

    response = ["You don't seem to have a `Makefile`?",
                "Or did you mean to execute, say, `make foo` instead of just `make`, whereby `foo.c` contains a program "
                "you'd like to compile?"]
    return lines[:1], response


@helper("make")
def nothing_to_be_done(lines):
    text = lines[0]
    if "Nothing to be done for" not in text:
        return

    target = text.split("for")[1].strip(" `'.c")

    response = [
        f"Try compiling your program with `make {target}` instead of `make {target}.c`."
    ]
    return lines[:1], response
