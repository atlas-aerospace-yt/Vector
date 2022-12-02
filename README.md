# Vector

A python vector library

## Contents
* [Why vector](#why-vector)
* [Usage](#usage)
* [Installation](#installation)

## Why vector

Vector is a mathematical library for python. In my search to understand artificial intelligence (AI) I strived to make my own neural network entirely from scratch. To do this I began with <a href = "https://numpy.org/">numpy</a> – a python library which is the “go-to” for mathematical things within python. As I started to make this program, I realised that I wanted more control over the objects and wanted to use them in such a way that would make sense for AI. So, I made my own library – vector – a simple vector library in python which holds the basic activation functions for neural networks, random generation, and of course a Vector object which is to be used in a way similar to `np.array`.

## Usage

To import the library:
```
from vector import Vector
from vector import activation
from vector import random
```
To define a vector object, `a = Vector([1, 0, 0, 1])` or `a = Vector(1)`. This class definition takes in either a list, tuple, int, or float. 
To generate a random vector, `a = random.random_vector(length, lower_bound, upper_bound)`, `lower_bound` and `upper_bound` are optional arguments and by default are -0.1 and 0.1 respectively.
The vector library has 2 activation functions and the 2 derivative functions of those functions:
```
activation.sigmoig(vec)
activation.sigmoid_prime(vec)
activation.linear(vec)
activation.linear_prime(vec)
```
In the example above, vec is either an integer, float, or Vector. `sigmoid` is: 1 / (1 + e ^ -x) and `linear` is: 0.5 * x.
The `_prime` in the function name means derivative. 

## Installation

To install this library using pip, you need to type `pip install vector-ai-ml`. This file can then be imported using `import vector`.

![pylint](https://github.com/atlas-aerospace-yt/Vector/actions/workflows/pylint.yml/badge.svg)<br>
