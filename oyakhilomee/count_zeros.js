let CountZeros = [1, 0, 5, 6, 0, 2];

let occurrences = {};
for (let i = 0, j = CountZeros.length; i < j; i++) {
  occurrences[CountZeros[i]] = (occurrences[CountZeros[i]] || 0) + 1;
}

console.log(occurrences[0]);
