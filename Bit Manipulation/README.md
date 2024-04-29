# Bit Manipulation

## Introduction

Bit manipulation refers to the manipulation of individual bits or groups of bits within a binary representation of data. 
In computing and programming, binary digits (bits) are the smallest unit of data and can have a value of either 0 or 1. Bit manipulation involves using bitwise operators to perform operations on these bits, such as setting a bit to 1 or 0, toggling a bit, or extracting specific bits from a binary number.


## Table of Contents

1. [Bitwise Operators](#bitwise-operators)
2. [Applications of Bit Manipulation](#applications-of-bit-manipulation)
3. [Common Techniques](#common-techniques)

## Bitwise Operators

Bitwise operators are fundamental in bit manipulation. They operate on the individual bits of integers. Here are the main bitwise operators:

- **Bitwise AND (`&`)**: Sets each bit to 1 if both bits are 1.
- **Bitwise OR (`|`)**: Sets each bit to 1 if either bit is 1.
- **Bitwise XOR (`^`)**: Sets each bit to 1 if only one bit is 1.
- **Bitwise NOT (`~`)**: Flips all bits, changing 1s to 0s and 0s to 1s.
- **Left Shift (`<<`)**: Shifts bits to the left by a specified number of positions.
- **Right Shift (`>>`)**: Shifts bits to the right by a specified number of positions.

## Applications of Bit Manipulation

Bit manipulation has various applications in programming:

- **Flags and Masks**: Used to represent and manipulate sets of Boolean flags efficiently.
- **Optimization**: Can lead to more efficient and compact code in certain algorithms.
- **Data Compression**: Techniques like Huffman coding and run-length encoding rely on bit manipulation.
- **Cryptography**: Building cryptographic algorithms often involves bitwise operations for encryption and decryption.

## Common Techniques

Here are some common bit manipulation techniques:

1. **Checking if a Bit is Set**: Use bitwise AND (`&`) with a mask to check if a specific bit is set.
2. **Setting a Bit**: Use bitwise OR (`|`) with a mask to set a specific bit.
3. **Clearing a Bit**: Use bitwise AND (`&`) with the complement of a mask to clear a specific bit.
4. **Toggling a Bit**: Use bitwise XOR (`^`) with a mask to toggle a specific bit.
