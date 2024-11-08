/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",               // If you have an index.html in the root
    "./src/**/*.{js,ts,jsx,tsx}", // Adjust according to where your components are
  ],
  theme: {
    extend: {}, // Extend or customize your theme here
  },
  plugins: [], // Add any Tailwind plugins here
};
