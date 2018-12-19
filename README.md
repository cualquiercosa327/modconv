# modconv
An experimental ASSIMP model converter for N64 development written in Python (now increasingly C). I am a very bad programmer so the code is super sloppy. Feel free to send a PR if you find my terrible coding practices unbearable.

Currently modconv can:
* Generate unstripped vertices with vertex RGBA.
* Generate dynlists for the Mario head demo for SM64. (modconv4)
* Prepare a basic displaylist without any faces.
* modconv2 is able to generate basic collision for the game *Super Mario 64*.

## Roadmap

* Texture generation (modconv and modconv3)
* Tristripping and F3DEX support (modconv3)
* Finish collision generator.

# Running

## Dependencies

* python3 assimp (also requires standard assimp)
* libassimp (required for the C and C++ files)

To compile simply run ``gcc -o modconv(number) modconv(number).c -lassimp``
Make sure to replace ``(number)`` with the actual number of the file you're compiling.

## Usage
``./modconv(number) PATHTOMODEL OUTPUTNAMES SCALE``
``python3 modconv.py PATHTOMODEL SCALE``

## CREDITS

* Trenavix and robiNerd for answering my stupid Fast3D questions.
* Simon for rewriting the Python scripts into C and C++.
* tehz for explaining how parts of the Mario head work.
