module.exports = {
  theme: {
    extend: {
      spacing: {
        "25vh": "25vh",
        "50vh": "50vh",
        "75vh": "75vh",
        "280px": "280px",
        "360px": "360px",
        "480px": "480px",
        "540px": "540px",
      },
      borderRadius: {
        xl: "1.5rem"
      },
      colors: {
        'yellow-gray': '#F5F5F5',
      },
    }
  },
  variants: {
    backgroundColor: ['responsive', 'hover', 'focus', 'active'],
    transitionTimingFunction: ['responsive', 'hover', 'focus'],
    opacity: ['responsive', 'hover', 'focus', 'active', 'group-hover'],
    transitionDuration: ['responsive', 'hover', 'focus'],
    display: ['responsive', 'hover', 'focus', 'group-hover'],

  },
  plugins: []
}
