from typing import (
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Union
)
from uuid import uuid4

from dash import html, dcc
import dash_bootstrap_components as dbc



class CharlotteTableError(ValueError):
    """Error on building a Charlotte Table."""
    pass



class TableColumn:
    """Table Column Base Class.

    Parameters
    ----------
    id : Iterable[str]
        A list of the ids of each cell.
    header : str
        Column name.
    **header_kwargs
        Every other argument of a `html.Th` component.

    Attributes
    ----------
    th : dash.html.Th
        HTML Header of the column.

    """

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            **header_kwargs
        ):

        # Check if `id` is a not-string iterable
        if not hasattr(id, '__iter__') or isinstance(id, str):
            raise CharlotteTableError('`id` must be an iterable object.')
        self.id = id

        self.header = header 

        self.th = html.Th(
            children = header,
            **header_kwargs
        )


    def __len__(self) -> int:
        return len(self.id)


    def __repr__(self) -> str:
        return f"<Charlotte Table Column: '{self.header}'>"


    def __str__(self) -> str:
        return f'Charlotte Table Column {self.header}'


    def _break_kwargs(self, kwargs:dict) -> List[dict]:

        # The Dropdown Options Exception
        if 'options' in kwargs:
            if isinstance(kwargs['options'][0], dict):
                kwargs['options'] = [kwargs['options'] for _ in self.id]

        # The Style Exception
        if 'style' in kwargs:
            if isinstance(kwargs['style'], dict):
                kwargs['style'] = [kwargs['style'] for _ in self.id]

        for kwarg in kwargs:
            kwargs[kwarg] = self._expand_param(kwargs[kwarg])

        list_of_kwargs = []
        for i, _ in enumerate(self.id):
            list_of_kwargs.append(
                {kwarg: kwargs[kwarg][i] for kwarg in kwargs}
            )

        return list_of_kwargs


    def _expand_param(self, param) -> Iterable:
        """Convert a single value into a list.

        Ignore if the value is already an iterable.

        Parameters
        ----------
        param : Any
            Value to be converted.
        
        """

        if not hasattr(param, '__iter__') or isinstance(param, str):
            param = [param for _ in self.id]
        return param


    def _filter_kwargs(self, kwargs:dict, component_type:str) -> dict:
        """Filter the original kwargs.

        Convert the original kwargs of the column component into a smaller set
        of one subcomponent kwargs.

        Parameters
        ----------
        kwargs : dict
            The original kwargs of the table.
        component_type : {'header', 'cell', 'loading', ...}
            Prefix of the desired subcomponent kwargs.
        
        Returns
        -------
        dict
            Subset of the original kwargs dict.

        """

        return {key[len(component_type)+1:]: kwargs[key] \
            for key in kwargs if key.startswith(f'{component_type}_')}


    def _loading_wrapper(
            self,
            dash_component,
            loading: bool,
            **loading_kwargs
        ):
        """Wraps a dash component in a `dcc.Loading` component.

        Ignore if `loading=False`.

        Parameters
        ----------
        dash_component
            The component to be wrapped.
        loading : bool
            Activate or not the `Loading` wrapper.
        **loading_kwargs
            All the arguments of a `dcc.Loading` component.
        
        """

        if not loading:
            return dash_component
        return dcc.Loading(
            children = dash_component,
            **loading_kwargs
        )

        

class TableButtonCol(TableColumn):
    """A columns of buttons for the `Table` component.

    Parameters
    ----------
    id : Iterable[str | dict]
        A series of ids for each button.
    header : str
        Name of the column.
    text : str, Iterable[str], optional
        The text of a series of text for each button.
    icon : str, Iterable[str], optional
        An icon reference of a series of icons for each button.
    cell_id : Iterable, optional
        A series of ids for each table cell.
    loading : bool, default=False
        Activate a loading wrapper in the buttons.

    Kwargs
    ------
    Pass every other subcomponent argument through kwargs using an underscore
    joining the component type and the argument name.

    e.g.: `loading_type`, `header_className`, `cell_style`

    These are the available subcomponents of these `TableColumn`
    - `button_{kwarg}`
    - `cell_{kwarg}`
    - `header_{kwarg}`
    - `loading_{kwarg}`
    
    Example
    -------
    >>> col = TableButtonCol(
    ...     id = ['id_1', 'id_2', 'id_n'],
    ...     header = 'Button Column,
    ...     text = 'Default Text',
    ...     icon = 'fas fa-exclamation-triangle',
    ...     header_style = {'background-color': 'cyan'},
    ...     button_size = 'sm',
    ...     cell_className = 'bg-shade1'
    ... )

    """

    def __init__(
            self,
            id: Iterable[Union[str, dict]],
            header: str,
            text: Union[str, Iterable[str], None] = None,
            icon: Union[str, Iterable[str], None] = None,
            cell_id: Optional[Iterable] = None,
            loading: bool = False,
            **kwargs
        ):

        button_kwargs = self._filter_kwargs(kwargs, 'button')
        cell_kwargs = self._filter_kwargs(kwargs, 'cell')
        header_kwargs = self._filter_kwargs(kwargs, 'header')
        loading_kwargs = self._filter_kwargs(kwargs, 'loading')

        super().__init__(
            id = id,
            header = header,
            **header_kwargs
        )

        z = zip(
            self.id,
            self._expand_param(cell_id),
            self._break_kwargs(button_kwargs),
            self._expand_param(text),
            self._expand_param(icon)
        )

        self.td = [
            html.Td(
                id = i_cell or str(uuid4()),
                children = self._loading_wrapper(
                    loading = loading,
                    dash_component = dbc.Button(
                        id = i_id,
                        children = [
                            i_icon and html.I(className=f'{i_icon} me-2'),
                            i_text and html.Span(children=i_text)
                        ],
                        **b_kwargs
                    ),
                    **loading_kwargs
                ),
                **cell_kwargs
            ) for i_id, i_cell, b_kwargs, i_text, i_icon in z
        ]



class TableCheckBoxCol(TableColumn):
    """A columns of checkboxes for the `Table` component.

    Parameters
    ----------
    id : Iterable[str | dict]
        A series of ids for each button.
    header : str
        Name of the column.
    cell_id : Iterable, optional
        A series of ids for each table cell.
    loading : bool, default=False
        Activate a loading wrapper in the buttons.

    Kwargs
    ------
    Pass every other subcomponent argument through kwargs using an underscore
    joining the component type and the argument name.

    e.g.: `loading_type`, `header_className`, `cell_style`

    These are the available subcomponents of these `TableColumn`
    - `checkbox_{kwarg}`
    - `cell_{kwarg}`
    - `header_{kwarg}`
    - `loading_{kwarg}`
    
    Example
    -------
    >>> col = TableCheckBoxCol(
    ...     id = ['id_1', 'id_2', 'id_n'],
    ...     header = 'Checkbox Column,
    ...     header_style = {'background-color': 'cyan'},
    ...     cell_className = 'bg-shade1',
    ...     checkbox_value = [False, True, False]
    ... )

    """

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            cell_id: Optional[Iterable] = None,
            loading: bool = False,
            **kwargs
        ):

        checkbox_kwargs = self._filter_kwargs(kwargs, 'checkbox')
        cell_kwargs = self._filter_kwargs(kwargs, 'cell')
        header_kwargs = self._filter_kwargs(kwargs, 'header')
        loading_kwargs = self._filter_kwargs(kwargs, 'loading')

        super().__init__(
            id = id,
            header = header,
            **header_kwargs
        )

        z = zip(
            self.id,
            self._expand_param(cell_id),
            self._break_kwargs(checkbox_kwargs)
        )

        self.td = [
            html.Td(
                id = i_cell or str(uuid4()),
                children = self._loading_wrapper(
                    loading = loading,
                    dash_component = dbc.Checkbox(
                        id = i_id,
                        **c_kwargs
                    ),
                    **loading_kwargs
                ),
                **cell_kwargs
            ) for i_id, i_cell, c_kwargs in z
        ]



class TableDropdownCol(TableColumn):
    """A columns of dropdown lists for the `Table` component.

    Parameters
    ----------
    id : Iterable[str | dict]
        A series of ids for each button.
    header : str
        Name of the column.
    cell_id : Iterable, optional
        A series of ids for each table cell.
    loading : bool, default=False
        Activate a loading wrapper in the buttons.

    Kwargs
    ------
    Pass every other subcomponent argument through kwargs using an underscore
    joining the component type and the argument name.

    e.g.: `loading_type`, `header_className`, `cell_style`

    These are the available subcomponents of these `TableColumn`
    - `dropdown_{kwarg}`
    - `cell_{kwarg}`
    - `header_{kwarg}`
    - `loading_{kwarg}`
    
    Example
    -------
    >>> col = TableDropdownCol(
    ...     id = ['id_1', 'id_2', 'id_n'],
    ...     header = 'Dropdown Column,
    ...     header_style = {'background-color': 'cyan'},
    ...     cell_className = 'bg-shade1',
    ...     dropdown_value = [True, False, True],
    ...     dropdown_options = [
    ...         {'label': 'Yes', 'value': True},
    ...         {'label': 'No', 'value': False}
    ...     ],
    ...     dropdown_clearable = False
    ... )

    """

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            cell_id: Optional[Iterable] = None,
            loading: bool = False,
            **kwargs
        ):

        dropdown_kwargs = self._filter_kwargs(kwargs, 'dropdown')
        cell_kwargs = self._filter_kwargs(kwargs, 'cell')
        header_kwargs = self._filter_kwargs(kwargs, 'header')
        loading_kwargs = self._filter_kwargs(kwargs, 'loading')

        super().__init__(
            id = id,
            header = header,
            **header_kwargs
        )

        z = zip(
            self.id,
            self._expand_param(cell_id),
            self._break_kwargs(dropdown_kwargs),
        )

        self.td = [
            html.Td(
                id = i_cell or str(uuid4()),
                children = self._loading_wrapper(
                    loading = loading,
                    dash_component = dcc.Dropdown(
                        id = i_id,
                        **d_kwargs
                    ),
                    **loading_kwargs
                ),
                **cell_kwargs
            ) for i_id, i_cell, d_kwargs in z
        ]



class TableInputCol(TableColumn):
    """A columns of input fields for the `Table` component.

    Parameters
    ----------
    id : Iterable[str | dict]
        A series of ids for each button.
    header : str
        Name of the column.
    cell_id : Iterable, optional
        A series of ids for each table cell.
    loading : bool, default=False
        Activate a loading wrapper in the buttons.

    Kwargs
    ------
    Pass every other subcomponent argument through kwargs using an underscore
    joining the component type and the argument name.

    e.g.: `loading_type`, `header_className`, `cell_style`

    These are the available subcomponents of these `TableColumn`
    - `input_{kwarg}`
    - `cell_{kwarg}`
    - `header_{kwarg}`
    - `loading_{kwarg}`
    
    Example
    -------
    >>> col = TableInputCol(
    ...     id = ['id_1', 'id_2', 'id_n'],
    ...     header = 'Input Column,
    ...     header_style = {'background-color': 'cyan'},
    ...     cell_className = 'bg-shade1',
    ...     input_type = 'number',
    ...     input_min = 0,
    ...     input_max = 9,
    ...     input_step = 1,
    ...     input_value = [2,3,4]
    ... )

    """

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            cell_id: Optional[Iterable] = None,
            loading: bool = False,
            **kwargs
        ):

        input_kwargs = self._filter_kwargs(kwargs, 'input')
        cell_kwargs = self._filter_kwargs(kwargs, 'cell')
        header_kwargs = self._filter_kwargs(kwargs, 'header')
        loading_kwargs = self._filter_kwargs(kwargs, 'loading')

        super().__init__(
            id = id,
            header = header,
            **header_kwargs
        )

        z = zip(
            self.id,
            self._expand_param(cell_id),
            self._break_kwargs(input_kwargs)
        )

        self.td = [
            html.Td(
                id = i_cell or str(uuid4()),
                children = self._loading_wrapper(
                    loading = loading,
                    dash_component = dbc.Input(
                        id = i_id,
                        **i_kwargs
                    ),
                    **loading_kwargs
                ),
                **cell_kwargs
            ) for i_id, i_cell, i_kwargs in z
        ]



class TableTextCol(TableColumn):
    """A columns of text for the `Table` component.

    Parameters
    ----------
    id : Iterable[str | dict]
        A series of ids for each button.
    header : str
        Name of the column.
    text : str | Iterable[str], optional
        Text or series of text to be shown in each cell.
    text_format : Callable, optional
        Text format function.
    cell_id : Iterable, optional
        A series of ids for each table cell.
    loading : bool, default=False
        Activate a loading wrapper in the buttons.

    Kwargs
    ------
    Pass every other subcomponent argument through kwargs using an underscore
    joining the component type and the argument name.

    e.g.: `loading_type`, `header_className`, `cell_style`

    These are the available subcomponents of these `TableColumn`
    - `text_{kwarg}`
    - `cell_{kwarg}`
    - `header_{kwarg}`
    - `loading_{kwarg}`
    
    Example
    -------
    >>> col = TableTextCol(
    ...     id = ['id_1', 'id_2', 'id_n'],
    ...     header = 'Text Column,
    ...     header_style = {'background-color': 'cyan'},
    ...     text = [1111.11, 2222.22, 3333.33],
    ...     text_format = '{:.2%}'.format,
    ...     text_className = 'red',
    ...     cell_className = 'bg-shade1'
    ... )

    """

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            text: Union[Iterable, str, None] = None,
            text_format: Optional[Callable] = None,
            cell_id: Optional[Iterable] = None,
            loading: bool = False,
            **kwargs
        ):

        fmt = text_format or '{}'.format

        text_kwargs = self._filter_kwargs(kwargs, 'text')
        cell_kwargs = self._filter_kwargs(kwargs, 'cell')
        header_kwargs = self._filter_kwargs(kwargs, 'header')
        loading_kwargs = self._filter_kwargs(kwargs, 'loading')

        super().__init__(
            id = id,
            header = header,
            **header_kwargs
        )

        z = zip(
            self.id,
            self._expand_param(cell_id),
            self._break_kwargs(text_kwargs),
            self._expand_param(text),
        )

        self.td = [
            html.Td(
                id = i_cell or str(uuid4()),
                children = self._loading_wrapper(
                    loading = loading,
                    dash_component = html.Span(
                        children = fmt(i_text),
                        id = i_id,
                        **t_kwargs
                    ),
                    **loading_kwargs
                ),
                **cell_kwargs
            ) for i_id, i_cell, t_kwargs, i_text in z
        ]



class Table(dbc.Table):
    """A wrapper for `TableColumns`.

    Parameters
    ----------
    columns : list[TableColumn]
        A list of `TableColumns`.
    header_style : dict[str,str], optional
        The style of the header of the table.
    body_style : dict[str,str], optional
        The style of the doby of the table.
    row_style : dict[str,str], optional
        The style applied to each row of the table.
    row_id : Iterable[str], optional
        A list of the `ids` of each row.
    **table_kwargs
        Every other argument of a `dbc.Table`
    
    """
    
    def __init__(
            self,
            columns: List[TableColumn],
            header_style: Optional[Dict[str,str]] = None,
            body_style: Optional[Dict[str,str]] = None,
            row_style: Optional[Dict[str,str]] = None,
            row_id: Optional[Iterable[str]] = None,
            **table_kwargs
        ):

        self.columns = columns

        super().__init__(
            children = [
                self._thead(
                    header_style = header_style or {},
                ),
                self._tbody(
                    body_style = body_style or {},
                    row_style = row_style or {},
                    row_id = row_id
                )
            ],
            **table_kwargs
        )


    def _thead(self, header_style:Dict[str,str]) -> html.Thead:
        return html.Thead(
            style = header_style,
            children = [col.th for col in self.columns]
        )


    def _tr(self, index:int, id:str, style:Dict[str,str]) -> html.Tr:
        return html.Tr(
            children = [col.td[index] for col in self.columns],
            id = id,
            style = style
        )


    def _tbody(
            self,
            body_style: Dict[str,str],
            row_style: Dict[str,str],
            row_id: Iterable
        ) -> html.Tbody:

        # Checking lenght of columns
        col_lenghts = [len(col) for col in self.columns]
        if len(set(col_lenghts)) > 1:
            raise CharlotteTableError("Lenghts of columns don't match.")

        # Checking row ids
        if row_id is None:
            row_id = [str(uuid4()) for _ in range(col_lenghts[0])]
        else:
            if len(row_id) != col_lenghts[0]:
                raise CharlotteTableError("Lenght of `row_id` doesn't match the columns lenghts.")

        # Creating a `html.Tr` for each id
        return html.Tbody(
            style = body_style,
            children = [
                self._tr(
                    index = i,
                    id = id,
                    style = row_style    
                ) for i, id in enumerate(row_id)
            ]
        )
