# Person A가 구현할 함수들 (UI/입력 관련)

def display_board(self):
    """
    현재 보드 상태를 출력하는 함수
    """
    print("\n   0   1   2")
    for i in range(3):
        print(f"{i}  {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
        if i < 2:
            print("  ---|---|---")
    print()

def make_move(self, row, col):
    """
    플레이어의 수를 보드에 반영하는 함수
    Args:
        row (int): 행 위치 (0-2)
        col (int): 열 위치 (0-2)
    Returns:
        bool: 유효한 수인지 여부
    """
    # 좌표가 범위를 벗어났는지 확인
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    
    # 해당 위치가 비어있는지 확인
    if self.board[row][col] != ' ':
        return False
    
    # 현재 플레이어의 마크 놓기
    self.board[row][col] = self.current_player
    
    # 플레이어 턴 바꾸기
    if self.current_player == 'X':
        self.current_player = 'O'
    else:
        self.current_player = 'X'
    
    return True

def get_user_input(self):
    """
    사용자로부터 입력을 받는 함수
    Returns:
        tuple: (row, col) 좌표
    """
    while True:
        try:
            user_input = input("행과 열을 입력하세요 (예: 1 2): ").strip()
            
            # 공백으로 분리
            parts = user_input.split()
            
            # 입력값이 2개인지 확인
            if len(parts) != 2:
                print("행과 열 두 개의 숫자를 입력해주세요.")
                continue
            
            # 숫자로 변환
            row = int(parts[0])
            col = int(parts[1])
            
            # 범위 확인 (0-2)
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("0부터 2 사이의 숫자를 입력해주세요.")
                continue
            
            return (row, col)
            
        except ValueError:
            print("숫자만 입력해주세요.")
        except KeyboardInterrupt:
            print("\n게임을 종료합니다.")
            raise
        except Exception as e:
            print(f"입력 오류: {e}")

# Person A가 메인 파일에서 교체해야 할 부분들:

# 1. display_board 함수 교체
# 2. make_move 함수 교체  
# 3. get_user_input 함수 교체