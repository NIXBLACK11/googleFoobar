def compute_generations(m, f, ans):
    if m == 1 and f == 1:
        return str(ans)
    elif m < 1 or f < 1 or m == f:
        return "impossible"
    elif m == 1 or f == 1:
        return str(ans + f * m - 1)
    elif m > f:
        temp = int(m/f)
        return compute_generations(m-f*temp, f, ans+temp)
    elif m < f:
        temp = int(f/m)
        return compute_generations(m, f-m*temp, ans+temp)

def solution(x, y):
    return compute_generations(int(x), int(y), 0)
