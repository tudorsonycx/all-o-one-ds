# All-O-One Data Structure

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description
This project implements a data structure that supports incrementing, decrementing, and retrieving keys with maximum and minimum counts, all in O(1) time complexity. It uses a doubly linked list to maintain the order of counts efficiently.

## Features
- O(1) increment and decrement operations
- O(1) retrieval of keys with maximum and minimum counts
- Efficiently maintains the order of counts using a doubly linked list

## Technologies Used
- Python 3.x

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/tudorsonycx/all-o-one-ds.git
    ```
2. Navigate to the project directory:
    ```sh
    cd all-o-one-ds
    ```

## Usage
1. Import the `AllOne` class:
    ```python
    from all_one import AllOne
    ```
2. Create an instance of `AllOne`:
    ```python
    all_one = AllOne()
    ```
3. Use the available methods:
    ```python
    all_one.inc("key1")
    all_one.inc("key2")
    all_one.inc("key1")
    print(all_one.getMaxKey())  # Output: "key1"
    print(all_one.getMinKey())  # Output: "key2"
    all_one.dec("key1")
    print(all_one.getMaxKey())  # Output: "key1"
    print(all_one.getMinKey())  # Output: "key1"
    ```

## License
This project is licensed under the MIT License.