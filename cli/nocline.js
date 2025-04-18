#!/usr/bin/env node

import fs from 'fs';
import { parse } from '../core/parser.js';
import { compile } from '../core/bytecode.js';
import { run } from '../core/runtime.js';

const args = process.argv.slice(2);
if (args[0] === 'run' && args[1]) {
  const code = fs.readFileSync(args[1], 'utf-8');
  const bytecode = compile(parse(code));
  const output = run(bytecode);
  console.log(output.join('\n'));
} else if (args[0] === 'repl') {
  process.stdin.setEncoding('utf8');
  process.stdout.write('Nocline > ');
  process.stdin.on('data', chunk => {
    const line = chunk.trim();
    try {
      const ast = parse(line);
      const bc = compile(ast);
      const result = run(bc);
      console.log(result.join('\n'));
    } catch (e) {
      console.error('⚠️', e.message);
    }
    process.stdout.write('Nocline > ');
  });
} else {
  console.log(`Usage:
    nocline run file.nc      # Run a Nocline script
    nocline repl             # Start interactive REPL`);
}
