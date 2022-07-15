# 11.07.2022
# Son topish o'yini 1-qism
# Muallif: Shaxzodjon Zoirov

import random


def sontop_pc(x=10):
        input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
        quyi = 1
        yuqori = x

        while True:
            if  quyi  != yuqori:
                   taxmin = random.randint(quyi,yuqori)
            else:
                taxmin = quyi 
            javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                          f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower)
            
            if javob == "-":
                yuqori = taxmin - 1
            elif javob == "+":
                quyi = taxmin + 1
            else:
                break
            print("Topdim!")


        def play(x=10):
            yana = True
            while yana:
                taxminlar_users = sontop(x)
                taxminlar_pc = sontop_pc(x)

                if taxminlar_user>taxminlar_pc:
                    print("Men yutdim!")
                elif taxminlar_user<taxminlar_pc:
                    print("Siz yutdingiz!")
                else:
                    print("Durrang")
                yana = int(intput("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))


