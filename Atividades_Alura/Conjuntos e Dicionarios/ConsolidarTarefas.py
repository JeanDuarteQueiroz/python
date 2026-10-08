equip1 = set(t.strip() for t in input("Digite as tarefas da equipe 1: ").lower().split(", "));
equip2 = set(t.strip() for t in input("Digite as tarefas da equipe 2: ").lower().split(", "));

todas = equip1 ^ equip2;
print(f"Suas tarefas são: {", ".join(todas)}");
