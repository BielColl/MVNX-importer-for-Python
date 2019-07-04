# MVNX Importer for Python
Simple library for importing MVNX files into Python, to access the data of a recording using XSense. Uses Python 3 and the untangle library.

## Creating a MVNX object (without using the prop tracker)
To import the data from a MVNX file and create a MVNX object in python, write the following line:

``` python
data=mvnx.MVNX('example.mvnx')
```
For an example of how to use the imported data inside python, take a look to the [example](https://github.com/BielColl/MVNX-importer-for-Python/blob/master/example.py). Also, for a closer inside in how to MVNX files are structured, I recommend to read [MVN Awinda User Manual](https://fccid.io/QILMTW2-3A7G6/User-Manual/Users-Manual-2695756).

## Creating a MVNX object (using the prop tracker)
If one have used the prop tracker during the recording, the importing function expalined above won't work. Instead use the following line of code to import it. 

``` python
data=mvnx.MVNX_1_PROP('example.mvnx')
```

How this object is used remains unchanged from the previous section. 
