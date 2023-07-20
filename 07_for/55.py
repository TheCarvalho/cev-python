
# *ex55 - Make a program that reads the weight of five people. At the end, show which was the highest and lowest weight read

weight_list = []
for i in range(0, 5):
    weight = int(input('Enter the weight (kg): '))
    weight_list.append(weight)

print('The heaviest weight is {}kg is and the lightest is {}kg'.format(
    max(weight_list),
    min(weight_list)
))
