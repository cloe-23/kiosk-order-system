import random

# 메뉴 클래스
class Menu:
    def __init__(self):
        self.items = {
            "아메리카노": True,
            "라떼": True,
            "모카": False  # 품절
        }

    def is_available(self, item):
        return self.items.get(item, False)

    def get_price(self, item):
        return 4000  # 모든 음료 동일 가격 처리

# 주문 처리 시스템
class OrderSystem:
    def __init__(self, menu):
        self.menu = menu

    def create_order(self, item):
        if not self.menu.is_available(item):
            return None
        price = self.menu.get_price(item)
        order_id = random.randint(1000, 9999)  # 주문번호 생성
        print(f"[OrderSystem] {item} 주문 요약 반환 (가격: {price}원, 주문번호: #{order_id})")
        return {"item": item, "price": price, "order_id": order_id}

# 결제 모듈
class PaymentModule:
    def process_payment(self, amount):
        print(f"[PaymentModule] {amount}원 결제 요청 중...")
        success = random.choice([True, False])  # 결제 성공 or 실패
        return success

# 커피 머신
class CoffeeMachine:
    def make_coffee(self, item):
        print(f"[CoffeeMachine] {item} 제조 중...")
        print(f"[CoffeeMachine] {item} 제조 완료!")

# 키오스크 UI (메인 조정자)
class KioskUI:
    def __init__(self):
        self.menu = Menu()
        self.order_system = OrderSystem(self.menu)
        self.payment_module = PaymentModule()
        self.coffee_machine = CoffeeMachine()

    def start(self, item):
        print(f"[Customer] '{item}' 메뉴 선택")

        # alt: 메뉴 없음
        if item not in self.menu.items:
            print("[KioskUI] 잘못된 메뉴입니다. 다시 입력해주세요.")
            return

        print("[KioskUI] 주문 요청 중...")
        
        # alt: 품절
        order = self.order_system.create_order(item)
        if not order:
            print("[KioskUI] 품절 알림 → 고객에게 안내")
            print("[Customer] '죄송합니다. 해당 메뉴는 품절입니다.'")
            return

        print("[Customer] 결제 클릭")

        # alt: 결제 실패 / 결제 성공
        success = self.payment_module.process_payment(order["price"])
        if not success:
            print("[KioskUI] 결제 실패 응답 → 고객에게 알림")
            print("[Customer] '결제에 실패했습니다. 다시 시도해주세요.'")
            return

        print("[KioskUI] 결제 성공 응답 → 제조 요청")
        self.coffee_machine.make_coffee(order["item"])
        print(f"[Customer] '주문이 완료되었습니다. 주문번호: #{order['order_id']}'")

# 실행부
if __name__ == "__main__":
    ui = KioskUI()
    while True:
        item = input("\n[고객] 주문할 메뉴 입력 (아메리카노/라떼/모카, 종료하려면 'exit'): ")
        if item.lower() == 'exit':
            print("[시스템] 키오스크를 종료합니다.")
            break
        ui.start(item)
