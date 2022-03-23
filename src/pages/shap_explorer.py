
from dash import html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

class ShapExplorer:
    def __init__(self, app):
        self.df = px.data.iris()

        species_search = dcc.Dropdown(
            sorted(list(self.df['species'].unique())),
            id="species_search",
            multi=True
        )

        partial_card = dbc.Card(
            [
                dbc.CardHeader("Features Displayed"),
                dbc.CardBody(
                    [
                        html.P("Select your features", className="card-text"),
                        species_search
                    ]
                )
            ],
            className="mb-3"
        )

        color_card = dbc.Card(
            [
                dbc.CardHeader("Color Dimension"),
                dbc.CardBody(
                    [
                        html.P("Select your colors", className="card-text"),
                    ]
                )
            ],
            className="mb-3"
        )   

        filters_card = dbc.Card(
            [
                dbc.CardHeader("Filters Card"),
                dbc.CardBody(
                    [
                        html.P("Select filters", className="card-text"),
                    ]
                )
            ],
            className="mb-3"
        ) 

        scatter_plot =  html.Div([
            dcc.Graph(id='graph-with-slider'),
        ])

        plot_card = dbc.Card( 
            [
                dbc.CardHeader("Plots go here"),
                dbc.CardBody(
                    [
                        scatter_plot,
                    ]
                )
            ],
            className="mb-3"
        )



        info_card = dbc.Card(
            [
                dbc.CardHeader("Summary"),
                dbc.CardBody(
                    [
                        html.P("Some info about the model", className="card-text"),
                    ]
                )               
            ]
        )

        row1 = dbc.Row(
            [
                dbc.Col(plot_card, width=12, lg=9),
                dbc.Col([partial_card, color_card, filters_card], width=12, lg=3),
            ], 
        ) 

        row2 = dbc.Row(
            [
                dbc.Col(info_card, width=12)
            ]
        )

        self.shap_explorer = html.Div([row1, row2])
        self.registered = False
        self.app = app

    def render(self):
        if not self.registered:
            self.register_callbacks(self.app)

        return self.shap_explorer

    def register_callbacks(self, app):
        @app.callback(
        Output('graph-with-slider', 'figure'),
        Input('species_search', 'value'))
        def update_figure(selected_species):
            filtered_df = self.df[self.df['species'].isin(selected_species)] if selected_species is not None and len(selected_species) > 0 else self.df
            fig = px.scatter(filtered_df, x="sepal_width", y="sepal_length", color='petal_length')
            fig.update_layout(transition_duration=500)

            return fig

        self.registered = True
