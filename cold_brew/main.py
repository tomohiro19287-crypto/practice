import sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.panel import Panel
from rich.text import Text
from notion import add_record

console = Console()


def ask_grind() -> int:
    while True:
        val = IntPrompt.ask("[bold]挽き目[/bold] (粗さ 1〜10)")
        if 1 <= val <= 10:
            return val
        console.print("[red]1〜10 の数値を入力してください[/red]")


def ask_rating() -> int:
    while True:
        val = IntPrompt.ask("[bold]評価[/bold] (1〜5)")
        if 1 <= val <= 5:
            return val
        console.print("[red]1〜5 の数値を入力してください[/red]")


def ask_brew_time() -> str:
    while True:
        val = Prompt.ask("[bold]抽出時間[/bold] (例: 12h, 18h)")
        val = val.strip()
        if val:
            return val
        console.print("[red]抽出時間を入力してください[/red]")


def main():
    console.print(Panel(Text("Cold Brew Coffee Logger", justify="center", style="bold cyan")))

    bean = Prompt.ask("[bold]豆の種類[/bold] (例: Kona, Ethiopia)")
    grind = ask_grind()
    bean_g = IntPrompt.ask("[bold]豆の量[/bold] (g)")
    water_ml = IntPrompt.ask("[bold]水の量[/bold] (ml)")
    brew_time = ask_brew_time()
    stir = Confirm.ask("[bold]撹拌あり？[/bold]")
    rating = ask_rating()
    comment = Prompt.ask("[bold]コメント[/bold] (Enterでスキップ)", default="")

    data = {
        "bean": bean,
        "grind": grind,
        "bean_g": bean_g,
        "water_ml": water_ml,
        "brew_time": brew_time,
        "stir": stir,
        "rating": rating,
        "comment": comment,
    }

    console.print("\n[yellow]Notionに記録中...[/yellow]")
    try:
        url = add_record(data)
        console.print(f"[green]✓ 記録しました:[/green] {url}")
    except Exception as e:
        console.print(f"[red]エラーが発生しました: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
