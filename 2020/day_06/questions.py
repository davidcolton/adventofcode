from collections import Counter


def total_yes_answers(input):
    questions_list = [l.replace("\n", "").strip().split() for l in input.split("\n\n")]
    answers_counters = [Counter(l[0]) for l in questions_list]
    return sum([len(c) for c in answers_counters])


def everyone_answered_yes(input):
    questions_list = [l.replace("\n", " ").strip().split() for l in input.split("\n\n")]
    answers_sets = [[set(person) for person in group] for group in questions_list]
    return sum(len(answers[0].intersection(*answers)) for answers in answers_sets)


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 04: A simple list
    # Split on \n\n and then strip \n
    with open("input") as f:
        input = f.read()

    print(f"Total number of Questions answered YES: {total_yes_answers(input)}")
    print(
        f"Total number of Questions everyone answered YES: {everyone_answered_yes(input)}"
    )
