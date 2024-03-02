import typer
import yaml
import os
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from rich.progress import track

#* Set woodpecker vararibles
app = typer.Typer()
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FILES = [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(ROOT) for f in filenames] 

#* Configuration types
FULL = [
    ".ruff_cache",
    "__pycache__"
]
MIN = [
    "text.txt"
]


@app.command()
def init():
    """
    Creates a configuration file 
    """
    print(Panel.fit(renderable="Welcome to [yellow]Woodpecker[/yellow], Select a config file type.\n"
                    "[b]1)[/b] [blue]Full config[/blue]\n"
                    "[b]2)[/b] Minimal config\n\n"
                    ""))
    ctype = Prompt.ask('', choices=['1','2'], default='1')

    for i in track(range(1), description="Generating config file..."):
        with open("woodpecker.yaml", 'w+') as config:
            if ctype == '1':
                yaml.dump(FULL, config, default_flow_style=False)
            elif ctype == '2':
                yaml.dump(MIN, config, default_flow_style=False)
    print("[green]Config file were generated! ✨[/green]")
        
@app.command()
def peck():
    print(FILES)

if __name__ == "__main__":
    app()
