import os

def scan_previous_code(folder):

    report = []

    if not os.path.exists(folder):
        return report

    for file in os.listdir(folder):

        if file.endswith(".py"):

            path = os.path.join(folder,file)

            with open(path,"r") as f:
                code = f.read()

            report.append({
                "file":file,
                "lines":len(code.splitlines()),
                "functions":code.count("def ")
            })

    return report