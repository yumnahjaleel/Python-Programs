class CPU:
    def __init__(self):
        self.registers = [0] * 4
        self.pc = 0
        self.memory = [0] * 256
        self.running = True

    def fetch(self):
        if self.pc >= len(self.memory):
            self.running = False
            return 0x3000
        instr = self.memory[self.pc]
        self.pc += 1
        return instr

    def decode_execute(self, instr):
        opcode = (instr & 0xF000) >> 12
        reg_a  = (instr & 0x0F00) >> 8
        reg_b  = (instr & 0x00F0) >> 4
        addr   = (instr & 0x00FF) # Use last 8 bits as a memory address

        # --- Existing Logic ---
        if opcode == 0x1: # ADD
            self.registers[reg_a] = (self.registers[reg_a] + self.registers[reg_b]) & 0xFFFF
        
        elif opcode == 0x2: # LOAD
            self.registers[reg_a] = addr
            
        # --- New Jump Logic ---
        elif opcode == 0x4:  # JMP: Unconditional Jump
            print(f"Jumping to address: {addr}")
            self.pc = addr

        elif opcode == 0x5:  # JZ: Jump to 'addr' if Reg A is Zero
            if self.registers[reg_a] == 0:
                print(f"R{reg_a} is zero. Branching to {addr}")
                self.pc = addr
            else:
                print(f"R{reg_a} is {self.registers[reg_a]}, no jump.")

        elif opcode == 0x3: # HALT
            self.running = False

    def run(self):
        while self.running:
            instr = self.fetch()
            self.decode_execute(instr)
        print("Final Register State:", self.registers)

# --- Simulation: Creating a Loop ---
# This program will count down from 3 to 0
cpu = CPU()

# 0: LOAD 3 into R0       (0x2003)
# 1: LOAD 1 into R1       (0x2101)
# 2: SUB R0 - R1 -> R0    (We'll simulate SUB by adding a negative or just a custom opcode)
# Let's simplify: 
cpu.memory[0] = 0x2003 # R0 = 3
cpu.memory[1] = 0x2101 # R1 = 1
# To simulate a loop, we manually decrement in a hypothetical SUB opcode 0x6
# For this demo, let's just show a conditional jump:
cpu.memory[2] = 0x5005 # JZ: If R0 is 0, jump to HALT (addr 5)
cpu.memory[3] = 0x4000 # JMP back to start (addr 0) to repeat
cpu.memory[5] = 0x3000 # HALT

cpu.run()
