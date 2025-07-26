def maxArea(self, height: List[int]) -> int:
        m_area=0
        l=len(height)
        i=0
        j=l-1
        for k in range(l):
            
            area=min(height[i],height[j])*(j-i)
            if area>m_area:
                m_area=area

            if height[i]>height[j]:
                j-=1
            else:
                i+=1
            if j==i:
                break

        return m_area