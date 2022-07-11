import os
from funcs import time_op


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def write_time():
    print(f"{time_op.get_difference()} passed since last time.")
    time_op.store_current_time()
    print("time written")
    input("\n\nPress enter to continue...")
    main()


def double_check():
    print('\n'.join([
        "You are about to store current time",
    ]))
    proceed = prompt()
    if proceed:
        write_time()
    else:
        main()


def prompt() -> bool:
    try:
        c = input("Do you want to proceed? (y/[n]) ")
        if c.strip().lower() == 'y':
            return True
        elif c.strip().lower() == 'n':
            return False
        elif c == '':
            return False
        else:
            raise ValueError("Invalid input")
    except ValueError:
        print("Invalid input")
        return prompt()


def get_diff():
    print(time_op.get_difference())
    input("\n\nPress enter to continue...")
    main()


def main():
    clear()
    print("""Please select the operation:
    1 - store current time
    2 - get difference of time
    3 - exit""")
    try:
        c = input("Your choice [3]: ")
        c = 3 if c == '' else int(c)
        if c == 1:
            double_check()
        elif c == 2:
            get_diff()
        elif c == 3:
            exit()
        else:
            raise ValueError("Invalid input")
    except ValueError:
        print("Invalid input")
        main()


def debug():
    time_op.store_current_time()


if __name__ == '__main__':
    main()
