# AAE6102 Assignment 1

## Satellite Communication and Navigation (2024/25 Semester 2)
 
**Name:** ZHANGDi 24046964R

**Due Date:** 12 March 2025  

## Overview  
We process the datasets seperately, started with Open-Sky!



## Open-Sky 

### **Task 1 – Acquisition**  
**Source:** Code is avaliable in Task_1_sky.py

**Result:**
![Uploading image.png…]()

The magnitude of the complex values reflects the strength of the signal at each frequency bin, while the phase gives information about the signal's phase shift. The larger magnitude values, such as 1.24600464e+05 + 36182.99329712j and 1.35773023e+05 + 42768.76777354j, indicate the presence of dominant frequency components in the signal, which likely correspond to the GNSS satellite signal you're trying to acquire. These peaks are essential for initial acquisition, as they represent the Doppler-shifted frequencies of the received signal.

The low-magnitude values (like -1.13064445e+02 -22313.8805029j) indicate noise or less relevant frequency components and can be filtered out. The overall goal is to identify the peaks in the FFT result, which correspond to the dominant frequencies, and use these to estimate the Doppler shift and lock onto specific satellite signals. This step is crucial for initial GNSS signal acquisition and further processing.

### **Task 2 – Tracking**  
Adapt the **tracking loop (DLL)** to generate **correlation plots** and analyze the tracking performance. Discuss the impact of urban interference on the correlation peaks. *(Multiple correlators must be implemented for plotting the correlation function.)*

### **Task 3 – Navigation Data Decoding**  
![alt text](image-1.png)

### **Task 4 – Position and Velocity Estimation**  
Using **pseudorange measurements** from tracking, implement the **Weighted Least Squares (WLS)** algorithm to compute the **user's position and velocity**.  
- Plot the user **position** and **velocity**.  
- Compare the results with the **ground truth**.  
- Discuss the impact of **multipath effects** on the WLS solution.

### **Task 5 – Kalman Filter-Based Positioning**  
Develop an **Extended Kalman Filter (EKF)** using **pseudorange and Doppler measurements** to estimate **user position and velocity**.
