
TRGA
==========
This is a demo of TRGA which contains the source code of TRGA and corresponding integrated fault localization techniques (Barinel, Ochiai, Dstar, Mseer, FLC (also called J2 in the source code file)), all faulty versions and their corresponding execution files of program Mockito have been given for better understanding. Furthr, all seed faults of benchmark programs are given in the Benchmark folder for reference.

Introduction
===
* Mockito -- The folder Mockito gives the detailed execution information of available faulty versions of program Mockito from Defects4J dataset. All faulty versions that can not be compiled or produce a runtime error are discarded.
    #matrix--the execution spectrum of each executable statement, including the execution result in the last column.
    #spectra--the detailed information about each executable statement.
* TRGA_Barinel -- The folder TRGA_Barinel gives the source code of TRGA with Barinel technique.
* TRGA_Ochiai -- The folder TRGA_Barinel gives the source code of TRGA with Ochiai technique.
* TRGA_Dstar -- The folder TRGA_Barinel gives the source code of TRGA with Dstar technique.
* TRGA_Clustering -- The folder TRGA_Barinel gives the source code of TRGA with two clustering techniques (Mseer and FLC).

Deployment
===
* Step1 -- Deploy the python environment (python 2.7) and download all sources of this project
* Step2 -- Add the matrix and spectra path into the main function of corresponding technique. Taking Ochiai as an example, if you want to run the TRGA with Ochiai technique, you need to open the main function (TRGA_Ochiai.py) and add the matrix and spectra path of specific Mockito program to parameter matrix_path and spectrum_path separately. After that, the exact position of faulty statements in spectra file should be assigned to parameter faulty_statements_list.
* Step3 -- Rewrite the main function (TRGA_Ochiai.py) to import the output to your desired location and run TRGA_Ochiai.py.

Notice
===
This project is only used for academic research.
