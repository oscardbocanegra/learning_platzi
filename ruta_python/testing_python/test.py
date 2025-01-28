def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total

def test_calculate_total_with_empty_list():
    print("prueba 1")
    assert calculate_total([]) == 0

if __name__ == '__main__':
    test_calculate_total_with_empty_list()