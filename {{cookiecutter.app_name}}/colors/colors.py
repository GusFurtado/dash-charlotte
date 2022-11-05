import colorsys



class Color:
    """Charlotte color object.

    Parmeters
    ---------
    rgb : str
        HEX code.

    Attributes
    ----------
    red : ype.colors.Color.ColorDecomposition
        Red component.
    green : ype.colors.Color.ColorDecomposition
        Green component.
    blue : ype.colors.Color.ColorDecomposition
        Blue component.
    
    Methods
    -------
    __call__(light:float) -> str
        Set a new color lightness.

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

        # Decompose
        self.red = self.ColorDecomposition(self.rgb[:2])
        self.green = self.ColorDecomposition(self.rgb[2:4])
        self.blue = self.ColorDecomposition(self.rgb[-2:])

        # Alias
        self.r = self.red
        self.g = self.green
        self.b = self.blue


    def __str__(self) -> str:
        return f'#{self.rgb}'


    def __repr__(self) -> str:
        return self.__str__()


    def __call__(self, light:float):
        """Set a new color lightness.

        Parameters
        ----------
        light : float
            New lightness value (between 0 and 1).

        Returns
        -------
        Color
            New color object.
        
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

        return Color(f'{float2hex(rgb[0])}{float2hex(rgb[1])}{float2hex(rgb[2])}')
