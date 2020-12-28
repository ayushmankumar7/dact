class React_templates():
    def __init__(self):
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
        self.webpack_config_js = '''
        const path = require("path");
            var webpack = require('webpack');
            var BundleTracker = require('webpack-bundle-tracker');


            module.exports = {
                entry:{ app:'./src/index.js'},
                devtool:'source-map',
                output: {
                path: path.resolve(__dirname,'dist'),
                filename: "[name].bundle.js",
            },

            plugins: [
                new BundleTracker({filename: './webpack-stats.json'}),
            ],
            module: {
            rules: [
            {
                test: /\.(js|jsx)$/,
                exclude:/node_modules/,
                use: ['babel-loader'], 
            },
            {
                test: /\.svg$/,
                use: ['react-svg-loader']
            },
            {
                test: /\.scss$/,
                use: [
                    {
                        loader: 'style-loader'
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: 'style-loader'
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            },
            {
                test: /\.(otf|ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                use: [{
                    loader: 'url-loader'
                }]
            }
            ]
            },
            resolve: {
                extensions: ['*', '.js', '.jsx','.scss']
            }
            };
        '''.strip()
    def get_intial_js_files(self):
        x = {
            'index.js':self.index_js,
            'App.js':self.app_js,
            'webpack.config.js':self.webpack_config_js,
            }
        return x