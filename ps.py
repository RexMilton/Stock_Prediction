from dash import dcc, html
from dash.dependencies import Input, Output
import dash
import plotly.graph_objs as go
import pandas as pd
import os
app = dash.Dash(__name__,
                meta_tags=[{'name': 'viewport',
                            'content': 'width-device-width, initial-scale=1.0'}]
                )
# @app.callback(Output("Temp","children"), Input('csvfile', 'contents'),
#               State('csvfile', 'filename'),
#               State('csvfile', 'last_modified'))
# def csvupload(x,y,z):
#    if x:
#       print("data set trained")
#       content_type, content_string = x[0].split(",")
#       decoded = base64.b64decode(content_string)
#       df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
#       fun(df)
#       # thread = Thread(target=fun, args=(df))
#       # thread.start()
#       df["Close"]=df["Close"]
#       print(df)
#    else:
#       print("No data set")
#    return ""

# df=None
# def sentimentAnalysis():
#    train_data=pd.read_csv("temp.csv")
#    valid_data=pd.read_csv("temp2.csv")
#    long_bot=pd.read_csv("temp3.csv")
#    fig=go.Figure(data=[go.Scatter(y=list(train_data["Close"]),x=train_data["Date"]),go.Scatter(x=valid_data["Date"],y=list(valid_data["Close"])),go.Scatter(x=valid_data["Date"],y=list(valid_data["Predictions"]))])
#    fig2=go.Figure(data=[go.Scatter(x=list(long_bot["Date"]),y=list(long_bot["longs"])),go.Scatter(x=list(long_bot["Date"]),y=list(long_bot["bots"]))])
#    # print(list(long_bot["Date"]))
#    # print(list(long_bot["longs"]))
#    return [fig,fig2]

def getCompaniesName():
   return [i for i in os.listdir('companiesGraph/companies1/')]

def processingLstm(company):
   train_data=pd.read_csv("./companiesGraph/companies1/"+company+"/temp.csv")
   valid_data=pd.read_csv("./companiesGraph/companies1/"+company+"/temp2.csv")
   # print(train_data)
   print(train_data["Date"])
   print("date")
   return dcc.Graph(figure=go.Figure(data=[go.Scatter(y=list(train_data["Close"]),x=train_data["Date"]),go.Scatter(x=valid_data["Date"],y=list(valid_data["Close"])),go.Scatter(x=valid_data["Date"],y=list(valid_data["Predictions"]))]))

@app.callback(Output("graph","children"), Input('company-list', 'value'))
def getCompannoneyGraph(value):
   if value==None:
      return "Select a value in drop down"
   return processingLstm(value)
long_bot=pd.read_csv("./temp3.csv")
app.layout =html.Div(className="body",children=[
dcc.Dropdown(getCompaniesName(), id='company-list'),
html.Div(id="graph"),
dcc.Graph(figure=go.Figure(data=[go.Scatter(x=list(long_bot["Date"]),y=list(long_bot["longs"])),go.Scatter(x=list(long_bot["Date"]),y=list(long_bot["bots"]))]))


# dcc.Graph(figure=sentimentAnalysis_data[1])
])
if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, dev_tools_hot_reload=True,)