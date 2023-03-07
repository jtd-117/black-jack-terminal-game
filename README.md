# BLACK JACK TERMINAL GAME

## Contents:
### 1. [Project Overview](#project-overview)
### 2. [Installation](#installation)
### 3. [Use](#use)

# Project Overview:
A python program that plays the [Black Jack](https://en.wikipedia.org/wiki/Blackjack) card game. 

The player is pitted against an AUTOMATED dealer who is programmed (i.e. winning strategy) to accrue as many cards that sum greater than or equal to 17 before standing. The program terminates when the cannot (virtually) afford to play another round.

<img src="assets/black-jack-demo.gif">

This implementation of Black Jack has the following features:
<table>
    <thead>
        <tr>
            <th>Supported:</th>
            <th>Unsupported:</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <ul>
                    <li>Hitting & standing</li>
                    <li>Doubling down</li>
                    <li>Insurance</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li>Splitting</li>
                    <li>Surrendering</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

# Installation:
<table>
    <thead>
        <tr>
            <th>OPTION 1 - Via Git Clone</th>
            <th>OPTION 2 - Via ZIP</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan=2>1. Click the `Code` button</td>
        </tr>
        <tr>
            <td>2. Using either the `HTTPS` or `SSH` option, copy the link</td>
            <td>2. Click on `Download ZIP`</td>
        </tr>
        <tr>
            <td>3. Using your device's terminal emulator run `git clone &ltlink here&gt` in a desired directory</td>
            <td>3. Unzip the download & move the folder in a desired directory</td>
        </tr>
    </tbody>
</table>

# Use:
1. Ensure `python3` is installed
2. Using terminal `cd` (change directory) into the `black_jack_terminal_game` directory
3. Execute the command: `python3 src/main.py`