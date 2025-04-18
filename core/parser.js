export function parse(code) {
  const lines = code.split('\n');
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
