import shlex
import re

def parse(content):
    """
    Parse the content of a .env file (a line-delimited KEY=value format) into a
    dictionary mapping keys to values.
    """
    values = {}
    for line in content.splitlines():
        lexer = shlex.shlex(line, posix=True)
        tokens = list(lexer)

        # parses the assignment statement
        if len(tokens) < 3:
            continue

        name, op = tokens[:2]
        value = ''.join(tokens[2:])

        if op != '=':
            continue
        if not re.match(r'[A-Za-z_][A-Za-z_0-9]*', name):
            continue

        value = value.replace(r'\n', '\n')
        value = value.replace(r'\t', '\t')
        values[name] = value

    return values
