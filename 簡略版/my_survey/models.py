# otree.api モジュールから必要なクラスと関数をすべてインポートしている
# これにより、BaseConstants, BaseSubsession, BaseGroup, BasePlayer, modes.StringFieldなどが使用できる
from otree.api import *

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
