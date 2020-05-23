import string
from itertools import groupby


class NewPassword:
    def __init__(self, old_password, excluded_letters=["i", "l", "o"]) -> None:
        self.old_password = old_password
        self.excluded_letters = excluded_letters
        self.available_letters = "".join(
            c for c in string.ascii_lowercase if c not in self.excluded_letters
        )

    def add_letter(self, passwd, num_letters=1):
        passwd_reversed = passwd[::-1]
        new_password_reversed = []
        for idx, char in enumerate(passwd_reversed):

            if self.available_letters.index(char) + 1 < len(self.available_letters):
                new_password_reversed.append(
                    self.available_letters[self.available_letters.index(char) + 1]
                )
                new_password_reversed.extend(passwd_reversed[idx + 1 :])
                break
            else:
                new_password_reversed.append(self.available_letters[0])

        return "".join(new_password_reversed[::-1])

    def three_straight_test(self, password):
        # Pass word should contain three straight letters
        # Generate the list of valid 3 straight letters
        three_straight_letters = [
            self.available_letters[idx : idx + 3]
            for idx, _ in enumerate(self.available_letters)
            if idx + 2 < len(self.available_letters)
        ]

        # Same list for the password
        three_straight_password = [
            password[idx : idx + 3]
            for idx, _ in enumerate(password)
            if idx + 2 < len(password)
        ]

        # Valid if any three letter combo from password in list
        return any(
            [three in three_straight_letters for three in three_straight_password]
        )

    def pairs_test(self, password):
        valid_password = False
        letter_groups = [(len(list(g)), list(k)) for k, g in groupby(password)]
        two_letter_groups = [grp for grp in letter_groups if grp[0] == 2]

        # Test pairs are valid
        if (
            len(two_letter_groups) == 2
            and two_letter_groups[0][1] != two_letter_groups[1][1]
        ):
            valid_password = True

        return valid_password

    def new_password(self):
        valid_password = False
        password = self.old_password
        while not valid_password:
            password = self.add_letter(password)
            if self.three_straight_test(password) and self.pairs_test(password):
                valid_password = True
        return password


np = NewPassword("vzbxxyzz")
print(f"Old Password: {np.old_password}")
print(f"New Password: {np.new_password()}")
