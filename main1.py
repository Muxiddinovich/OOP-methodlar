# # class Pupil:
# #     school_name="ABC"

# #     def __init__(self, name):
# #         self.name=name

# #     @classmethod
# #     def change_name(cls, name):
# #         Pupil.school_name=name


# # pupil=Pupil("Sherbek")

# # print(pupil.school_name)

# # Pupil.change_name("PDP School")

# # print(pupil.school_name)


# # from typing import Any


# # class Talaba:
# #     summa1=30000000


# #     def __init__(self, summa):
# #         self.summa=summa


# #     @classmethod
# #     def change_summa(cls, summa):
# #         Talaba.change_summa=summa


# # talaba=Talaba("36000000")
# # print(talaba.summa1)
# # Talaba.change_summa(36000000)
# # print(talaba.summa)








# # d={
# #     "I":1,
# #     "V":5,
# #     "X":10,
# #     "L":50,
# #     "C":100,
# #     "D":500,
# #     "M":1000
# # }


# # rim=input(">>> ")
# # ans=0

# # for i in range(len(rim)-1):
# #     if d[rim[i]]<d[rim[i+1]]:
# #         ans-=d[rim[i]]

# #     else:
# #         ans+=d[rim[i]]



# # ans+=d[rim[-1]]
# # print(ans)





# class Pupil:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def __str__(self):
#         return f"{self.name} -> {self.age}"
    


#     def __add__(self, other):
#         return Pupil(self.name, self.age+other)



# p1=Pupil("Sherbek", 17)


# p1=p1+1

# print(p1)



class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"Point({self.x};{self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
       return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return Point(self.x*other.x, self.y*other.y)
    
    def __truediv__(self,other):
        return Point(self.x/other.x, self.y/other.y)
p1 = Point(1,1)
p2 = Point(3,2)


print(p1/p2)





print(o[num])