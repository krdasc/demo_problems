# sample problem: eight queens puzzle, backtracking solution

def n_queens(n: int):
    def f(queens: list, xy_dif: list, xy_sum: list):
        p = len(queens)
        if p == n:
            result.append(queens)
            return
        for q in range(n):
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                f(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

    result = []
    f([], [], [])
    return result
