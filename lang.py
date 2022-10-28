from sys import *

vars = {}

def open_file(fileName):
    data = open(fileName, "r").read()
    data = data.replace("\n","")
    data = data.split(";")
    data = data[:-1]
    return data

def parse(fileContents):
    for i in fileContents:
        if i[0:5] == "print":
            error = True
            text = i.replace("print ", "")
            text = text.replace(r"\n", "\n")
            quotes = []
            spaces = []
            for j in range(len(text)):
                if text[j] == "\"":
                    quotes.append(j)
                if text[j] == " ":
                    spaces.append(j)
            
            if len(quotes) == 0:
                for i in vars:
                    if i == text:
                        print(vars[i], end="")
                        error = False
            else:
                print(text[quotes[0]+1:quotes[1]], end="")
                error = False

            if error == True:
                raise Exception(f"'{text}' Is Not Defined.")

        elif i[0:3] == "var":
            var = i.replace("var", "")
            equals = var.index("=")
            if "\"" in var:
                firstQuote = var.index("\"")
                varValue = var[firstQuote+1:-1]
            else:
                varValue = var[equals+2:]
                if varValue == "input":
                    varValue = input()
                elif "eval" in varValue:
                    math_str = varValue.split(" ")[1]
                    for i in vars:
                        math_str.replace(i, vars[i])
                    varValue = eval(math_str)
                else:
                    raise Exception(f"'{varValue}' Is Not Defined.")

            varName = var[:equals].replace(" ", "")

            vars[varName] = varValue

def run(file):
    data = open_file(file)
    parse(data)