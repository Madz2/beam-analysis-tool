# Beam Analysis Tool

A Python tool that calculates and plots the structural response of a 
simply-supported beam under point and uniformly distributed loads.

## What it does
- Computes support reactions from static equilibrium
- Calculates shear force and bending moment at every point along the span
- Plots the shear force and bending moment diagrams
- Handles a central point load, an off-centre point load, and a UDL

## Why I built it
I taught myself to build this after identifying a gap in my own 
engineering toolkit. Rather than rely on a ready-made calculator, I 
derived every governing equation by hand from first principles 
(equilibrium, shear and bending relationships), implemented them in 
code, and validated the output against my own hand calculations to 
confirm accuracy.

## Built with
Python, NumPy, Matplotlib

## How to run
Run `beam_tool_v1.py`, choose a load case (point load or UDL), and 
enter the span and load values when prompted. The tool prints the 
reactions and maximum bending moment, and plots the diagrams.

## Author
Nigel Madziyire — BEng Civil Engineering, Aston University
