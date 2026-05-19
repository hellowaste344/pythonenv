def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        sequence.append(a)
if __name__ == "__main__":
    sequence = []
    fibonacci()
    print(sequence, end='\t')