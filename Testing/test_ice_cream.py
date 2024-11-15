from desserts import IceCream

def test_calculate_cost():
    test_cookie=IceCream("Purple and black mix",12,5.0)
    assert test_cookie.calculate_cost()==60.0

def test_calculate_tax():
    test_cookie=IceCream("Purple and black mix",12,5.0)
    assert test_cookie.calculate_tax()==4.35