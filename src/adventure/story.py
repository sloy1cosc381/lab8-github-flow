from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console

console=Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[green4]You stand still, unsure what to do.[/green4] [dark_red]The forest swallows you.[/dark_red]"

def left_path(event):
    return "[green4]You walk[/green4] [blue3]left[/blue3][green4]. " + event + "[/green4]"

def right_path(event):
    return "[green4]You walk[/green4] [magenta]right[/magenta][green4]. " + event + "[/green4]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[green4]You wake up in a dark forest. You can go[/green4] [blue3]left[/blue3] [green4]or[/green4] [magenta]right[/magenta][green4].[/green4]")
    while True:
        choice = console.input("Which direction do you choose? ([blue3]left[/blue3]/[magenta]right[/magenta]/[dark_red]exit[/dark_red]): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
