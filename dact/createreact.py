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
                watch:true,
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

def write_react_app():
    open("App.js",'x')
    with open('App.js','w') as file:
        file.write(
            '''
            import React from 'react';
            
            '''
        )

def create():
    x = getcurrent()
    make_dirs(x)

     


