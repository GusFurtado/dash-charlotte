from typing import Optional
from uuid import uuid4

from dash import html, dcc
import dash_bootstrap_components as dbc



class LoginSvgPanel(html.Div):
    """A panel containing an image.

    Parameters
    ----------
    src : str
        Source of the image.
    background : {'svg', one of the color classes}, default='svg'
        Background color of the panel.
    padding : int, default=30
        Padding of the panel, in pixels

    """

    def __init__(
            self,
            src: str,
            background: str = 'svg',
            padding: int = 30
        ):

        if background == 'svg':
            background = 'login-svg-background'
        else:
            background = f'bg-{background}'

        super().__init__(
            className = background,
            children = html.Img(
                src = src,
                style = {
                    'maxHeight': '100%',
                    'maxWidth': '100%',
                    'padding': padding
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
    user_placeholder : str, default='Username'
        Placeholder text of the user input.
    password_placeholder : str, default='Password'
        Placeholder text of the password input.
    button_text : str, default='Log in'
        Text of the submit button.
    button_color : str, default='blue'
        Color class of the submit button.

    Component Properties
    --------------------
    {id}
        Main content (children).
    {id}--title
        Title text element.
    {id}--subtitle
        Subtitle text element.
    {id}--user
        Value of the user input field.
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
            user_placeholder: str = 'Username',
            password_placeholder: str = 'Password',
            button_text: str = 'Log in',
            button_color: str = 'blue'
        ):

        self.id = id or str(uuid4())

        super().__init__(
            style = {
                'min-height': '100%',
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
                    self.user_input(
                        placeholder = user_placeholder
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


    def user_input(self, placeholder:str) -> html.Div:
        return html.Div(
            className = 'input-field',
            children = [
                html.I(
                    className = 'fas fa-user'
                ),
                dcc.Input(
                    id = f'{self.id}--user',
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
                    placeholder = placeholder,
                    debounce = True
                )
            ]
        )


    def submit_button(self, text:str, color:str) -> html.Div:
        return html.Div(
            children = text,
            id = f'{self.id}--button',
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

    Component Properties
    --------------------
    {id}--left-panel : list of Dash components
        Content of the left panel.
    {id}--right-panel : list of Dash components
        Content of the right panel.
    {id}--location : dash.dcc.Location
        URL manager.

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
            children = [
                dcc.Location(id = f'{id}--location'),
                dbc.Row([
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
                )
            ],
            style = {
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
                'text-align': 'center',
                'min-height': '90vh'
            }
        )
