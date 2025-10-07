
lista_comandi = ["mov r3,[10]", "mov r4,[11]", "add r3,r4", "mov r0,r3", "mov [12],r0"]
REG_PC = 0 

# Memoria RAM
MEMORY = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Valori iniziali 
MEMORY[10] = 7
MEMORY[11] = 3
MEMORY[12] = 5

# Registro
registers = {
    "eax": 0,
    "ebx": 0,
    "r0": 0,
    "r1": 0,
    "r2": 0,
    "r3": 0,
    "r4": 0,
}


def move(par1,par2):
    #registers[par1] = par2
    if par1 in registers and par2 in registers:
        registers[par1] = registers[par2]
    elif isinstance(par1, int) and par2 in registers:
        MEMORY[par1] = registers[par2]
    elif par1 in registers and isinstance(par2, int):
        registers[par1] = MEMORY[par2]
    
    
def add(par1, par2):
    registers[par1] = registers[par1] + registers[par2]
    



# Funzione per decodificare il comando assembly
def decode(cmd):
    parts = cmd.split()
    commands = parts[0] 
    params = parts[1].split(",")
    par1 = params[0]
    par2 = params[1]
    return commands, par1, par2


# Funzione per eseguire il comando (mov, add, ...)
def execute(cmd,par1,par2):
    ##print(cmd,par1,par2)
    if cmd == "mov":
        if par1.startswith("["):
            memory_addr = int(par1[1:-1]) # indirizzo di memoria
            move(memory_addr,par2) # scrivere la memoria
        elif par2.startswith("["):
            memory_addr = int(par2[1:-1]) # indirizzo di memoria
            move(par1,memory_addr) # scrivere la memoria
        else:
            move(par1,par2)
    elif cmd == "add":
        add(par1,par2) # somma tra due registri 


## Ciclo FDE
for cmd in lista_comandi:
    c,par1,par2 = decode(cmd)
    execute(c,par1,par2)
    REG_PC += 1 

## Output
print("Register: ", registers)
print("Memory: ", MEMORY)
print("REG_PC: ", REG_PC)


