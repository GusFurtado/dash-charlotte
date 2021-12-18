from dash import Dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc



app = Dash(
    name = __name__,
    title = 'Sign in',
    external_scripts = [
        'https://kit.fontawesome.com/64d58efce2.js',
        'https://raw.githubusercontent.com/sefyudem/Sliding-Sign-In-Sign-Up-Form/master/app.js'
    ]
)



sign_in_form = html.Form(
    className = 'sign-in-form',
    children = [
        html.H2(
            className = 'title',
            children = 'Sign in'
        ),
        html.Div(
            className = 'input-field',
            children = [
                html.I(
                    className = 'fas fa-user'
                ),
                dcc.Input(
                    type = 'text',
                    placeholder = 'Username'
                )
            ]
        ),
        html.Div(
            className = 'input-field',
            children = [
                html.I(
                    className = 'fas fa-lock'
                ),
                dcc.Input(
                    type = 'password',
                    placeholder = 'Password'
                )
            ]
        ),
        dcc.Input(
            type = 'submit',
            value = 'Login',
            className = 'btn solid'
        )
    ]
)



sign_up_form = html.Form(
    className = 'sign-up-form',
    children = [
        html.H2(
            className = 'title',
            children = 'Sign up'
        ),
        html.Div(
            className = 'input-field',
            children = [
                html.I(
                    className = 'fas fa-user'
                ),
                dcc.Input(
                    type = 'text',
                    placeholder = 'Username'
                )
            ]
        ),
        html.Div(
            className = 'input-field',
            children = [
                html.I(
                    className = 'fas fa-lock'
                ),
                dcc.Input(
                    type = 'password',
                    placeholder = 'Password'
                )
            ]
        ),
        dcc.Input(
            type = 'submit',
            value = 'Sign up',
            className = 'btn solid'
        )
    ]
)



forms_container = html.Div(
    className = 'forms-container',
    children = html.Div(
        className = 'signin-signup',
        children = [
            sign_in_form,
            sign_up_form
        ]
    )
)



left_panel = html.Div(
    className = 'panel left-panel',
    children = [
        html.Div(
            className = 'content',
            children = [
                html.H3(
                    children = 'New here?'
                ),
                html.P(
                    children = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Debitis, ex ratione. Aliquid!'
                ),
                html.Button(
                    className = 'btn transparent',
                    id = 'sign-up-btn',
                    children = 'Sign up',
                    n_clicks_timestamp = 0
                )
            ]
        ),
        html.Img(
            src = 'assets/img/log.svg',
            className = 'image',
            alt = ''
        )
    ]
)



right_panel = html.Div(
    className = 'panel right-panel',
    children = [
        html.Div(
            className = 'content',
            children = [
                html.H3(
                    children = 'One of us?'
                ),
                html.P(
                    children = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Debitis, ex ratione. Aliquid!'
                ),
                html.Button(
                    className = 'btn transparent',
                    id = 'sign-in-btn',
                    children = 'Sign in',
                    n_clicks_timestamp = 0
                )
            ]
        ),
        html.Img(
            src = 'assets/img/register.svg',
            className = 'image',
            alt = ''
        )
    ]
)



panels_container = html.Div(
    className = 'panels-container',
    children = [
        left_panel,
        right_panel
    ]
)



app.layout = html.Div(
    className = 'container',
    id = 'container',
    children = [
        forms_container,
        panels_container
    ]
)



@app.callback(
    Output('container', 'className'),
    Input('sign-up-btn', 'n_clicks_timestamp'),
    Input('sign-in-btn', 'n_clicks_timestamp'),
    prevent_initial_call = True)
def click(signup, signin):
    print(signup, signin)
    if signup > signin:
        return 'container sign-up-mode'
    return 'container'



if __name__ == '__main__':
    app.run_server()
