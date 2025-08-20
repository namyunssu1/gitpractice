# Person B가 구현할 함수들 (게임 로직 관련)

def check_winner(self):
    """
    승부 판정을 하는 함수
    Returns:
        str: 승자 ('X', 'O', 'Tie', None)
    """
    # 가로 3줄 체크
    for row in range(3):
        if (self.board[row][0] == self.board[row][1] == self.board[row][2] != ' '):
            return self.board[row][0]
    
    # 세로 3줄 체크
    for col in range(3):
        if (self.board[0][col] == self.board[1][col] == self.board[2][col] != ' '):
            return self.board[0][col]
    
    # 대각선 체크 (좌상->우하)
    if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ' '):
        return self.board[0][0]
    
    # 대각선 체크 (우상->좌하)
    if (self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
        return self.board[0][2]
    
    # 무승부 체크 (보드가 가득 참)
    if self.is_board_full():
        return 'Tie'
    
    # 아직 게임이 끝나지 않음
    return None

def is_board_full(self):
    """
    보드가 가득 찼는지 확인하는 함수
    Returns:
        bool: 보드가 가득 찼는지 여부
    """
    for row in range(3):
        for col in range(3):
            if self.board[row][col] == ' ':
                return False
    return True

def reset_game(self):
    """
    게임을 초기화하는 함수
    """
    # 보드 초기화
    self.board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # 현재 플레이어를 X로 설정
    self.current_player = 'X'
    
    # 게임 상태 초기화
    self.game_over = False
    self.winner = None
    
    print("게임이 초기화되었습니다!")

# Person B가 추가로 구현할 수 있는 보조 함수들:

def get_empty_positions(self):
    """
    빈 칸들의 위치를 반환하는 함수 (AI 구현시 유용)
    Returns:
        list: 빈 칸들의 (row, col) 좌표 리스트
    """
    empty_positions = []
    for row in range(3):
        for col in range(3):
            if self.board[row][col] == ' ':
                empty_positions.append((row, col))
    return empty_positions

def check_line_winner(self, positions):
    """
    주어진 3개 위치가 같은 플레이어인지 확인하는 보조 함수
    Args:
        positions (list): 3개의 (row, col) 좌표 리스트
    Returns:
        str: 승자 또는 None
    """
    values = [self.board[row][col] for row, col in positions]
    if values[0] == values[1] == values[2] != ' ':
        return values[0]
    return None

# Person B가 메인 파일에서 교체해야 할 부분들:

# 1. check_winner 함수 교체
# 2. is_board_full 함수 교체
# 3. reset_game 함수 교체
# 4. 원한다면 보조 함수들도 추가