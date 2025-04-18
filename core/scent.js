export function decodeScent(scentStr) {
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
