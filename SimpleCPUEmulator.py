class SimpleALU:
    """Simulates Digital Logic Gates inside the ALU."""
    @staticmethod
    def add(a, b):
        return (a + b) & 0xFFFF  # Simulate 16-bit overflow
    
    @staticmethod
    def logical_and(a, b):
        return a & b

    @staticmethod
    def logical_or(a, b):
        return a | b

class CPU:
    def __init__(self):
        # 16-bit Registers (R0 to R3)
        self.registers = [0] * 4
        self.pc = 0  # Program Counter
        self.memory = [0] * 256  # 256 words of memory
        self.alu = SimpleALU()
        self.running = True

    def fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def decode_execute(self, instr):
        # Format: [Opcode (4 bits)][Reg A (4 bits)][Reg B (4 bits)][Value/Reg C (4 bits)]
        # For simplicity, we use hex-based logic:
        # 0x1ABC -> ADD Reg A, Reg B and store in Reg C
        # 0x2A0F -> LOAD Value 0F into Reg A
        # 0x3000 -> HALT
        
        opcode = (instr & 0xF000) >> 12
        reg_a  = (instr & 0x0F00) >> 8
        reg_b  = (instr & 0x00F0) >> 4
        target = (instr & 0x000F)

        if opcode == 0x1:  # ADD Logic
            val1 = self.registers[reg_a]
            val2 = self.registers[reg_b]
            self.registers[target] = self.alu.add(val1, val2)
            print(f"Executed ADD: R{target} = {self.registers[target]}")

        elif opcode == 0x2:  # LOAD Logic
            value = instr & 0x00FF # Get last 8 bits as value
            self.registers[reg_a] = value
            print(f"Executed LOAD: R{reg_a} = {value}")

        elif opcode == 0x3:  # HALT Logic
            print("CPU Halted.")
            self.running = False

    def run(self):
        print("--- CPU Execution Started ---")
        while self.running:
            instr = self.fetch()
            self.decode_execute(instr)

# --- Simulation ---
my_cpu = CPU()

# Hardcoding a small "Program" in Machine Code
# 1. LOAD 10 into R0 (0x200A)
# 2. LOAD 20 into R1 (0x2114)
# 3. ADD R0 + R1 and store in R2 (0x1012)
# 4. HALT (0x3000)
my_cpu.memory[0] = 0x200A
my_cpu.memory[1] = 0x2114
my_cpu.memory[2] = 0x1012
my_cpu.memory[3] = 0x3000

my_cpu.run()
