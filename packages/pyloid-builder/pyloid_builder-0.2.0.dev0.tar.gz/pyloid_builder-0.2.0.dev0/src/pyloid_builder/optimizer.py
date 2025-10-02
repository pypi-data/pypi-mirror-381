import os
import shutil
from pathlib import Path
from typing import List
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.layout import Layout


def optimize(name: str, distpath: str, files_to_remove: List[str] = None):
    """
    Optimize the application size by removing unnecessary files from __internal folder.
    for pyloid applications.

    Parameters
    ----------
    name : str
        The name of the application to optimize.
    distpath : str
        The path to the application to optimize.
    files_to_remove : List[str], optional
        List of files/folders to remove from __internal directory.
        If None, uses default list of common unnecessary files.
    """
    console = Console()

    # 터미널 크기 가져오기
    terminal_height = console.size.height
    terminal_width = console.size.width

    # 좌측 정보 패널 너비 동적 계산 (전체 너비의 45%, 최소 45)
    info_panel_width = max(45, int(terminal_width * 0.45))

    if files_to_remove is None:
        files_to_remove = [
            # Common unnecessary files in PyInstaller apps
            "tcl",
            "tk",
            "test",
            "unittest",
            "pydoc",
            "pdb",
            "profile",
            "cgitb",
            "idlelib",
            "turtledemo",
            "tkinter",
            "turtledemo",
            "test",
            "tests",
            "*.pyc",
            "__pycache__",
            "*.pyo",
            "*.pyd",
            "distutils",
            "setuptools",
            "pip",
            "wheel",
            "venv",
            "env",
            "Lib/site-packages/pip*",
            "Lib/site-packages/setuptools*",
            "Lib/site-packages/wheel*",
            "Lib/site-packages/distutils*",
        ]

    app_path = Path(distpath) / name
    internal_path = app_path / "_internal"

    if not internal_path.exists():
        console.print(f"[bold yellow]⚠ Warning: {internal_path} not found. Skipping optimization.[/bold yellow]")
        return

    # 파일 목록을 보기 좋게 포맷팅
    def format_file_list(files_list):
        if not files_list:
            return "[dim]None[/dim]"

        formatted_lines = []
        max_line_length = max(35, info_panel_width - 12)

        for file_item in files_list:
            # 각 파일을 별도 줄로 표시하되, 너무 길면 축약
            if len(file_item) > max_line_length - 2:
                display_item = file_item[:max_line_length-5] + "..."
            else:
                display_item = file_item
            formatted_lines.append(f"• [bold yellow]{display_item}[/bold yellow]")

        return "\n".join(formatted_lines)

    # 정보 패널 내용
    formatted_files = format_file_list(files_to_remove)
    files_lines = len(formatted_files.split('\n'))
    info_content_lines = 3 + files_lines  # Application(1줄) + Path(1줄) + Files(1줄 + 여러 줄)
    info_panel_height = info_content_lines + 4  # 내용 + 테두리 + 타이틀

    # 로그 박스 높이 동적 계산 (터미널 높이의 85%, 최소 15줄)
    available_height = max(15, int(terminal_height * 0.85))
    log_box_height = available_height

    # 최대 로그 라인 수 계산 (박스 높이 - 테두리 - 여유 공간)
    max_log_lines = log_box_height - 6

    # 상단 고정 정보 패널 생성 - 정보 표시 개선
    info_panel = Panel(
        f"[bold green]📱 Application:[/bold green] [white]{name}[/white]\n"
        f"[bold green]📂 Path:[/bold green] [white]{distpath}[/white]\n"
        f"[bold green]🗑️  Files to Remove:[/bold green]\n{formatted_files}",
        title="[bold blue]🧹 Optimization Info[/bold blue]",
        border_style="blue",
        width=info_panel_width,
        height=info_panel_height
    )

    # 로그를 담을 텍스트 객체
    log_text = Text("", style="dim white")
    log_panel = Panel.fit(
        log_text,
        title="[bold green]📋 Optimization Log[/bold green]",
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

    console.print("[bold blue]Starting optimization process...[/bold blue]\n")

    removed_count = 0
    total_size_saved = 0

    # 파일 크기 계산 함수
    def get_size(path):
        total = 0
        for file in path.rglob('*'):
            if file.is_file():
                total += file.stat().st_size
        return total

    # 최적화 전 크기 측정
    initial_size = get_size(internal_path)
    update_log(f"[Initial] __internal size: {initial_size / 1024 / 1024:.2f} MB")

    with Live(layout, console=console, refresh_per_second=4) as live:
        for file_pattern in files_to_remove:
            update_log(f"[Scanning] pattern: {file_pattern}")

            # Handle both files and directories
            for item in internal_path.rglob(file_pattern):
                if item.is_file() or item.is_dir():
                    try:
                        item_size = get_size(item) if item.is_dir() else item.stat().st_size

                        if item.is_dir():
                            shutil.rmtree(item)
                            update_log(f"[DIR] Removed directory: {item.relative_to(internal_path)} ({item_size / 1024:.1f} KB)")
                        else:
                            item.unlink()
                            update_log(f"[FILE] Removed file: {item.relative_to(internal_path)} ({item_size / 1024:.1f} KB)")

                        removed_count += 1
                        total_size_saved += item_size

                    except Exception as e:
                        update_log(f"[ERROR] removing {item.relative_to(internal_path)}: {e}")

            live.update(layout)  # 레이아웃 업데이트

        # 최적화 완료 후 최종 크기 계산
        final_size = get_size(internal_path)
        size_reduction = initial_size - final_size

        update_log(f"[SUCCESS] Optimization complete!")
        update_log(f"[STATS] Items removed: {removed_count}")
        update_log(f"[STATS] Size reduction: {size_reduction / 1024 / 1024:.2f} MB")
        update_log(f"[STATS] Final __internal size: {final_size / 1024 / 1024:.2f} MB")

        # 성공 상태로 패널 업데이트
        log_panel.border_style = "green"
        log_panel.title = "[bold green]Optimization Complete[/bold green]"
        live.update(layout)

    console.print("\n[bold green]Optimization completed successfully![/bold green]")
    console.print(f"[dim]Results: {removed_count} items removed, {size_reduction / 1024 / 1024:.2f} MB saved[/dim]")
