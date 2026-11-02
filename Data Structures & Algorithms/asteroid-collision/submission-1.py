class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        st = []
        for a in asteroids:
            if not st:
                st.append(a)

            else:
                if a<0 and st[-1] > 0:  # collide
                    while st and st[-1] > 0 and st[-1] < abs(a):
                        st.pop()

                    if not st or st[-1]<0:
                        st.append(a)
                    elif st[-1] == abs(a):
                        st.pop()
                else:
                    st.append(a)
        return st
