from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable

from fetch_initial_anime import fetch_top_anime

ROWS = [
    ("title", "score")
]

anime_list = fetch_top_anime()

for anime in anime_list:
        ROWS.append((anime["title"]["english"], anime["averageScore"]))

class RoninApp(App):


    BINDINGS = [("j", "cursor_up", "go up"), ("k", "cursor_down", "go down")]


    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable()
        yield Footer()


    def on_mount(self) -> None:
        self.theme = "catppuccin-mocha"

        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])
        pass

def main():

    app = RoninApp()
    app.run()


if __name__ == "__main__":
    main()
