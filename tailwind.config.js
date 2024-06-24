/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {colors: {
      'paynes-gray': {
        DEFAULT: '#5d737e',
        100: '#131719',
        200: '#252e32',
        300: '#38454c',
        400: '#4b5c65',
        500: '#5d737e',
        600: '#79919c',
        700: '#9bacb5',
        800: '#bcc8ce',
        900: '#dee3e6',
      },
      'verdigris': {
        DEFAULT: '#64b6ac',
        100: '#122624',
        200: '#244c48',
        300: '#36726b',
        400: '#48998f',
        500: '#64b6ac',
        600: '#82c4bd',
        700: '#a1d3cd',
        800: '#c1e2de',
        900: '#e0f0ee',
      },
      'celeste': {
        DEFAULT: '#c0fdfb',
        100: '#035653',
        200: '#05aca7',
        300: '#13f8f0',
        400: '#69faf5',
        500: '#c0fdfb',
        600: '#ccfdfc',
        700: '#d8fefd',
        800: '#e5fefd',
        900: '#f2fffe',
      },
      'mint-green': {
        DEFAULT: '#daffef',
        100: '#005f36',
        200: '#00be6c',
        300: '#1eff9d',
        400: '#7cffc6',
        500: '#daffef',
        600: '#e2fff3',
        700: '#eafff6',
        800: '#f1fff9',
        900: '#f8fffc',
      },
      'baby-powder': {
        DEFAULT: '#fcfffd',
        100: '#006522',
        200: '#00ca43',
        300: '#30ff75',
        400: '#95ffb8',
        500: '#fcfffd',
        600: '#fbfffc',
        700: '#fcfffd',
        800: '#fdfffe',
        900: '#fefffe',
      },
    },},
  },
  plugins: [],
}

