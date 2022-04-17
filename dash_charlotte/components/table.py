from dataclasses import dataclass
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



@dataclass
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

    Methods
    -------
    expand_param(param, reference, param_type=str)
        Convert a single value into a list.

    """

    header: str
    header_style: Optional[Dict[str,str]] = None
    cell_id: Optional[Iterable] = None
    cell_style: Optional[Dict[str,str]] = None
    cell_class: Optional[str] = None

    def __post_init__(self):
        self.th = html.Th(
            children = self.header,
            style = self.header_style or {}
        )

    def expand_param(
            self,
            param,
            reference: Iterable,
            param_type = str
        ) -> Iterable:
        """Convert a single value into a list.

        Ignore if the value is already a list.

        Parameters
        ----------
        param : Any
            Value to be converted.
        reference : Iterable
            Reference column.
            Necessary to know how many columns there are in the table.
        param_type : Type, default=str
            Type of the value.
        
        """

        if (param is None) or isinstance(param, param_type):
            param = [param for _ in reference]
        return param

        

class TableButtonCol(TableColumn):

    def __init__(
            self,
            button_id: Optional[Iterable[str]],
            button_text: Union[str, Iterable[str], None] = None,
            button_icon: Union[str, Iterable[str], None] = None,
            button_size: Union[str, Iterable[str]] = 'sm',
            button_color: Union[str, Iterable[str]] = 'primary',
            **kwargs
        ):

        super().__init__(**kwargs)
        self.button_id = button_id

        params = zip(
            button_id,
            self.expand_param(button_text, button_id),
            self.expand_param(button_icon, button_id),
            self.expand_param(button_size, button_id),
            self.expand_param(button_color, button_id)
        )

        self.td = [
            html.Td(
                style = self.cell_style,
                className = self.cell_class,
                children = dbc.Button(
                    size = size,
                    color = color,
                    id = id,
                    children = [
                        icon and html.I(className=f'{icon} me-2'),
                        text and html.Span(children=text)
                    ]
                )
            ) for id, text, icon, size, color in params
        ]

    def __len__(self) -> int:
        return len(self.button_id)



class TableCheckBoxCol(TableColumn):

    def __init__(
            self,
            checkbox_id: Optional[Iterable[str]],
            checkbox_value: Union[str, Iterable[bool]] = False,
            checkbox_label: Union[str, Iterable[bool], None] = None,
            checkbox_disabled: Union[bool, Iterable[bool]] = False,
            **kwargs
        ):

        super().__init__(**kwargs)
        self.checkbox_id = checkbox_id

        params = zip(
            checkbox_id,
            self.expand_param(checkbox_value, checkbox_id, bool),
            self.expand_param(checkbox_label, checkbox_id),
            self.expand_param(checkbox_disabled, checkbox_id, bool)
        )

        self.td = [
            html.Td(
                style = self.cell_style,
                className = self.cell_class,
                children = dbc.Checkbox(
                    value = value,
                    label = label,
                    disabled = disabled,
                    id = id
                )
            ) for id, value, label, disabled in params
        ]

    def __len__(self) -> int:
        return len(self.checkbox_id)



class TableDropdownCol(TableColumn):

    def __init__(
            self,
            dropdown_id: Optional[Iterable[str]],
            dropdown_value: Union[str, Iterable[str], None] = None,
            dropdown_options: Optional[List[Dict[str,str]]] = None,
            dropdown_clearable: Union[bool, Iterable[bool]] = False,
            dropdown_placeholder: Union[str, Iterable[str], None] = None,
            dropdown_multi: Union[bool, Iterable[bool]] = False,
            **kwargs
        ):

        super().__init__(**kwargs)
        self.dropdown_id = dropdown_id

        params = zip(
            dropdown_id,
            self.expand_param(dropdown_value, dropdown_id),
            self.expand_param(dropdown_clearable, dropdown_id, bool),
            self.expand_param(dropdown_placeholder, dropdown_id),
            self.expand_param(dropdown_multi, dropdown_id, bool),
        )

        self.td = [
            html.Td(
                style = self.cell_style,
                className = self.cell_class,
                children = dcc.Dropdown(
                    value = value,
                    clearable = clear,
                    placeholder = holder,
                    id = id,
                    options = dropdown_options,
                    multi = multi
                )
            ) for id, value, clear, holder, multi in params
        ]

    def __len__(self) -> int:
        return len(self.dropdown_id)



class TableInputCol(TableColumn):

    def __init__(
            self,
            input_id: Optional[Iterable[str]],
            input_value: Union[str, Iterable[str], None] = None,
            input_placeholder: Union[str, Iterable[str], None] = None,
            input_type: Union[str, Iterable[str]] = 'text',
            input_max: Union[int, Iterable[int], None] = None,
            input_min: Union[int, Iterable[int], None] = None,
            input_size: Union[str, Iterable[str]] = 'md',
            input_debounce: Union[bool, Iterable[bool]] = False,
            **kwargs
        ):

        super().__init__(**kwargs)
        self.input_id = input_id

        params = zip(
            input_id,
            self.expand_param(input_value, input_id),
            self.expand_param(input_placeholder, input_id),
            self.expand_param(input_type, input_id),
            self.expand_param(input_max, input_id, int),
            self.expand_param(input_min, input_id, int),
            self.expand_param(input_size, input_id),
            self.expand_param(input_debounce, input_id, bool)
        )

        self.td = [
            html.Td(
                style = self.cell_style,
                className = self.cell_class,
                children = dbc.Input(
                    value = value,
                    placeholder = holder,
                    id = id,
                    type = typ,
                    max = mx,
                    min = mn,
                    size = size,
                    debounce = debounce
                )
            ) for id, value, holder, typ, mx, mn, size, debounce in params
        ]

    def __len__(self) -> int:
        return len(self.input_id)



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
            text: Iterable,
            text_formatting: Optional[Callable] = None,
            **kwargs
        ):

        super().__init__(**kwargs)
        self.text = text
        fmt = text_formatting or '{}'.format

        if self.cell_id is None:
            self.cell_id = [str(uuid4()) for _ in text]

        params = zip(
            text,
            self.cell_id
        )

        self.td = [
            html.Td(
                style = self.cell_style or {},
                className = self.cell_class,
                children = fmt(txt),
                id = id
            ) for txt, id in params
        ]
        
    def __len__(self) -> int:
        return len(self.text)



class Table(dbc.Table):
    
    def __init__(
            self,
            columns: List[TableColumn],
            header_style: Optional[Dict[str,str]] = None,
            body_style: Optional[Dict[str,str]] = None,
            row_style: Optional[Dict[str,str]] = None,
            **kwargs
        ):

        self.columns = columns

        super().__init__(
            children = [
                self.thead(
                    header_style = header_style or {},
                ),
                self.tbody(
                    body_style = body_style or {},
                    row_style = row_style or {}
                )
            ],
            **kwargs
        )


    def thead(self, header_style:Dict[str,str]) -> html.Thead:
        return html.Thead(
            style = header_style,
            children = [col.th for col in self.columns]
        )


    def tr(self, index:int, style:Dict[str,str]) -> html.Tr:
        return html.Tr(
            style = style,
            children = [col.td[index] for col in self.columns]
        )


    def tbody(
            self,
            body_style: Dict[str,str],
            row_style: Dict[str,str]   
        ) -> html.Tbody:

        col_lenghts = [len(col) for col in self.columns]
        if len(set(col_lenghts)) > 1:
            raise CharlotteTableError("Lenghts of columns don't match.")

        return html.Tbody(
            style = body_style,
            children = [
                self.tr(
                    index = i,
                    style = row_style    
                ) for i in range(col_lenghts[0])
            ]
        )
