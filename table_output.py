def print_table(columns, rows):
    if not isinstance(columns, list):
        columns = list(columns)
    table = PrettyTable()
    table.field_names = columns
    table.add_rows(rows)
    print(table)

def print_selected_columns(data, columns, rows=5): #
    indices = []
    for i, column in enumerate(data.columns):
        if column in columns:
            indices.append(i)
    rows_data = data.head(rows).values.tolist()
    selected_rows = [[row[i] for i in indices] for row in rows_data]
    print_table(columns, selected_rows)