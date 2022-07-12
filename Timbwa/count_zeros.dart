import 'dart:math';

void main(List<String> args) {
  final rand = Random(777);

  /// Generate uniformly-distributed integers in the range [0, 10)
  final list = List<int>.generate(1000, (index) => rand.nextInt(10));

  final result = countZeros(list);

  /// Number of Zeros should be close to 100 in number
  print(result);
}

int countZeros(List<int> A) {
  List<int> B = [...A];
  B.retainWhere((element) => element == 0);

  return B.length;
}
