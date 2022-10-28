# Import Packages
import os
from math import *
from colorama import Fore, init, Style
import lang

init()

helpMenu = {
    "python": "python <FILE>",
    "carbon": "carbon <FILE>",
    "edit": "edit <FILE>",
    "create_file": "create_file <FILE>",
    "install": "install <PIP PACKAGE>",
    "create_folder": "create_folder <FOLDER>",
    "eval": "eval <PROBLEM>",
    "cd": "cd <PATH>",
    "clone_repo": "clone_repo <REPOSITORY>",
    "view_dir": "view_dir <PATH>",
    "color": "color <CODE>",
    "clone_file": "clone_file <FILE>",
}

# Init Console Function
def console():
    while True:
        try:
            cmd = input(f"{os.getcwd()} >>> ")
            if "python " in cmd:
                file = cmd.replace("python ", "")
                if file.endswith(".py"):
                    python(file)
                else:
                    print(f"{Fore.RED}FileTypeError: {file}{Style.RESET_ALL}")
            elif "carbon " in cmd:
                file = cmd.replace("carbon ", "")
                if file.endswith(".car"):
                    lang.run(file)
                    print("")
                else:
                    print(f"{Fore.RED}FileTypeError: {file}{Style.RESET_ALL}")
            elif "help" in cmd:
                help()
            elif "color " in cmd:
                _color = cmd.replace("color ", "")
                color(_color)
            elif "edit " in cmd:
                file = cmd.replace("edit ", "")
                edit(file)
            elif "create_file " in cmd: 
                file = cmd.replace("create_file ", "")
                create(file)
            elif "install " in cmd:
                package = cmd.replace("install ", "")
                install(package)
            elif "create_folder " in cmd:
                folder = cmd.replace("create_folder ", "")
                create_folder(folder)
            elif "eval " in cmd:
                inp = cmd.replace("eval ", "")
                print(evaluate(inp))
            elif "view_dir " in cmd:
                folder = cmd.replace("view_dir ", "")
                view_dir(folder)
            elif "clone_repo " in cmd:
                repo = cmd.replace("clone_repo ", "")
                clone_repo(repo)
            elif "cd " in cmd:
                dir = cmd.replace("cd ", "")
                cd(dir)
            elif "clone_file " in cmd:
                file = cmd.replace("clone_file ", "")
                new_file = input("What Is The Name Of This File? ")
                clone_file(file, new_file)
            else:
                print(f"{Fore.RED} SYNTAX ERROR: Could Not Find The Command {cmd}.")
                print(Style.RESET_ALL, end = "")
        except SyntaxError:
            print(f"{Fore.RED}SyntaxError: {cmd}{Style.RESET_ALL}")
        except NameError:
            print(f"{Fore.RED}NameError: {cmd}{Style.RESET_ALL}")
        except FileNotFoundError:
            print(f"{Fore.RED}FileNotFoundError: {cmd}{Style.RESET_ALL}")
            
# Init Python Function
def python(file):
    exec(open(file).read())

# Init Cd Function
def cd(dir):
    os.chdir(dir)
    print(f"Successfully Changed Directory To {dir}.")

# Init Create Folder Function
def create_folder(folder):
    os.mkdir(folder)
    print(f"Successfully Created Folder {folder}.")

# Init Clone File Function
def clone_file(file, new_file):
    with open(file, "r") as f:
        data = f.read()

    with open(new_file, "w") as f:
        f.write(data)

    print(f"Successfully Cloned File {file}.")

# Init Clone Repo Function
def clone_repo(repo):
    os.system(f"git clone {repo}")
    print("Successfully Cloned Repository.")

def color(color):
    os.system(f'color {color}')
    print(f"Successfully Changed Color.")

# Init View Dir Function
def view_dir(folder):
    for i in os.listdir(folder):
        print(f" - {i}")

# Init Install Function
def install(package):
    os.system(f"pip install {package}")

# Init Help Function
def help():
    for i in helpMenu:
        print(f"{i} : {helpMenu[i]}")

# Init Create Function
def create(file):
    with open(file, "w") as f:
        pass

    print(f"Successfully Created File {file}.")

# Init Eval Function
def evaluate(inp):
    if " " not in inp:
        return eval(inp)
    else:
        return f"{Fore.RED}EvalSpaceError: {inp}. This Is An Error To Prevent Malicious Code From Executing.{Style.RESET_ALL}"

# Init Edit Function
def edit(file):
    with open(file, "r") as f:
        data = f.readlines()

    for i in data:
        print(i.strip())

    isEditing = True
    while isEditing:
        with open(file, "r") as f:
            data = f.readlines()

        cmd = input(f"Editing {file} >>> ")

        # Check For Commands And Run Commands
        if "$line " in cmd:
            line = int(cmd.replace("$line", "").split(" ")[1])
            rawtext = cmd.replace(f"{str(line)} ", "").replace("$line ", "")
            text = ""

            for i in rawtext:
                text += i

            data[line] = f"{text}\n"

            with open(file, "w") as f:
                f.writelines(data)
        elif "$view" == cmd:
            for i in data:
                print(i.strip())
        elif "$stop" == cmd:
            isEditing = False
        else:
            with open(file, "a") as f:
                f.write(f"{cmd}\n")

# Init Boot Function
def boot():
    print("""
░█████╗░░█████╗░██████╗░██████╗░░█████╗░███╗░░██╗  ░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░██║  ██╔══██╗██╔════╝
██║░░╚═╝███████║██████╔╝██████╦╝██║░░██║██╔██╗██║  ██║░░██║╚█████╗░
██║░░██╗██╔══██║██╔══██╗██╔══██╗██║░░██║██║╚████║  ██║░░██║░╚═══██╗
╚█████╔╝██║░░██║██║░░██║██████╦╝╚█████╔╝██║░╚███║  ╚█████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝  ░╚════╝░╚═════╝░
Is Now Booting Up...
                            Sulfur Tech.
                            2022
    """)

boot()
console()