export function run(bytecode) {
  const output = [];
  for (const instr of bytecode) {
    switch (instr.op) {
      case 'LOAD': output.push(`Set ${instr.args[0]} = ${instr.args[1]}`); break;
      case 'CALL': output.push(`Invoke ${instr.fn}()`); break;
      case 'SLEEP': output.push(`Pause ${instr.ms}ms`); break;
      case 'LOOP': output.push(`Loop through ${instr.range.join(' ')}`); break;
      case 'TRIGGER': output.push(`Trigger ${instr.target}`); break;
      default: output.push(`NOOP at unknown instruction`);
    }
  }
  return output;
}
