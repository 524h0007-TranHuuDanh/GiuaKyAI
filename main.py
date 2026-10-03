from source.gui.gameApp import GameApp


def main():
    singleData = {
        "walls": [],
        "state": None,
        "rows": 0,
        "columns": 0
    }

    competitiveData = {
        "walls": [],
        "state": None,
        "rows": 0,
        "columns": 0
    }

    app = GameApp(singleData, competitiveData)

    app.run()


if __name__ == "__main__":
    main()