leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Muutetaan kaikki luodeiksi
luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit

# Yksi luoti painaa 13,3 grammaa
grammat = luodit_yhteensa * 13.3

# Muutetaan kilogrammoiksi ja grammoiksi
kilogrammat = int(grammat // 1000)
jäljelle = grammat % 1000

print(f"Massa on {kilogrammat} kilogrammaa ja {jäljelle:.1f} grammaa.")