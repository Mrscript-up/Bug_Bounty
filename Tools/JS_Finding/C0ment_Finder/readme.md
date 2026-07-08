## 📝 Comment Extractor

#### A robust, single-file Python tool that extracts all comments from source code files (.html, .js, .css, .php, .py, .java, .c, .cpp, .go, .rs, .rb, .sql, .sh, .lua, .hs, .lisp, .vim, .ps1, .bat, YAML/INI/TOML, JSONC/JSON5, Dockerfile, Makefile and many more) and saves the result to a structured output file.

Unlike naive regex-based extractors, Comment Extractor uses a character-level state machine that correctly skips strings — so it won't falsely extract things like "// not a comment" from inside string literals.
## ✨ Features

    * 🔍 Accurate extraction — character-level state machine that ignores comment-like text inside strings.
    * 🌐 20+ language families supported out of the box.
    * 📦 Single file — no dependencies beyond the Python standard library.
    * 📁 Recursive directory scanning with sensible default exclusions (node_modules, .git, venv, dist, …).
    * 🧾 Three output formats — plain text (txt), Markdown (md), or JSON (json).
    * ✂️ Optional --split-by-language mode writes one output file per language.
    * 📊 Per-language statistics (file count + comment count).
    * 🚫 Binary file detection — binary files are skipped automatically.
    * ⚙️ Filtering — by extension, by minimum comment length.
    * 🛡️ Graceful handling of encoding errors and unreadable files.

## 🚀 Installation

#### No installation required — just download and run.
```
Requirements: Python 3.7+ (standard library only).
```
## 🧪 Quick Start

### Extract every comment from a project folder and save as text:
```bash
python comment_extractor.py ./my_project -o comments.txt
```
### Extract only Python and JavaScript comments as Markdown:
```bash
python comment_extractor.py ./src -e .py,.js -f md -o comments.md
```
### Extract comments and split output into one file per language:
```bash
python comment_extractor.py ./webapp --split-by-language -o ./out/comments# -> ./out/comments_html___xml.txt# -> ./out/comments_css___scss___less.txt# -> ./out/comments_javascript___typescript.txt# ...
```
### JSON output with verbose stats:
```bash
python comment_extractor.py ./backend -f json -o comments.json --stats -v
```
### Ignore short comments (e.g. // TODO):
```bash
python comment_extractor.py ./src --min-length 15 -o comments.txt
```
## 🎛️ CLI Reference
```text
Flag / Arg	Description	Default
path (positional)	File or directory to scan	— (required)
-o, --output	Output file path (or prefix if --split-by-language)	comments_output.txt
-f, --format	Output format: txt, md, json	txt
-e, --extensions	Comma-separated extensions/filenames to include	(all supported)
--min-length N	Drop comments shorter than N characters	0
--exclude-dirs	Comma-separated directory names to skip	(see below)
--split-by-language	Write one file per language	off
--stats	Print summary stats to stderr	off
-v, --verbose	Verbose progress output	off
```
#### Default excluded dirs: .git, .svn, .hg, node_modules, __pycache__, venv, env, .venv, dist, build, target, out, .idea, .vscode
## 🌍 Supported Languages
```
Family	Languages / Extensions
Web markup	HTML, XML, XHTML, Vue SFC, SVG — <!-- … -->
Stylesheets	CSS, SCSS, SASS, LESS — /* … */ (and // for SCSS/LESS)
JS family	JavaScript, TypeScript, JSX/TSX, MJS/CJS — //, /* … */, template strings
PHP	//, #, /* … */
Python	# (triple-quoted strings are treated as strings, not comments)
C-family	C, C++, Java, C#, Go, Rust, Swift, Kotlin — //, /* … */
Ruby	#, =begin … =end
Shell	Bash, Zsh, Ksh, Fish — #
SQL	--, /* … */
Config files	YAML, INI, TOML, .properties — #, ;
JSONC/JSON5	//, /* … */
Build files	Dockerfile, Makefile — #
Vim script	"
Lua	--, --[[ … ]]
Haskell	--, {- … -}
Lisp family	Lisp, Clojure, Scheme, Racket — ;, `#
Erlang	%
Fortran	!
PowerShell	#, <# … #>
Batch/CMD	REM, ::
```
## 📄 Example Output (Text)
<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/35be83ab-b3fb-402a-9ceb-dc844110ec02" />


## ⚠️ Known Limitations
```
    Ruby =begin/=end are recognized as block comments but the tool does not enforce start-of-column placement (rare edge case).
    SQL -- is treated as a comment even in expressions like 5--3. SQL parsers themselves disagree on this; we follow the common interpretation.
    Python docstrings ("""…""") are treated as strings, not comments — this is technically correct. If you want docstrings, post-process the JSON output or extend the language config.
    Nested block comments (e.g. Haskell {- {- -} -}) are not supported — the outer block ends at the first closing marker.
    Batch REM mid-line is treated as a comment even when it appears as text after echo. Real-world batch files rarely do this.
```
## 🧩 Extending

#### Add a new language by appending an entry to the LANGUAGES dict in comment_extractor.py:
```json
'my_lang': {    'name': 'My Language',    'extensions': ('.myl',),    'filenames': (),    'line_comments': ('//',),    'block_comments': (('/*', '*/'),),    'strings': ('"', "'"),    'escape': '\\',}
```
## ✅ How to use it

- Save the Python code as comment_extractor.py.
- Make it executable: chmod +x comment_extractor.py.
- Run it on any file or folder:

```bash
python comment_extractor.py ./my_project -o comments.txt --stats -v
```
#### The tool will recursively scan, skip binary files and excluded directories, run a string-aware state machine on every supported source file, and write a clean report to your specified output file. You can also use --split-by-language to get one file per language, or -f json / -f md for structured output
<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=00FF00&height=120&section=footer"/> </p>
