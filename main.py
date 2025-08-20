class TicTacToe:
    def __init__(self):
        # 3x3 보드 초기화 (빈 칸은 ' '로 표시)
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # X가 먼저 시작
        self.game_over = False
        self.winner = None

    def display_board(self):
        """
        현재 보드 상태를 출력하는 함수
        담당자: Person A가 구현 예정
        """
        # TODO: 보드를 예쁘게 출력하는 코드 작성
        print("보드 출력 기능 - Person A가 구현 예정")
        pass

    def make_move(self, row, col):
        """
        플레이어의 수를 보드에 반영하는 함수
        담당자: Person A가 구현 예정
        Args:
            row (int): 행 위치 (0-2)
            col (int): 열 위치 (0-2)
        Returns:
            bool: 유효한 수인지 여부
        """
        # TODO: 
        # 1. 해당 위치가 비어있는지 확인
        # 2. 비어있다면 현재 플레이어의 마크 놓기
        # 3. 플레이어 턴 바꾸기
        # 4. 성공 여부 반환
        print(f"수 놓기 기능 - Person A가 구현 예정: ({row}, {col})")
        return False

    def check_winner(self):
        """
        승부 판정을 하는 함수
        담당자: Person B가 구현 예정
        Returns:
            str: 승자 ('X', 'O', 'Tie', None)
        """
        # TODO:
        # 1. 가로 3줄 체크
        # 2. 세로 3줄 체크  
        # 3. 대각선 2줄 체크
        # 4. 무승부 체크 (보드가 가득 참)
        print("승부 판정 기능 - Person B가 구현 예정")
        return None

    def is_board_full(self):
        """
        보드가 가득 찼는지 확인하는 함수
        담당자: Person B가 구현 예정
        Returns:
            bool: 보드가 가득 찼는지 여부
        """
        # TODO: 모든 칸이 채워져 있는지 확인
        print("보드 가득참 체크 - Person B가 구현 예정")
        return False

    def get_user_input(self):
        """
        사용자로부터 입력을 받는 함수
        담당자: Person A가 구현 예정
        Returns:
            tuple: (row, col) 좌표
        """
        # TODO:
        # 1. 사용자에게 좌표 입력 요청
        # 2. 입력값 검증 (0-2 범위, 숫자인지 등)
        # 3. 유효한 좌표 반환
        print("사용자 입력 기능 - Person A가 구현 예정")
        return (0, 0)

    def reset_game(self):
        """
        게임을 초기화하는 함수
        담당자: Person B가 구현 예정
        """
        # TODO: 
        # 1. 보드 초기화
        # 2. 현재 플레이어를 X로 설정
        # 3. 게임 상태 초기화
        print("게임 리셋 기능 - Person B가 구현 예정")
        pass


def main():
    """
    메인 게임 루프
    """
    print("=== 틱택토 게임에 오신 것을 환영합니다! ===")
    print("좌표는 0-2 사이의 숫자로 입력하세요.")
    print("예: 1 1 (가운데 칸)")
    
    game = TicTacToe()
    
    while not game.game_over:
        # 현재 보드 상태 출력
        game.display_board()
        
        # 현재 플레이어 표시
        print(f"\n현재 차례: {game.current_player}")
        
        # 사용자 입력 받기
        try:
            row, col = game.get_user_input()
            
            # 수 놓기 시도
            if game.make_move(row, col):
                # 승부 판정
                winner = game.check_winner()
                if winner:
                    game.display_board()
                    if winner == 'Tie':
                        print("무승부입니다!")
                    else:
                        print(f"플레이어 {winner}의 승리!")
                    game.game_over = True
                    game.winner = winner
            else:
                print("유효하지 않은 수입니다. 다시 시도하세요.")
                
        except KeyboardInterrupt:
            print("\n게임을 종료합니다.")
            break
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")
    
    # 게임 종료 후 재시작 여부 확인
    if game.game_over:
        restart = input("\n다시 게임하시겠습니까? (y/n): ")
        if restart.lower() == 'y':
            game.reset_game()
            main()  # 재귀 호출로 게임 재시작


if __name__ == "__main__":
    main()