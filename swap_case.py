def swap_case(s):
    ans = []
    for st in s:
        if st.isalpha():
            if st.isupper():
                ans.append(st.lower())
            else:
                ans.append(st.upper())
            continue
        ans.append(st)
    return "".join(ans)

if __name__ == '__main__':
