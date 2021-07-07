
class ValueCalculator:
    def __init__(self, val: str):
        self.val = val
    def __add__(self, other):
        return self.val + other.val

# 공통적으로 쓰이는 클래스(import로 실행될때 모아놓음) ==> 여러 스크립트에서 사용되는 기능을 하나에 모아 놓고 스크립트에서 이 파일과 클래스를 불러와서 사용
print(__name__)
if __name__ == "__main__":
    print('hi')           #이 파일의 클래스를 import로 실행할때 이 출력함수가 안 나오고 이 파일 자체를 실행했을때만 hi가 나오도록


