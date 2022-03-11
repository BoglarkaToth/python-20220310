from tkinter import E


#i = 0
#while i < 10:
#    print(i)
#    i += 1

#num = 1
#while num != 0:
#    num = int(input("írj be egy számot:"))
#    print(num)
# terminálba beírni egy számot, megy tovább, míg nem írok 0t

# gondoltam egy számra 1-10 között

min = 1
max = 10

# DRY - dont repeat yourself
print("Gondolj egy számra {min} és {max} között!")

answer = "x"
prev_guess = -1
guess = -2
while answer != "e":
        prev_guess = guess
        guess = (min + max) // 2

        if guess == prev_guess:
            # ha pl k..k..k..k..k..k (vagy n...)
            print("Ne szórakozz!")
            answer = "e" or "E"
        else:
            print(f"""A szám, amire gondoltam: {guess}
            Válassz kérlek!
            e - egyenlő
            k - kisebb
            n - nagyobb""")

            answer = input("Mi a válaszod?")

            if answer == "k" or answer == "K":
                max = guess
            elif answer == "n" or answer == "N":
                min = guess
            elif answer == "e" or answer == "E":
                print(f"Eltaláltam, a szám a {guess}")
            else:
                # ha mást válaszol, mint e/k/n, akkor ezt írja ki:
                print(f"Ez NEM válasz!")
