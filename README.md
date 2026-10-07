# Drill #9: 소년 상하좌우 이동

`pico2d`로 만든 방향키 이동 과제입니다. 배경은 `TUK_GROUND.png`, 소년 애니메이션은 `animation_sheet.png`를 사용합니다.

## 실행

Python과 `pico2d`가 설치된 환경에서 다음 명령을 실행합니다.

```powershell
cd DRILL_09
python drill09.py
```

이미지 경로는 `drill09.py`의 위치를 기준으로 찾으므로 상위 폴더에서 `python .\DRILL_09\drill09.py`로 실행해도 됩니다.

## 조작

| 키 | 동작 |
| --- | --- |
| `←` / `→` | 좌우 이동 및 바라보는 방향 변경 |
| `↑` / `↓` | 현재 바라보는 방향을 유지하면서 상하 이동 |
| `Esc` | 종료 |

멈추면 바라보는 방향의 IDLE 애니메이션이 재생됩니다. 화면 가장자리에서는 소년 이미지가 화면 밖으로 나가지 않습니다.

## 확인

```powershell
python -m unittest -v test_drill09.py
```

과제 요구사항과 검증 항목은 `PRD.MD`에 정리되어 있습니다.
