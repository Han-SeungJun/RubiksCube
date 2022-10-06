# Cube Emulator 🎲🧊

> a cube Emulator in python

![cube_ui](https://user-images.githubusercontent.com/105290026/192979037-34962af3-eaf3-4153-a8a5-9fa64b6ec1df.jpg)

This project is a program made of a well-known 3×3×3 cube in everyone.

As you might have expected, the cube is composed of a three-dimensional array.

But implementing this as a function is quite complicated.

Because, the rotation of the cube is a 90degree rotation transformation.

The rotation of the cube causes the color data of each piece to be transformed into a non-linear mechanism.

However, this project description will allow you to understand not only a simple implementation, but also what algorithm it is  made of.


## Release History

* 1.0
    * 2019.3
    * Implemente a Cube operating environment
    * Fabricate a rotating function
    * Create a function to determine if cube was solved

* 2.0
    * 2019.4.7
    * Implemente a `mixCube()` (using ``random`` module)
    * Implemente a Cube GUI (using ``wxPython`` module)

* 2.1
    * 2021.7.19
    * Implemente a `saveCube()` and `loadCube()` (using ``sqlite3`` module)

* 2.2
    * 2021.7.21
    *  Implemente a keyboard manipulation and hotkey
    *  using `keyboard.is_pressed()` and `keyboard.add_hotkey()`
