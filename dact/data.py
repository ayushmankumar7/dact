class Data:
    def __init__(self):
        self.index_html = '''
        {%load static%}
        <html lang="en">
            <body>
                <div id="root"></div>
            </body>
            <script src = "{% static '/dist/app.bundle.js' %}"></script>
        </html>
        '''.strip()
        self.index_css = '''
        '''
        self.index_js = '''
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
import './index.css'
ReactDOM.render(
            <App />,
            document.getElementById('root')
);
        '''.strip()
        self.app_js = '''
import React from 'react';
import './App.css';
import Dact from './dact.svg';

const App = () => {
return(
        <div className="App">
            <Dact className="Applogo"/>
            <div className="Apptext">
                <br></br>    
                <h4>It's Up and Running !!!</h4>
                <h6>
                    <p>
                    Edit App.js to get started with frontend!!
                    </p>
                    <p>
                    Server Running at 127.0.0.1:8000
                    </p>
                    <p>
                        Run dact-watch in BASE_DIR to start dev mode
                    </p>
                </h6>
            </div>
        </div>
        );
}
export default App;
        '''.strip()
        self.app_css = '''
.App
{
    text-align: center;
    color:black;
}
.Applogo
{
    max-width: 100%;
    height: 50%;
    width: 90%; 
}
.Apptext
{
    font-family: sans-serif;
    color:#169A9A;
}
        '''