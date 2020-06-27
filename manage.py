import sys
import dataconn
dataConn = dataconn.DataConn('demo.db')
def add_user_prog(argv):
    if len(argv) != 4:
        print("add-user [username] [password]")
        return
    username = argv[2]
    password = argv[3]
    dataConn.add_user(username, password)

def set_password_prog(argv):
    if len(argv) != 4:
        print("set-password [username] [password]")
        return
    username = argv[2]
    password = argv[3]
    dataConn.update_user_password(username, password)

def print_help_prog():
    print("Virtual Orchard Manager")
    print("  add-user [username] [password]")
    print("  set-password [username] [new password]")

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print_help_prog()
        exit(0)
    program_name = argv[1]

    if program_name == "add-user":
        add_user_prog(argv)
        exit(0)    
    elif program_name == "set-password":
        set_password_prog(argv)
        exit(0)
    else:
        print_help_prog()

