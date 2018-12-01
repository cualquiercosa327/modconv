# modconv
An experimental ASSIMP model converter for N64 development written in Python.
I am a very bad programmer so the code is super sloppy. Feel free to send a PR if you find my terrible coding practices unbearable.

Currently modconv can:
* Generate unstripped vertices with vertex RGBA.
* Prepare a basic displaylist without any faces.
* modconv2 is able to generate basic collision for the game *Super Mario 64*.

# Running

## Dependencies
python3 assimp (also requires standard assimp)

## Usage

``python3 modconv.py PATHTOMODEL SCALE``
