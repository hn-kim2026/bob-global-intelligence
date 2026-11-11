BOB v19 무료 온라인 RSS 수집기 설치 안내 (GitHub)

준비: 무료 GitHub 계정, 인터넷, v19 HTML 파일. 이 설정은 처음 한 번 사람이 직접 해야 합니다.

1. github.com 로그인 → 오른쪽 + → New repository.
2. 저장소 이름 예: bob-news-feed. Public 선택 → Create repository.
3. Add file → Upload files를 사용해 collector.py와 docs/index.json을 업로드합니다.
   docs/index.json은 docs 폴더 안에 있어야 합니다.
4. .github/workflows/collect.yml 파일도 같은 폴더 구조로 올립니다.
   GitHub 웹 화면에서 Add file → Create new file을 눌러 파일명에
   .github/workflows/collect.yml을 입력하고 ZIP 안의 내용을 붙여 넣어도 됩니다.
5. 저장소 Settings → Actions → General → Workflow permissions에서
   Read and write permissions 선택 후 Save (허용되는 경우).
6. Actions 탭 → BOB RSS collection → Run workflow → Run workflow.
   작업이 완료되어 docs/index.json에 실제 기사 목록이 생겼는지 확인합니다.
7. Settings → Pages → Build and deployment → Deploy from a branch 선택.
   Branch: main, Folder: /docs 선택 → Save.
8. 수 분 후 다음 주소가 열리는지 확인합니다:
   https://내GitHub아이디.github.io/bob-news-feed/index.json
   (저장소 이름이 다르면 주소도 바꿔 주세요.)
9. v19 HTML 파일을 Edge로 열어 위 주소를 입력하고
   '온라인 수집함 가져오기' 버튼을 누릅니다.

중요:
- GitHub Pages는 공개 사이트입니다. 개인정보나 비밀 정보를 올리지 마세요.
- GitHub Actions 예약 작업은 정확한 시각 실행이 보장되지 않으며 지연/중단될 수 있습니다.
- 무료 제공 범위 및 사용 조건은 GitHub 정책에 따라 달라집니다.
- 일부 RSS 피드는 변경되거나 차단될 수 있습니다. 수집기는 실패한 정보원을 기록합니다.
- RSS 기사 제목/URL은 사실검증이 아닙니다.
- 이 ZIP은 자동 설치 프로그램이 아닙니다. GitHub 설정은 사용자가 직접 수행해야 합니다.
- GitHub 계정 비밀번호나 토큰을 BOB HTML에 입력하지 마세요.
