mass_units = {'Kg': 1, 'MyCat': 4.5, 'Sun': 1.989e30}
info_units = {'B': 1, 'KB': 1e3, 'MB': 1e6, 'GB': 1e9}

units = [mass_units, info_units]


scale_one = float(input('Введите численное значение величины '))
unit_one = input('Введите единицу измерения введенной величины ')
unit_two = input('Введите единицу измерения величины в которую\
                  хотите перевести ')
is_correct_units = False

for unit in units:
    if unit_one in unit and unit_two in unit:
        scale_two = scale_one * unit[unit_one] / unit[unit_two]
        print(f'{scale_one} {unit_one} = {scale_two} {unit_two}')
        is_correct_units = True

if not is_correct_units:
    print('Wrong units')
