#%%

import os
import MeCab
import numpy as np

tagger = MeCab.Tagger()
def sym_to_dec(inchar:str):
    # from symbolic char to dec representation of unicode #
    # ex. あ -> 12354
    if len(inchar) > 1:
        return None
    return int(str(inchar.encode("unicode_escape"))[5:-1], base=16)
#%%
all_kata = """ァ ア ィ イ ゥ ウ ェ エ ォ オ カ ガ キ ギ ク グ ケ ゲ コ ゴ サ ザ シ ジ ス ズ セ ゼ ソ ゾ タ ダ チ ヂ ッ ツ ヅ テ デ ト ド ナ ニ ヌ ネ ノ ハ バ パ ヒ ビ ピ フ ブ プ ヘ ベ ペ ホ ボ ポ マ ミ ム メ モ ャ ヤ ュ ユ ョ ヨ ラ リ ル レ ロ ヮ ワ  ヰ  ヱ  ヲ  ン  ヴ ヵ ヶ ヷ ヸ  ヹ  ヺ ・ ー  ヽ  ヾ  ヿ """
romaji = "_a a _i i _u u _e e _o o ka ga ki gi ku gu ke ge ko go sa za shi ji su zu se ze so zo ta da chi dji ! tsu dzu te de to do na ni nu ne no ha ba pa hi bi pi fu bu pu he be pe ho bo po ma mi mu me mo _ya ya _yu yu _yo yo ra ri ru re ro _wa wa wi we wo n ヴ ヵ ヶ ヷ  ヸ  ヹ  ヺ・ & ヽ ヾ  ヿ "
# Special cases:
all_kata = all_kata.replace("  "," ")
romaji = romaji.replace("  ", " ")
all_kata = all_kata.split(" ")
romaji = romaji.split(" ")
for i in range(len(romaji)):
    if romaji[i] == all_kata[i]:
        romaji[i] = "^"
def katakana_to_romaji(kata_string):
    nextc = ""
    outstr = ""
    # Exceptions:
    # ! probleme avec petit tsu (ex. shusseki / participate)
    # & probleme avec tiret (ex. elebe-ta- / elevator)
    # _ probleme des petits kanas (ex. fuairu / file)
    for character in kata_string:
        if nextc != "!":
            nextc = ""
        nextc += romaji[sym_to_dec(character)-12449]
        if nextc.startswith("!") and len(nextc>1):
            nextc = nextc[1]+nextc[1:]
        if nextc == "&":
            nextc = outstr[-1]
        if nextc != "!":
            outstr += nextc
    return outstr

    
#%%
test_sentence="年始から、パソコン講師を始めました。"
ascii_input = []

parse = tagger.parse(test_sentence).split("\n")

for entry in parse[:-1]:
    katakana_to_romaji(entry.split("\t")[1])
ascii_input

# %%
