import codecs
import re


class MatchSticks:
    def __init__(self, strings):
        self.strings_raw = strings
        self.strings_list = strings.split("\n")
        self.total_length_raw = 0
        self.total_length_decoded = 0
        self.total_length_escaped = 0

    @property
    def get_strings_list(self):
        return self.strings_list

    @property
    def get_total_length_raw(self):
        return self.total_length_raw

    @property
    def get_total_length_decoded(self):
        return self.total_length_decoded

    @property
    def get_total_length_escaped(self):
        return self.total_length_escaped

    def calculate_string_lengths(self):
        for string in self.strings_list:
            self.total_length_raw += len(string)
            self.total_length_decoded += len(codecs.escape_decode(string[1:-1])[0])
            escaped_string = self.calculate_escaped_length(string)
            self.total_length_escaped += len(escaped_string)
            # print(f"Raw: {len(string)}, {string}")
            # print(f"Act: {len(codecs.escape_decode(string[1:-1])[0])}")
            # print(f"Esc: {len(escaped_string)}, {escaped_string}\n")
        return self

    def calculate_escaped_length(self, string):
        string = re.sub(r"\\", r"\\\\", string)
        string = re.sub(r'"', r'\\"', string)
        string = '"' + string + '"'
        return string


if __name__ == "__main__":
    with codecs.open("./input.txt", "r") as data:
        input_strings = data.read()

    ms = MatchSticks(input_strings)

    print(ms.get_strings_list[2])

    ms.calculate_string_lengths()
    print(f"Total raw length of strings is: {ms.get_total_length_raw}")
    print(f"Total decoded length of strings is: {ms.get_total_length_decoded}")
    print(f"Total escaped length of strings is: {ms.get_total_length_escaped}")
    print(
        f"Part 01 answers is: {ms.get_total_length_raw - ms.get_total_length_decoded}"
    )

    print(
        f"Part 02 answers is: {ms.get_total_length_escaped - ms.get_total_length_raw}"
    )

