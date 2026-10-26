"""Coin change functions and a simple timing comparison."""

from math import inf
from time import perf_counter


def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    best = inf
    for coin in coins:
        answer = coin_change_recursive(coins, amount - coin)
        if answer != -1:
            best = min(best, answer + 1)
    return -1 if best == inf else best


def coin_change_memoized(coins, amount, memo=None):
    if memo is None:
        memo = {}
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in memo:
        return memo[amount]
    best = inf
    for coin in coins:
        answer = coin_change_memoized(coins, amount - coin, memo)
        if answer != -1:
            best = min(best, answer + 1)
    memo[amount] = -1 if best == inf else best
    return memo[amount]


def coin_change_dp(coins, amount):
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)
    return -1 if dp[amount] == inf else dp[amount]


def compare_times(coins, amounts):
    """Print a simple timing comparison in milliseconds."""
    methods = [
        ("Recursive", coin_change_recursive),
        ("Memoized", lambda c, a: coin_change_memoized(c, a, {})),
        ("Bottom-up", coin_change_dp),
    ]
    for amount in amounts:
        print(f"\nAmount: {amount}")
        for name, function in methods:
            start = perf_counter()
            answer = function(coins, amount)
            elapsed_ms = (perf_counter() - start) * 1000
            print(f"{name}: {elapsed_ms:.4f} ms (answer: {answer})")


if __name__ == "__main__":
    compare_times([1, 2, 5], [11, 16, 21])
