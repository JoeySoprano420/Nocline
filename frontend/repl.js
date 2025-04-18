import { parse } from '../core/parser.js';
import { compile } from '../core/bytecode.js';
import { run } from '../core/runtime.js';

document.getElementById('code').addEventListener('input', e => {
  const code = e.target.value;
  try {
    const ast = parse(code);
    const bytecode = compile(ast);
    const output = run(bytecode);
    document.getElementById('output').textContent = JSON.stringify(output, null, 2);
  } catch (err) {
    document.getElementById('output').textContent = `⚠️ Error:\n${err.message}`;
  }
});
