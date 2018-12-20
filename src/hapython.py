import sys
import codecs

GENERAL = {"הדפס": "print", "טווח": "range"}
CONDITIONS = {"אחרת אם": "elif", "אחרת": "else", "אם": "if", "וגם": "and", "או": "or"}
LOOPS = {"עבור": "for", "בתוך": "in", "כל עוד": "while", "המשך": "continue", "עצור": "break"}
FUNCTIONS = {"הגדר": "def", "החזר": "return"}

PARSING = [GENERAL, CONDITIONS, LOOPS, FUNCTIONS]


def replace_part(part):
    for parsing in PARSING:
        for command in parsing.items():
            part = part.replace(command[0], command[1])
    return part


def find_quote_start(code, search_from=0):
    single_quote = code.find("'", search_from)
    double_quote = code.find('"', search_from)
    if single_quote == -1:
        return double_quote
    if double_quote == -1:
        return single_quote
    return min(single_quote, double_quote)


def parse_code(code):
    parsed_code = ""
    quote_end = 0
    prev_quote_end = 0

    # TODO this is bad
    quote_start = find_quote_start(code)
    while quote_start > -1:
        quote_type = code[quote_start]
        quote_end = code.find(quote_type, quote_start + 1)
        while quote_end != -1 and code[quote_end - 1] == "\\":
            quote_end = code.find(quote_type, quote_end + 1)
        if quote_end == -1:
            quote_end = len(code) - 1
        part = code[prev_quote_end:quote_start]
        parsed_code += replace_part(part)
        parsed_code += code[quote_start:quote_end]
        prev_quote_end = quote_end
        quote_start = find_quote_start(code, quote_end + 1)

    part = code[quote_end:]
    parsed_code += replace_part(part)
    return parsed_code


def execute_code(code):
    exec(code)


def main():
    if len(sys.argv) != 2:
        print("שימוש: %s <קובץ הפייתון>" % sys.argv[0])
        exit(1)
    # TODO add missing file error handling
    # TODO Add encoding detection?
    code = codecs.open(sys.argv[1], "r", encoding="utf-8").read()
    parsed_code = parse_code(code)
    execute_code(parsed_code)


if __name__ == "__main__":
    main()
