from glob import glob

def get_all_lines(path):
    files = glob(path+"*")
    all_lines = []
    for i in files:
        with open(i,"rt") as reader:
            all_lines += reader.readlines()
    return all_lines

def get_line_number(lines):
    return len(lines)

def get_char_number(lines):
    total_length = 0
    for i in lines:
        total_length += len(i)
    return total_length
        
def main():
    path = "E:/macos_backup/soft_lpcm/local-explorer-tools/src/"
    lines = get_all_lines(path)
    print("Number of lines :", get_line_number(lines))
    print("Number of characters :", get_char_number(lines))

main()