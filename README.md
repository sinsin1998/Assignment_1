# AAE6102 Assignment 1

## Satellite Communication and Navigation (2024/25 Semester 2)
 
**Name:** ZHANGDi 24046964R

**Date:** 12 March 2025  

## Overview  
This assignment focuses on processing **GNSS Software-Defined Receiver (SDR) signals** to develop a deeper understanding of **GNSS signal processing**. Students will analyze **two real Intermediate Frequency (IF) datasets** collected in different environments: **open-sky** and **urban**. The urban dataset contains **multipath and non-line-of-sight (NLOS) effects**, which can degrade positioning accuracy.

### Dataset Information  

| Environment | Carrier Frequency | IF Frequency | Sampling Frequency | Data Format | Ground Truth Coordinates | Data Length | Collection Date (UTC) |
|------------|------------------|--------------|-------------------|------------|-----------------------|------------|-----------------|
| Open-Sky  | 1575.42 MHz | 4.58 MHz | 58 MHz | 8-bit I/Q samples | (22.328444770087565, 114.1713630049711) | 90 seconds | 14/10/2021 12.21pm|
| Urban     | 1575.42 MHz | 0 MHz | 26 MHz | 8-bit I/Q samples | (22.3198722, 114.209101777778) | 90 seconds | 07/06/2019 04.49am |


## Assignment Results  

### **Task 1 – Acquisition**  
Process the **IF data** using a **GNSS SDR** and generate the initial acquisition results. Code relative shows as follow
``` matlab
% Skips acquisition in the script postProcessing.m if set to 1
settings.skipAcquisition    = 0;
% List of satellites to look for. Some satellites can be excluded to speed
% up acquisition
settings.acqSatelliteList   = 1:32;         %[PRN numbers]
% Band around IF to search for satellite signal. Depends on max Doppler.
% It is single sideband, so the whole search band is tiwce of it.
settings.acqSearchBand      = 7000;           %[Hz]
% Threshold for the signal presence decision rule
settings.acqThreshold       = 1.5; % Original: 1.8
% Sampling rate threshold for downsampling 
settings.resamplingThreshold    = 8e6;            % [Hz]
% Enable/dissable use of downsampling for acquisition
settings.resamplingflag         = 0;              % 0 - Off
                                                  % 1 - On
```

**1.1 Down-Conversion and Synchronous Demodulation:**

The received GNSS signal is down-converted from RF to IF by mixing with a locally generated carrier signal. This retains the PRN code and navigation data. The signal is transformed to the frequency domain for analysis, with the search range set as IF.

**1.2 Frequency Domain Transformation and PRN Code Matching:**

Each candidate satellite’s PRN code is converted to the frequency domain using FFT. The frequency representation of the received signal is multiplied point-by-point with the PRN code, corresponding to time-domain convolution. The result is converted back to the time domain using IFFT to obtain the correlation function.

**1.3 Correlation Peak Detection and Threshold Judgment:**

The peak of the correlation function indicates the code phase, and its amplitude reflects the match quality. Two adjacent 1 ms segments are processed, and the maximum correlation coefficient is chosen for each element. If the ratio of the highest to the second-highest peak satisfies P_{max1}/p_{max2} > 1.5 and the peaks are sufficiently separated, the satellite is considered successfully acquired.

**1.4 Result Output and Transition to Fine Acquisition:**

This process repeats for all visible satellites, estimating their code phases and Doppler shifts. Successfully acquired satellites and their parameters are then used for fine acquisition and further signal processing.
We get the results in the figure below, where in the open sky dataset, satellites 16, 22, 26, 27, and 31 were successfully acquired, and in the urban dataset, satellites 1, 3, 11, and 18 were detected and acquired.
![image](https://github.com/sinsin1998/Assignment_1/blob/main/figures/Task%201/acquisition%20result%20sky%20and%20urban.png)

### **Task 2 – Tracking**  
Adapt the **tracking loop (DLL)** to generate **correlation plots** and analyze the tracking performance. Discuss the impact of urban interference on the correlation peaks. *(Multiple correlators must be implemented for plotting the correlation function.)* 

![image](https://github.com/user-attachments/assets/b3c0b98d-828e-4d8b-ba7a-0813caf2f41b)
As the figure shows the opensky tracking results.

![image](https://github.com/user-attachments/assets/b97702bd-4bd8-4f19-97cb-59b79851a367)
The figure shows the urban tracking results.

![image](https://github.com/user-attachments/assets/5113d387-adf8-4a16-a9a4-e15f4db802c0)
The figure shows the correlation.

![image](https://github.com/user-attachments/assets/1bc3f6af-932d-4be6-8669-8db4052dd0b9)
The table above shows the channel to process the data and here we set the channel number as 6.
### **Task 3 – Navigation Data Decoding**  
Decode the **navigation message** and extract key parameters, such as **ephemeris data**, for at least one satellite.
![image](https://github.com/user-attachments/assets/178c9cc9-271c-43ae-8dcf-892afebdf901)
the sky navigation data decoding result.
![image](https://github.com/user-attachments/assets/6b4f72ac-18c4-483d-85ca-335dffa81541)
the urban navigation data decoding result.
### **Task 4 – Position and Velocity Estimation**  
Using **pseudorange measurements** from tracking, implement the **Weighted Least Squares (WLS)** algorithm to compute the **user's position and velocity**.  
- Plot the user **position** and **velocity**.  
- Compare the results with the **ground truth**.  
- Discuss the impact of **multipath effects** on the WLS solution.

### **Task 5 – Kalman Filter-Based Positioning**  
Develop an **Extended Kalman Filter (EKF)** using **pseudorange and Doppler measurements** to estimate **user position and velocity**.



