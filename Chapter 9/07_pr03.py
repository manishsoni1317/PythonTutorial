for i in range(2, 20):
    table = ""
    for j in range(1, 11):
        table += f"{i} x {j} = {i*j}\n"
    with open(f"tables/table_of_{i}.txt", "w") as f:
        f.write(table)