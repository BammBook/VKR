import math

B_s = 1.21
B_r = 0.42

# coef_A = 1 - B_s + B_r

coef_A = 0.06
print(f'coef A = {round(coef_A, 2)}')

first_part_1 = (coef_A ** 2 + 0.5)
second_part_1 = (1 - 1/math.pi * math.acos(coef_A))
third_part_1 = 3/(2 * math.pi) * coef_A * math.sqrt(1 - coef_A ** 2)

I_relative_value = round(math.sqrt(first_part_1 * second_part_1 + third_part_1) * math.sqrt(2), 3)

print(f'I_relative_value = {I_relative_value}')


# first_part_2 = 1/math.pi * math.acos(coef_A)
# second_part_2 = coef_A/math.pi * math.sqrt(1 - coef_A ** 2)
#
# I_relative_effective = 1/math.sqrt(2) * (1 - first_part_2 + second_part_2)
# print(f'I_relative_effective = {round(I_relative_effective * math.sqrt(2), 3)}')
