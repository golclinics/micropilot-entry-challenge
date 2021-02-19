def Zeros(A):
    return (A.count(0))


arrays = input('input values with comma(,) to separate each : ')
member = []
for arrays in arrays.split(sep=','):
    arrays = int(arrays)
    member.append(arrays)

counter = Zeros(A=member)
print("Zeros count is {0}".format(counter))