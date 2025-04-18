export function compile(ast) {
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
