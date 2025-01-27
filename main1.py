class Pupil:
    school_name="ABC"

    def __init__(self, name):
        self.name=name

    @classmethod
    def change_name(cls, name):
        Pupil.school_name=name


pupil=Pupil("Sherbek")

print(pupil.school_name)

Pupil.change_name("PDP School")

print(pupil.school_name)


from typing import Any


class Talaba:
    summa1=30000000


    def __init__(self, summa):
        self.summa=summa


    @classmethod
    def change_summa(cls, summa):
        Talaba.change_summa=summa


talaba=Talaba("36000000")
print(talaba.summa1)
Talaba.change_summa(36000000)
print(talaba.summa)





