# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

source /usr/share/cachyos-zsh-config/cachyos-config.zsh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

PATH=~/.console-ninja/.bin:$PATH
export GTK_THEME=Lavanda-Sea-Dark




# --------------------------------------------------------- A R C - Z E N ------------------------------------------------------------- #
#                                                                                                                                   #
# ---------------------------------------------------------    END    ------------------------------------------------------------- #

# Source commands from commands.yaml
source_commands() {
    if [[ -f $HOME/Rice/commands.yaml ]]; then
        yq -r '.[] | select(.command != null) | .command' $HOME/Rice/commands.yaml | while read -r cmd; do
            # echo $cmd
        done
    fi
}

# Function to add new commands
add_command() {
    echo "- command: $1" >>$HOME/Rice/commands.yaml
    echo "  description: $2" >>$HOME/Rice/commands.yaml
    echo "Command added 🚀🚀"
}

# Function to display commands using bat
show_commands() {
    if command -v bat &>/dev/null; then
        bat $HOME/Rice/commands.yaml
    else
        cat $HOME/Rice/commands.yaml
    fi
}

# Aliases for adding and displaying commands
alias super-shit='add_command'
alias list-shit='show_commands'

# Run neofetch if interactive shell and not in tmux
if [[ $- == *i* && -z $TMUX ]]; then
    neofetch --off --disable cpu gpu memory shell resolution packages kernel theme icons --color_blocks off --bold off --cpu_temp off
fi

# Minifetch alias
alias minifetch="neofetch --off --disable cpu gpu memory shell resolution packages kernel theme icons --color_blocks off --bold off --cpu_temp off"

# Set PATH
export PATH="$HOME/.console-ninja/.bin:$PATH"
export LIBVIRT_DEFAULT_URI='qemu:///system'
export GTK_THEME="Lavanda-Sea-Dark"
export fish_user_paths="$fish_user_paths:$HOME/.config/composer/vendor/bin"
export PATH="$PATH:$HOME/.config/composer/vendor/bin"

# Call source_commands function
source_commands
