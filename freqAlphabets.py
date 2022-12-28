class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        a_i = "abcdefghi"
        j_z = "jklmnopqrstuvwxyz"
        ai_map = {str(i): x for i, x in enumerate(a_i, 1)}
        jz_map = {f"{i}#": x for i, x in enumerate(j_z, 10)}
        print(jz_map)
        for l in s:
            if l != "#":
                stack.append(l)
            else:
                i1 = stack.pop()
                i2 = stack.pop()
                i = i2 + i1 + "#"
                i = jz_map[i]
                stack.append(i)
        new_stack = []
        for st in stack:
            if st.isnumeric():
                new_val = ai_map[st]
                new_stack.append(new_val)
            else:
                new_stack.append(st)
        return "".join(new_stack)
