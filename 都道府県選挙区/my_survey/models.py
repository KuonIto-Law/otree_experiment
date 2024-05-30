# otree.api モジュールから必要なクラスと関数をすべてインポートしている
# これにより、BaseConstants, BaseSubsession, BaseGroup, BasePlayer, modes.StringFieldなどが使用できる
from otree.api import *
import json

# ゲーム全体にかかわる定数を定義する
class Constants(BaseConstants):
    
    name_in_url = 'my_survey'
    players_per_group = None
    num_rounds = 1

# 本家も同様にパス
class Subsession(BaseSubsession):
    pass

# 本家も同様にパス
class Group(BaseGroup):
    pass

# has different structure, wouldn't work with get_config
# when you open the file that is written in Japanese, you have to add encoding='utf-8'!! 
file_path = "lituanian_municipalities.json"
with open(file_path, encoding='utf-8') as f:
    municipalities = json.load(f)
    # get unique polling places
# どこに回答者が選択した選択肢が、できれば変数、どこに保存されているか？    
# It should be stored as part of the player class
# この下にあるplayerクラスのprep_federal_stateとかにはいっている
    polling_places = {i for j in municipalities["data"].values() for i in j}
    # choice for "i don't know which polling place I vote at"
    polling_place_no_idea = municipalities["polling_place_no_idea"]
    municipalities["polling_places"] = [polling_place_no_idea] + list(polling_places)

class Player(BasePlayer):
    prep_federal_state = models.StringField(
        blank=True,  # doesn't need to be checked to continue
        label=municipalities["label_municipalities"],  # change to lithuanian
        choices=sorted(municipalities["data"]),
    )

    prep_polling_place = models.StringField(
        blank=True,  # doesn't need to be checked to continue
        label=municipalities["label_polling_places"],  # change to lithuanian
        choices=municipalities["polling_places"],
    )
    
    candidates = models.StringField(
        choices=[],  # 初期値は空のリストにする
        label="候補者"
    )


"""
# 各プレイヤーのデータを管理するためのクラス
# ここでPlayerモデルにはchoice1, choice2というフィールドが定義されている
class Player(BasePlayer):
    choice_1 = models.StringField(
        choices=['A', 'B', 'C', 'D', 'E'],
        label="1ページ目の質問"
    )
    # 1ページ目の選択に応じて動的に設定されるために、ここは空のリストにする
    # ここの選択肢は動的に後で設定される
    choice_2 = models.StringField(
        choices=[],  # 初期値は空のリストにする
        label="2ページ目の質問"
    )
"""
