def solution(players, callings):
    # 1. 선수의 이름과 현재 등수를 저장할 딕셔너리 생성
    # {"mumu": 0, "soe": 1, ...} 형태
    player_indices = {player: idx for idx, player in enumerate(players)}
    
    for called in callings:
        # 2. 호명된 선수의 현재 등수와 바로 앞 선수의 등수 찾기
        current_idx = player_indices[called]
        front_idx = current_idx - 1
        
        # 3. 바로 앞 선수의 이름 가져오기
        front_player = players[front_idx]
        
        # 4. players 배열에서 두 선수의 위치를 스왑(추월)
        players[front_idx], players[current_idx] = players[current_idx], players[front_idx]
        
        # 5. 딕셔너리(해시맵)에서도 등수 정보를 갱신
        player_indices[called] = front_idx
        player_indices[front_player] = current_idx
        
    return players