import sys
import logging
import requests
from datetime import datetime
from typing import List, Dict
from dataclasses import dataclass
import io
import sys

# 터미널 한글 깨짐 방지 (Windows용 땜질)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 로깅 설정: 깔끔하게 포맷팅
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)] # sys.stdout으로 명시
)
logger = logging.getLogger(__name__)

@dataclass
class GitHubConfig:
    username: str
    api_url: str = "https://api.github.com/users/{}/events/public"

class GitHubActivityMonitor:
    """
    GitHub 사용자 활동 모니터링 모듈
    """
    
    def __init__(self, username: str):
        if not username:
            raise ValueError("사용자 ID가 입력되지 않았습니다.")
        self.config = GitHubConfig(username=username)

    def _fetch_events(self) -> List[Dict]:
        """GitHub API에서 공개 이벤트 목록을 조회합니다."""
        url = self.config.api_url.format(self.config.username)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"GitHub API 호출 중 오류 발생: {e}")
            return []

    def check_today_push_event(self) -> bool:
        """
        금일 PushEvent 발생 여부를 확인합니다.
        
        Returns:
            bool: 커밋 활동이 있으면 True, 없으면 False
        """
        events = self._fetch_events()
        if not events:
            logger.warning("조회된 이벤트가 없거나 API 호출에 실패했습니다.")
            return False

        # 서버 로컬 시간 기준 오늘 날짜
        today_str = datetime.now().strftime("%Y-%m-%d")
        
        push_events = [
            event for event in events
            if event.get('type') == 'PushEvent' 
            and event.get('created_at', '').startswith(today_str)
        ]

        commit_count = len(push_events)

        if commit_count > 0:
            logger.info(f"금일 커밋 활동이 확인되었습니다. (횟수: {commit_count}회)")
            return True
        else:
            logger.info("금일 커밋 이력이 존재하지 않습니다.")
            return False

if __name__ == "__main__":
    # 여기에 아이디 넣기
    TARGET_USER = "MinDongIl" 
    
    try:
        monitor = GitHubActivityMonitor(TARGET_USER)
        has_activity = monitor.check_today_push_event()
        
        if not has_activity:
            # 커밋 없음: 종료 코드 1 반환 (추후 배치 작업에서 실패로 처리됨)
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"시스템 예외 발생: {e}")
        sys.exit(1)