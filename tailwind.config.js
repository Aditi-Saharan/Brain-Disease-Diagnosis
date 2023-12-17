
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // "./src/**/*.{js}",
    "./templates/*.html",
    "./node_modules/tw-elements/dist/js/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        'poppins': ['Poppins', 'sans-serif'],
        'yellowtail': ['Yellowtail', 'cursive'],
        'noto-sans':['Noto Sans', 'sans-serif'],
      },
      backgroundImage: {
        'heroSection': "url('/static/src/images/hero-section.jpg')"
      }
    },
  },
  darkMode: "class",
  plugins: [require("tw-elements/dist/plugin.cjs"),
            require('tailwindcss-animate')
  ],

};
