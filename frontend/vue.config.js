const webpack = require('webpack');

module.exports = {
  devServer: {
    proxy: 'http://localhost:5000',
  },
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        // Define process.env flags that Vue relies on
        __VUE_OPTIONS_API__: JSON.stringify(true),
        __VUE_PROD_DEVTOOLS__: JSON.stringify(false),
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: JSON.stringify(true),
      })
    ]
  }
};
