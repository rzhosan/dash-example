from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

class ExecutiveSumary:

    def __init__(self):

        summary_card = dbc.Card(
            [
                dbc.CardHeader("Model Last Scored: 20/12/21 12:04:21"),
                dbc.CardBody(
                    [
                        html.P("Model Stats", className="card-text"),
                    ]
                )
            ],
            className="mb-3"
        )

        behaviors_card = dbc.Card(
            [
                dbc.CardHeader("Most Important Behaviours"),
                dbc.CardBody(
                    dbc.ListGroup(
                        [
                            dbc.ListGroupItem("Behaviour 1"),
                            dbc.ListGroupItem("Behaviour 2"),
                            dbc.ListGroupItem("Behaviour 3"),
                        ],
                        flush=True,
                    )
                )
            ],
            className="mb-3"
        )  

        row1 = dbc.Row(
            [
                dbc.Col(summary_card, width=12, lg=6),
                dbc.Col(behaviors_card, width=12, lg=6),
            ], 
        )  

        date_range = dbc.Card(
            [
                dbc.CardHeader("Dates Range"),
                dbc.CardBody(
                    [
                        html.P("Date range chart", className="card-text"),
                    ]
                )
            ],
            className="mb-3"
        ) 

        row2 = dbc.Row(
            [
                dbc.Col(date_range, width=12),
            ], 
        )  

        accuracy_card = dbc.Card(
            [
                dbc.CardHeader("Model Accuracy"),
                dbc.CardBody(
                    [
                        html.P("72.3% (Good)", className="card-text"),
                    ]
                )
            ],
            className="mb-3"
        ) 

        survey_card = dbc.Card(
            [
                dbc.CardHeader("Weekly Surveys Collected"),
                dbc.CardBody(
                    [
                        html.P("21.2k", className="card-text"),
                    ]
                )
            ],
            className="mb-3"
        ) 

        survey_score = dbc.Card(
            [
                dbc.CardHeader("Survey Direct Score"),
                dbc.CardBody(
                    [
                        html.P("71.2%", className="card-text"),
                    ]
                )
            ],
            className="mb-3"
        ) 


        row3 = dbc.Row(
            [
                dbc.Col(accuracy_card, width=12, lg=4),
                dbc.Col(survey_card, width=12, lg=4),
                dbc.Col(survey_score, width=12, lg=4),
            ], 
        )

        
        self.exec_sum = html.Div([row1, row2, row3])

    def render(self):
        return self.exec_sum