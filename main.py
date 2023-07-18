def row_wise_sums(matrix):
    sums = []
    for row in matrix:
        row_sum = sum(row)  # Calculate the sum of each row
        sums.append(row_sum)
    return sums
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row_values = list(map(int, input(f"Enter space-separated values for row {i + 1}: ").split()))
    matrix.append(row_values)
result = row_wise_sums(matrix)
print("Output:", result)
