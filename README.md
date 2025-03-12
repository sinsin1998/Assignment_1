# AAE6102 Assignment 1

## Satellite Communication and Navigation (2024/25 Semester 2)
 
**Name:** ZHANGDi 24046964R

**Date:** 12 March 2025  

# AAE6102 Assignment 1

## Satellite Communication and Navigation (2024/25 Semester 2)


## Overview  
This assignment focuses on processing **GNSS Software-Defined Receiver (SDR) signals** to develop a deeper understanding of **GNSS signal processing**. Students will analyze **two real Intermediate Frequency (IF) datasets** collected in different environments: **open-sky** and **urban**. The urban dataset contains **multipath and non-line-of-sight (NLOS) effects**, which can degrade positioning accuracy.

### Dataset Information  

| Environment | Carrier Frequency | IF Frequency | Sampling Frequency | Data Format | Ground Truth Coordinates | Data Length | Collection Date (UTC) |
|------------|------------------|--------------|-------------------|------------|-----------------------|------------|-----------------|
| Open-Sky  | 1575.42 MHz | 4.58 MHz | 58 MHz | 8-bit I/Q samples | (22.328444770087565, 114.1713630049711) | 90 seconds | 14/10/2021 12.21pm|
| Urban     | 1575.42 MHz | 0 MHz | 26 MHz | 8-bit I/Q samples | (22.3198722, 114.209101777778) | 90 seconds | 07/06/2019 04.49am |

![image](https://github.com/IPNL-POLYU/AAE6102-assignments/blob/main/Picture1.png)

## Assignment Results  

### **Task 1 – Acquisition**  
Process the **IF data** using a **GNSS SDR** and generate the initial acquisition results. We get the results as the figure below. 
![image](https://github.com/sinsin1998/Assignment_1/blob/main/figures/Task%201/acquisition%20result%20sky%20and%20urban.png)

### **Task 2 – Tracking**  
Adapt the **tracking loop (DLL)** to generate **correlation plots** and analyze the tracking performance. Discuss the impact of urban interference on the correlation peaks. *(Multiple correlators must be implemented for plotting the correlation function.)* 

![image](https://github.com/user-attachments/assets/b3c0b98d-828e-4d8b-ba7a-0813caf2f41b)
As the figure shows the opensky tracking results.

![image](https://github.com/user-attachments/assets/b97702bd-4bd8-4f19-97cb-59b79851a367)
The figure shows the urban tracking results.

![image](https://github.com/user-attachments/assets/5113d387-adf8-4a16-a9a4-e15f4db802c0)
The figure shows the correlation.
### **Task 3 – Navigation Data Decoding**  
Decode the **navigation message** and extract key parameters, such as **ephemeris data**, for at least one satellite.

### **Task 4 – Position and Velocity Estimation**  
Using **pseudorange measurements** from tracking, implement the **Weighted Least Squares (WLS)** algorithm to compute the **user's position and velocity**.  
- Plot the user **position** and **velocity**.  
- Compare the results with the **ground truth**.  
- Discuss the impact of **multipath effects** on the WLS solution.

### **Task 5 – Kalman Filter-Based Positioning**  
Develop an **Extended Kalman Filter (EKF)** using **pseudorange and Doppler measurements** to estimate **user position and velocity**.



