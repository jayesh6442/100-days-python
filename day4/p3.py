# tragger game
row1 = ["☁️","☁️","☁️"]
row2 = ["☁️","☁️","☁️"]
row3 = ["☁️","☁️","☁️"]
final_map = [row1, row2, row3];
print(f"{row1}\n{row2}\n{row3}")
position = (input("Enter where you want to hide: "))
row_wise =int(position[0])
col_wise = int(position[1])
final_map[row_wise-1][col_wise-1]="X"
print(f"{row1}\n{row2}\n{row3}")