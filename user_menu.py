def main_menu(cur_db: str, db_dict: dict):
    while True:
        print("Input command or 'help'")
        choice = input(">>> ")
        match choice:
            case 'help':
                print('''
                Commands:
                <select_db> to choose dataset for analysis
                <show_info> to show general information of chosen data
                <exit> to end program
                ''')
            case 'select_db':
                datasets = list(db_dict.keys())
                print('Dataset list:\n')
                for i, name in enumerate(datasets):
                    print(f'{i} {datasets[i]}')
                cur_db = datasets[int(input('Input dataset number: '))]
                cur_df = db_dict[cur_db]['obj']
            case 'show_info':
                print(db_dict[cur_db])
                print(cur_db)
                print(cur_df.head())
                print("Table shape:", cur_df.shape, sep='\n')
                print("Table info:")
                cur_df.info()
                print("Total missing values:", cur_df.isna().sum().sum())
            case 'exit':
                print("End work")
                break
            case _:
                print("Invalid input")