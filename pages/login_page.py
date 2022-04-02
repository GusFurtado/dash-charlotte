from dash import register_page

from dash_charlotte.layouts import login



register_page(
    __name__,
    path = '/login',
    title = 'Log In'
)



layout = login.LoginPage(
    left_panel = login.SvgImage(src='/assets/img/register.svg'),
    right_panel = login.LoginForm()
)
