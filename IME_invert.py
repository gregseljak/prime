
import cutlet
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False
katsu.add_exception("は","ha")
katsu.add_exception("へ","he")

def IME_invert(insentence):
    # INPUT:  sentence in japanese
    # OUTPUT: sequence of ASCII characters which correspond to IME input
    outsent =  katsu.romaji(insentence.replace("ー",  "-"))
    return outsent.replace(" - ",  "-")

if __name__=="""__main__""":

    test_sentence="ぬくもりホールの会要請 国内屈指のクリスタルホール音楽堂 「設備の劣化への十分な対策を」"
    IME_invert(test_sentence)

