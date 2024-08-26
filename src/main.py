import argparse

def main():
    parser = argparse.ArgumentParser(description="My CLI Tool")
    parser.add_argument('command', help="The command to execute")
    args = parser.parse_args()

    if args.command == 'greet':
        print("Hello, World!")
    elif args.command == 'how':
        print("fine ! what about you?")    
    else :
        print("Unknown command")
if __name__ == "__main__":
    main()
