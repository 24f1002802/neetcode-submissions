class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        st = []
        for a in asteroids:
            alive = True

            while st and st[-1] > 0 and a < 0:
                if st[-1] < abs(a):
                    st.pop()

                elif st[-1] == abs(a):
                    st.pop()
                    alive = False
                    break

                else:
                    alive = False
                    break

            if alive:
                st.append(a)

        return st