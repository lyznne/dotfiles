<div class="center">
        <h1 style="color: crimson;">A R C *  Z E N</h1>
</div>

# . files

## font

- 0xProto Nerd Font
- oxProto mono

## colors

## system

- OS : arcolinux
- WM Qtile
- composer Picom
- login manager - SDDM
- grub - rEFInd
- terminal - warpterminal + alacritty

# dot files for

1. refind - theme (`arczen-r[EFI]nd`)
2. sddm - `arzen-sddm`
3. WM - `Qtile `(arczen)
4. picom - `picom`
5. starship -
6. spicetify - spotify
7. neofetch
8. Alacritty
9. drun , Dmenu,
10. lockscreen
11. (menu for lock-screen)
12. sxhkdrc
13. nvim
14. Vscode
15. colorscheme
16. qtile-bar
17. Firefox
18. betterlockscreen [+]

---

<div class="center">
        <h2 style="color: crimson;">Q T I L E </h2>
</div>

## Set-up

### \_dir

`.config/qtile/`

### edit file

`.config/qtile/config.py`

### testing the configs

- use Xephyr server to test the config

- start the xephyr

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
```

- expose our Display

```bash
export DISPAY=:1
```

- Check if the **Qtile `config.py`** has errors.

```bash
qtile check -c <config.py path>
```

- start the qtile config file.

```bash
qtile start -c ~/.config/qtile/config.py
```

## \_dir tree

```
~/.config/qtile/
├── assets/
├── config.py
├── scripts/
├── sxhkd
│   └── sxhkdrc
└── themes
     └──arcozen.theme

```
