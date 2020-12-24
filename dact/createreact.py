import os
from pathlib import Path as path

def getcurrent():
    y = os.getcwdb()
    return y

def make_dirs(x):
    os.mkdir("static")
    os.chdir("static")
    os.mkdir("src")
    os.mkdir("js")
    os.mkdir("css")
    os.chdir("..")
    os.chdir(x)
    os.mkdir("templates")

def make_template():
    open("index.html",'x')
    with open("index.html",'r+') as file:
        file.write('''
        {%load static%}
        <html lang="en">
            <body>
                <div id="root"></div>
            </body>
            <script src = "{% static '/dist/app.bundle.js' %}"></script>
        </html>
        ''')
        file.close()

def write_webpack_config():
    open('webpack.config.js','x')
    with open('webpack.config.js','r+') as file:
        file.write(
            '''
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
        )
        file.close()

def write_react_App_js():
    open("App.js",'x')
    with open('App.js','w') as file:
        file.write(
            '''
            import React from 'react';
             const App = () => {
                 return(
                     <div className="App">
                        <h4>Hello World!!!</h4>
                     </div>
                 );
             }
             export default App;
            '''.strip()
        )
        file.close()

def write_index_js():
    open('index.js','x')
    with open('index.js','w') as file:
        file.write(
            '''
            import React from 'react'
            import ReactDOM from 'react-dom'
            import App from './App'
            ReactDOM.render(
                    <App />,
                document.getElementById('root')
            );
            '''.strip()
        )
        file.close()

def write_package_json():
    open('package.json','x')
    with open('package.json','w') as file:
        file.write(
            '''
            {
                "name": "blog_project",
                "version": "1.0.0",
                "description": "",
                "main": "./src/index.js",
                "scripts": {
                        "test": "echo Error: no test specified && exit 1",
                        "webpack": "webpack",
                        "watch": "./node_modules/.bin/webpack --watch --config webpack.dev.js",
                        "dev":"webpack --mode development --watch"
                },
                "author": "",
                "license": "ISC",
                "devDependencies": {
                        "@babel/preset-react": "^7.12.10",
                        "@svgr/webpack": "^5.5.0",
                        "babel-core": "^6.26.3",
                        "babel-loader": "^8.2.2",
                        "babel-preset-env": "^1.7.0",
                        "babel-preset-react": "^6.24.1",
                        "css-loader": "^5.0.1",
                        "dotenv-webpack": "^6.0.0",
                        "extract-text-webpack-plugin": "^3.0.2",
                        "file-loader": "^6.2.0",
                        "html-loader": "^1.3.2",
                        "mini-css-extract-plugin": "^1.3.3",
                        "multi-loader": "^0.1.0",
                        "node-sass": "^5.0.0",
                        "postcss-loader": "^4.1.0",
                        "raw-loader": "^4.0.2",
                        "react-markdown-loader": "^1.3.1",
                        "react-svg-loader": "^3.0.3",
                        "sass": "^1.30.0",
                        "sass-loader": "^10.1.0",
                        "style-loader": "^2.0.0",
                        "stylelint": "^13.8.0",
                        "stylelint-webpack-plugin": "^2.1.1",
                        "svg-inline-loader": "^0.8.2",
                        "svg-url-loader": "^7.1.1",
                        "url-loader": "^4.1.1",
                        "webpack": "^5.11.0",
                        "webpack-bundle-tracker": "^1.0.0-alpha.1",
                        "webpack-cli": "^4.2.0"
                },
                "dependencies": {
                        "node-loader": "^1.0.2",
                        "react": "^17.0.1",
                        "react-dom": "^17.0.1",
                        "react-router-dom": "^5.2.0",
                        "react-scripts": "^4.0.1"
                },
                "babel": {
                        "presets": [
                            "@babel/preset-react",
                            "@babel/preset-env"
                        ],
                        "plugins": [
                            "@babel/plugin-transform-react-jsx"
                        ]
                }
            }
            '''.strip()
        )
        file.close()

def create():
    x = getcurrent()
    make_dirs(x)
    os.chdir("static")
    write_webpack_config()
    write_package_json()
    os.system(f"npm install --package-lock")
    os.chdir("src")
    write_index_js()
    write_react_App_js()
    os.chdir('..')
    os.chdir(x)
    os.chdir('templates')
    make_template()
    os.chdir('..')
    os.chdir(x)
    os.chdir("static")
    try:
        os.system(f"npm run webpack --no-hot")
    except:
        print("Exited")
    os.chdir("..")
    os.chdir(x)



     


