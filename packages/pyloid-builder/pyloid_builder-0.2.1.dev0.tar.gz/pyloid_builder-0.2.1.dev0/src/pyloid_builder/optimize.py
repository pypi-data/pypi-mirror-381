import os
import shutil
import time
from typing import List, Tuple
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.layout import Layout
from rich.padding import Padding

def optimize(name: str, distpath: str, remove_list: List[str]):
    """
    PyInstaller 빌드 결과물에서 불필요한 파일을 제거하여 최적화합니다.

    Parameters
    ----------
    name : str
        빌드된 애플리케이션의 이름 (PyInstaller --name 옵션과 동일).
    distpath : str
        빌드 결과물이 위치한 'dist' 폴더의 경로.
    remove_list : List[str]
        제거할 파일 또는 폴더의 목록.
    """
    console = Console()

    # 최적화 대상 경로
    target_dir = os.path.join(distpath, name, "_internal")

    # 터미널 크기 가져오기
    terminal_width = console.size.width

    # 좌측 정보 패널 너비 동적 계산 (전체 너비의 50%, 최소 40)
    info_panel_width = max(40, int(terminal_width * 0.5))

    def get_size_info(path: str) -> Tuple[int, int, int]:
        """경로의 크기 정보를 반환 (총 크기, 파일 수, 폴더 수)"""
        total_size = 0
        file_count = 0
        dir_count = 0

        if os.path.isfile(path):
            total_size = os.path.getsize(path)
            file_count = 1
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                dir_count += len(dirs)
                for file in files:
                    try:
                        total_size += os.path.getsize(os.path.join(root, file))
                        file_count += 1
                    except OSError:
                        pass
            dir_count += 1  # 현재 디렉토리 포함

        return total_size, file_count, dir_count

    def format_size(size_bytes: int) -> str:
        """바이트를 사람이 읽기 쉬운 형식으로 변환"""
        if size_bytes == 0:
            return "0 B"
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} GB"

    # 제거 목록을 보기 좋게 포맷팅
    def format_remove_list(items: List[str]):
        if not items:
            return "None"
        
        formatted_lines = []
        current_line = ""
        max_line_length = max(30, info_panel_width - 10)

        for item in items:
            if len(current_line) + len(item) + 2 <= max_line_length:
                current_line += (", " + item) if current_line else item
            else:
                if current_line:
                    formatted_lines.append(current_line)
                current_line = item
        
        if current_line:
            formatted_lines.append(current_line)
            
        return "\n".join(formatted_lines)

    # 정보 패널 내용 - 동적 업데이트를 위해 함수로 변경
    def create_info_panel(processed=0, total_size_saved=0, current_item=""):
        formatted_list = format_remove_list(remove_list)
        progress_percent = int((processed / len(remove_list)) * 100) if remove_list else 0

        panel_content = (
            f"[bold cyan]Target Directory:[/bold cyan]\n[dim]{target_dir}[/dim]\n\n"
            f"[bold cyan]Remove List ({len(remove_list)} items):[/bold cyan]\n{formatted_list}\n\n"
            f"[bold cyan]Progress:[/bold cyan] {processed}/{len(remove_list)} ({progress_percent}%)\n"
            f"[bold cyan]Space Saved:[/bold cyan] {format_size(total_size_saved)}\n"
        )

        if current_item:
            panel_content += f"[bold cyan]Processing:[/bold cyan] {current_item}"

        return Panel(
            panel_content,
            title="[bold blue]Optimization Progress[/bold blue]",
            border_style="blue",
            width=info_panel_width,
        )

    # 초기 정보 패널 생성
    info_panel = create_info_panel()

    # 로그를 담을 텍스트 객체
    log_text = Text("", style="dim white")
    log_panel = Panel(
        log_text,
        title="[bold green]Optimization Log[/bold green]",
        border_style="green"
    )

    # 레이아웃 생성
    layout = Layout()
    layout.split_row(
        Layout(info_panel, name="info", size=info_panel_width),
        Layout(log_panel, name="log")
    )

    # 레이아웃 업데이트 함수
    def update_layout(processed=0, total_size_saved=0, current_item=""):
        layout["info"].update(create_info_panel(processed, total_size_saved, current_item))

    log_lines = []
    max_log_lines = console.size.height - 6  # 패널 높이를 고려한 최대 라인 수

    def update_log(new_line: str, style: str = "white"):
        """로그 텍스트 업데이트 (스크롤 기능 포함)"""
        log_lines.append(Text(new_line, style=style))
        if len(log_lines) > max_log_lines:
            del log_lines[0]
        
        log_text.truncate(0) # 기존 텍스트 클리어
        for line in log_lines:
            log_text.append_text(line)
            log_text.append("\n")

    try:
        if not os.path.isdir(target_dir):
            console.print(f"\n[bold red]ERROR: Target directory not found.[/bold red]")
            console.print(f"[dim]Path: {target_dir}[/dim]")
            raise FileNotFoundError(f"Target directory '{target_dir}' does not exist.")

        console.print("[bold blue]>>> Starting optimization...[/bold blue]\n")

        # 통계 변수 초기화
        start_time = time.time()
        removed_count = 0
        not_found_count = 0
        total_removed_size = 0
        total_removed_files = 0
        total_removed_dirs = 0
        error_count = 0

        with Live(layout, console=console, refresh_per_second=10, vertical_overflow="visible") as live:
            total_items = len(remove_list)

            for i, item in enumerate(remove_list):
                item_path = os.path.join(target_dir, item)

                # 정보 패널 업데이트 (현재 처리 중인 항목 표시)
                update_layout(i, total_removed_size, item)

                # 가상 딜레이로 시각적 효과 부여
                time.sleep(0.05)

                if os.path.exists(item_path):
                    try:
                        # 제거 전 크기 계산
                        size_before, files_before, dirs_before = get_size_info(item_path)

                        if os.path.isfile(item_path) or os.path.islink(item_path):
                            os.remove(item_path)
                            update_log(f"[OK] Removed File: {item} ({format_size(size_before)})", "green")
                            total_removed_files += 1
                        elif os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                            update_log(f"[OK] Removed Dir:  {item} ({format_size(size_before)}, {files_before} files)", "green")
                            total_removed_dirs += 1
                            total_removed_files += files_before

                        removed_count += 1
                        total_removed_size += size_before

                        # 정보 패널 업데이트 (진행 상황 반영)
                        update_layout(i + 1, total_removed_size)

                    except OSError as e:
                        update_log(f"[ERROR] Error removing {item}: {e}", "bold red")
                        error_count += 1
                        # 정보 패널 업데이트 (진행 상황 반영)
                        update_layout(i + 1, total_removed_size)
                else:
                    update_log(f"[SKIP] Not found:    {item}", "yellow")
                    not_found_count += 1
                    # 정보 패널 업데이트 (진행 상황 반영)
                    update_layout(i + 1, total_removed_size)

                live.update(layout)

            # 최종 결과 업데이트
            end_time = time.time()
            elapsed_time = end_time - start_time

            update_log("\n" + "="*30, "dim")
            update_log("Optimization Complete!", "bold magenta")
            update_log("="*30, "dim")

            # 상세 통계 표시
            update_log(f"Processing Time: {elapsed_time:.1f}s", "cyan")
            update_log(f"Space Saved: {format_size(total_removed_size)}", "green")
            update_log(f"Items Removed: {removed_count} ({total_removed_files} files, {total_removed_dirs} dirs)", "green")
            update_log(f"Not Found: {not_found_count}", "yellow" if not_found_count > 0 else "dim")
            if error_count > 0:
                update_log(f"Errors: {error_count}", "red")

            update_log("="*30, "dim")
            update_log("Optimization successful!", "bold green")

            log_panel.border_style = "green"
            log_panel.title = "[bold green][COMPLETE] Optimization Complete[/bold green]"

            # 최종 정보 패널 업데이트 (완료 상태)
            update_layout(len(remove_list), total_removed_size, "Complete!")
            live.update(layout)

        console.print("\n[bold green]Your application has been optimized![/bold green]")
        console.print(f"[dim]Space saved: {format_size(total_removed_size)}[/dim]")
        console.print(f"[dim]Processing time: {elapsed_time:.1f} seconds[/dim]")
        console.print(f"[dim]Total items processed: {removed_count + not_found_count + error_count}[/dim]")

    except Exception as e:
        console.print(f"\n[bold red]An unexpected error occurred: {str(e)}[/bold red]")
        # Live가 활성화 상태일 때 에러가 발생하면 패널 상태를 변경하기 어려우므로, 여기서는 콘솔에만 출력
        raise

if __name__ == '__main__':
    # --- 테스트용 예제 ---
    # 1. 가짜 빌드 폴더 및 파일 생성
    app_name = "MyApp"
    dist_path = "dist"
    internal_path = os.path.join(dist_path, app_name, "_internal")
    
    print("Creating dummy build files for testing...")
    os.makedirs(internal_path, exist_ok=True)
    
    files_to_create = [
        "Qt5Core.dll", "Qt5Gui.dll", "libEGL.dll", 
        "tcl/tcl8.6/init.tcl", "tk/tk8.6/tk.tcl",
        "tcl/tcl8.6/encoding/ascii.enc", "tk/tk8.6/images/logo.gif",
        "ucrtbase.dll", "python3.dll", "useless_temp_file.tmp"
    ]
    for f in files_to_create:
        p = os.path.join(internal_path, f)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as fp:
            fp.write("dummy content")
    print("Dummy files created.\n")

    # 2. 최적화할 파일 목록 정의
    files_to_remove = [
        "tcl",          # tcl 폴더 전체
        "tk",           # tk 폴더 전체
        "libEGL.dll",   # 특정 파일
        "non_existent_file.dll" # 존재하지 않는 파일 (테스트용)
    ]

    # 3. 최적화 함수 실행
    try:
        optimize(name=app_name, distpath=dist_path, remove_list=files_to_remove)
    except Exception as e:
        print(f"Optimization failed: {e}")
    finally:
        # 4. 테스트 후 생성된 폴더 삭제
        if os.path.exists(dist_path):
            print("\nCleaning up dummy build files...")
            shutil.rmtree(dist_path)
            print("Cleanup complete.")
