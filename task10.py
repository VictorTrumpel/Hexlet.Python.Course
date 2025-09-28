def hanoi(n, src, dst, aux):
    if n == 1:
        print(f"Переместить диск 1 со стержня {src} на стержень {dst}")
        return
    
    hanoi(n - 1, src, aux, dst)

    print(f"Переместить диск {n} со стержня {src} на стержень {dst}")

    hanoi(n - 1, aux, dst, src)

hanoi(3, "1", "3", "2")
