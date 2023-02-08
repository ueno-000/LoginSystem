from django.shortcuts import render
from django.http import HttpResponseRedirect

def LoginView(request):
    return HttpResponseRedirect('social:begin', kwargs=dict(backend='google-oauth2'))

def index(request):
    pass
    
# ログイン後に行いたい処理
#ユーザー登録
def signup_view(request):
    pass


#ユーザーログイン
def login_view(request):
    pass


#ユーザーログアウト
def logout_view(request):
    pass


#ログインしているユーザーの情報表示画面
def user_view(request):
    pass


#他のユーザーの情報の表示
def other_view(request):
    pass
