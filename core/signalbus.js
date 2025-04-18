const listeners = [];

export function register(fn) {
  listeners.push(fn);
}

export function send(signal) {
  listeners.forEach(fn => fn(signal));
}
