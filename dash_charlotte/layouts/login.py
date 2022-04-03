from typing import Optional
from uuid import uuid4

from dash import html, dcc
import dash_bootstrap_components as dbc



class SvgImage(html.Div):
    """A panel containing an image.

    Parameters
    ----------
    src : str
        Source of the image.
    
    """

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
    """Form to be added in the `LoginPage` component.

    Parameters
    ----------
    id : str, optional
        Component id.
    title_text : str, default='Log in'
        Text displayed at the top of the form.
    title_color : str, default='shade6'
        Color class of the title text.
    subtitle_text : str, default='Enter your username and password'
        Text display right below the title text.
    subtitle_color : str, default='shade4'
        Color class of the subtitle text.
    email_placeholder : str, default='Username'
        Placeholder text of the email input.
    password_placeholder : str, default='Password'
        Placeholder text of the password input.
    button_text : str, default='Log in'
        Text of the submit button.
    button_color : str, default='blue'
        Color class of the submit button.

    Components IDs
    --------------
    {id}
        Main content (children).
    {id}--title
        Title text element.
    {id}--subtitle
        Subtitle text element.
    {id}--email
        Value of the email input field.
    {id}--password
        Value of the password input field.
    {id}--button
        Submit button.

    """

    def __init__(
            self,
            id: Optional[str] = None,
            title_text: str = 'Log in',
            title_color: str = 'shade6',
            subtitle_text: str = 'Enter your username and password',
            subtitle_color: str = 'shade4',
            email_placeholder: str = 'Username',
            password_placeholder: str = 'Password',
            button_text: str = 'Log in',
            button_color: str = 'blue'
        ):

        self.id = id or str(uuid4())

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
                        text = title_text,
                        color = title_color
                    ),
                    self.subtitle_text(
                        text = subtitle_text,
                        color = subtitle_color
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


    def title_text(self, text, color:str) -> html.H2:
        return html.H2(
            className = f'{color} mb-2',
            id = f'{self.id}--title',
            children = text
        )


    def subtitle_text(self, text, color:str) -> html.H5:
        return html.H5(
            className = f'{color} mb-4',
            id = f'{self.id}--subtitle',
            children = text,
            style = {'text-align': 'center'}
        )


    def email_input(self, placeholder:str) -> html.Div:
        return html.Div(
            className = 'input-field',
            children = [
                html.I(
                    className = 'fas fa-user'
                ),
                dcc.Input(
                    id = f'{self.id}--email',
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
                    id = f'{self.id}--password',
                    type = 'password',
                    placeholder = placeholder
                )
            ]
        )


    def submit_button(self, text:str, color:str) -> dcc.Input:
        return dcc.Input(
            id = f'{self.id}--button',
            type = 'submit',
            value = text,
            className = f'login-button bg-{color} bg-hover-{color}'
        )



class LoginPage(dbc.Container):
    """LoginPage layout.

    Parameters
    ----------
    left_panel : list of Dash components
        Content of the left panel.
    right_panel : list of Dash components
        Content of the right panel.
    left_panel_width : int, default = 6
        Width of the left panel, from 1 to 12.
    right_panel_width : int, default = 6
        Width of the right panel, from 1 to 12.
    id : str, optional
        Component id.

    Attributes
    ----------
    {id}-left-panel : list of Dash components
        Content of the left panel.
    {id}-right-panel : list of Dash components
        Content of the right panel.

    """

    def __init__(
            self,
            left_panel,
            right_panel,
            left_panel_width: int = 6,
            right_panel_width: int = 6,
            id: Optional[str] = None
        ):

        id = id or str(uuid4())

        super().__init__(
            children = dbc.Row([
                dbc.Col(
                    children = left_panel,
                    id = f'{id}--left-panel',
                    width = left_panel_width,
                    style = {'min-height': '100%'}
                ),
                dbc.Col(
                    children = right_panel,
                    id = f'{id}--right-panel',
                    width = right_panel_width,
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
