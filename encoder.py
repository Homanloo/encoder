import random


def encode(text):

    try:
        text_lower = text.lower()
        words = text_lower.split()
        ch = []

        for i in range(len(words)):
            for j in words[i]:
                ch.append(j)
            if len(words) != int(i) + 1:
                ch.append("Space")

        all_ch = []
        unique_ch = []
        for i in ch:
            all_ch.append(i)

        for i in all_ch:
            if i not in unique_ch:
                unique_ch.append(i)

        unique_ch.sort()

        ab = {'!': 1, "'": 2, ',': 3, '.': 4, '?': 5, 'Space': 6, 'a': 7, 'b': 8, 'c': 9, 'd': 10, 'e': 11, 'f': 12,
              'g': 13, 'h': 14, 'i': 15, 'j': 16, 'k': 17, 'l': 18, 'm': 19, 'n': 20, 'o': 21, 'p': 22, 'q': 23,
              'r': 24, 's': 25, 't': 26, 'u': 27, 'v': 28, 'w': 29, 'x': 30, 'y': 31, 'z': 32, '*': 33, '(': 34,
              ')': 35, '"': 36, '1': 37, '2': 38, '3': 39, '4': 40, '5': 41, '6': 42, '7': 43, '8': 44, '9': 45,
              '0': 46}

        for i in range(len(ch)):
            if ch[i] not in ab.keys():
                ch[i] = '*'

        a_list_alpha = []
        b_list_alpha = []
        n = random.randrange(3, 10)
        for i in range(n):
            a_alpha = random.randrange(1, 30)
            a_list_alpha.append(a_alpha)
            b_alpha = random.randrange(1, 30)
            b_list_alpha.append(b_alpha)

        total_a_alpha = sum(a_list_alpha)
        total_b_alpha = sum(b_list_alpha)

        a_list_beta = []
        b_list_beta = []
        n = random.randrange(5, 15)
        for i in range(n):
            a_beta = random.randrange(8, 80)
            a_list_beta.append(a_beta)
            b_beta = random.randrange(8, 80)
            b_list_beta.append(b_beta)

        total_a_beta = sum(a_list_beta)
        total_b_beta = sum(b_list_beta)

        encoded_list = []
        for i in ch:
            gama = random.randrange(1, 10)
            if gama % 2 == 1:
                x = ab.get(i) * total_a_alpha + total_b_beta
                y = str(gama) + str(x)
                encoded_list.append(y)

            if gama % 2 == 0:
                x = ab.get(i) * total_a_beta + total_b_alpha
                y = str(gama) + str(x)
                encoded_list.append(y)

        result = ""
        for i in encoded_list:
            result += i
            result += " "
        result += "/" + str(total_a_alpha) + "." + str(total_a_beta) + "." + str(total_b_alpha) + "." + str(total_b_beta)
        return result

    except ValueError:
        print("Something went wrong...")


def decode(code):

    try:
        code_and_key = code.split(" /")
        keys = code_and_key[-1]
        encoded = code_and_key[0].split(" ")

        total_a_alpha = int(keys.split(".")[0])
        total_a_beta = int(keys.split(".")[1])
        total_b_alpha = int(keys.split(".")[2])
        total_b_beta = int(keys.split(".")[3])

        ab = {'!': 1, "'": 2, ',': 3, '.': 4, '?': 5, 'Space': 6, 'a': 7, 'b': 8, 'c': 9, 'd': 10, 'e': 11, 'f': 12,
              'g': 13, 'h': 14, 'i': 15, 'j': 16, 'k': 17, 'l': 18, 'm': 19, 'n': 20, 'o': 21, 'p': 22, 'q': 23,
              'r': 24, 's': 25, 't': 26, 'u': 27, 'v': 28, 'w': 29, 'x': 30, 'y': 31, 'z': 32, '*': 33, '(': 34,
              ')': 35, '"': 36, '1': 37, '2': 38, '3': 39, '4': 40, '5': 41, '6': 42, '7': 43, '8': 44, '9': 45,
              '0': 46}

        ch = []
        for i in encoded:
            if int(i[0]) % 2 == 1:
                num = int((int(i[1:]) - total_b_beta) / total_a_alpha)
                for key, value in ab.items():
                    if num == value:
                        ch.append(key)

            if int(i[0]) % 2 == 0:
                num = int((int(i[1:]) - total_b_alpha) / total_a_beta)
                for key, value in ab.items():
                    if num == value:
                        ch.append(key)

        result = ""
        for i in ch:
            if i == "Space":
                result += " "
                continue
            result += i

        return result

    except ValueError:
        print("Something wrong with the encoded massage")


while True:
    operation = input("""Type "E" for encoding or "D" for decoding or "Q" to quit: """)

    if operation == "E" or operation == "e" or operation == "encoding" or operation == "Encoding":
        text_input = str(input("Type or paste the text: "))
        print(encode(text_input))

    elif operation == "D" or operation == "d" or operation == "decoding" or operation == "Decoding":
        text_input = str(input("Enter the encoded text: "))
        print(decode(text_input))

    elif operation == "Q" or operation == "q":
        exit()

    else:
        print("Invalid input")
