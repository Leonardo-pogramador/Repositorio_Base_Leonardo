
# ----------------------------------------------8

nota1 = float(input("Digite sua primeira nota"))

nota2 = float(input("Digite sua Segunda nota"))

nota3 = float(input("Digite sua Terceira nota"))

nota4 = float(input("Digite sua Quarta nota"))

media = (nota1 + nota2 + nota3 + nota4) /4

if media >= 7:
    print(f"Sua nota foi {media}. Aprovado(a) ✅")

elif media >= 5 and media <= 6.9:
    print(f"Sua nota foi {media}. Voçê está de Recuperação ⚠️")

elif media <= 4.9:
    print(f"Sua nota foi {media}. Reprovado(a) ❌")

# ----------------------------------------------

