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
    header : str
        Column name.
    header_style : dict[str,str], optional
        Style of the header of the column.
    cell_id : Iterable, optional
        IDs of the cells.
    cell_style : dict[str,str], optional
        Dictionary of CSS to be applied to every cell.
    cell_class : str, optional
        Class name of the cell.

    Attributes
    ----------
    th : dash.html.Th
        HTML Header of the column.

    """

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            header_style: Optional[Dict[str,str]] = None
        ):

        # Check if `id` is a not-string iterable
        if not hasattr(id, '__iter__') or isinstance(id, str):
            raise CharlotteTableError('`id` must be an iterable object.')
        self.id = id

        self.th = html.Th(
            children = header,
            style = header_style or {}
        )


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

        

class TableButtonCol(TableColumn):

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            header_style: Optional[Dict[str,str]] = None,
            cell_id: Optional[Iterable] = None,
            cell_style: Optional[Dict[str,str]] = None,
            cell_class: Optional[str] = None,
            text: Union[str, Iterable[str], None] = None,
            icon: Union[str, Iterable[str], None] = None,
            **button_kwargs
        ):

        super().__init__(
            id = id,
            header = header,
            header_style = header_style
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
                style = cell_style or {},
                className = cell_class,
                id = i_cell or str(uuid4()),
                children = dbc.Button(
                    id = i_id,
                    children = [
                        i_icon and html.I(className=f'{i_icon} me-2'),
                        i_text and html.Span(children=i_text)
                    ],
                    **kwargs
                )
            ) for i_id, i_cell, kwargs, i_text, i_icon in z
        ]


    def __len__(self) -> int:
        return len(self.id)



class TableCheckBoxCol(TableColumn):

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            header_style: Optional[Dict[str,str]] = None,
            cell_id: Optional[Iterable] = None,
            cell_style: Optional[Dict[str,str]] = None,
            cell_class: Optional[str] = None,
            **checkbox_kwargs
        ):

        super().__init__(
            id = id,
            header = header,
            header_style = header_style
        )

        z = zip(
            self.id,
            self._expand_param(cell_id),
            self._break_kwargs(checkbox_kwargs)
        )

        self.td = [
            html.Td(
                style = cell_style or {},
                className = cell_class,
                id = i_cell or str(uuid4()),
                children = dbc.Checkbox(
                    id = i_id,
                    **kwargs
                )
            ) for i_id, i_cell, kwargs in z
        ]



    def __len__(self) -> int:
        return len(self.id)



class TableDropdownCol(TableColumn):

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            header_style: Optional[Dict[str,str]] = None,
            cell_id: Optional[Iterable] = None,
            cell_style: Optional[Dict[str,str]] = None,
            cell_class: Optional[str] = None,
            **dropdown_kwargs
        ):

        super().__init__(
            id = id,
            header = header,
            header_style = header_style
        )

        z = zip(
            self.id,
            self._expand_param(cell_id),
            self._break_kwargs(dropdown_kwargs),
        )

        self.td = [
            html.Td(
                style = cell_style or {},
                className = cell_class,
                id = i_cell or str(uuid4()),
                children = dcc.Dropdown(
                    id = i_id,
                    **kwargs
                )
            ) for i_id, i_cell, kwargs in z
        ]


    def __len__(self) -> int:
        return len(self.id)



class TableInputCol(TableColumn):

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            header_style: Optional[Dict[str,str]] = None,
            cell_id: Optional[Iterable] = None,
            cell_style: Optional[Dict[str,str]] = None,
            cell_class: Optional[str] = None,
            **input_kwargs
        ):

        super().__init__(
            id = id,
            header = header,
            header_style = header_style
        )

        z = zip(
            self.id,
            self._expand_param(cell_id),
            self._break_kwargs(input_kwargs)
        )

        self.td = [
            html.Td(
                style = cell_style or {},
                className = cell_class,
                id = i_cell or str(uuid4()),
                children = dbc.Input(
                    id = i_id,
                    **kwargs
                )
            ) for i_id, i_cell, kwargs in z
        ]


    def __len__(self) -> int:
        return len(self.id)



class TableTextCol(TableColumn):
    """Default Text Column.
    
    Parameters
    ----------
    text : Iterable
        Text inside the cell before formatting.
    text_formatting : Callable, optional
        Format function to be applied to the children.

    Attributes
    ----------
    td : list[dash.html.Td]
        List of HTML table data.

    """

    def __init__(
            self,
            id: Iterable[str],
            header: str,
            header_style: Optional[Dict[str,str]] = None,
            text_formatting: Optional[Callable] = None,
            cell_id: Optional[Iterable] = None,
            cell_style: Optional[Dict[str,str]] = None,
            cell_class: Optional[str] = None,
            text: Union[Iterable, str, None] = None,
            **span_kwargs
        ):

        fmt = text_formatting or '{}'.format

        super().__init__(
            id = id,
            header = header,
            header_style = header_style
        )

        z = zip(
            self.id,
            self._expand_param(cell_id),
            self._break_kwargs(span_kwargs),
            self._expand_param(text),
        )

        self.td = [
            html.Td(
                style = cell_style or {},
                className = cell_class,
                id = i_cell or str(uuid4()),
                children = html.Span(
                    children = fmt(i_text),
                    id = i_id,
                    **kwargs
                )
            ) for i_id, i_cell, kwargs, i_text in z
        ]


    def __len__(self) -> int:
        return len(self.id)



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
    
    """
    
    def __init__(
            self,
            columns: List[TableColumn],
            header_style: Optional[Dict[str,str]] = None,
            body_style: Optional[Dict[str,str]] = None,
            row_style: Optional[Dict[str,str]] = None,
            row_id: Optional[Iterable[str]] = None,
            **kwargs
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
            **kwargs
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
