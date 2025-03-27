import subprocess

def compile_and_run(code, lang="python"):
    filename = "temp.py" if lang == "python" else "temp.cpp"
    
    with open(filename, "w") as f:
        f.write(code)

    if lang == "python":
        subprocess.run(["python", filename])  
    elif lang == "cpp":
        subprocess.run(["g++", filename, "-o", "output"])
        subprocess.run(["./output"])  

if __name__ == "__main__":
    test_code = """print("Hello, Compiler!")"""
    compile_and_run(test_code, lang="python")
