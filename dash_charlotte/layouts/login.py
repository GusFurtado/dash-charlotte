from typing import List

from dash import (
    html,
    dcc
)
import dash_bootstrap_components as dbc



class SvgImage(html.Div):

    def __init__(
            self,
            src: str
        ):

        super().__init__(
            className = 'login-svg-image',
            children = html.Img(
                src = src,
                style = {
                    'maxHeight': '100%',
                    'maxWidth': '100%'
                }
            )
        )



class LoginForm(html.Div):

    def __init__(
            self,
            title_text: str = 'Log in',
            email_placeholder: str = 'Username',
            password_placeholder: str = 'Password',
            button_text: str = 'Log in',
            button_color: str = 'blue'
        ):

        super().__init__(
            style = {
                'minHeight': '100%',
                'text-align': 'left',
                'padding': 20
            },
            className = 'bg-shade0',
            children = html.Form(
                className = 'sign-in-form',
                children = [
                    self.title_text(
                        text = title_text
                    ),
                    self.email_input(
                        placeholder = email_placeholder
                    ),
                    self.password_input(
                        placeholder = password_placeholder
                    ),
                    self.submit_button(
                        text = button_text,
                        color = button_color
                    )
                ]
            )
        )


    def title_text(self, text) -> html.H2:
        return html.H2(
            className = 'shade6',
            children = text,
            style = {
                'font-size': '2.2rem',
                'margin-bottom': '10px',
            }
        )


    def email_input(self, placeholder:str) -> html.Div:
        return html.Div(
            className = 'input-field',
            children = [
                html.I(
                    className = 'fas fa-user'
                ),
                dcc.Input(
                    type = 'text',
                    placeholder = placeholder
                )
            ]
        )


    def password_input(self, placeholder:str) -> html.Div:
        return html.Div(
            className = 'input-field',
            children = [
                html.I(
                    className = 'fas fa-lock'
                ),
                dcc.Input(
                    type = 'password',
                    placeholder = placeholder
                )
            ]
        )


    def submit_button(self, text:str, color:str) -> dcc.Input:
        return dcc.Input(
            type = 'submit',
            value = text,
            className = f'login-button bg-{color} bg-hover-{color}'
        )



class LoginPage(dbc.Container):

    def __init__(self, left_panel, right_panel):
        super().__init__(
            children = dbc.Row([
                dbc.Col(
                    left_panel,
                    width = 6,
                    style = {'min-height': '100%'}
                ),
                dbc.Col(
                    right_panel,
                    width = 6,
                    style = {'min-height': '100%'}
                )
            ],
                class_name = 'g-0 shadow'
            ),
            style = {
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
                'text-align': 'center',
                'min-height': '90vh'
            }
        )
