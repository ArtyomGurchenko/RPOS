import sys

ignore = ['duplex', 'alias', 'Current configuration']

def should_ignore(line):
    for word in ignore:
        if word in line:
            return True
    return False

def process_config_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                if not should_ignore(line):
                    outfile.write(line)
    except FileNotFoundError:
        print(f"File {input_filename} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Using python script.py input_config.txt output_config.txt")
    else:
        process_config_file(sys.argv[1], sys.argv[2])