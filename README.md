# Knowledge of Python2 to Python3 migration (lib2to3). 
Migration of python 2 code into python 3 using lib2to3 library.

**Key Difference Between python2 and python3**


1. range() and xrange(): Python 3 offers Range() function to perform iterations whereas, In Python 2, 
the xrange() is used for iterations.

        # Python 2 only:
            for i in xrange(10**8):
              ...
        # Python 3:
            for i in range(10**8):
              ...
                
2. print function: 

          print 'Hello, World'      # Python 3.x doesn't support  
  
          print('Hope You like these facts') 
          
3. Exception Handling: There is a small change in error handling in both versions. In python 3.x, ‘as’ keyword is required.

                # Python 2:
                try:  
  
                    trying_to_check_error  
  
                except NameError, err:  
  
                    print err, 'Error Caused'
                    
                # Python 3:
                try:  
  
                    trying_to_check_error  
  
                except NameError as err:  
  
                    print (err, 'Error Caused')  

4. Input function:

            # Python 2: raw_input() gets the input as text.
                val1 = raw_input("Enter any number: ") 
                val2 = raw_input("Enter any string: ") 
                
            # Python 3: input() gets the input as text.
                val1 = input("Enter any number: ") 
                val2 = input("Enter any string: ") 

5. Integer Division: 

            # Python 2: The return type of a division (/) operation depends on its operands. If both operands are of type int, floor division is performed and an int is returned. If either operand is a float, a classic division is performed
             and a float is returned   
                print 5 / 2
                print -5//2  
                
                # Output: 
                # 2 
                # -3     
                
            # Python 3: Division (/) always returns a float.
            
                print (-5 / 2) 
                print (5//2)   
                
                # Output: 
                # -2.5 
                # 2 

6. Round function: 

            # Python 2: The output always results in a floating point number.
                print(round(69.9))   
                print(round(69.4))   
                
                # Output:  
                # 70.0 
                # 69.0 
                
            # Python 3: The return results in n digit precision.
                print(round(69.9))   
                print(round(69.4))  
                 
                # Output: 
                # 70 
                # 69 

**Instructions to run the code**

- Python 3 code can be seen in python3.py

- lib2to3 migration library used for python 2 to 3 migration.

- Following are the command:

    - 2to3 python2.py
    
        - Lists the line of code which can be converted in python 3, on console.
        
    - 2to3 -w python2.py 
    
        - Makes changes in code and creates .bak file to keep python 2
           version code before conversion.


# References:
- [GeeksforGeeks](https://www.geeksforgeeks.org)

- [Python-Future](https://python-future.org/)
