# Native Python packages
import logging
from socket import gethostname

# Web stuff
from dash import (
    Dash,
    Input,
    Output,
    no_update,
    page_container
)
from flask import Flask
{% if cookiecutter.environment == "windows" %}from waitress import serve
{% endif %}
# Charlotte components
from components import (
    Dashboard,
    Drawer,
    DrawerSingleItem,
    DrawerMultiItem,
    DrawerSubItem,
    DrawerFooter,
    Navbar
)
from pages.login.login_auth import LoginAuth


# Create server with secret key
server = Flask(__name__)
server.secret_key = 'SECRET_KEY'



# Instanciate Dash app
app = Dash(
    name = __name__,
    server = server,
    title = '{{cookiecutter.app_name}}',
    use_pages = True,
    update_title = 'Updating...',
)



# Instanciate Error Handler
file_handler = logging.FileHandler('data/errorlog.log')
file_handler.setLevel(logging.WARNING)
server.logger.addHandler(file_handler)



# Create Drawer
nav_links = [
    DrawerSingleItem(
        name = 'Login',
        icon = 'bx:log-in',
        href = '/login'
    ),
    DrawerSingleItem(
        name = 'Page 1',
        icon = 'bx:scatter-chart',
        href = '/page1'
    ),
    DrawerMultiItem(
        name = 'Page2',
        icon = 'bx:line-chart',
        href = '/page2/subpage1',
        submenu = [
            DrawerSubItem(
                name = 'Subpage 1',
                href = '/page2/subpage1'
            ),
            DrawerSubItem(
                name = 'Subpage 2',
                href = '/page2/subpage2'
            )
        ]
    ),
    DrawerFooter(
        title = 'Footer',
        subtitle = 'Footer Subtitle'
    )
]



# Create Dashboard Layout
app.layout = Dashboard(
    children = page_container,
    id = 'dashboard',
    navbar = Navbar(
        title = 'My Web App',
        id = 'dashboard-navbar'
    ),
    drawer = Drawer(
        menu = nav_links,
        logo_name = 'Charlotte',
        logo_icon = 'heroicons:rocket-launch-20-solid'
    )
)



{% if cookiecutter.add_login_page %}@app.callback(
    Output('dashboard--location', 'href'),
    Output('dashboard-navbar--title', 'children'),
    Input('dashboard--location', 'pathname'))
def init_app(path):
    """Redirects to login page if user is not logged in.
    
    Inputs
    ------
    dashboard--location.pathname
        Page the user is trying to access.

    Outputs
    -------
    dashboard--location.href
        URL of the login page to which the user is redirected.
    dashboard-navbar--title.children
        Updated navbar title.

    """

    # Get current HTTP status
    status = LoginAuth.check_status()

    # Change Navbar title if user is authenticated
    if (status==200) or (path=='/login'):
        try:
            return no_update, {
                '/login': 'User Authentication',
                '/page1': 'Example Page 1'
            }[path]
        except KeyError:
            return no_update, '{{cookiecutter.app_name}}'

    # Change Navbar title if user had access denied
    elif path=='/forbidden':
        return no_update, 'Unauthorized User'

    # Go to 403 page
    elif status==403:
        return f'http://{gethostname()}:{{cookiecutter.port}}/forbidden', no_update

    # Go to login page
    elif status==401:
        return f'http://{gethostname()}:{{cookiecutter.port}}/login?page={path}', no_update
{% endif %}{% if cookiecutter.environment == "windows" %}


# Run app
if __name__ == '__main__':
    serve(
        app = app.server,
        port = {{cookiecutter.port}}
    )
{% elif cookiecutter.environment == "dev" %}


# Run app
if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = {{cookiecutter.port}}
    )
{% endif %}