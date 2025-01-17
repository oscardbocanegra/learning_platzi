def check_employee_acces(func):
    def wrapper(employee):
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            raise ValueError('Acceso denegado')
    return wrapper

@check_employee_acces
def delete_employe(employee):
    print(f'Empleado {employee['name']} eliminado')


admin = {'name': 'Juan', 'role': 'admin'}
employee = {'name': 'Pedro', 'role': 'employee'}