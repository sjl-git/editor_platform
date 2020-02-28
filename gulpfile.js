const gulp = require("gulp");
const bro = require("gulp-browserify")
const babel = require("babelify")
const paths = {
    js: {
        src: "assets/js/main.js",
        dest: "static/js",
        watch: "assets/js/**/*.js"
    }
}

const css = () => {
    const postCSS = require("gulp-postcss");
    const sass = require("gulp-sass");
    const minify = require("gulp-csso");
    sass.compiler = require("node-sass");
    return gulp
        .src("assets/scss/styles.scss")
        .pipe(sass().on("error", sass.logError))
        .pipe(postCSS([require("tailwindcss"), require("autoprefixer")]))
        .pipe(minify())
        .pipe(gulp.dest("static/css"));
};

const js = async () => {
    gulp
        .src(paths.js.src)
        .pipe(bro({
            transform: [babel.configure({
                presets: ["@babel/preset-env"]
            })]
        }))
        .pipe(gulp.dest(paths.js.dest))
}
const wathFiles = () => {
    gulp.watch(paths.js.watch, js)
}
const js_dev = gulp.series(js, wathFiles)
exports.css = css
exports.js_dev = js_dev