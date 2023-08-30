import math

def calculate_s_with_uvt():
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    v = float(input('Enter the Final Velocity(v)(m/s): '))
    t = float(input('Enter the time(t)(s): '))
    s = ((u + v) * t) / 2
    return s

def calculate_s_uva():
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    v = float(input('Enter the Final Velocity(v)(m/s): '))
    a = float(input('Enter the Accelaration(a)(m/s²): '))
    s = (v ** 2 - u ** 2) / 2 * a
    return s

def calculate_s_uat():
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    a = float(input('Enter the Accelaration(a)(m/s²): '))
    t = float(input('Enter the time(t)(s): '))
    s = (u * t) + 0.5 * a * (t ** 2)
    return s

def calculate_u_sva():
    s = float(input('Enter the Displacment(s)(m): '))
    v = float(input('Enter the Final Velocity(v)(m/s): '))
    a = float(input('Enter the Accelaration(a)(m/s²): '))
    u = v ** 2 - 2*a*s
    u = math.sqrt(u)
    return u

def calculate_u_vat():
    v = float(input('Enter the Final Velocity(v)(m/s): '))
    a = float(input('Enter the Accelaration(a)(m/s²): '))
    t = float(input('Enter the time(t)(s): '))
    u = v - a*t
    return u

def calculate_u_sat():
    s = float(input('Enter the Displacment(s)(m): '))
    a = float(input('Enter the Accelaration(a)(m/s²): '))
    t = float(input('Enter the time(t)(s): '))
    u = ((0.5 * a * (t ** 2)) - s) / t
    return u

def calculate_u_svt():
    s = float(input('Enter the Displacment(s)(m): '))
    v = float(input('Enter the Final Velocity(v)(m/s): '))
    t = float(input('Enter the time(t)(s): '))
    u = ((2 * s) / t) - v
    return u

def calculate_v_sua():
    s = float(input('Enter the Displacment(s)(m): '))
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    a = float(input('Enter the Accelaration(a)(m/s²): '))
    v = (u ** 2) + (2 * a * s)
    v = math.sqrt(v)
    return v

def calculate_v_uat():
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    a = float(input('Enter the Accelaration(a)(m/s²): '))
    t = float(input('Enter the time(t)(s): '))
    v = u + (a * t)
    return v

def calculate_v_sut():
    s = float(input('Enter the Displacment(s)(m): '))
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    t = float(input('Enter the time(t)(s): '))
    v = ((2 * s) / t) - u
    return v

def calculate_a_suv():
    s = float(input('Enter the Displacment(s)(m): '))
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    v = float(input('Enter the Final Velocity(v)(m/s): '))
    a = ((v ** 2) - (u ** 2)) / (2 * s)
    return a

def calculate_a_uvt():
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    v = float(input('Enter the Final Velocity(v)(m/s): '))
    t = float(input('Enter the time(t)(s): '))
    a = (v - u) / t
    return a

def calculate_a_sut():
    s = float(input('Enter the Displacment(s)(m): '))
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    t = float(input('Enter the time(t)(s): '))
    a = (2 * (s - (u * t))) / t ** 2
    return a

def calculate_t_suv():
    s = float(input('Enter the Displacment(s)(m): '))
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    v = float(input('Enter the Final Velocity(v)(m/s): '))
    t = (2 * s) / (v + u)
    return t

def calculate_t_uva():
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    v = float(input('Enter the Final Velocity(v)(m/s): '))
    a = float(input('Enter the Accelaration(a)(m/s²): '))
    t = (v - u) / a
    return t

def calculate_t_sua():
    s = float(input('Enter the Displacment(s)(m): '))
    u = float(input('Enter the Initial Velocity(u)(m/s): '))
    acc = float(input('Enter the Accelaration(a)(m/s²): '))
    a = 0.5 * acc
    b = u
    c = -s
    discriminant = (b ** 2) - (4 * a * c)
    t1 = (-b + math.sqrt(discriminant)) / (2 * a)
    t2 = (-b - math.sqrt(discriminant)) / (2 * a)
    t = f'{t1} s or {t2} s'
    return t

def main():
    print('Welcome to Kinematic Calculator')
    while True:
        print('''
    Choose the quantity to calculate:
    1. Displacement (s)
    2. Initial Velocity (u)
    3. Final Velocity (v)
    4. Acceleration (a)
    5. Time (t)
    ''')

        choice = input('Enter the number corresponding to your choice: ')

        if choice == '1':
            print('''Calculate Displacement with --
        1. Initial Velocity, Final Velocity, and Time
        2. Initial Velocity, Acceleration, and Time
        3. Initial Velocity, Final Velocity, and Acceleration''')

            choice_s = input('Enter the number of your choosen option: ')

            if choice_s == '1':
                s = calculate_s_with_uvt()
                print(f'The Displacement(s) is {s} m')

            elif choice_s == '2':
                s = calculate_s_uat()
                print(f'The Displacement(s) is {s} m')

            elif choice_s == '3':
                s = calculate_s_uva()
                print(f'The Displacement(s) is {s} m')

            else:
                print('Enter a valid number')

        elif choice == '2':
            print('''Calculate Initial Velocity with --
        1. Displacement, Final Velocity, and Acceleration
        2. Final Velocity, Acceleration, and Time
        3. Displacement, Acceleration, and Time
        4. Displacement, Final Velocity, and Time
        ''')

            choice_u = input('Enter the number of your choosen option: ')

            if choice_u == '1':
                u = calculate_u_sva()
                print(f'The Initial Velocity is {u} m/s')

            elif choice_u == '2':
                u = calculate_u_vat()
                print(f'The Initial Velocity is {u} m/s')

            elif choice_u == '3':
                u = calculate_u_sat()
                print(f'The Initial Velocity is {u} m/s')

            elif choice_u == '4':
                u = calculate_u_svt()
                print(f'The Initial Velocity is {u} m/s')

            else:
                print('Enter a valid number')

        elif choice == '3':
            print('''Calculate Final Velocity with --
        1. Displacement, Initial Velocity, and Acceleration
        2. Initial Velocity, Acceleration, and Time
        3. Displacement, Initial Velocity, and Time
        ''')
            
            choice_v = input('Enter the number of your choosen option: ')
            
            if choice_v == '1':
                v = calculate_v_sua()
                print(f'The Final Velocity is {v} m/s')
                
            elif choice_v == '2':
                v = calculate_v_uat()
                print(f'The Final Velocity is {v} m/s')
                
            elif choice_v == '3':
                v = calculate_v_sut()
                print(f'The Final Velocity is {v} m/s')
                
            else:
                print('Enter a valid number')

        elif choice == '4':
            print('''Calculate Acceleration with --
        1. Displacement, Initial Velocity, and Final Velocity
        2. Initial Velocity, Final Velocity, and Time
        3. Displacement, Initial Velocity, and Time
        ''')
            
            choice_a = input('Enter the number of your choosen option: ')
            
            if choice_a == '1':
                a = calculate_a_suv()
                print(f'The Accelaration is {a} m/s²')
                
            elif choice_a == '2':
                a = calculate_a_uvt()
                print(f'The Accelaration is {a} m/s²')
                
            elif choice_a == '3':
                a = calculate_a_sut()
                print(f'The Accelaration is {a} m/s²')
                
            else:
                print('Enter a valid number')

        elif choice == '5':
            print('''Calculate Time with --
        1. Displacement, Initial Velocity, and Final Velocity
        2. Initial Velocity, Final Velocity, and Acceleration
        3. Displacement, Initial Velocity, and Acceleration
        ''')
            
            choice_t = input('Enter the number of your choosen option: ')
            
            if choice_t == '1':
                t = calculate_t_suv()
                print(f'The Time is {t} s')
                
            elif choice_t == '2':
                t = calculate_t_uva()
                print(f'The Time is {t} s')
                
            elif choice_t == '3':
                t = calculate_t_sua()
                print(f'The Time is {t}')
                
            else:
                print('Enter a valid number')
                
        another_calculation = input('Do you want to perform another calculation? (y/n): ')
        
        if another_calculation != 'y':
            print('Thank you for using Kinematic Calculator.....!')
            break

if __name__ == '__main__':
    main()
