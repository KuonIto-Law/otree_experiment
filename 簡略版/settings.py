from os import environ

# セッションのデフォルト設定
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
)

# セッションの設定
SESSION_CONFIGS = [
    dict(
        name='my_survey',
        display_name="My Survey",
        app_sequence=['my_survey'],
        num_demo_participants=1,
    ),
]

# 言語コード
LANGUAGE_CODE = 'en'

# 通貨コードとポイントの使用
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

# 部屋の設定（必要に応じて追加）
ROOMS = []

# 管理者ユーザー名とパスワード
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# デモページのイントロHTML
DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# セキュリティキー
SECRET_KEY = 'your-secret-key'

# インストールされているアプリ
INSTALLED_APPS = ['otree']
