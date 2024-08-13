def get_matrix(m=3, n=4, value="val"):
    matrix = []
    if isinstance(m, int) and isinstance(n, int):
        for columns in range(m):
            row = []
            for rows in range(n):
                row.append(value)
            matrix.append(row)
    return matrix


columns = input("Enter the number of columns: ")
rows = input("Enter the number of rows: ")
value = input("Enter the value: ")

if columns.isdigit() and rows.isdigit():
    matrix = get_matrix(int(rows), int(columns), value)
    print(matrix)
else:
    print("Invalid data")
