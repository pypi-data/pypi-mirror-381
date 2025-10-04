[![CI](https://github.com/comictagger/comictagger/actions/workflows/build.yaml/badge.svg?branch=develop&event=push)](https://github.com/comictagger/comictagger/actions/workflows/build.yaml)
[![GitHub release (latest by date)](https://img.shields.io/github/downloads/comictagger/comictagger/latest/total)](https://github.com/comictagger/comictagger/releases/latest)
[![PyPI](https://img.shields.io/pypi/v/comictagger)](https://pypi.org/project/comictagger/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/comictagger)](https://pypistats.org/packages/comictagger)
[![Chocolatey package](https://img.shields.io/chocolatey/dt/comictagger?color=blue&label=chocolatey)](https://community.chocolatey.org/packages/comictagger)
[![WinGet](https://img.shields.io/winget/v/ComicTagger.ComicTagger)](https://github.com/microsoft/winget-pkgs/tree/master/manifests/c/ComicTagger/ComicTagger)
[![PyPI - License](https://img.shields.io/pypi/l/comictagger)](https://opensource.org/licenses/Apache-2.0)

[![GitHub Discussions](https://img.shields.io/github/discussions/comictagger/comictagger)](https://github.com/comictagger/comictagger/discussions)
[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/comictagger/community)
[![Google Group](https://img.shields.io/badge/discuss-on%20groups-%23207de5)](https://groups.google.com/forum/#!forum/comictagger)
[![Twitter](https://img.shields.io/badge/%40comictagger-twitter-lightgrey)](https://twitter.com/comictagger)
[![Facebook](https://img.shields.io/badge/comictagger-facebook-lightgrey)](https://www.facebook.com/ComicTagger-139615369550787/)

# ComicTagger

ComicTagger is a **multi-platform** app for **writing metadata to digital comics**, written in Python and PyQt.

![ComicTagger logo](https://raw.githubusercontent.com/comictagger/comictagger/develop/comictaggerlib/graphics/app.png)

## Features

* Runs on macOS, Microsoft Windows, and Linux systems
* Get comic information from [Comic Vine](https://comicvine.gamespot.com/)
* **Automatic issue matching** using advanced image processing techniques
* **Batch processing** in the GUI for tagging hundreds or more comics at a time
* Support for **ComicRack** and **ComicBookLover** tagging formats
* Native full support for **CBZ** digital comics
* Native read only support for **CBR** digital comics: full support enabled installing additional [rar tools](https://www.rarlab.com/download.htm)
* Command line interface (CLI) enabling **custom scripting** and **batch operations on large collections**

For details, screen-shots, and more, visit [the Wiki](https://github.com/comictagger/comictagger/wiki)


## Installation

### Binaries

Windows, Linux and MacOS binaries are provided in the [Releases Page](https://github.com/comictagger/comictagger/releases).

Just unzip the archive in any folder and run, no additional installation steps are required.

### PIP installation

A pip package is provided, you can install it with:

```
 $ pip3 install comictagger[GUI]
```

There are optional dependencies. You can install the optional dependencies by specifying one or more of them in braces e.g. `comictagger[CBR,GUI]`

Optional dependencies:
1. `ICU`: Ensures that comic pages are supported correctly. This should always be installed. *Currently only exists in the latest alpha release *
1. `CBR`: Provides support for CBR/RAR files.
1. `GUI`: Installs the GUI.
1. `7Z`: Provides support for CB7/7Z files.
1. `all`: Installs all of the above optional dependencies.

### Chocolatey installation (Windows only)

A [Chocolatey package](https://community.chocolatey.org/packages/comictagger), maintained by @Xav83, is provided, you can install it with:
```powershell
choco install comictagger
```
### WinGet installation (Windows only)

A [WinGet package](https://github.com/microsoft/winget-pkgs/tree/master/manifests/c/ComicTagger/ComicTagger), maintained by @Sn1cket, is provided, you can install it with:
```powershell
winget install ComicTagger.ComicTagger
```
### From source

 1. Ensure you have python 3.9 installed
 2. Clone this repository `git clone https://github.com/comictagger/comictagger.git`
 7. `pip3 install .[ICU]` or `pip3 install .[GUI,ICU]`


## Contributors

<!-- readme: beville,davide-romanini,collaborators,contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/beville">
            <img src="https://avatars.githubusercontent.com/u/7294848?v=4" width="100;" alt="beville"/>
            <br />
            <sub><b>beville</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/davide-romanini">
            <img src="https://avatars.githubusercontent.com/u/731199?v=4" width="100;" alt="davide-romanini"/>
            <br />
            <sub><b>davide-romanini</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/fcanc">
            <img src="https://avatars.githubusercontent.com/u/4999486?v=4" width="100;" alt="fcanc"/>
            <br />
            <sub><b>fcanc</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/lordwelch">
            <img src="https://avatars.githubusercontent.com/u/7547075?v=4" width="100;" alt="lordwelch"/>
            <br />
            <sub><b>lordwelch</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/mizaki">
            <img src="https://avatars.githubusercontent.com/u/1141189?v=4" width="100;" alt="mizaki"/>
            <br />
            <sub><b>mizaki</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/MichaelFitzurka">
            <img src="https://avatars.githubusercontent.com/u/27830765?v=4" width="100;" alt="MichaelFitzurka"/>
            <br />
            <sub><b>MichaelFitzurka</b></sub>
        </a>
    </td></tr>
<tr>
    <td align="center">
        <a href="https://github.com/abuchanan920">
            <img src="https://avatars.githubusercontent.com/u/368793?v=4" width="100;" alt="abuchanan920"/>
            <br />
            <sub><b>abuchanan920</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/N-Hertstein">
            <img src="https://avatars.githubusercontent.com/u/64664577?v=4" width="100;" alt="N-Hertstein"/>
            <br />
            <sub><b>N-Hertstein</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Kijaru">
            <img src="https://avatars.githubusercontent.com/u/9641432?v=4" width="100;" alt="Kijaru"/>
            <br />
            <sub><b>Kijaru</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/kcgthb">
            <img src="https://avatars.githubusercontent.com/u/186807?v=4" width="100;" alt="kcgthb"/>
            <br />
            <sub><b>kcgthb</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/rhaussmann">
            <img src="https://avatars.githubusercontent.com/u/7084007?v=4" width="100;" alt="rhaussmann"/>
            <br />
            <sub><b>rhaussmann</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/AlbanSeurat">
            <img src="https://avatars.githubusercontent.com/u/500180?v=4" width="100;" alt="AlbanSeurat"/>
            <br />
            <sub><b>AlbanSeurat</b></sub>
        </a>
    </td></tr>
<tr>
    <td align="center">
        <a href="https://github.com/Sn1cket">
            <img src="https://avatars.githubusercontent.com/u/32904645?v=4" width="100;" alt="Sn1cket"/>
            <br />
            <sub><b>Sn1cket</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/emmanuel-ferdman">
            <img src="https://avatars.githubusercontent.com/u/35470921?v=4" width="100;" alt="emmanuel-ferdman"/>
            <br />
            <sub><b>emmanuel-ferdman</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/jpcranford">
            <img src="https://avatars.githubusercontent.com/u/21347202?v=4" width="100;" alt="jpcranford"/>
            <br />
            <sub><b>jpcranford</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/PawlakMarek">
            <img src="https://avatars.githubusercontent.com/u/26022173?v=4" width="100;" alt="PawlakMarek"/>
            <br />
            <sub><b>PawlakMarek</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/DrMcCoy">
            <img src="https://avatars.githubusercontent.com/u/156130?v=4" width="100;" alt="DrMcCoy"/>
            <br />
            <sub><b>DrMcCoy</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Xav83">
            <img src="https://avatars.githubusercontent.com/u/6787157?v=4" width="100;" alt="Xav83"/>
            <br />
            <sub><b>Xav83</b></sub>
        </a>
    </td></tr>
<tr>
    <td align="center">
        <a href="https://github.com/thFrgttn">
            <img src="https://avatars.githubusercontent.com/u/39759781?v=4" width="100;" alt="thFrgttn"/>
            <br />
            <sub><b>thFrgttn</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/tlc">
            <img src="https://avatars.githubusercontent.com/u/19436?v=4" width="100;" alt="tlc"/>
            <br />
            <sub><b>tlc</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: beville,davide-romanini,collaborators,contributors -end -->
