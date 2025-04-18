import zipfile
import os

# Define file structure and contents
project_files = {
    "frontend/index.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Nocline REPL 🌐</title>
  <style>
    body { font-family: monospace; background: #121212; color: #d0f0ff; }
    textarea { width: 100%; height: 200px; background: #1a1a1a; color: #7cf; border: 1px solid #444; }
    pre { background: #1e1e1e; padding: 10px; border: 1px solid #333; }
    .highlight { color: #ffe27a; }
  </style>
</head>
<body>
  <h1>Nocline REPL 🌐</h1>
  <textarea id="code" placeholder="Type Nocline here..."></textarea>
  <pre id="output"></pre>
  <script src="repl.js"></script>
</body>
</html>
""",
    "frontend/repl.js": """import { parse } from '../core/parser.js';
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
    document.getElementById('output').textContent = `⚠️ Error:\\n${err.message}`;
  }
});
""",
    "core/parser.js": """export function parse(code) {
  const lines = code.split('\\n');
  const ast = lines.map((line, index) => {
    const tokens = line.trim().split(' ');
    return {
      type: tokens[0],
      args: tokens.slice(1),
      line: index + 1,
    };
  });
  return ast;
}
""",
    "core/bytecode.js": """export function compile(ast) {
  return ast.map(node => {
    switch (node.type) {
      case 'assign': return { op: 'LOAD', args: node.args };
      case 'action': return { op: 'CALL', fn: node.args[0] };
      case 'pause': return { op: 'SLEEP', ms: parseInt(node.args[0]) };
      case 'loop': return { op: 'LOOP', range: node.args };
      case 'trigger': return { op: 'TRIGGER', target: node.args[0] };
      default: return { op: 'NOOP', meta: node };
    }
  });
}
""",
    "core/runtime.js": """export function run(bytecode) {
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
""",
    "core/scent.js": """export function decodeScent(scentStr) {
  const [note, phase] = scentStr.split(':');
  const emotionalWeights = {
    "musk": 0.85,
    "vanilla": 0.65,
    "cyan": 0.92,
  };
  return {
    note,
    phase,
    weight: emotionalWeights[note] || 0.5
  };
}
""",
    "core/signalbus.js": """const listeners = [];

export function register(fn) {
  listeners.push(fn);
}

export function send(signal) {
  listeners.forEach(fn => fn(signal));
}
""",
    "cli/nocline.js": """#!/usr/bin/env node

import fs from 'fs';
import { parse } from '../core/parser.js';
import { compile } from '../core/bytecode.js';
import { run } from '../core/runtime.js';

const args = process.argv.slice(2);
if (args[0] === 'run' && args[1]) {
  const code = fs.readFileSync(args[1], 'utf-8');
  const bytecode = compile(parse(code));
  const output = run(bytecode);
  console.log(output.join('\\n'));
} else if (args[0] === 'repl') {
  process.stdin.setEncoding('utf8');
  process.stdout.write('Nocline > ');
  process.stdin.on('data', chunk => {
    const line = chunk.trim();
    try {
      const ast = parse(line);
      const bc = compile(ast);
      const result = run(bc);
      console.log(result.join('\\n'));
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
""",
    "package.json": """{
  "name": "nocline-dev",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "start": "node cli/nocline.js repl",
    "dev": "live-server frontend"
  },
  "dependencies": {}
}
"""
}

# Create zip archive
zip_path = "/mnt/data/nocline-dev-kit.zip"
with zipfile.ZipFile(zip_path, 'w') as z:
    for path, content in project_files.items():
        z.writestr(path, content)

zip_path

import zipfile
import os

# Define paths
src_zip_path = "/mnt/data/nocline-dev-kit.zip"
extract_dir = "/mnt/data/nocline-dev-kit"

# Extract the ZIP file
with zipfile.ZipFile(src_zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# List extracted files and directories
extracted_files = []
for root, dirs, files in os.walk(extract_dir):
    for file in files:
        extracted_files.append(os.path.join(root, file))

extracted_files[:20]  # Show a preview of the first few files

import shutil
import os

# Define the project directory structure for zipping
project_root = "/mnt/data/nocline_devkit"
zip_output_path = "/mnt/data/nocline_with_jit_and_game_engine.zip"

# Create the required directory structure and sample files
os.makedirs(f"{project_root}/frontend", exist_ok=True)
os.makedirs(f"{project_root}/core", exist_ok=True)
os.makedirs(f"{project_root}/cli", exist_ok=True)
os.makedirs(f"{project_root}/game", exist_ok=True)

# Create core JIT compiler
with open(f"{project_root}/core/jit.js", "w") as f:
    f.write("""// core/jit.js
import { resolveFrame } from './runtime.js';

export function compileToJIT(bytecode) {
    let fnBody = `let frameStack = []; let pc = 0;\\n`;
    fnBody += `while (pc < bytecode.length) {\\n`;
    fnBody += `  switch (bytecode[pc]) {\\n`;

    fnBody += `    case 0x01: /* trigger */\\n`;
    fnBody += `      console.log("Triggering", bytecode[pc+1]);\\n`;
    fnBody += `      pc += 2; break;\\n`;

    fnBody += `    case 0x02: /* loop */\\n`;
    fnBody += `      let count = bytecode[pc+1];\\n`;
    fnBody += `      for (let i = 0; i < count; i++) { console.log("Loop", i); }\\n`;
    fnBody += `      pc += 2; break;\\n`;

    fnBody += `    case 0x03: /* pause */\\n`;
    fnBody += `      console.log("Pausing..."); pc += 1; break;\\n`;

    fnBody += `    default:\\n`;
    fnBody += `      throw new Error("Unknown opcode " + bytecode[pc]);\\n`;

    fnBody += `  }\\n}\\n`;

    return new Function("bytecode", fnBody);
}
""")

# Game engine file
with open(f"{project_root}/game/engine.js", "w") as f:
    f.write("""// game/engine.js
import { compileToJIT } from '../core/jit.js';
import { parseNocline, compileBytecode } from '../core/bytecode.js';

export function runGameScript(noclineCode) {
    const ast = parseNocline(noclineCode);
    const bytecode = compileBytecode(ast);
    const run = compileToJIT(bytecode);
    run(bytecode);
}
""")

# Create a placeholder Nocline script
with open(f"{project_root}/game/scene1.nc", "w") as f:
    f.write("""frame:
    loop 3:
        trigger "moodShift"
        pause
""")

# Zip the entire project directory
shutil.make_archive(zip_output_path.replace(".zip", ""), 'zip', project_root)

zip_output_path
