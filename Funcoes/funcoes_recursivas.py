def fatorial(n: int) -> int:
    #Caso base
    if n == 1:
        return 1
    return n * fatorial(n - 1)


if __name__ == "__main__":
    fat5 = fatorial(5)

    print(fat5)