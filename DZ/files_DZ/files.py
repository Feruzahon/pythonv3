'====== 1 ======'
file=open("test_1DZ.txt",'r')
print(file.read())

'======= 2 ====='
login = input('Введите логин: ')
parol=input('Введите пароль: ')

file=open('user.txt','w')
file.write(f"Логин: {login}\nПароль: {parol}")

'========= 3 ======='
letter = 'w'
with open('test_1DZ.txt','r') as f:
    for line in f:
        if letter in line:
            print('Да, в тексте есть w')
        else:
            print('Нет, в тестке нет w')
# '========= 4 ========'
letter = 'o'
o_words=[]
with open('python.txt','r') as file:
   for line in file:
        words = line.strip().split()
        for word in words:
            if letter.lower() in word.lower():
                o_words.append(word)

print(f"Слова содержащие букву 'о':")
print(o_words)


# '========= 5 ========='
with open('new_file.txt','w') as file:
    file.write(""".detacilpmoc naht retteb si xelpmoC\n.xelpmoc naht retteb si elpmiS\n.ticilpmi naht retteb si ticilpxE\n.ylgu naht retteb si lufituaeB
     """ )

with open('new_file.txt')as file:
    texts = file.readlines()
    for text in reversed(texts):
        print(text.strip())

# '========== 6 ======'
with open('new_num_file.txt','w') as file:
    file.write("""123\naaa456\nfxdya 500""")


chislo = 0
with open('new_num_file.txt') as file:
    for line in file:
        digit = ''
        for number in line:
         
            if number.isdigit():
                digit +=number
        if digit:
            numbers = int(digit)
            chislo += numbers
            print(f"Извлечено число из строки: {numbers}")
        else:
            print("Цифр в строке не найдено.")

print("Сумма всех чисел:", chislo)

