class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = "+*-/"
        st = []

        for i in tokens:
            if i in s:
                b = st.pop()
                a = st.pop()
                
                if i == "+":
                    st.append(a+b)
                elif i == "-":
                    st.append(a-b)
                elif i == "*":
                    st.append(a*b)
                elif i == "/":
                    st.append(int(a/b))

            else:
                st.append(int(i))
        return st[-1]