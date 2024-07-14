from typer import Context, Exit, Option, Typer
from rich import print as rprint
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.progress import track
from bs4 import BeautifulSoup
import requests
import os
from deep_translator import GoogleTranslator
import time
import db_connection


app = Typer()

__version__ = "0.1.0"


def version(arg: bool):
    if arg:
        rprint(f"CLI version {__version__}")
        raise Exit(code=0)


def validate_month(month: str):
    if len(month) != 2 or month == "00" or int(month) > 12:
        rprint("\n[bold red]Mês inválido. Inicie o programa novamente.[/]\n[bold green]Finalizando...\n")
        raise Exit(code=1)
    else:
        try:
            month = int(month)
            return month
        except ValueError:
            rprint("\n[bold red]Mês inválido. Inicie o programa novamente.[/]\n[bold green]Finalizando...\n")
            raise Exit(code=1)


def validate_day(day: str, month: str):
    if len(day) != 2:
        rprint("\n[bold red]Dia inválido. Inicie o programa novamente.[/]\n[bold green]Finalizando...\n")
        raise Exit(code=1)
    else:
        try:
            day = int(day)
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day > 31:
                    rprint("\n[bold red]Dia inválido. Inicie o programa novamente.[/]\n[bold green]Finalizando...\n")
                    raise Exit(code=1)
                else:
                    return day
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day > 30:
                    rprint("\n[bold red]Dia inválido. Inicie o programa novamente.[/]\n[bold green]Finalizando...\n")
                    raise Exit(code=1)
                else:
                    return day
            else:
                if day > 29:
                    rprint("\n[bold red]Dia inválido. Inicie o programa novamente.[/]\n[bold green]Finalizando...\n")
                    raise Exit(code=1)
                else:
                    return day
        except ValueError:
            rprint("\n[bold red]Dia inválido. Inicie o programa novamente.[/]\n[bold green]Finalizando...\n")
            raise Exit(code=1)


def get_sign(day: int, month: int):
    if month == 3 and day >= 21 or month == 4 and day <= 20:
        return 'aries'

    elif month == 4 and day >= 21 or month == 5 and day <= 20:
        return 'taurus'

    elif month == 5 and day >= 21 or month == 6 and day <= 20:
        return 'gemini'

    elif month == 6 and day >= 21 or month == 7 and day <= 22:
        return 'cancer'

    elif month == 7 and day >= 23 or month == 8 and day <= 22:
        return 'leo'

    elif month == 8 and day >= 23 or month == 9 and day <= 22:
        return 'virgo'

    elif month == 9 and day >= 23 or month == 10 and day <= 22:
        return 'libra'

    elif month == 10 and day >= 23 or month == 11 and day <= 21:
        return 'scorpio'

    elif month == 11 and day >= 22 or month == 12 and day <= 21:
        return 'sagittarius'

    elif month == 12 and day >= 22 or month == 1 and day <= 20:
        return 'capricorn'

    elif month == 1 and day >= 21 or month == 2 and day <= 18:
        return 'aquarius'

    elif month == 2 and day >= 19 or month == 3 and day <= 20:
        return 'pisces'


def get_horoscope_today(sign: int):
    response = requests.get(
        f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign}"
                            )
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find("div", attrs={"class": "main-horoscope"})

    return data.p.text


def progress_bar():
    total = 0
    for value in track(range(100), description="Processando..."):
        time.sleep(0.03)
        total += 1


@app.callback(invoke_without_command=True)
def typer_callback(
    ctx: Context,
    version: bool = Option(
        False, "--version", "-v", help="Show the CLI version.", is_eager=True, is_flag=True, callback=version,
    )
):
    if ctx.invoked_subcommand:
        return
    
    rprint("\nUse o comando 'init' para iniciar o programa ou a opção '--help' para obter ajuda.\n")


@app.command()
def init():
    """
    Start the program.
    """
    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    en_to_pt = GoogleTranslator(source="en", target="pt")

    month: str = Prompt.ask("Em que mês você nasceu?[bold red](não se esqueça do 0)[/][bold green]Ex. 01, 08, 12 ")
    vmonth = validate_month(month)
    print()
    day: str = Prompt.ask("Que dia você nasceu?[bold red](não se esqueça do 0)[/][bold green]Ex. 05, 09, 15, 29 ")
    vday = validate_day(day, vmonth)

    sign = get_sign(vday, vmonth)

    progress_bar()

    os.system("clear")
    match sign:
        case 'aries':
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Março[/] a [bold green]20[/] de [bold green]abril[/] é de [bold red]Áries[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Áries[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))

            horoscope = get_horoscope_today(1)
            translation = en_to_pt.translate(horoscope)

            rprint(f"[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'taurus':
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Abril[/] a [bold green]20[/] de [bold green]Maio[/] é de [bold red]Touro[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Touro[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))

            horoscope = get_horoscope_today(2)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'gemini':
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Maio[/] a [bold green]20[/] de [bold green]Junho[/] é de [bold red]Gêmeos[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Gêmeos[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))
            
            horoscope = get_horoscope_today(3)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'cancer':
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Junho[/] a [bold green]22[/] de [bold green]Julho[/] é de [bold red]Câncer[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Câncer[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))

            horoscope = get_horoscope_today(4)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'leo':
            rprint(
                f"Quem nasce entre o dia [bold green]23[/] de [bold green]Julho[/] a [bold green]22[/] de [bold green]Agosto[/] é de [bold red]Leão[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Leão[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))
            
            horoscope = get_horoscope_today(5)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'virgo':
            rprint(
                f"Quem nasce entre o dia [bold green]23[/] de [bold green]Agosto[/] a [bold green]22[/] de [bold green]Setembro[/] é de [bold red]Virgem[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Virgem[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))
            
            horoscope = get_horoscope_today(6)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'libra':
            rprint(
                f"Quem nasce entre o dia [bold green]23[/] de [bold green]Setembro[/] a [bold green]22[/] de [bold green]Outubro[/] é de [bold red]Libra[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Libra[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))
            
            horoscope = get_horoscope_today(7)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'scorpio':
            rprint(
                f"Quem nasce entre o dia [bold green]23[/] de [bold green]Outubro[/] a [bold green]21[/] de [bold green]Novembro[/] é de [bold red]Escorpião[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Escorpião[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))
            
            horoscope = get_horoscope_today(8)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'sagittarius':
            rprint(
                f"Quem nasce entre o dia [bold green]22[/] de [bold green]Novembro[/] a [bold green]21[/] de [bold green]Dezembro[/] é de [bold red]Sagitário[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Sagitário[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))
            
            horoscope = get_horoscope_today(9)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'capricorn':
            rprint(
                f"Quem nasce entre o dia [bold green]22[/] de [bold green]Dezembro[/] a [bold green]20[/] de [bold green]Janeiro[/] é de [bold red]Capricórnio[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Capricórnio[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))
            
            horoscope = get_horoscope_today(10)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'aquarius':
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Janeiro[/] a [bold green]18[/] de [bold green]Fevereiro[/] é de [bold red]Aquário[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Aquário[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))
            
            horoscope = get_horoscope_today(11)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 'pisces':
            rprint(
                f"Quem nasce entre o dia [bold green]19[/] de [bold green]Fevereiro[/] a [bold green]20[/] de [bold green]Março[/] é de [bold red]Peixes[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Peixes[/].\n"
                )
            
            text = db_connection.get_text(sign)
            rprint(''.join(text))
            
            horoscope = get_horoscope_today(12)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")

app()
