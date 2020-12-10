from collections import Counter


def joltage_differences(input):
    # Start with a 0 value and add the sorted adaptors
    sorted_adapters = [0] + sorted(input)
    # Add the final adaptor rated value ... max + 3
    sorted_adapters.append(max(sorted_adapters) + 3)
    differences = [
        sorted_adapters[i] - sorted_adapters[i - 1]
        for i in range(1, len(sorted_adapters))
    ]
    differences_counter = Counter(differences)
    return differences_counter[1] * differences_counter[3]


def count_combinations(input):
    # Start with a 0 value and add the sorted adaptors
    sorted_adapters = [0] + sorted(input)
    # Add the final adaptor rated value ... max + 3
    sorted_adapters.append(max(sorted_adapters) + 3)

    dp = [1]
    for i in range(1, len(sorted_adapters)):
        ans = 0
        for j in range(i):
            if sorted_adapters[j] + 3 >= sorted_adapters[i]:
                ans += dp[j]
        dp.append(ans)
    return dp[-1]


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 10: Just read text in split into list of lines,
    with open("input") as f:
        input = [int(n) for n in f.read().splitlines()]

    print(joltage_differences(input))
    print(count_combinations(input))