import random


class Generator:
    """한국어 닉네임 생성기 클래스"""

    ADJECTIVES = [
        "빠른", "느린", "귀여운", "심쿵", "용감한", "재밌는", "우울한",
        "행복한", "차가운", "뜨거운", "멋진", "고독한", "상쾌한", "새침한",
        "활발한", "엉뚱한", "똑똑한", "어두운", "밝은", "화려한", "차분한",
        "섹시한", "쿨한", "깜찍한", "든든한", "순수한", "부드러운", "쌈박한",
        "웃긴", "진지한", "시크한", "단단한", "예쁜", "청순한", "잔망스러운"
    ]

    NOUNS = [
        "여우", "고래", "사자", "토끼", "호랑이", "펭귄", "곰", "늑대",
        "햄스터", "독수리", "다람쥐", "돌고래", "너구리", "침팬지", "판다",
        "앵무새", "고양이", "강아지", "치타", "돌고래", "악어", "수달",
        "참새", "비둘기", "부엉이", "매", "하마", "기린", "코끼리",
        "두더지", "까치", "문어", "오리", "너구리", "두루미", "해달"
    ]

    def __init__(self, adjectives=None, nouns=None, use_number=True, number_range=(1, 99)):
        """
        :param adjectives: 사용자 정의 형용사 리스트 (없으면 기본값 사용)
        :param nouns: 사용자 정의 명사 리스트 (없으면 기본값 사용)
        :param use_number: 닉네임 끝에 숫자 붙일지 여부
        :param number_range: 숫자를 붙일 경우 (최소, 최대) 범위
        """
        self.adjectives = adjectives if adjectives else self.ADJECTIVES
        self.nouns = nouns if nouns else self.NOUNS
        self.use_number = use_number
        self.number_range = number_range

    def generate_k_nickname(self):
        adj = random.choice(self.adjectives)
        noun = random.choice(self.nouns)

        if self.use_number:
            number = random.randint(*self.number_range)
            return f"{adj}{noun}{number}"
        else:
            return f"{adj}{noun}"
            
