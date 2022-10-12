import requests



def minify(file_content:str) -> str:
    """Access Toptal's CSS Minifier API.
    
    Parameters
    ----------
    file_content : str
        CSS file content in str format.

    Returns
    -------
    str
        Minifier CSS in str format.

    """

    payload = {'input': file_content}
    url = 'https://www.toptal.com/developers/cssminifier/raw'
    r = requests.post(url, payload)
    return r.text



if __name__ == '__main__':

    # Names of the files located at `css_themes` folder
    CSS_FILES = [
        'components',
        'charlotte_dark',
        'charlotte_light',
        'dracula'
    ]

    for file in CSS_FILES:

        with open(f'css_themes/{file}.css', 'r') as r:
            file_content = r.read()
        
        minified = minify(file_content)

        with open(f'css_themes/{file}.min.css', 'w') as w:
            w.write(minified)
