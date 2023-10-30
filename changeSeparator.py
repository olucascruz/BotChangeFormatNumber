import pygetwindow as gw

def change_separator(bot, separator_1, separator_2):
    bot.type_keys(["win", "r"])
    bot.kb_type("control")
    bot.enter()
    bot.wait(2000)
    bot.tab(presses=2)
    bot.wait(1000)
    bot.type_right()
    bot.tab(presses=4)
    bot.enter()
    bot.wait(1000)
    bot.tab(presses=7)
    bot.enter()
    bot.wait(1000)
    bot.kb_type(f"{separator_1}")
    bot.tab(presses=2)
    bot.kb_type(f"{separator_2}")
    bot.tab(presses=12)
    bot.enter()
    bot.wait(1500)
    window_title = "Personalizar Formato"

    window = gw.getWindowsWithTitle(window_title)
    if window:
    # Traga a janela para o primeiro plano.
        window[0].activate()
    else:
        print("Janela não encontrada.")



    bot.tab(presses=12)
    bot.wait(2000)
    bot.enter()
    bot.wait(1000)
    bot.alt_f4()
    bot.wait(1000)
    bot.alt_f4()
    print("fechou")