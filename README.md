# 🧠 Simulatore FDE: Fetch-Decode-Execute in Python

Questo progetto è un **simulatore semplice del ciclo FDE** (Fetch-Decode-Execute), che riproduce il funzionamento di base di una CPU.  
È pensato per chi vuole capire come un processore esegue istruzioni assembly-like, passo dopo passo.

---

## 🔧 Cosa fa

Il simulatore:
- Carica un programma con istruzioni assembly semplici
- Simula una CPU con registri e memoria RAM
- Esegue ogni istruzione attraverso il ciclo **Fetch → Decode → Execute**
- Supporta operazioni come:
  - `mov` → copia dati tra registri e memoria
  - `add` → somma valori nei registri

Alla fine, calcola `7 + 3 = 10` e salva il risultato in memoria.

---

## 🔄 Il ciclo FDE

Ogni istruzione passa per tre fasi:

### 1. **FETCH** (preleva)
Il programma legge l’istruzione corrente dalla lista `program`.

### 2. **DECODE** (decodifica)
L’istruzione viene divisa in:
- **Comando** (`mov`, `add`)
- **Parametri** (es: `r3`, `[10]`)

### 3. **EXECUTE** (esegui)
Viene eseguita l’azione richiesta:
- Lettura/scrittura in memoria
- Operazioni tra registri

Il **Program Counter (PC)** aumenta dopo ogni istruzione, fino alla fine.

---

## 📦 Componenti principali

### 🔹 **Registri**
Variabili veloci accessibili direttamente dalla CPU:
```python
registers = {
    "r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0,
    "eax": 0, "ebx": 0
}
```
### 🔹 **Memoria**
Un array di 15 celle:
```python
MEMORY = [0] * 15
MEMORY[10] = 7
MEMORY[11] = 3
```


🔹 Istruzioni supportate
Istruzione	Esempio	Effetto
mov	mov r3, [10]	Carica in r3 il valore di MEMORY[10]
mov	mov [12], r0	Salva il valore di r0 in MEMORY[12]
mov	mov r0, r3	Copia il valore da r3 a r0
add	add r3, r4	r3 = r3 + r4

