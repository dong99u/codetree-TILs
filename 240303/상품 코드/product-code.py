class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

# 첫 번째 객체를 초기화
product1 = Product("codetree", "50")

# 사용자로부터 입력 받아 두 번째 객체를 초기화
input_name, input_code = input().split()
product2 = Product(input_name, input_code)

# 두 객체의 상품명과 상품 코드를 출력
print(f'product {product1.code} is {product1.name}')
print(f'product {product2.code} is {product2.name}')