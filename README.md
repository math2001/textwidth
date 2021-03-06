# `textwidth`

<a href="https://gitmoji.carloscuesta.me" target="_blank"><img src="https://camo.githubusercontent.com/2a4924a23bd9ef18afe793f4999b1b9ec474e48f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746d6f6a692d253230f09f989c253230f09f988d2d4646444436372e7376673f7374796c653d666c61742d737175617265" alt="Gitmoji" data-canonical-src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square" style="max-width:100%;"></a>

A little Sublime Text 3 plugin to automatically insert line breaks at a
specific column. It just splits *before* the word. It's my adaptation of vim's
`textwidth` setting (which is the reason for this package name).

## Usage

This plugin is useful for writing text (markdown, plain text, etc), as it
automatically insert a line break at x characters or less (it wouldn't split a
word).

### Enabling automatic wrapping

If you want to enable this behaviour everywhere, just add this to your global
settings:

```json
"textwidth": 80
```

I wouldn't recommend doing that though, it might be annoying when you're
programming. If you just want this to work in Markdown for example:

1. open a markdown file
2. open the command palette (<kbd>ctrl+shift+p</kbd>)
3. type `settings syntax specific` and hit <kbd>enter</kbd>
4. add the same code as above (`"textwidth": 80`) in there

Done!

### Manual reorganizing

Sometimes, you write a paragraph, but then you change some words, and the
wrapping is just wrong.

Well, you don't have to re do everything manually: you just need to run
`textwidth` command. It'll reorganize the selection if there is some, or the
paragraph you have a cursor in.

#### Add it to the command palette

Create a file called `Default.sublime-commands` in your `User` directory, and
write this:

```json
[
    { "caption": "Text Width: Wrap", "command": "textwidth" }
]
```

#### Bind a shortcut to it

In your keybinding file

```json
{
    "keys": ["alt+w"],
    "command": "textwidth"
}
```

### For VIM users

If you use a vim emulating package, `gq` will re-wrap the selection. You can use
`gqap` to wrap the current paragraph you're in (`gq` a paragraph).


---

Hope you like it :heart: