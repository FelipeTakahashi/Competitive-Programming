from math import sqrt
reps = int(input())

for i in range(1, reps+1):
    pokemon, level = map(str, input().split())
    hp_b, hp_iv, hp_ev = map(int, input().split())
    atk_b, atk_iv, atk_ev = map(int, input().split())
    def_b, def_iv, def_ev = map(int, input().split())
    sp_b, sp_iv, sp_ev = map(int, input().split())

    level = int(level)

    hp = (((hp_iv + hp_b + sqrt(hp_ev)/8 + 50) * level)/50) + 10
    atk = (((atk_iv + atk_b + sqrt(atk_ev)/8) * level)/50) + 5
    defesa = (((def_iv + def_b + sqrt(def_ev)/8) * level)/50) + 5
    sp = (((sp_iv + sp_b + sqrt(sp_ev)/8) * level)/50) + 5

    print(f"Caso #{i}: {pokemon} nivel {level}")
    print(f"HP: {int(hp)}")
    print(f"AT: {int(atk)}")
    print(f"DF: {int(defesa)}")
    print(f"SP: {int(sp)}")
