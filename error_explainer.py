def explain_error(error):
    error_type = type(error).__name__
    message = str(error)

    if error_type == "SyntaxError":
        return (
            "I found a syntax error in your program. "
            "This usually happens when brackets, quotes, or colons are missing. "
            "Please carefully check the line where the error occurred."
        )

    elif error_type == "NameError":
        return (
            "You are using a variable that has not been defined yet. "
            "Please make sure the variable is created before you use it."
        )

    elif error_type == "ZeroDivisionError":
        return (
            "You attempted to divide a number by zero. "
            "In mathematics, division by zero is not allowed."
        )

    elif error_type == "IndentationError":
        return (
            "There is an indentation mistake in your program. "
            "Python uses spaces to define code blocks, so please fix the alignment."
        )

    else:
        return f"I found an error in your program: {message}"