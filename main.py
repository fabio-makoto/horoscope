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
        # print("Áries")
        sign = 1
        return sign
    elif month == 4 and day >= 21 or month == 5 and day <= 20:
        # print("Touro")
        sign = 2
        return sign
    elif month == 5 and day >= 21 or month == 6 and day <= 20:
        # print("Gêmeos")
        sign = 3
        return sign
    elif month == 6 and day >= 21 or month == 7 and day <= 22:
        # print("Câncer")
        sign = 4
        return sign
    elif month == 7 and day >= 23 or month == 8 and day <= 22:
        # print("Leão")
        sign = 5
        return sign
    elif month == 8 and day >= 23 or month == 9 and day <= 22:
        # print("Virgem")
        sign = 6
        return sign
    elif month == 9 and day >= 23 or month == 10 and day <= 22:
        # print("Libra")
        sign = 7
        return sign
    elif month == 10 and day >= 23 or month == 11 and day <= 21:
        # print("Escorpião")
        sign = 8
        return sign
    elif month == 11 and day >= 22 or month == 12 and day <= 21:
        # print("Sagitário")
        sign = 9
        return sign
    elif month == 12 and day >= 22 or month == 1 and day <= 20:
        # print("Capricórnio")
        sign = 10
        return sign
    elif month == 1 and day >= 21 or month == 2 and day <= 18:
        # print("Aquário")
        sign = 11
        return sign
    elif month == 2 and day >= 19 or month == 3 and day <= 20:
        # print("Peixes")
        sign = 12
        return sign


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
        case 1:
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Março[/] a [bold green]20[/] de [bold green]abril[/] é de [bold red]Áries[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Áries[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Áries[/]: [i]É Representado pelo elemento fogo e pela cabeça de carneiro como símbolo, o signo de áries "\
                "é conhecido pelo senso de liderança, autonomia e pioneirismo, assim como pela sua coragem e autoconfiança. Outra "\
                "característica associada ao primeiro signo do zodíaco é a impulsividade, muitas vezes relacionada a um perfil mais "\
                "'explosivo' e impaciente.\n"
                )
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 2:
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Abril[/] a [bold green]20[/] de [bold green]Maio[/] é de [bold red]Touro[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Touro[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Touro[/]: [i]Os taurinos têm a terra como elemento e a cabeça de um touro"
                 "simbolizando o signo, normalmente representada por um círculo com dois chifres. Eles são considerados pessoas leais," 
                 "protetoras e determinadas. Além disso, o signo é conhecido por gostar de aproveitar os prazeres da vida, como comer e" 
                 "dormir, por exemplo — por isso é associado à preguiça e à gula. Também podem apresentar a teimosia como um aspecto forte" 
                 "de personalidade."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 3:
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Maio[/] a [bold green]20[/] de [bold green]Junho[/] é de [bold red]Gêmeos[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Gêmeos[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Gêmeos[/]: [i]O signo de gêmeos é comunicativo, sociável e inteligente. Regido"
                  "pelo elemento ar e representado pelo número 2 em algarismos romanos, esse é um signo adaptável e tem uma energia ligada"
                  "ao mental. Geminianos também são conhecidos pela curiosidade e vontade de aprender, o que se relaciona a essa energia" 
                  "mental — que também pode despertar impaciência, ansiedade e superficialidade."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 4:
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Junho[/] a [bold green]22[/] de [bold green]Julho[/] é de [bold red]Câncer[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Câncer[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Câncer[/]: [i]O significado dos signos se relaciona com o símbolo que os"
                "representa e com câncer isso não é diferente. Representado por um caranguejo, esse signo pode ser mais reservado e "
                "cauteloso, protegendo suas emoções — assim como o caranguejo se protege em sua casca. Além disso, os cancerianos, regidos"
                "pelo elemento água, são conhecidos pela sensibilidade e por serem carinhosos, assim como pela conexão com a família e com"
                "o passado. Por outro lado, tem como desafio não alimentar mágoas."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 5:
            rprint(
                f"Quem nasce entre o dia [bold green]23[/] de [bold green]Julho[/] a [bold green]22[/] de [bold green]Agosto[/] é de [bold red]Leão[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Leão[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Leão[/]: [i]Representados por um leão e regidos pelo elemento fogo, os "
                "leoninos apresentam como características a criatividade, o carisma e a generosidade. Esse signo também é associado à "
                "coragem, determinação e a autoconfiança — que pode ser relacionada a uma arrogância em alguns momentos. A individualidade "
                "também é uma característica que pode atenuar o senso de egocentrismo."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 6:
            rprint(
                f"Quem nasce entre o dia [bold green]23[/] de [bold green]Agosto[/] a [bold green]22[/] de [bold green]Setembro[/] é de [bold red]Virgem[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Virgem[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Virgem[/]: [i]Virgem é um signo de terra, representado pela letra “M” ou "
                "pela imagem de uma mulher. Conhecidos pelo senso de organização, os virginianos são determinados, trabalhadores e "
                "disciplinados. Ao avaliar o significado dos signos, características como a capacidade analítica e detalhista — muitas "
                "vezes relacionadas ao perfeccionismo e ao hipercriticismo — também são relacionados ao signo de virgem, assim como a "
                "praticidade e o altruísmo."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 7:
            rprint(
                f"Quem nasce entre o dia [bold green]23[/] de [bold green]Setembro[/] a [bold green]22[/] de [bold green]Outubro[/] é de [bold red]Libra[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Libra[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Libra[/]: [i]Representado pelo símbolo da balança, os librianos são "
                "conhecidos pelo senso de justiça e pela diplomacia, assim como pela harmonia e a busca pelo equilíbrio. O signo de "
                "libra é regido pelo elemento ar e tem como características associadas a ele a sociabilidade, inteligência e a capacidade "
                "de apreciar a beleza das coisas. Tem como desafio aprender a dizer não."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 8:
            rprint(
                f"Quem nasce entre o dia [bold green]23[/] de [bold green]Outubro[/] a [bold green]21[/] de [bold green]Novembro[/] é de [bold red]Escorpião[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Escorpião[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Escorpião[/]: [i]O signo de escorpião é representado pelo animal de mesmo "
                "nome e tem o elemento de água como seu regente. É conhecido pela intensidade e profundidade emocional, assim como pela "
                "persistência e o carisma. Além disso, o signo está associado a um interesse por temas esotéricos e mais profundos ou "
                "misteriosos. Os escorpianos também têm como características a capacidade de transformação."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 9:
            rprint(
                f"Quem nasce entre o dia [bold green]22[/] de [bold green]Novembro[/] a [bold green]21[/] de [bold green]Dezembro[/] é de [bold red]Sagitário[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Sagitário[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Sagitário[/]: [i]O símbolo do Sagitário é uma flecha, associada ao "
                "centauro, que também pode aparecer em algumas representações do signo. Ligado ao elemento fogo, é um signo que tem como "
                "características o senso de aventura, exploração e sabedoria. Sagitarianos também prezam pela autonomia, a liberdade e "
                "pela espontaneidade. Além disso, é um signo relacionado à impulsividade."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 10:
            rprint(
                f"Quem nasce entre o dia [bold green]22[/] de [bold green]Dezembro[/] a [bold green]20[/] de [bold green]Janeiro[/] é de [bold red]Capricórnio[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Capricórnio[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Capricórnio[/]: [i]Regido pelo elemento terra, Capricórnio é representado "
                "pela cabra marinha e é um signo conhecido pela determinação, responsabilidade e pelo pragmatismo. Os capricornianos também "
                "são trabalhadores, ambiciosos e práticos. Outras características são a busca pela estabilidade, segurança e a capacidade "
                "visionária. Vale se atentar em aprender a ser menos solitário."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 11:
            rprint(
                f"Quem nasce entre o dia [bold green]21[/] de [bold green]Janeiro[/] a [bold green]18[/] de [bold green]Fevereiro[/] é de [bold red]Aquário[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Aquário[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Aquário[/]: [i]Assim como o significado dos signos de ar, como Gêmeos, "
                "aquarianos também tem uma energia mais mental, que confere algumas características relacionadas ao signo, como capacidade "
                "analítica, lógica e objetiva. Representado por duas ondas, esse é um signo conhecido pela originalidade, individualidade "
                "e sociabilidade. Além disso, Aquário pode ser relacionado a rebeldia, a inovação e a mudanças."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")
        case 12:
            rprint(
                f"Quem nasce entre o dia [bold green]19[/] de [bold green]Fevereiro[/] a [bold green]20[/] de [bold green]Março[/] é de [bold red]Peixes[/].\n"
                f"\nComo você nasceu no dia [bold green]{vday}[/] de [bold green]{months[vmonth-1]}[/] o seu signo é [bold red]Peixes[/].\n"
                )

            rprint(
                f"[b]As características do signo de[/] [bold red]Peixes[/]: [i]Signo de elemento água, Peixes tem como características a "
                "sensibilidade, criatividade e a empatia. Representado por dois peixes, o último signo do zodíaco é conhecido por ser "
                "sonhador, intuitivo e conectado a emoções. Esse signo também é conhecido pela relação com a arte, capacidade de adaptação "
                "e conexão com a espiritualidade."
                )
            
            horoscope = get_horoscope_today(sign)
            translation = en_to_pt.translate(horoscope)

            rprint(f"\n[i b]O seu horóscopo do dia.[/][i]\n{translation}\n")

app()
