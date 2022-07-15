# indexError- biron bir ro'yxatni ichidagi mavjud bo'lmagan ma'lumotga murojaat qilsangiz indexError yuzaga keladi
mevalar = ['olma','anor','anjir','uzum']
try:
    print(mevalar[4])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos.")
