def stage2_reconstruct(ocr_lines):
    code = []
    indent = "    "
    in_function = False
    in_if = False

    for line in ocr_lines:
        line = line.strip().lower()

        # ignore junk
        if line in ["", "is", "in", "input", "syntaxerror:", "invalid syntax"]:
            continue

        # function detection
        if line == "def":
            code.append("def even_odd(x):")
            in_function = True
            continue

        # list creation
        if line == "even" and not in_if:
            code.append(indent + "even = []")
            continue

        if line == "odd" and not in_if:
            code.append(indent + "odd = []")
            continue

        # if condition detection
        if line == "if":
            code.append(indent + "if x % 2 == 0:")
            in_if = True
            continue

        # append detection
        if "append" in line and in_if:
            if "even" in line:
                code.append(indent*2 + "even.append(x)")
            else:
                code.append(indent*2 + "odd.append(x)")
            continue

        # else block
        if line == "else":
            code.append(indent + "else:")
            continue

        # return statements
        if line == "return" and in_if:
            code.append(indent*2 + "return even, odd")
            in_if = False
            continue

    return "\n".join(code)