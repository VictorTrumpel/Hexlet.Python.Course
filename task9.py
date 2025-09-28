def Inverse(f1, f2):
    with open(f1, 'r', encoding='utf-8') as f:
        text = f.read()
    
    parts = text.split('\n')

    open(f2, 'w').close()

    def write_in_f2(parts, idx):
        if (idx < 0):
            return

        with open(f2, 'a', encoding='utf-8') as f:
            f.write(parts[idx])
            f.write("\n")

        write_in_f2(parts, idx - 1)

    write_in_f2(parts, len(parts) - 1)

Inverse("f1.txt", "f2.txt")