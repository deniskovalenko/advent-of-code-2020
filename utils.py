

def read_input_lines(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    return content