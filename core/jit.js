// core/jit.js
import { resolveFrame } from './runtime.js';

export function compileToJIT(bytecode) {
    let fnBody = `let frameStack = []; let pc = 0;\n`;
    fnBody += `while (pc < bytecode.length) {\n`;
    fnBody += `  switch (bytecode[pc]) {\n`;

    fnBody += `    case 0x01: /* trigger */\n`;
    fnBody += `      console.log("Triggering", bytecode[pc+1]);\n`;
    fnBody += `      pc += 2; break;\n`;

    fnBody += `    case 0x02: /* loop */\n`;
    fnBody += `      let count = bytecode[pc+1];\n`;
    fnBody += `      for (let i = 0; i < count; i++) { console.log("Loop", i); }\n`;
    fnBody += `      pc += 2; break;\n`;

    fnBody += `    case 0x03: /* pause */\n`;
    fnBody += `      console.log("Pausing..."); pc += 1; break;\n`;

    fnBody += `    default:\n`;
    fnBody += `      throw new Error("Unknown opcode " + bytecode[pc]);\n`;

    fnBody += `  }\n}\n`;

    return new Function("bytecode", fnBody);
}
