import dash
import dash_bootstrap_components as dbc
from pages.shap_explorer import ShapExplorer

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

page = ShapExplorer(app)

app.layout = page.render()

if __name__ == "__main__":
    app.run_server(port=8888, debug=True, host='0.0.0.0')
