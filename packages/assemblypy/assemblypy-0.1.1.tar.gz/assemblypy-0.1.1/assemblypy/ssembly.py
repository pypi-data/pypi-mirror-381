class asm:
    def __init__(self):
        self.register = {}   # السجلات ديناميكية بالكامل
        self.memory = {}   
        self.log = [] 
    def show_logs(self):
        for entry in self.log:
            print(entry)   
    # أوامر أساسية
    def mov(self, reg, val):
        self.register[reg] = val

    def add(self, reg):
        self.register[reg] = self.register.get(reg,0) + 1
        self.log.append(f"ADD: ({reg} + 1)  = {self.register.get(reg,0)}")

    def sub(self, reg):
        self.register[reg] = self.register.get(reg,0) - 1
        self.log.append(f"SUB: (reg - 1)  = {self.register.get(reg,0)}")

    def mul(self, reg):
        self.register[reg] = self.register.get(reg,0) * 2
        self.log.append(f"MUL: (reg * 1)  = {self.register.get(reg,0)}")

    def load(self, reg, addr):
        self.register[reg] = self.memory.get(addr,0)
        

    def save(self, reg, addr):
        self.memory[addr] = self.register.get(reg,0)

    def show(self, reg):
        print(f"{reg} : {self.register.get(reg,0)}")

    def reset(self, reg):
        self.register[reg] = 0
        self.log.append(f"RESET: (reg = 0)  = {self.register.get(reg,0)}")

    def set(self, reg, val):
        self.register[reg] = val
        self.log.append(f"SET: (reg = {val})  = {self.register.get(reg,0)}")

    def read_mem(self, addr):
        print(f"{addr} : {self.memory.get(addr,0)}")
        self.log.append(f"PRINT:  = {self.register.get(addr,0)}")

    # أوامر النصوص
    def add_text(self, reg1, reg2, dest):
        self.register[dest] = str(self.register.get(reg1,"")) + " " + str(self.register.get(reg2,""))
        self.log.append(f"ADD_TEXT: ({reg1} + {reg2})  = {self.register.get(dest,0)}")

    def mov_text(self, reg, val):
        self.register[reg] = str(val)

    # العمليات المنطقية
    def OR(self, reg1, reg2, dest):
        self.register[dest] = self.register.get(reg1,0) | self.register.get(reg2,0)
        self.log.append(f"OR: ({reg1} or {reg2}) = {self.register.get(dest,0)}")

    def XOR(self, reg1, reg2, dest):
        self.register[dest] = self.register.get(reg1,0) ^ self.register.get(reg2,0)
        self.log.append(f"XOR: ({reg1} xor {reg2}) = {self.register.get(dest,0)}")

    def AND(self, reg1, reg2, dest):
        self.register[dest] = self.register.get(reg1,0) & self.register.get(reg2,0)
        self.log.append(f"AND: ({reg1} and {reg2}) = {self.register.get(dest,0)}")
        

    def NOT(self, reg, dest):
        self.register[dest] = ~self.register.get(reg,0)
        self.log.append(f"NOT: ( not {reg}) = {self.register.get(dest,0)}")

    def print_reg(self, reg):
        print(f"{reg} : {bin(self.register.get(reg,0))}")
        self.log.append(f"print: ({reg})= {self.register.get(reg,0)}")

    def write_mem(self, addr):
        return self.memory.get(addr,0)
    def JNZ(self, reg, red, wa,text):
        if red == ">":
            if self.register.get(reg,0) >= wa:
                print(f"{text}")
                self.log.append(f"JNZ: (reg > wa)  = {self.register.get(text,0)}")
        if red == "<":
            if self.register.get(reg,0) <= wa:
                print(f"{text}")
                self.log.append(f"JNZ: (reg < wa)  = {self.register.get(text,0)}")
        if red == "!":
            if self.register.get(reg,0) != wa:
                 print(f"{text}")
                 self.log.append(f"JNZ: (reg ! wa)  = {self.register.get(text,0)}")
    def NAND(self, reg, req, dast):
        temp = self.register.get(reg,0) & self.register.get(req,0)
        self.register[dast] = ~temp
        self.log.append(f"NAND: (~{reg} & {req})  = {self.register.get(dast,0)}") 
    def add_multi_text(self, *regs, dest):
        total = ""
        for reg in regs:
            total += str(self.register.get(reg," "))
            total += " "
            self.register[dest] = total.strip()
            

        
        self.log.append(f"ADD_MULTI_TEXT: = {self.register[dest]}")
    def INPUT(self, reg, type,prompt):
        if type =="str":
            val = str(input(prompt))
            self.register[reg] = val
            self.log.append(f"INPUT-STR: input = {val}")
        if type =="int":
            val = int(input(prompt))
            self.register[reg] = val
            self.log.append(f"INPUT-INT: input = {val}")
        if type =="float":
            val = float(input(prompt))
            self.register[reg] = val
            self.log.append(f"INPUT-FLOAT: input = {val}")
    def show_text(self, reg):
        print(f"{self.register.get(reg, '')}")
        self.log.append(f"SHOW-TEXT: text = {self.register.get(reg, '')}")
        


            
            



