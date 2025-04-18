# Patch the run method to properly convert opcode strings to Enum before calling the corresponding method

class BytecodeVM:
    def __init__(self, bytecode: List[Instruction]):
        self.bytecode = bytecode
        self.pc = 0  # Program counter
        self.frames = []
        self.current_frame = None
        self.signal_bus = {}

    def run(self):
        while self.pc < len(self.bytecode):
            instr = self.bytecode[self.pc]
            opcode_str = instr['opcode']
            opcode = Opcode[opcode_str]  # Convert string to Enum
            args = instr.get('args', [])
            method_name = f'op_{opcode.name.lower()}'
            if hasattr(self, method_name):
                getattr(self, method_name)(*args)
            else:
                print(f"[ERROR] Unknown opcode: {opcode}")
            self.pc += 1

    def op_enter_frame(self, name):
        frame = Frame(name)
        self.frames.append(frame)
        self.current_frame = frame
        print(f"[FRAME] Entering frame: {name}")

    def op_assign(self, var, value):
        self.current_frame.vars[var] = value
        print(f"[ASSIGN] {var} = {value}")

    def op_loop_start(self, var, start, end):
        self.current_frame.loop_stack.append((self.pc, var, start, end, start))
        self.current_frame.vars[var] = start
        print(f"[LOOP] Starting loop: {var} in {start}..{end}")

    def op_loop_end(self):
        loop_info = self.current_frame.loop_stack[-1]
        pc_start, var, start, end, current = loop_info
        if current < end - 1:
            current += 1
            self.current_frame.vars[var] = current
            self.current_frame.loop_stack[-1] = (pc_start, var, start, end, current)
            self.pc = pc_start  # loop back
        else:
            self.current_frame.loop_stack.pop()
            print(f"[LOOP] Exiting loop.")

    def op_trigger(self, action, params):
        param_values = [self.current_frame.vars.get(p, p) for p in params]
        print(f"[TRIGGER] Action: {action}({', '.join(map(str, param_values))})")

    def op_pause(self, duration):
        print(f"[PAUSE] {duration}ms")

    def op_if(self, condition):
        condition_value = self.resolve_condition(condition)
        self.current_frame.if_stack.append(condition_value)
        if not condition_value:
            self.skip_to_else_or_endif()

    def op_else(self):
        if self.current_frame.if_stack and self.current_frame.if_stack[-1]:
            self.skip_to_endif()

    def op_end_if(self):
        if self.current_frame.if_stack:
            self.current_frame.if_stack.pop()

    def op_exit_frame(self):
        print(f"[FRAME] Exiting frame: {self.current_frame.name}")
        self.frames.pop()
        if self.frames:
            self.current_frame = self.frames[-1]
        else:
            self.current_frame = None

    def resolve_condition(self, condition):
        # Simulated condition check for demo purposes
        return condition == "system::confirmed"

    def skip_to_else_or_endif(self):
        depth = 0
        while self.pc < len(self.bytecode) - 1:
            self.pc += 1
            opcode = Opcode[self.bytecode[self.pc]['opcode']]
            if opcode == Opcode.IF:
                depth += 1
            elif opcode == Opcode.END_IF and depth == 0:
                break
            elif opcode == Opcode.ELSE and depth == 0:
                break
            elif opcode == Opcode.END_IF:
                depth -= 1

    def skip_to_endif(self):
        depth = 0
        while self.pc < len(self.bytecode) - 1:
            self.pc += 1
            opcode = Opcode[self.bytecode[self.pc]['opcode']]
            if opcode == Opcode.IF:
                depth += 1
            elif opcode == Opcode.END_IF and depth == 0:
                break
            elif opcode == Opcode.END_IF:
                depth -= 1

# Run the patched VM
vm = BytecodeVM(sample_bytecode)
vm.run()
