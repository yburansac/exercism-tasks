def rows(letter):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alpha_position = alphabet.index(letter)

    size = 2 * alpha_position + 1
    half_size = size // 2
    result = []

    for i in range(size): # rows
        # 0 → 1 → 2 → 3 → 4 → 3 → 2 → 1 → 0
        # A → B → C → D → E → D → C → B → A
        level = min(i, size - 1 - i)
        letter_to_write = chr(65 + level)

        row = ""
        for j in range(size):  # columns
            if j == half_size - level or j == half_size + level:
                row += letter_to_write
            else:
                row += " "
        result.append(row)
                
    return result