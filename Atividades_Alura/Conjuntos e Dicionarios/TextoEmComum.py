txt1 = set(input("Texto 1: ").lower().split());
txt2 = set(input("Texto 2: ").lower().split());

print(f"Palavras em comum nos textos: {txt1&txt2}")