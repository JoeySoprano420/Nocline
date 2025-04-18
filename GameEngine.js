// game/engine.js
import { compileToJIT } from '../core/jit.js';
import { parseNocline, compileBytecode } from '../core/bytecode.js';

export function runGameScript(noclineCode) {
    const ast = parseNocline(noclineCode);
    const bytecode = compileBytecode(ast);
    const run = compileToJIT(bytecode);
    run(bytecode);
}
