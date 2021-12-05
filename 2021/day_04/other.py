def check_columns(board):
    for c in range(len(board[0])):
        if set(
            [False if list(row.values())[c] == False else True for row in board]
        ) == set([True]):
            return True
    return False


def check_rows(board):
    for row in board:
        if list(row.values()).count(True) == len(board[0]):
            return True
    return False


def record_number(num, board):
    for row in board:
        if str(num) in row.keys():
            row[str(num)] = True


def calc_result(num, board):
    return sum([int(k) for row in board for k, v in row.items() if v is False]) * int(
        num
    )


def is_board_solved(board: list[dict[str, bool]]):
    return check_columns(board) or check_rows(board)


def count_boards(boards):
    return sum([1 for b in boards if b is not None])


def first(numbers, all_boards):
    first_boards = [b for b in all_boards]
    for n in numbers:
        for board in first_boards:
            record_number(n, board)
            if is_board_solved(board):
                print(n, board)
                return calc_result(n, board)


def second(numbers, all_boards):
    second_boards = [b for b in all_boards]
    for n in numbers:
        for i, board in enumerate(second_boards):
            if board is None:
                continue
            record_number(n, board)
            if is_board_solved(board):
                if count_boards(second_boards) == 1:
                    return calc_result(n, board)
                second_boards[i] = None


all_boards = []
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    numbers = [n for n in data.pop(0).split(",")]
    del data[0]  # remove the blank line
    board = []
    for line in data:
        if line.strip() == "":
            all_boards.append(board)
            board = []
            continue
        board.append({e.strip(): False for e in line.split(" ") if e.strip()})


print(first(numbers, all_boards))
print(second(numbers, all_boards))
