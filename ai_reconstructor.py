def reconstruct_code(lines):
    code = []
    indent = 0

    keywords_no_indent = ["def", "if", "else", "for", "while"]
    keywords_indent = ["return", "print", "append"]

    for line in lines:
        word = line.strip()

        if not word:
            continue

        # function definition
        if word == "def":
            indent = 0
            code.append("def function_name():")
            indent = 1
            continue

        # if condition
        if word == "if":
            code.append("    " * indent + "if condition:")
            indent += 1
            continue

        # else
        if word == "else":
            indent -= 1
            code.append("    " * indent + "else:")
            indent += 1
            continue

        # return or append
        if word in keywords_indent:
            code.append("    " * indent + word)
            continue

        # normal line
        code.append("    " * indent + word)

    return "\n".join(code)