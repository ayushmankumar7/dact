class Package_Json():
    def __init__(self):
        self.package_json = '''
        {
                "name": "dact_project",
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
    def get_package_json(self):
        x = self.package_json
        return x