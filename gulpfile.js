var basePaths = {
  src: 'frontdev/',
  dist: 'src/assets/'
};

var paths = {
  fonts: {
    src: basePaths.src + 'font/',
    dist: basePaths.dist + 'font/'
  },
  images: {
    src: basePaths.src + 'img/',
    dist: basePaths.dist + 'img/'
  },
  scripts: {
    src: basePaths.src + 'js/',
    dist: basePaths.dist + 'js/'
  },
  styles: {
    css: basePaths.src + 'css/',
    src: basePaths.src + 'sass/',
    dist: basePaths.dist + 'css/'
  },
  templates: {
    src: basePaths.src + 'template/',
  }
};

var appFiles = {
  fonts: paths.fonts.src + '**',
  images: paths.images.src + '**',
  scripts: paths.scripts.src + '*.js',
  all_scripts: paths.scripts.src + '**/*.js',
  styles: paths.styles.src + '**/*.scss',
  templates: paths.templates.src + '**/*.hbs'
};

/*Let the magic begin*/
var browserify  = require('browserify');
var buffer      = require('gulp-buffer');
var compass     = require('gulp-compass');
var cssnano     = require('gulp-cssnano');
var del         = require('del');
var gulp        = require('gulp');
var gulpif      = require('gulp-if');
var gutil       = require('gulp-util');
var hbsfy       = require('hbsfy');
var imagemin    = require('gulp-imagemin');
var importCss   = require('gulp-import-css');
var livereload  = require('gulp-livereload');
var notify      = require("gulp-notify");
var plumber     = require('gulp-plumber');
var runSequence = require('run-sequence');
var sourcemaps  = require('gulp-sourcemaps');
var tap         = require('gulp-tap');
var uglify      = require('gulp-uglify');

var DEBUG       = true;

function onError(err) {
  notify.onError({
    title:    "Gulp",
    subtitle: "Failure!",
    message:  "Error: <%= error.message %>",
    sound:    "Beep"
  })(err);

  this.emit('end');
}

gulp.task('clean', function(cb) {
  return del([basePaths.dist, paths.styles.css], cb);
});

gulp.task('copy', function() {
  gulp.src(paths.templates.src + 'index.html')
      .pipe(gulp.dest(basePaths.dist));
  gulp.src(paths.fonts.src + '**')
      .pipe(gulp.dest(paths.fonts.dist));
  gulp.src(paths.images.src + '**')
      .pipe( gulpif ( !DEBUG, imagemin ({
        progressive: true,
        svgoPlugins: [{removeViewBox: false}]
      })))
      .pipe(gulp.dest(paths.images.dist))
      .pipe(livereload());
});

gulp.task('compass', function() {
  return gulp.src(appFiles.styles)
      .pipe(plumber({errorHandler: onError}))
      .pipe(compass({
        sass: paths.styles.src,
        css: paths.styles.css,
        font: paths.fonts.src,
        image: paths.images.src
      }))
      .pipe(importCss())
      .pipe(gulpif(!DEBUG, cssnano()))
      .pipe(gulp.dest(paths.styles.dist))
      .pipe(livereload());
});

gulp.task('scripts', function() {
  // no need of reading file because browserify does.
  return gulp.src(appFiles.scripts, {read: false})

    // transform file objects using gulp-tap plugin
    .pipe(tap(function (file) {

      gutil.log('bundling ' + file.path);

      // replace file contents with browserify's bundle stream
      file.contents = browserify({
        entries: [file.path],
        insertGlobals: false,
        transform: [hbsfy],
        debug: DEBUG,
        paths: ['./node_modules', './frontdev/']
      }).bundle();
    }))

    // transform streaming contents into buffer contents (because gulp-sourcemaps does not support streaming contents)
    .pipe(buffer())

    // load and init sourcemaps
    .pipe(sourcemaps.init({loadMaps: true}))

    .pipe(gulpif(!DEBUG, uglify()))

    // write sourcemaps
    .pipe(sourcemaps.write('./'))

    .pipe(gulp.dest(paths.scripts.dist))

    .pipe(livereload());
});

// Rerun the task when a file changes
gulp.task('watch', function() {
  gulp.watch(appFiles.images, ['copy']);
  gulp.watch(appFiles.fonts, ['copy']);
  gulp.watch(appFiles.styles, ['compass']);
  gulp.watch(appFiles.all_scripts, ['scripts']);
  gulp.watch(appFiles.templates, ['scripts']);
  livereload.listen();
});

gulp.task('default', ['dev'], function() {
  gulp.start('watch');
});

gulp.task('dev', function(callback) {
  runSequence(
    'clean',
    'compass',
    'copy',
    'scripts',
    callback
    );
});

gulp.task('dist', ['clean'], function() {
  DEBUG = false;
  gulp.start('copy', 'scripts');
});