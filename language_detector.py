def detect_language(code):

    if "#include" in code or "cout" in code:
        return "cpp"

    elif "System.out.println" in code or "public class" in code:
        return "java"

    elif "print(" in code or "def " in code:
        return "python"

    else:
        return "unknown"