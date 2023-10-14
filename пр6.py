N = int(input("Введите размер массива: "))
masiv=[]
for i in range(N):
    element = int(input("Введите элемент: "))
    masiv.append(element)
elementmax = max(masiv)
print("Массив в обратном порядке:")
for element in reversed(masiv):
    print(element, end=" ")
print("\nМаксимальный элемент в массиве:", elementmax)