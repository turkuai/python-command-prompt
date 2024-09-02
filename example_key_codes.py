import prompt

prompt.clear()

size = prompt.size()
center = { 
    "line": int(size.lines / 2),
    "column": int(size.columns / 2)
}

output = ""
line = center["line"]
column = None

key = -1

# Press ESC to end the loop
while key != 27:

    key = prompt.read()

    # Clear the previous code(s) from the screen
    if output:
        prompt.write(" " * len(output), line, column)

    output = ""

    # When special keys like arrow or functional keys are pressed,
    # a second code must be read to identify the key pressed.
    if key == 0 or key == 224:
        output += str(key) + " "

        key = prompt.read()

    output += str(key)
    column = center["column"] - int(len(output) / 2)

    prompt.write(output, line, column)
