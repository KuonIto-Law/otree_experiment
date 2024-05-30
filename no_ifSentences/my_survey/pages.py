from otree.api import Page, WaitPage

# ConstantsとPlayerクラスを同じディレクトリ内のmodels.py空インポートしている
from .models import Constants, Player

# アンケートの1ページ目を定義している
class FirstPage(Page):
    # フォームデータを保存するのが以下の二つの変数
    # フォームデータとは、ユーザーがウェブページ上のフォームに入力した情報のこと
    # この場合"player"がモデルに保存されている
    form_model = 'player'
    form_fields = ['choice_1']
    template_name = 'my_survey/FirstPage.html'

class SecondPage(Page):
    form_model = 'player'
    form_fields = ['choice_2']
    template_name = 'my_survey/SecondPage.html'
    
    # フォームフィールドを動的に設定するためには、ページクラス内でこのメソッドをオーバーライドする。
    # このメソッドでは、ユーザーの前のページでの選択に基づいてフォームフィールドを動的に変更する
    def get_form_fields(self):
        form_fields = ['choice_2']
        
        data = [{"alphabet":"A", "answer":"1,2"},
        {"alphabet":"B", "answer":"3,4"},
        {"alphabet":"C", "answer":"5,6"},
        {"alphabet":"D", "answer":"7,8"},
        {"alphabet":"E", "answer":"9,10"}
        ]

        # self.playerとは、現在のプレイヤーインスタンスを指す
        # 各ページクラスのインスタンスが生成されるときに、ページが関連付けられているプレイヤーオブジェクトがself.playerとして自動的に割り当てられる
        # これにより、そのプレイヤーのデータにアクセスし、操作することができる
        choice_1 = self.player.choice_1
        
        """
        if choice_1 == 'A':
            self.player.choice_2 = '1,2'
        elif choice_1 == 'B':
            self.player.choice_2 = '3,4'
        elif choice_1 == 'C':
            self.player.choice_2 = '5,6'
        elif choice_1 == 'D':
            self.player.choice_2 = '7,8'
        elif choice_1 == 'E':
            self.player.choice_2 = '9,10'
        return ["choice_2"]
        """
    
        self.player.choice_2 = [item["answer"] for item in data if item["alphabet"] == choice_1][0]
        
        return ["choice_2"]

    # テンプレートへの変数の渡し方
    # テンプレートへ変数を渡すためには、このメソッドを使用する
    # 具多的には、choice_1に基づいて、choicesリストを設定する
    def vars_for_template(self):
        
        data = [{"alphabet":"A", "answer":"1,2"},
        {"alphabet":"B", "answer":"3,4"},
        {"alphabet":"C", "answer":"5,6"},
        {"alphabet":"D", "answer":"7,8"},
        {"alphabet":"E", "answer":"9,10"}
        ]
        
        """
        choice_1 = self.player.choice_1
        if choice_1 == 'A':
            choices = ['1', '2']
        elif choice_1 == 'B':
            choices = ['3', '4']
        elif choice_1 == 'C':
            choices = ['5', '6']
        elif choice_1 == 'D':
            choices = ['7', '8']
        elif choice_1 == 'E':
            choices = ['9', '10']
        else:
            choices = []
        """
        
        choice_1 = self.player.choice_1
        choices = [item["answer"].split(",") for item in data if item["alphabet"] == choice_1][0]
        #self.player.choice_2 = ",".join(choices) #ここはコメントアウトしてもいい

        # choicesリストは、choice_2_choicesという名前でテンプレートに渡される
        return dict(choice_2_choices=choices)

# ここでページの順序を定義する
page_sequence = [FirstPage, SecondPage]


#まとめ
#フォームデータは、ユーザーがフォームに入力したデータのこと。
#フォームフィールドは、ユーザーがデータを入力するための個々の要素。
#フォームフィールドの定義は、モデルクラス内で行い、適切なデータ型を使用する。
#フォームフィールドの使用は、ページクラスでform_modelとform_fieldsを指定する。
#フォームフィールドの動的設定は、get_form_fieldsメソッドをオーバーライドして行う。
#テンプレートへの変数の渡し方は、vars_for_templateメソッドを使用する。
