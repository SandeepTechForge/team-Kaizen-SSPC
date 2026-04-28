import subprocess

def execute_python(code):
    try:
        exec(code)
        return "success", ""
    except Exception as e:
        return "error", str(e)


def execute_cpp(code):
    with open("temp.cpp", "w") as f:
        f.write(code)

    compile_result = subprocess.run(
        ["g++", "temp.cpp", "-o", "temp"],
        capture_output=True,
        text=True
    )

    if compile_result.stderr:
        return "error", compile_result.stderr

    return "success", ""


def execute_java(code):
    with open("Temp.java", "w") as f:
        f.write(code)

    compile_result = subprocess.run(
        ["javac", "Temp.java"],
        capture_output=True,
        text=True
    )

    if compile_result.stderr:
        return "error", compile_result.stderr

    return "success", ""