#!/usr/bin/env python3
"""법무 문서 md → GitHub Pages용 스타일 HTML 빌드.

SSOT는 루트의 terms_of_service.md / privacy_policy.md.
이 문서들에서 쓰는 마크다운 부분집합(제목/굵게/코드/링크/목록(중첩)/문단)만 변환한다.
의존성 없음(표준 라이브러리). 문서 갱신 후 재실행:

    python scripts/build_legal_html.py
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

PAGES = [
    ("terms_of_service.md", "terms-of-service.html", "이용약관 (Terms of Service)"),
    ("privacy_policy.md", "privacy-policy.html", "개인정보처리방침 (Privacy Policy)"),
]

STYLE = """
  :root{
    --bg:#ffffff; --fg:#1a1a1a; --muted:#5c6370; --line:#e3e6ea;
    --accent:#2563eb; --card:#f7f8fa;
  }
  @media (prefers-color-scheme: dark){
    :root{ --bg:#15171a; --fg:#e8eaed; --muted:#9aa3af; --line:#2c3036;
           --accent:#7aa2f7; --card:#1c1f24; }
  }
  *{box-sizing:border-box}
  body{
    margin:0; background:var(--bg); color:var(--fg);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans KR",
                "Malgun Gothic",Roboto,Helvetica,Arial,sans-serif;
    line-height:1.75; font-size:16px;
  }
  .wrap{max-width:720px; margin:0 auto; padding:40px 20px 96px}
  header{border-bottom:1px solid var(--line); padding-bottom:24px; margin-bottom:36px}
  h1{font-size:1.6rem; line-height:1.35; margin:0 0 10px}
  h2{font-size:1.15rem; margin:44px 0 12px}
  .lead{color:var(--muted); margin:0; font-size:.95rem}
  ol,ul{padding-left:22px} li{margin:6px 0}
  a{color:var(--accent)}
  .updated{color:var(--muted); font-size:.9rem}
  footer{margin-top:56px; padding-top:20px; border-top:1px solid var(--line);
         color:var(--muted); font-size:.88rem}
  @media (max-width:520px){
    .wrap{padding:28px 16px 72px} h1{font-size:1.35rem}
  }
"""

TEMPLATE = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — TTSTextReader</title>
<style>{style}</style>
</head>
<body><div class="wrap">

<header>
  <h1>{title}</h1>
  <p class="lead">앱: <strong>TTSTextReader</strong> · 개발자: kybirdlabs · 문의:
    <a href="mailto:kybirdlabs@gmail.com">kybirdlabs@gmail.com</a></p>
</header>

{body}

<footer>
  <a href="./terms-of-service.html">이용약관</a> ·
  <a href="./privacy-policy.html">개인정보처리방침</a> ·
  <a href="./account-deletion.html">계정 및 데이터 삭제</a> ·
  <a href="./index.html">지원 홈</a>
</footer>

</div></body>
</html>
"""

CODE_RE = re.compile(r"`([^`]+)`")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")

# 웹 빌드에서 문서 간 상대 링크(.md)는 같은 문서의 .html 판으로 바꾼다.
# 앱(raw md) 쪽은 .md 상대 링크가 그대로 유효하므로 원문은 손대지 않는다.
MD_TO_HTML = {md: out for md, out, _ in PAGES}


def inline(text: str) -> str:
    out = html.escape(text, quote=False)
    out = CODE_RE.sub(r"<code>\1</code>", out)

    def link_repl(m: re.Match) -> str:
        href = MD_TO_HTML.get(m.group(2), m.group(2))
        return f'<a href="{html.escape(href, quote=True)}">{m.group(1)}</a>'

    out = LINK_RE.sub(link_repl, out)
    out = BOLD_RE.sub(r"<strong>\1</strong>", out)
    return out


ITEM_RE = re.compile(r"^(\s*)(?:(\d+)\.\s+|-\s+)(.*)$")


def render(markdown: str) -> str:
    lines_out: list[str] = []
    para: list[str] = []
    # (type, indent) 스택 — 중첩 목록(제4조: ol 안 ul) 지원.
    stack: list[tuple[str, int]] = []

    def flush_para() -> None:
        if para:
            lines_out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def close_to(indent: int) -> None:
        while stack and stack[-1][1] > indent:
            t, _ = stack.pop()
            lines_out.append(f"</li></{t}>")

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            continue
        if line.strip() == "---":
            flush_para()
            continue
        if line.startswith("## "):
            flush_para()
            close_to(-1)
            lines_out.append(f"<h2>{inline(line[3:])}</h2>")
            continue
        if line.startswith("# "):
            # h1은 템플릿 헤더가 담당 — 본문에서는 건너뛴다.
            continue
        m = ITEM_RE.match(line)
        if m:
            flush_para()
            indent_ws, num, content = m.group(1), m.group(2), m.group(3)
            indent = len(indent_ws)
            typ = "ol" if num else "ul"
            close_to(indent)
            if stack and stack[-1][1] == indent:
                if stack[-1][0] == typ:
                    lines_out.append("</li><li>")
                else:
                    t, _ = stack.pop()
                    lines_out.append(f"</li></{t}><{typ}><li>")
            else:
                lines_out.append(f"<{typ}>")
                stack.append((typ, indent))
                lines_out.append("<li>")
            lines_out.append(inline(content))
            continue
        # 본문 문단은 열려 있는 목록을 닫는다.
        if stack:
            close_to(-1)
        if line.startswith("**최종 업데이트**"):
            flush_para()
            close_to(-1)
            lines_out.append(f'<p class="updated">{inline(line)}</p>')
            continue
        para.append(line.strip())

    flush_para()
    close_to(-1)
    return "\n".join(lines_out)


def main() -> int:
    for md_name, html_name, title in PAGES:
        md_path = REPO / md_name
        if not md_path.exists():
            print(f"skip: {md_name} 없음", file=sys.stderr)
            continue
        doc = TEMPLATE.format(
            title=title,
            style=STYLE,
            body=render(md_path.read_text(encoding="utf-8")),
        )
        out = REPO / html_name
        out.write_text(doc, encoding="utf-8", newline="\n")
        print(f"{md_name} -> {html_name} ({len(doc)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
