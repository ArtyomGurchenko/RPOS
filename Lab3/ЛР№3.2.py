import sys

def process_config_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if not line.startswith('!'):
                    print(line.strip())
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Using python script.py config_sw1.txt")
    else:
        process_config_file(sys.argv[1])