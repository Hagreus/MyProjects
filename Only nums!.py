try:
    user = input()
    print(int(user))

except ValueError:
    print("Enter only numbers!")
finally:
    print('Final')