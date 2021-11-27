# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from gooey import Gooey,GooeyParser

def hello(name):
    # Use a breakpoint in the code line below to debug your script.
    return f'Hi, {name}'  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
@Gooey(program_name='Hello app')
def main():
    parser = GooeyParser(description="GUI Hello Program")
    parser.add_argument('name',help="Please enter your real name")
    args = parser.parse_args()
    print(hello(args.name))

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
