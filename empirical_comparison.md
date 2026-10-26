# Empirical Comparison

I used coins [1, 2, 5] and timed each function while making change for 11, 16, and 21. The table shows the average time for one run in milliseconds.

| Amount | Recursive (ms) | Memoized (ms) | Bottom-up (ms) |
| ---: | ---: | ---: | ---: |
| 11 | 0.2882 | 0.0132 | 0.0065 |
| 16 | 6.1051 | 0.0162 | 0.0079 |
| 21 | 94.7320 | 0.0312 | 0.0153 |

The plain recursive method became much slower as the amount increased because it repeats the same work. Memoization and bottom-up dynamic programming reuse earlier answers, so they stayed fast. Bottom-up was fastest in this small test.
