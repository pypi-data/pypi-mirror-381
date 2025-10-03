# pmatlib

**pmatlib** is a lightweight Python library that implements the **Progressive Moving Average Transform (PMAT)**.  
PMAT is a signal transformation technique that converts **1D discrete signals** into **2D representations** by progressively applying Moving Averages (MA) with varying window sizes.  

This transform is particularly useful for **feature extraction**, **fault diagnosis**, and **machine learning applications** (e.g., CNNs on time–series data).  

---

## Features
- Implementation of the **Progressive Moving Average Transform (PMAT)**.  
- Supports three variants:  
  - **LPMAT** (Left PMAT)  
  - **RPMAT** (Right PMAT)  
  - **CPMAT** (Centered PMAT)  
- Based on **NumPy** for efficiency.  
- Easy integration into ML pipelines.  

---

## Installation

```bash
pip install pmatlib
