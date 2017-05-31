'use strict';

var basePaths = {
  src: 'frontdev/',
  dist: 'src/assets/'
};

var gulp = require('gulp'),
    watch = require('gulp-watch'),
    browserSync = require("browser-sync"),
    rigger = require('gulp-rigger'),
    less = require('gulp-less'),
    reload = browserSync.reload,
    rimraf = require('gulp-rimraf');//,
    //cleanCSS = require('gulp-clean-css'),
    //htmlmin = require('gulp-htmlmin');

var path = {
    bower: {
        jquery: ['./bower_components/jquery/dist/jquery.min.js','./frontdev/js/vendor/jquery/jquery.min.js']
    },
    build: { // compiled files
        partialsJs: basePaths.dist + 'js/',
        js: basePaths.dist + 'js/',
        css: basePaths.dist + 'css/',
        fonts: basePaths.dist + 'css/fonts/',
        img: basePaths.dist + 'img/',
        assets: basePaths.dist + 'assets/'
    },
    dev: { // development files
        partialsJs: [basePaths.src + 'js/**/**/*.js', basePaths.src + 'js/**/**/*.json'],
        js: basePaths.src + 'js/app.js',
        less: basePaths.src + '/less/styles.less',
        fonts: basePaths.src + 'less/fonts/**/*.*',
        img: basePaths.src + 'img/**/*.*',
        assets: basePaths.src + 'assets/**/*.*'
    },
    watch: { // watching files
        js: basePaths.src + 'js/**/*.js',
        less: basePaths.src + 'less/**/*.less',
        fonts: basePaths.src + 'less/fonts/**/*.*',
        img: basePaths.src + 'img/**/*.*',
        assets: basePaths.src + 'assets/**/*.*'
    },
    clean: [basePaths.src + 'css']
};

gulp.task('style:build', function () {
    return gulp.src(path.dev.less)
        .pipe(less())
        //.pipe(cleanCSS())
        .pipe(gulp.dest(path.build.css))
        .pipe(reload({stream: true}));
});

gulp.task('fonts:build', function () {
    return gulp.src(path.dev.fonts)
        .pipe(gulp.dest(path.build.fonts))
        .pipe(reload({stream: true}));
});

gulp.task('js:build', function () {
    gulp.src(path.dev.partialsJs).pipe(gulp.dest(path.build.partialsJs));

    return gulp.src(path.dev.js)
        .pipe(gulp.dest(path.build.js))
        .pipe(reload({stream: true}));
});

gulp.task('img:build', function () {
    return gulp.src(path.dev.img)
        .pipe(gulp.dest(path.build.img))
        .pipe(reload({stream: true}));
});

gulp.task('assets:build', function () {
    return gulp.src(path.dev.assets)
        .pipe(gulp.dest(path.build.assets))
        .pipe(reload({stream: true}));
});

gulp.task('build', [
    'style:build',
    'fonts:build',
    'js:build',
    'img:build',
    'assets:build'
]);

gulp.task('watch', function(){
    watch([path.watch.html], function(event, cb) {
        gulp.start('html:build');
    });
    watch([path.watch.css], function(event, cb) {
        gulp.start('style:build');
    });
    watch([path.watch.fonts], function(event, cb) {
        gulp.start('fonts:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('js:build');
    });
    watch([path.watch.img], function(event, cb) {
        gulp.start('img:build');
    });
    watch([path.watch.assets], function(event, cb) {
        gulp.start('assets:build');
    });
});

gulp.task('clean', function (cb) {
    rimraf(path.clean, cb);
});

gulp.task('default', ['build', 'watch']);