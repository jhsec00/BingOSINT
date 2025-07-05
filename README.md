# BingOSINT

**BingOSINT**는 Bing 검색 결과를 HTML 기반으로 크롤링하여 특정 키워드에 대한 웹 링크, 제목, 내용을 수집하고 이를 엑셀(.xlsx)로 저장하는 OSINT 도구입니다.

## 🔍 주요 기능

- Bing 검색결과에서 **제목 / 링크 / 설명** 수집
- 수집된 데이터를 자동으로 엑셀로 저장
- 결과 엑셀 파일에 **자동 번호, 열 너비 조정, 테두리 적용**

## ⚠️ Bing 크롤링 주의사항

- Bing 공식 API를 사용하지 않고 HTML을 파싱하는 방식이므로 **User-Agent, 딜레이 설정**, 그리고 **쿠키 설정**이 필요합니다.
- 반드시 아래 두 쿠키 값을 **수동으로 복사해서 코드 내 headers에 넣어야 정상 작동**합니다:
  - `MUIDB`
  - `SRCHHPGUSR`

→ 크롬 개발자 도구(F12) > Application > Cookies 항목에서 `www.bing.com`의 값을 확인하여 직접 입력하세요.

예시:
```python
"Cookie": "MUIDB=...; SRCHHPGUSR=..."
```

## 💻 사용법

### 1. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 스크립트 실행

```bash
python bing_osint.py
```

### 3. 검색어 입력

```text
search(ex: site:https://google.com...)>site:github.com frida
```

띄어쓰기 포함 검색어도 그대로 입력하면 됩니다.

### 4. 출력결과

- 현재 경로에 `MMDD_hhmm_BingResult.xlsx` 형식으로 저장됩니다.
- 엑셀에는 `No`, `제목`, `링크`, `내용` 컬럼이 포함됩니다.
- 모든 셀에 테두리 및 열 너비 자동 조정이 적용됩니다.

---

✅ BingOSINT는 OSINT 조사, 버그 바운티 활동, 도메인 노출 확인 등에 유용하게 사용할 수 있습니다.
