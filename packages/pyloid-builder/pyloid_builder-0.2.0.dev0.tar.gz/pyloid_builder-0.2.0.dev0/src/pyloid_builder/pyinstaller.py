from typing import List
import subprocess
import sys
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.layout import Layout

def pyinstaller(scriptname: str, options: List[str]):
    """
    Build a PyInstaller application for Pyloid.
    
    Parameters
    ----------
    scriptname : str
        The name of the script to build.
    options : List[str]
        The options to pass to PyInstaller. (https://pyinstaller.org/en/stable/usage.html#options)
    """

    console = Console()

    # 터미널 크기 가져오기
    terminal_height = console.size.height
    terminal_width = console.size.width

    # 좌측 정보 패널 너비 동적 계산 (전체 너비의 50%, 최소 40)
    info_panel_width = max(40, int(terminal_width * 0.5))

    # 옵션들을 보기 좋게 포맷팅 (여러 줄로 나누기)
    def format_options(options_list):
        if not options_list:
            return "None"

        # 각 옵션을 별도의 줄로 표시하되, 너무 길면 줄바꿈
        formatted_lines = []
        current_line = ""
        max_line_length = max(30, info_panel_width - 10)  # 패널 너비 고려

        for option in options_list:
            if len(current_line) + len(option) + 1 <= max_line_length:
                current_line += (" " + option) if current_line else option
            else:
                if current_line:
                    formatted_lines.append(current_line)
                current_line = option

        if current_line:
            formatted_lines.append(current_line)

        return "\n".join(formatted_lines)

    # 정보 패널 내용
    formatted_options = format_options(options)
    options_lines = len(formatted_options.split('\n'))
    info_content_lines = 1 + options_lines  # Script(1줄) + Options(여러 줄)
    info_panel_height = info_content_lines + 4  # 내용 + 테두리 + 타이틀

    # 로그 박스 높이 동적 계산 (터미널 높이의 80%, 최소 10줄)
    available_height = max(10, int(terminal_height * 0.8))
    log_box_height = available_height

    # 최대 로그 라인 수 계산 (박스 높이 - 테두리)
    max_log_lines = log_box_height - 4

    # 상단 고정 정보 패널 생성
    info_panel = Panel(
        f"[bold cyan]Script:[/bold cyan] {scriptname}\n"
        f"[bold cyan]Options:[/bold cyan]\n{formatted_options}",
        title="[bold blue]PyInstaller Build Info[/bold blue]",
        border_style="blue",
        width=info_panel_width,
        height=info_panel_height
    )

    # 로그를 담을 텍스트 객체
    log_text = Text("", style="dim white")
    log_panel = Panel.fit(
        log_text,
        title="[bold green]Build Log[/bold green]",
        border_style="green",
        height=log_box_height
    )

    # 레이아웃 생성
    layout = Layout()
    layout.split_row(
        Layout(info_panel, name="info", size=info_panel_width),  # 좌측: 동적 너비 정보
        Layout(log_panel, name="log")                           # 우측: 로그 박스
    )

    def update_log(new_line: str):
        """로그 텍스트 업데이트"""
        current_text = str(log_text.plain)
        log_text.plain = current_text + new_line + "\n"
        # 최신 로그를 위해 최대 라인 수만큼만 유지
        lines = log_text.plain.split('\n')
        if len(lines) > max_log_lines:
            log_text.plain = '\n'.join(lines[-max_log_lines:])

    try:
        console.print("[bold blue]🚀 Starting PyInstaller build...[/bold blue]\n")

        # PyInstaller 명령어 준비
        cmd = [sys.executable, "-m", "PyInstaller", scriptname] + options

        # Live 표시 시작
        with Live(layout, console=console, refresh_per_second=4) as live:
            # subprocess로 PyInstaller 실행
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )

            # 실시간으로 출력 캡처
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    update_log(output.strip())
                    live.update(layout)  # 레이아웃 업데이트

            # 프로세스 완료 대기
            return_code = process.wait()

            if return_code == 0:
                # 성공 메시지
                update_log("✓ Build completed successfully!")
                log_panel.border_style = "green"
                log_panel.title = "[bold green]✓ Build Complete[/bold green]"
                live.update(layout)

                console.print("\n[bold green]🎉 Your application has been built![/bold green]")
                console.print("[dim]Check the 'dist' folder for the executable.[/dim]")
            else:
                # 실패 메시지
                update_log(f"✗ Build failed with return code: {return_code}")
                log_panel.border_style = "red"
                log_panel.title = "[bold red]✗ Build Failed[/bold red]"
                live.update(layout)

                console.print(f"\n[bold red]❌ Build failed with return code: {return_code}[/bold red]")
                raise Exception(f"PyInstaller build failed with return code: {return_code}")

    except FileNotFoundError:
        console.print("\n[bold red]❌ Error: PyInstaller not found. Please install PyInstaller.[/bold red]")
        raise
    except Exception as e:
        console.print(f"\n[bold red]❌ Error occurred during build: {str(e)}[/bold red]")
        raise