HEXADECIMAL_DICTIONARY = {"AliceBlue".lower(): "#f0f8ff", "AntiqueWhite".lower(): "#faebd7", "aquamarine1".lower(): "#7fffd4", "azure1".lower(): "#f0ffff", "beige".lower(): "#f5f5dc", "black".lower(): "#000000", "blue1".lower(): "#0000ff", "BlueViolet".lower(): "#8a2be2", "brown".lower(): "#a52a2a", "coral".lower(): "#ff7f50"}

name = input("Enter a colour: ").lower()
if name in HEXADECIMAL_DICTIONARY:
    print(HEXADECIMAL_DICTIONARY[name])
else:
    print("That colour name is not in the dictionary")