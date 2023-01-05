import textwrap
def wrap(string, max_width):
    n = len(string)
    idx = 0
    stack = []
    while idx < n:
        stack.append(string[idx: idx + max_width])
        idx += max_width  
    return "\n".join(stack)

if __name__ == '__main__':
