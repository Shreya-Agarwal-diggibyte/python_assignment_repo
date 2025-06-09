def print_formatted(number):
    width = len(bin(number)) - 2  # Calculate the width based on the binary representation
    lines = []

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]


        lines.append(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

    return "\n".join(lines)
