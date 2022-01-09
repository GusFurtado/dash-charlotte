"""Módulo de padronização de cores do Dash Charlotte.

"""


import colorsys



class Color:
    """Objeto Cor

    Parmeters
    ---------
    rgb : str
        Código HEX da cor.

    Attributes
    ----------
    red : ype.colors.Color.ColorDecomposition
        Componente vermelho da cor.
    green : ype.colors.Color.ColorDecomposition
        Componente verde da cor.
    blue : ype.colors.Color.ColorDecomposition
        Componente azul da cor.
    
    Methods
    -------
    __call__(light:float) -> str
        Altera a luminosidade da cor.

    """

    class ColorDecomposition:
        def __init__(self, hex):
            self.hex = hex
            self.int = int(hex,16)
        def __str__(self) -> str:
            return self.hex
        def __repr__(self) -> str:
            return self.hex


    def __init__(self, rgb:str):

        # Parsing
        self.rgb = str(rgb)
        if self.rgb.startswith('#'):
            self.rgb = self.rgb[1:]

        # Decompor
        self.red = self.ColorDecomposition(self.rgb[:2])
        self.green = self.ColorDecomposition(self.rgb[2:4])
        self.blue = self.ColorDecomposition(self.rgb[-2:])

        # Alias
        self.r = self.red
        self.g = self.green
        self.b = self.blue


    def __repr__(self) -> str:
        return f'<ype.colors.Color: #{self.rgb}>'


    def __str__(self) -> str:
        return f'#{self.rgb}'


    def __call__(self, light:float) -> str:
        """Altera a luminosidade da cor.

        Parameters
        ----------
        light : float
            Novo valor percentual de luminosidade (entre 0 e 1).

        Returns
        -------
        str
            Nova cor no formato '#RRGGBB'.
        
        """

        float2hex = lambda x: f'0{int(round(255*x,0)):x}'[-2:]

        hls = colorsys.rgb_to_hls(
            r = self.r.int/255,
            g = self.g.int/255,
            b = self.b.int/255
        )

        rgb = colorsys.hls_to_rgb(
            h = hls[0],
            l = light,
            s = hls[2]
        )

        return f'#{float2hex(rgb[0])}{float2hex(rgb[1])}{float2hex(rgb[2])}'
