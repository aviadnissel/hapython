import sys
import codecs

PRINT = {"הדפס": "print"}

PARSING = [PRINT]


def parse_code(code):
    parsed_code = []
    for line in code:
        for parsing in PARSING:
            for command in parsing.items():
                line = line.replace(command[0], command[1])
        parsed_code.append(line)
    return parsed_code


def execute_code(code):
    for line in code:
        exec(line)


def main():
    if len(sys.argv) != 2:
        print("שימוש: %s <קובץ הפייתון>" % sys.argv[0])
        exit(1)
    # TODO add missing file error handling
    # TODO Add encoding detection?
    code = codecs.open(sys.argv[1], "r", encoding="utf-8").readlines()
    parsed_code = parse_code(code)
    execute_code(parsed_code)


if __name__ == "__main__":
    main()