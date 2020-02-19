# pretvori iz binarnega sistema v desetiškega
n = int(input(), 2)
# uporabimo funksijo oct inodrežemo 0o na začetku
print(oct(n)[2:])