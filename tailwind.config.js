
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js}",
    "./templates/*.{html}",
    "./node_modules/tw-elements/dist/js/**/*.js",
  ],
  theme: {
    extend: {},
  },
  darkMode: "class",
  plugins: [require("tw-elements/dist/plugin.cjs")],
};
