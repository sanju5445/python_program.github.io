matrix=[]
cln=int(input("enter the no of Row: "))
ron=int(input("enter the no of Column: "))
print("enter the elements row wise:")
for i in range(ron):
    a=[]
    for j in range(cln):
        a.append(int(input()))
    matrix.append(a)

# to print the matrix
for i in range(ron):
    for j in range(cln):
        print(matrix[i][j], end=" ")











        # n_rows = int(input("Number of rows:"))
        # print("n_rows => ", n_rows)
        # n_columns = int(input("Number of columns:"))
        # print("n_columns => ", n_columns)
        #
        # # Define the matrix
        #
        # matrix = []
        #
        # print("Enter the entries row-wise:")
        #
        # # for user input
        #
        # for i in range(n_rows):  # A for loop for row entries
        #
        #     a = []
        #
        #     for j in range(n_columns):  # A for loop for column entries
        #
        #         a.append(int(input()))
        #
        #     matrix.append(a)
        #
        # # To print the matrix
        #
        # for i in range(n_rows):
        #
        #     for j in range(n_columns):
        #         print(matrix[i][j], end=" ")
        #
        #     print()