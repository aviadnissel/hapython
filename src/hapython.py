import sys
import codecs

PRINT = {"הדפס": "print"}
CONDITIONS = {"אחרת אם": "elif", "אחרת": "else", "אם": "if", "וגם": "and", "או": "or"}

PARSING = [PRINT, CONDITIONS]


def parse_code(code):
    # TODO Only repalce outside of ""
    parsed_code = []
    for line in code:
        for parsing in PARSING:
            for command in parsing.items():
                line = line.replace(command[0], command[1])
        parsed_code.append(line)
    return parsed_code


def execute_code(code):
    exec("\n".join(code))


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
